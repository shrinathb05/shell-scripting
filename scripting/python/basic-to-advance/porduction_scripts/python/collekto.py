import subprocess
import os
from datetime import datetime

# --- CONFIGURATION / VARIABLES ---
config = {
    "APP_NAME": "collekto-crm-reporting",
    "NEW_TAG": "ltfsprod-1.5.1",
    "OLD_TAG": "ltfsprod-1.5.0",
    "WORK_DIR": "/home/ltfadmin.collekto/Launch_Agent/var/work/collekto-crm-reporting",
    "HOME_DIR": "/home/ltfadmin.collekto/",
    "BACKUP_DIR": "/home/ltfadmin.collekto/Launch_Backup/",
    "PROD_DIR": "/home/ltfadmin.collekto/projects/collekto-crm-reporting/prod",
    "COMPOSE_FILE": "docker-compose-prod.yml",
    "STACK_NAME": "collekto-crm-reporting"
}

def run_command(cmd, cwd=None):
    """Executes a shell command and handles errors."""
    print(f"Executing: {cmd} in {cwd or 'current directory'}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)
    return result

def main():
    # 1. Clean working directory
    run_command(f"rm -rf {config['WORK_DIR']}/*")

    # 2. Cleanup Old Backups (Keep only the latest 2)
    # Using a simplified pythonic approach or the bash one-liner
    cleanup_cmd = (
        f"find {config['BACKUP_DIR']} -type f -name '{config['APP_NAME']}.tar_*' "
        f"| sort | head -n -2 | xargs rm -f"
    )
    run_command(cleanup_cmd)

    # 3. Backup current TAR
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file = f"{config['APP_NAME']}.tar_{timestamp}"
    run_command(f"mv {config['HOME_DIR']}{config['APP_NAME']}.tar {config['BACKUP_DIR']}{backup_file}")

    # 4. Deploy New Tar from Work Dir to Home
    run_command(f"cp {config['WORK_DIR']}/{config['APP_NAME']}.tar {config['HOME_DIR']}")

    # 5. Load Docker Image
    run_command(f"docker load -i {config['HOME_DIR']}{config['APP_NAME']}.tar")

    # 6. Update Image Tag in Docker Compose
    # sed -i 's/(image: name)[^ ]*/\1:tag/'
    sed_cmd = f"sed -i 's/\\(image: {config['APP_NAME']}\\)[^ ]*/\\1:{config['NEW_TAG']}/' {config['COMPOSE_FILE']}"
    run_command(sed_cmd, cwd=config['PROD_DIR'])

    # 7. Remove existing service (Optional in Swarm, but kept per your flow)
    run_command(f"docker service rm {config['STACK_NAME']}_{config['APP_NAME']}")

    # 8. Deploy Stack
    run_command(f"docker stack deploy -c {config['COMPOSE_FILE']} {config['STACK_NAME']}", cwd=config['PROD_DIR'])

    # 9. Delete Old Image
    run_command(f"docker rmi -f {config['APP_NAME']}:{config['OLD_TAG']}")

    # 10. Verify
    run_command("docker service ls")
    run_command(f"docker service ps {config['STACK_NAME']}_{config['APP_NAME']}")

if __name__ == "__main__":
    main()