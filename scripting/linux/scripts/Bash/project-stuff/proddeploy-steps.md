To set up your **Deployment Pipeline** from scratch, follow these step-by-step instructions. This guide covers the plugin installation, tool configuration, and job creation.

---

### **Step 1: Install Necessary Plugins**

You need specific plugins to handle Git, Credentials, and Email notifications.

1. Log in to Jenkins and go to **Manage Jenkins** > **Plugins** > **Available Plugins**.
2. Search for and install:
* **Pipeline**: (Standard) The core engine for your script.
* **Git Plugin**: To fetch metadata from GitHub.
* **Credentials Binding Plugin**: To securely handle your `my-github-token`.
* **Email Extension Plugin**: For the `mail` steps in your `post` block.


3. Click **Install without restart** (or restart if prompted).

---

### **Step 2: Configure Your Credentials**

Your pipeline uses `credentials('my-github-token')`. You must define this in the Jenkins global store.

1. Go to **Manage Jenkins** > **Credentials**.
2. Click on the **(global)** domain under **Stores scoped to Jenkins**.
3. Click **Add Credentials**.
4. **Kind**: Select **Secret text**.
5. **Secret**: Paste your GitHub Personal Access Token (PAT).
6. **ID**: Type `my-github-token` (this must match your script exactly).
7. Click **Create**.

---

### **Step 3: Set Up Email (For Notifications)**

If you want the `mail` block to work, Jenkins needs an SMTP server.

1. Go to **Manage Jenkins** > **System**.
2. Scroll down to **E-mail Notification**.
3. Enter your SMTP server (e.g., `smtp.gmail.com`).
4. Click **Advanced**, check **Use SMTP Authentication**, and enter your email/app password.
5. Set **SMTP Port** (usually `465` for SSL or `587` for TLS).

---

### **Step 4: Create the Pipeline Job**

1. On the Jenkins Dashboard, click **New Item**.
2. Enter the name: `WelcomeKit-Production-Deploy`.
3. Select **Pipeline** and click **OK**.
4. (Optional) Check **This project is parameterized** if you want to add a `TAG_NAME` parameter as we discussed earlier.

---

### **Step 5: Configure the Pipeline Script**

1. Scroll down to the **Pipeline** section.
2. Under **Definition**, ensure **Pipeline script** is selected.
3. Paste your code into the **Script** box.

**Important Adjustment for your script:** The `REPO_URL` in your snippet is currently hardcoded to `.../assets/ID`. Since you are doing **Tag-Based Deployment**, replace that specific line with the dynamic API logic we discussed:

```groovy
// Use this inside your 'Download Artifact' stage to find the ID automatically
def assetId = sh(script: "curl -s -H 'Authorization: token ${GITHUB_TOKEN}' https://api.github.com/repos/YourOrg/Repo/releases/tags/${params.TAG_NAME} | grep -Po '\"id\": \\K[0-9]+' | head -n 2 | tail -n 1", returnStdout: true).trim()

```

---

### **Step 6: Server Permissions (Crucial)**

Jenkins runs as the `jenkins` user. It usually does not have permission to write to `/home/ltfadmin.dn/...`. You must grant access on your Linux server:

1. Open your terminal on the Jenkins server.
2. Add Jenkins to the owner's group:
```bash
sudo usermod -a -G ltfadmin.dn jenkins

```


3. Set directory permissions so the group can write:
```bash
sudo chmod -R 775 /home/ltfadmin.dn/app/Launch_Agent/
sudo chmod -R 775 /home/ltfadmin.dn/ApacheTomcat/webapps

```



---

### **Step 7: Run the Deployment**

1. Click **Build Now** (or **Build with Parameters** if you added the Tag parameter).
2. The pipeline will run Stage 1–3.
3. **Approval Step:** The pipeline will pause at Stage 4. You must hover over the stage in the UI and click **Proceed** for the deployment to actually finish.

### **The Workflow Summary**

1. **Local Script:** You build and push the tag.
2. **GitHub:** You upload the `.war` to the release.
3. **Jenkins:** This pipeline downloads that specific version, backs up the old one, waits for your "OK," and swaps the files in Tomcat.

**Would you like me to show you how to set up "Slack Notifications" instead of Email so you get deployment alerts on your phone?**