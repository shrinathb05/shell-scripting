Since you have already written a very functional shell script, you are halfway there. To turn this into a professional Jenkins Pipeline, you can either call this script from Jenkins or (better yet) convert the logic directly into a **Jenkins Declarative Pipeline** to get better visibility into each stage.

Here is the step-by-step guide to configuring Jenkins and creating the pipeline.

---

### **Step 1: Install Required Plugins**

To make your script work inside Jenkins, you need these plugins:

1. Go to **Manage Jenkins** > **Plugins** > **Available Plugins**.
2. Search and install:
* **Pipeline**: (Core plugin) to run the script.
* **Git Plugin**: To pull your code.
* **Credentials Binding**: To securely use your `GITHUB_TOKEN`.
* **Email Extension**: To handle the `mailx` equivalent in Jenkins.
* **Pipeline: Stage View**: (Optional) For a nice visual of the deployment steps.



---

### **Step 2: Configure System Credentials**

Never hardcode your GitHub Token in the script.

1. Go to **Manage Jenkins** > **Credentials** > **System** > **Global credentials**.
2. Click **Add Credentials**.
3. **Kind**: Secret text.
4. **Secret**: (Paste your GitHub Personal Access Token).
5. **ID**: `github-token`.
6. Click **Create**.

---

### **Step 3: Create the Pipeline Job**

1. From the Dashboard, click **New Item**.
2. Name it `WelcomeKit-Production-Deploy`.
3. Select **Pipeline** and click **OK**.
4. Scroll to the **Pipeline** section and choose **Pipeline script**.

---

### **Step 4: The Pipeline Code (Jenkinsfile)**

Copy this code into the Jenkins script box. It translates your shell functions into organized Jenkins Stages.

```groovy
pipeline {
    agent any

    environment {
        WORKING_DIR = "/home/ltfadmin.dn/app/Launch_Agent/var/work/Welcome_KIT"
        BACKUP_DIR  = "/home/ltfadmin.dn/app/Launch_Agent/Backup"
        DEPLOY_DIR  = "/home/ltfadmin.dn/ApacheTomcat/webapps"
        APP_NAME    = "WelcomeKitApp"
        GITHUB_TOKEN = credentials('github-token') // Uses the ID from Step 2
        TIMESTAMP   = sh(script: "date +%Y%m%d%H%M%S", returnStdout: true).trim()
    }

    stages {
        stage('Stage 1: Clean Workspace') {
            steps {
                sh "rm -rf ${env.WORKING_DIR}/*"
            }
        }

        stage('Stage 2: Download Artifact') {
            steps {
                sh """
                    curl -L -H "Authorization: token ${env.GITHUB_TOKEN}" \
                         -H "Accept: application/octet-stream" \
                         "https://api.github.com/repos/YourOrg/WelcomeKitRepo/releases/assets/ASSET_ID" \
                         -o "${env.WORKING_DIR}/${env.APP_NAME}.war"
                """
            }
        }

        stage('Stage 3: Backup & Cleanup') {
            steps {
                sh """
                    # Cleanup old backups (keep 2)
                    cd ${env.BACKUP_DIR} || exit 1
                    find . -type f -name "${env.APP_NAME}.war_*" -printf '%T@\t%p\n' | sort -t \$'\t' -g | head -n -2 | cut -d \$'\t' -f 2- | xargs rm -f
                    
                    # Backup current live file
                    cd ${env.DEPLOY_DIR}
                    if [ -f "${env.APP_NAME}.war" ]; then
                        mv "${env.APP_NAME}.war" "${env.BACKUP_DIR}/${env.APP_NAME}.war_${env.TIMESTAMP}"
                    fi
                """
            }
        }

        stage('Stage 4: Wait for Tomcat Undeploy') {
            steps {
                echo "Waiting 30s for Tomcat to clear the old directory..."
                sleep 30
                script {
                    def exists = sh(script: "[ -d ${env.DEPLOY_DIR}/${env.APP_NAME} ]", returnStatus: true)
                    if (exists == 0) {
                        error("Deployment Aborted: Tomcat directory ${env.APP_NAME} still exists.")
                    }
                }
            }
        }

        stage('Stage 5: Deploy') {
            steps {
                sh "cp ${env.WORKING_DIR}/${env.APP_NAME}.war ${env.DEPLOY_DIR}/"
                sleep 30
            }
        }

        stage('Stage 6: Verify Checksum') {
            steps {
                script {
                    def sourceCK = sh(script: "cksum ${env.WORKING_DIR}/${env.APP_NAME}.war | awk '{print \$1}'", returnStdout: true).trim()
                    def destCK   = sh(script: "cksum ${env.DEPLOY_DIR}/${env.APP_NAME}.war | awk '{print \$1}'", returnStdout: true).trim()
                    
                    if (sourceCK != destCK) {
                        error("Checksum Mismatch! Source: ${sourceCK}, Dest: ${destCK}")
                    }
                }
            }
        }
    }

    post {
        success {
            echo "SUCCESSFUL DEPLOYMENT"
            mail to: 'admin@yourdomain.com',
                 subject: "Deployment SUCCESS: ${env.APP_NAME}",
                 body: "Build ${env.BUILD_NUMBER} successful at ${env.TIMESTAMP}."
        }
        failure {
            echo "FAILURE: Initiating Rollback..."
            sh """
                if [ -f "${env.BACKUP_DIR}/${env.APP_NAME}.war_${env.TIMESTAMP}" ]; then
                    cp "${env.BACKUP_DIR}/${env.APP_NAME}.war_${env.TIMESTAMP}" "${env.DEPLOY_DIR}/${env.APP_NAME}.war"
                    echo "Rollback successful."
                fi
            """
            mail to: 'admin@yourdomain.com',
                 subject: "Deployment FAILED & ROLLED BACK: ${env.APP_NAME}",
                 body: "Build ${env.BUILD_NUMBER} failed. System rolled back to previous version."
        }
    }
}

```

