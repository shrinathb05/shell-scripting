import subprocess
import os
import sys
import hashlib
import json
from datetime import datetime

# --- CONFIGURATION ---
config = {
    "GITHUB_TOKEN": "ghp_your_secret_token_here", 
    "WEBHOOK_URL": "https://discord.com/api/webhooks/your_webhook_url_here",
    "REPO_PATH": "shrinathb05/webapp-java",
    "APP_NAME": "maven-web-app",
    "WORKING_DIR": "/home/shri/Desktop/projects/app/var/work",
    "DEPLOY_DIR": "/opt/tomcat/webapps",
    "BACKUP_DIR": "/opt/tomcat/backup",
}

config["LOCAL_WAR"] = f"{config['WORKING_DIR']}/{config['APP_NAME']}.war"
config["FINAL_WAR"] = f"{config['DEPLOY_DIR']}/{config['APP_NAME']}.war"

# --- HELPER FUNCTIONS ---

def run(cmd, cwd=None, halt_on_error=True):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        if halt_on_error:
            send_notification(f"⚠️ **Command Failed:** `{cmd}`\nError: `{result.stderr[:100]}`")
            sys.exit(1)
    return result.stdout.strip()

def send_notification(message):
    if not config["WEBHOOK_URL"] or "your_webhook" in config["WEBHOOK_URL"]: return
    payload = {"content": message}
    subprocess.run(f"curl -s -H 'Content-Type: application/json' -d '{json.dumps(payload)}' {config['WEBHOOK_URL']}", shell=True)

def get_file_checksum(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# --- THE LOGIC ---

def rollback():
    """Restores the most recent backup."""
    print("\n--- 🔄 INITIATING AUTOMATIC ROLLBACK ---")
    find_backup_cmd = f"ls -t {config['BACKUP_DIR']}/{config['APP_NAME']}.war_* | head -n 1"
    latest_backup = run(find_backup_cmd, halt_on_error=False)

    if not latest_backup:
        send_notification("❌ **Critical:** Rollback failed. No backups found.")
        return

    run("stop || true")
    run(f"rm -rf {config['DEPLOY_DIR']}/{config['APP_NAME']} {config['FINAL_WAR']}")
    run(f"cp {latest_backup} {config['FINAL_WAR']}")
    run("start")
    
    send_notification(f"🔄 **Rollback Triggered & Completed.** Restored: `{os.path.basename(latest_backup)}`")
    print("Rollback complete.")

def main():
    start_time = datetime.now()
    print(f"--- Starting Auto-Deployment: {start_time.strftime('%Y-%m-%d %H:%M:%S')} ---")
    
    os.makedirs(config['WORKING_DIR'], exist_ok=True)
    os.makedirs(config['BACKUP_DIR'], exist_ok=True)

    # 1. Download Latest Release
    api_url = f"https://api.github.com/repos/{config['REPO_PATH']}/releases/latest"
    release_json = run(f"curl -s -H 'Authorization: token {config['GITHUB_TOKEN']}' {api_url}")
    
    tag_name = run(f"echo '{release_json}' | grep '\"tag_name\":' | head -n 1 | awk -F'\"' '{{print $4}}'")
    asset_id = run(f"echo '{release_json}' | grep -B 1 '\"name\": \"{config['APP_NAME']}.war\"' | grep '\"id\":' | head -n 1 | awk '{{print $2}}' | tr -d ','")
    
    run(f"curl -fLJ -H 'Authorization: token {config['GITHUB_TOKEN']}' -H 'Accept: application/octet-stream' https://api.github.com/repos/{config['REPO_PATH']}/releases/assets/{asset_id} -o {config['LOCAL_WAR']}")

    # 2. Backup and Deploy
    run("stop || true")
    if os.path.exists(config["FINAL_WAR"]):
        ts = datetime.now().strftime("%Y%m%d%H%M%S")
        run(f"mv {config['FINAL_WAR']} {config['BACKUP_DIR']}/{config['APP_NAME']}.war_{tag_name}_{ts}")

    run(f"rm -rf {config['DEPLOY_DIR']}/{config['APP_NAME']}")
    run(f"cp {config['LOCAL_WAR']} {config['DEPLOY_DIR']}/")
    
    # 3. Start & Verification
    run("start")
    print("Waiting for extraction...")
    run("sleep 15") # Increased sleep for safety

    # --- VERIFICATION & SELF-HEALING ---
    if os.path.isdir(f"{config['DEPLOY_DIR']}/{config['APP_NAME']}"):
        success_msg = f"✅ **Deployment Successful:** `{config['APP_NAME']}` ({tag_name})"
        print(success_msg)
        send_notification(success_msg)
    else:
        print("❌ Extraction failed! Starting Rollback...")
        send_notification(f"⚠️ **Extraction Failed** for {tag_name}. Initiating auto-rollback...")
        rollback()
        sys.exit(1)

    run(f"rm -rf {config['WORKING_DIR']}/*")

if __name__ == "__main__":
    main()
