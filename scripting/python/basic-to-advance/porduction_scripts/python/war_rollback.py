import subprocess
import os
import sys
from datetime import datetime

# --- CONFIGURATION (Must match your deploy script) ---
config = {
    "WEBHOOK_URL": "https://discord.com/api/webhooks/your_webhook_url_here",
    "APP_NAME": "maven-web-app",
    "DEPLOY_DIR": "/opt/tomcat/webapps",
    "BACKUP_DIR": "/opt/tomcat/backup",
}

config["FINAL_WAR"] = f"{config['DEPLOY_DIR']}/{config['APP_NAME']}.war"

def run(cmd, halt_on_error=True):
    """Executes local bash commands."""
    print(f"---> Executing: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: {result.stderr}")
        if halt_on_error: sys.exit(1)
    return result.stdout.strip()

def send_notification(message):
    """Sends a message to Discord/Slack."""
    if not config["WEBHOOK_URL"] or "your_webhook" in config["WEBHOOK_URL"]:
        return
    import json
    payload = {"content": message}
    cmd = f"curl -s -H 'Content-Type: application/json' -d '{json.dumps(payload)}' {config['WEBHOOK_URL']}"
    subprocess.run(cmd, shell=True)

def main():
    print(f"--- Rollback Started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")

    # 1. Identify the latest backup file
    # We sort by time to find the most recent .war file in the backup folder
    print("Finding latest backup...")
    find_backup_cmd = f"ls -t {config['BACKUP_DIR']}/{config['APP_NAME']}.war_* | head -n 1"
    latest_backup = run(find_backup_cmd, halt_on_error=False)

    if not latest_backup or not os.path.exists(latest_backup):
        msg = "❌ Rollback Failed: No backup files found in " + config['BACKUP_DIR']
        print(msg)
        send_notification(msg)
        sys.exit(1)

    print(f"Found latest backup: {latest_backup}")

    # 2. Stop Tomcat
    print("Stopping Tomcat for rollback...")
    run("stop || true")

    # 3. Remove current failed deployment
    if os.path.exists(config["FINAL_WAR"]):
        run(f"rm -f {config['FINAL_WAR']}")
    
    # Remove the extracted folder to ensure a clean re-extraction
    app_folder = f"{config['DEPLOY_DIR']}/{config['APP_NAME']}"
    run(f"rm -rf {app_folder}")

    # 4. Restore the backup
    print(f"Restoring backup to {config['FINAL_WAR']}...")
    run(f"cp {latest_backup} {config['FINAL_WAR']}")

    # 5. Start Tomcat
    run("start")
    print("Waiting for Tomcat extraction (12s)...")
    run("sleep 12")

    # 6. Verify
    if os.path.isdir(app_folder):
        success_msg = f"↩️ **Rollback Successful!**\nRestored from: `{os.path.basename(latest_backup)}`"
        print(success_msg)
        send_notification(success_msg)
    else:
        fail_msg = "❌ **Rollback Failed!** Tomcat did not extract the restored WAR."
        print(fail_msg)
        send_notification(fail_msg)
        sys.exit(1)

if __name__ == "__main__":
    main()