---

### **Step 5: Setting Linux Permissions**

Jenkins runs as a user called `jenkins`. Your script paths are in `/home/ltfadmin.dn`. For Jenkins to run your script, you must grant it permission:

1. Run this on your Linux server:
```bash
# Add jenkins user to the ltfadmin.dn group
sudo usermod -a -G ltfadmin.dn jenkins

# Give the group write permissions to the folders
sudo chmod -R 775 /home/ltfadmin.dn/app/Launch_Agent/
sudo chmod -R 775 /home/ltfadmin.dn/ApacheTomcat/webapps

```



### **Step 6: Running the Pipeline**

1. Click **Build Now**.
2. Watch the **Stage View**. If any stage fails (like the Checksum stage), Jenkins will immediately jump to the `post { failure }` block, perform the rollback, and email you.

### **Why this is better than a simple Shell Script?**

1. **Visualization:** You see exactly which stage took the most time or failed.
2. **Audit Log:** Jenkins keeps a history of every build, who started it, and the logs.
3. **Automatic Rollback:** The `post` block ensures that even if a stage crashes, the rollback logic *always* runs.

**Would you like me to show you how to add a "Wait for Manual Approval" button inside this pipeline so you can check things before the final deployment?**

To add a manual approval step, you need to use the `input` step. This is placed between the **Backup** and **Deploy** stages to create a "Gate" where the pipeline pauses and waits for you to click a button.

Here is the updated pipeline script with the **Approval Gate** and the **Step-by-Step** instructions to configure it.

### **1. The Updated Pipeline Script**

I have added **Stage 4** to handle the manual verification.

