To explain this project in simple words—whether to an interviewer or just for your own notes—think of it as a **6-step safety process**.

Here are the stages in plain English:

### **1. The "Clean Slate" Stage**

We wipe away any old files in our temporary workspace. This ensures that we don't accidentally deploy an old version of the app. It's like cleaning the kitchen before you start cooking.

### **2. The "Fetch" Stage**

Jenkins reaches out to GitHub and downloads the specific version of the app (the `.war` file) that we tagged. This makes sure we are only moving code that has been officially "approved" and versioned.

### **3. The "Insurance" (Backup) Stage**

Before we touch the live website, we take the current working version and save a copy of it in a backup folder with a timestamp. If the new version breaks, we have a "save point" to go back to instantly.

### **4. The "Human Check" (Approval) Stage**

The pipeline pauses and sends a notification. It waits for a human to click a button in Jenkins to say "Yes, I am ready to deploy this now." This prevents accidental deployments during busy hours.

### **5. The "Switch" (Deployment) Stage**

This is the main event. We remove the old file from the Tomcat server, wait for it to clear out, and then drop the new file in. This is where the website actually updates.

### **6. The "Double Check" (Verification) Stage**

We don't just assume it worked. We run a **Checksum** (a digital fingerprint) to make sure the file wasn't corrupted during the move. We also check if Tomcat successfully created the new application folder. If anything looks wrong, the **Automatic Rollback** kicks in and restores our backup from Stage 3.

---

### **Summary for an Interview:**

> "I followed a **Backup-First** strategy. My project ensures that we never delete the old version until the new version is proven to be 100% correct via checksums and automated health checks."

**I'm ready whenever you start your first run. Just paste any errors here if they pop up!**