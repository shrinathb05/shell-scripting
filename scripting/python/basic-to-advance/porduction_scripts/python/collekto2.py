import subprocess
import os
from datetime import datetime

# --- CONFIGURATION ---
config = {
    "APP_NAME": "collekto-crm-reporting",
    "NEW_TAG": "ltfsprod-1.5.1",  # You only update this one!
    "WORK_DIR": "/home/ltfadmin.collekto/Launch_Agent/var/work/collekto-crm-reporting",
    "HOME_DIR": "/home/ltfadmin.collekto/",
    "BACKUP_DIR": "/home/ltfadmin.collekto/Launch_Backup/",
    "PROD_DIR": "/home/ltfadmin.collekto/projects/collekto-crm-reporting/prod",
    "COMPOSE_FILE": "docker-compose-prod.yml",
    "STACK_NAME": "collekto-crm-reporting"
}

def run_command(cmd, cwd=None):
    """Executes command and returns the text output."""
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing [{cmd}]: {result.stderr}")
        return None
    return result.stdout.strip()

def main():
    # 1. AUTOMATICALLY DETECT OLD TAG
    # We look for the image name and grab the TAG column (column 2)
    print("--- Detecting current image tag ---")
    get_tag_cmd = f"docker images | grep {config['APP_NAME']} | awk '{{print $2}}' | head -n 1"
    old_tag = run_command(get_tag_cmd)
    
    if not old_tag:
        print("Warning: Could not find an existing image tag. Skipping old image deletion later.")
    else:
        print(f"Detected Old Tag: {old_tag}")

    # 2. CLEAN WORKING DIR
    run_command(f"rm -rf {config['WORK_DIR']}/*")

    # 3. CLEANUP OLD BACKUPS (Keep 2)
    cleanup_cmd = f"find {config['BACKUP_DIR']} -type f -name '{config['APP_NAME']}.tar_*' | sort | head -n -2 | xargs rm -f"
    run_command(cleanup_cmd)

    # 4. BACKUP & MOVE NEW FILES
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    run_command(f"mv {config['HOME_DIR']}{config['APP_NAME']}.tar {config['BACKUP_DIR']}{config['APP_NAME']}.tar_{ts}")
    run_command(f"cp {config['WORK_DIR']}/{config['APP_NAME']}.tar {config['HOME_DIR']}")

    # 5. DOCKER LOAD
    run_command(f"docker load -i {config['HOME_DIR']}{config['APP_NAME']}.tar")

    # 6. UPDATE COMPOSE FILE (SED)
    sed_cmd = f"sed -i 's/\\(image: {config['APP_NAME']}\\)[^ ]*/\\1:{config['NEW_TAG']}/' {config['COMPOSE_FILE']}"
    run_command(sed_cmd, cwd=config['PROD_DIR'])

    # 7. REDEPLOY STACK
    run_command(f"docker service rm {config['STACK_NAME']}_{config['APP_NAME']}")
    run_command(f"docker stack deploy -c {config['COMPOSE_FILE']} {config['STACK_NAME']}", cwd=config['PROD_DIR'])

    # 8. DELETE OLD IMAGE (Using the tag we detected at the start)
    if old_tag and old_tag != config['NEW_TAG']:
        print(f"Cleaning up old image: {config['APP_NAME']}:{old_tag}")
        run_command(f"docker rmi -f {config['APP_NAME']}:{old_tag}")

    print("--- Deployment Complete ---")

if __name__ == "__main__":
    main()