```groovy
pipeline {
    agent any

    environment {
        WORKING_DIR = "/home/ltfadmin.dn/app/Launch_Agent/var/work/Welcome_KIT"
        BACKUP_DIR  = "/home/ltfadmin.dn/app/Launch_Agent/Backup"
        DEPLOY_DIR  = "/home/ltfadmin.dn/ApacheTomcat/webapps"
        APP_NAME    = "WelcomeKitApp"
        GITHUB_TOKEN = credentials('github-token')
        TIMESTAMP   = sh(script: "date +%Y%m%d%H%M%S", returnStdout: true).trim()
    }

    stages {
        stage('Stage 1: Clean Workspace') {
            steps { sh "rm -rf ${env.WORKING_DIR}/*" }
        }

        stage('Stage 2: Download Artifact') {
            steps {
                sh """
                    curl -L -H "Authorization: token ${env.GITHUB_TOKEN}" \
                         -H "Accept: application/octet-stream" \
                         "https://api.github.com/repos/YourOrg/WelcomeKitRepo/releases/assets/ASSET_ID" \
                         -o "${env.WORKING_DIR}/${env.APP_NAME}.war"
                """
            }
        }

        stage('Stage 3: Backup Current WAR') {
            steps {
                sh """
                    # Cleanup old backups (keep 2)
                    cd ${env.BACKUP_DIR} || exit 1
                    find . -type f -name "${env.APP_NAME}.war_*" -printf '%T@\t%p\n' | sort -t \$'\t' -g | head -n -2 | cut -d \$'\t' -f 2- | xargs rm -f
                    
                    # Backup live file
                    cd ${env.DEPLOY_DIR}
                    if [ -f "${env.APP_NAME}.war" ]; then
                        cp "${env.APP_NAME}.war" "${env.BACKUP_DIR}/${env.APP_NAME}.war_${env.TIMESTAMP}"
                    fi
                """
            }
        }

        // --- NEW MANUAL APPROVAL STAGE ---
        stage('Stage 4: Manual Approval') {
            steps {
                script {
                    // This creates a popup in the Jenkins UI
                    input message: "Finished Backup. Do you want to proceed with deploying version ${env.TIMESTAMP} to Production?", 
                          ok: "Deploy Now"
                }
            }
        }

        stage('Stage 5: Deploy') {
            steps {
                // Remove the old file to trigger Tomcat undeploy
                sh "rm -f ${env.DEPLOY_DIR}/${env.APP_NAME}.war"
                echo "Waiting for Tomcat to undeploy..."
                sleep 20
                
                // Copy new file
                sh "cp ${env.WORKING_DIR}/${env.APP_NAME}.war ${env.DEPLOY_DIR}/"
                echo "Waiting for Tomcat to deploy..."
                sleep 30
            }
        }

        stage('Stage 6: Final Verification') {
            steps {
                script {
                    def sourceCK = sh(script: "cksum ${env.WORKING_DIR}/${env.APP_NAME}.war | awk '{print \$1}'", returnStdout: true).trim()
                    def destCK   = sh(script: "cksum ${env.DEPLOY_DIR}/${env.APP_NAME}.war | awk '{print \$1}'", returnStdout: true).trim()
                    
                    if (sourceCK != destCK) {
                        error("Checksum Mismatch! Deployment Corrupted.")
                    }
                    
                    // Verify Tomcat folder exists
                    def dirExists = sh(script: "[ -d ${env.DEPLOY_DIR}/${env.APP_NAME} ]", returnStatus: true)
                    if (dirExists != 0) {
                        error("Tomcat failed to extract the WAR folder.")
                    }
                }
            }
        }
    }

    post {
        success { echo "DEPLOYMENT SUCCESSFUL" }
        failure {
            echo "FAILURE: Rolling back to ${env.TIMESTAMP}"
            sh "cp ${env.BACKUP_DIR}/${env.APP_NAME}.war_${env.TIMESTAMP} ${env.DEPLOY_DIR}/${env.APP_NAME}.war"
        }
    }
}

```

---

### **2. How to use the Approval Gate**

Once you run this pipeline, it will follow these steps:

1. **Automation:** It downloads the file and makes a backup automatically.
2. **The Pause:** The pipeline will turn **yellow (Paused)**.
3. **To Approve:** * Go to the Pipeline "Stage View" on the main job page.
* Hover over the **Manual Approval** stage.
* You will see a button: **"Proceed"** or **"Abort"**.


4. **Result:** If you click "Proceed," it continues to Stage 5 (Deploy). If you click "Abort," the job stops without touching your live Tomcat server.

---

### **3. Setting up the Pipeline Step-by-Step**

If you haven't created the job yet:

1. **Create Job:** Click **New Item** > **Pipeline** > Name it `WelcomeKit-Deploy`.
2. **Add Credentials:** Go to **Manage Jenkins** > **Credentials**. Add your `github-token` as **Secret Text**.
3. **Install Plugins:** Ensure **"Pipeline"** and **"Pipeline: Basic Steps"** plugins are installed (they usually are).
4. **Configure Script:** Paste the code above into the Pipeline script section.
5. **Run:** Click **Build Now**.

### **Pro-Tip: Blue Ocean View**

If you want a much better visual interface for the approval button:

1. Install the **"Blue Ocean"** plugin.
2. Click **"Open Blue Ocean"** on the left side of your Jenkins job.
3. The approval step will appear as a big, clear button in the middle of your screen.

**Would you like me to show you how to add a "Timeout" so that if no one clicks 'Approve' within 1 hour, the deployment automatically aborts for safety?**