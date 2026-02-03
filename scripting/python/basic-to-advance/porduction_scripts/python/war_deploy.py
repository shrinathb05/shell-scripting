import subprocess
import os
import sys
import hashlib
import json
from datetime import datetime

# --- CONFIGURATION ---
config = {
    "GITHUB_TOKEN": "ghp_your_secret_token_here", 
    "WEBHOOK_URL": "https://discord.com/api/webhooks/your_webhook_url_here", # Discord or Slack
    "REPO_PATH": "shrinathb05/webapp-java",
    "APP_NAME": "maven-web-app",
    "WORKING_DIR": "/home/shri/Desktop/projects/app/var/work",
    "DEPLOY_DIR": "/opt/tomcat/webapps",
    "BACKUP_DIR": "/opt/tomcat/backup",
}

# Derived Paths
config["LOCAL_WAR"] = f"{config['WORKING_DIR']}/{config['APP_NAME']}.war"
config["FINAL_WAR"] = f"{config['DEPLOY_DIR']}/{config['APP_NAME']}.war"

def run(cmd, cwd=None, halt_on_error=True):
    """Executes local bash commands and returns output."""
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        error_msg = f"ERROR: {result.stderr}"
        print(error_msg)
        send_notification(f"❌ Deployment Failed!\nCommand: `{cmd}`\nError: `{result.stderr[:100]}`")
        if halt_on_error: sys.exit(1)
    return result.stdout.strip()

def send_notification(message):
    """Sends a message to Discord/Slack via Webhook."""
    if not config["WEBHOOK_URL"] or "your_webhook" in config["WEBHOOK_URL"]:
        return # Skip if URL is not set
    
    # Payload for Discord (Slack uses similar format)
    payload = {"content": message}
    
    # We use curl here to avoid needing the 'requests' library
    cmd = f"curl -H 'Content-Type: application/json' -d '{json.dumps(payload)}' {config['WEBHOOK_URL']}"
    subprocess.run(cmd, shell=True, capture_output=True)

def get_file_checksum(filename):
    """Generates SHA256 hash of a local file."""
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def download_latest_artifact():
    """Fetches metadata for the latest release and downloads the .war."""
    print("Checking GitHub for the latest release...")
    api_url = f"https://api.github.com/repos/{config['REPO_PATH']}/releases/latest"
    api_cmd = f"curl -s -H 'Authorization: token {config['GITHUB_TOKEN']}' {api_url}"
    release_json = run(api_cmd)
    
    tag_name = run(f"echo '{release_json}' | grep '\"tag_name\":' | head -n 1 | awk -F'\"' '{{print $4}}'")
    asset_id = run(f"echo '{release_json}' | grep -B 1 '\"name\": \"{config['APP_NAME']}.war\"' | grep '\"id\":' | head -n 1 | awk '{{print $2}}' | tr -d ','")
    
    if not tag_name or not asset_id:
        print("ERROR: Could not find the latest release.")
        sys.exit(1)

    print(f"Detected Version: {tag_name}")
    download_cmd = (
        f"curl -fLJ -H 'Authorization: token {config['GITHUB_TOKEN']}' "
        f"-H 'Accept: application/octet-stream' "
        f"https://api.github.com/repos/{config['REPO_PATH']}/releases/assets/{asset_id} "
        f"-o {config['LOCAL_WAR']}"
    )
    run(download_cmd)
    return tag_name

def main():
    start_time = datetime.now()
    print(f"--- Deployment Started at {start_time.strftime('%Y-%m-%d %H:%M:%S')} ---")
    
    os.makedirs(config['WORKING_DIR'], exist_ok=True)
    os.makedirs(config['BACKUP_DIR'], exist_ok=True)

    # 1. DOWNLOAD
    latest_tag = download_latest_artifact()

    # 2. CHECKSUM
    file_hash = get_file_checksum(config['LOCAL_WAR'])

    # 3. STOP & BACKUP
    run("stop || true") 
    if os.path.exists(config["FINAL_WAR"]):
        ts = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_name = f"{config['APP_NAME']}.war_{latest_tag}_{ts}"
        run(f"mv {config['FINAL_WAR']} {config['BACKUP_DIR']}/{backup_name}")

    # 4. CLEANUP & DEPLOY
    run(f"find {config['BACKUP_DIR']} -type f -name '{config['APP_NAME']}.war_*' | sort | head -n -2 | xargs rm -f")
    run(f"rm -rf {config['DEPLOY_DIR']}/{config['APP_NAME']}")
    run(f"cp {config['LOCAL_WAR']} {config['DEPLOY_DIR']}/")

    # 5. START & VERIFY
    run("start")
    run("sleep 12")

    if os.path.isdir(f"{config['DEPLOY_DIR']}/{config['APP_NAME']}"):
        duration = (datetime.now() - start_time).seconds
        success_msg = (
            f"✅ **Deployment Successful!**\n"
            f"**App:** `{config['APP_NAME']}`\n"
            f"**Version:** `{latest_tag}`\n"
            f"**Duration:** `{duration}s`\n"
            f"**SHA256:** `{file_hash[:10]}...`"
        )
        print(success_msg)
        send_notification(success_msg)
    else:
        send_notification(f"❌ `{config['APP_NAME']}` failed to extract after start.")
        sys.exit(1)

    run(f"rm -rf {config['WORKING_DIR']}/*")

if __name__ == "__main__":
    main()
