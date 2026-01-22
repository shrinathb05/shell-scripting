To automate the build and release process using the script you provided, we will create a **CI (Continuous Integration) Pipeline**. This pipeline will live separately from your Deployment pipeline.

Here is the step-by-step guide to setting this up, including the necessary plugins.

---

### **Step 1: Install Required Plugins**

Before creating the pipeline, ensure Jenkins has the tools to talk to GitHub and run Maven.

1. Go to **Manage Jenkins** > **Plugins** > **Available Plugins**.
2. Search for and install the following:
* **Git Plugin**: (Usually installed by default) for cloning your code.
* **Pipeline**: (Usually installed by default) to run Jenkinsfiles.
* **Maven Integration**: To allow Jenkins to recognize `mvn` commands.
* **Config File Provider**: (Optional but recommended) for managing `settings.xml`.



---

### **Step 2: Configure Maven and JDK**

Jenkins needs to know where your build tools are located.

1. Go to **Manage Jenkins** > **Tools**.
2. Scroll to **JDK installations**: Click **Add JDK**, name it `Java17` (or your version), and check "Install automatically".
3. Scroll to **Maven installations**: Click **Add Maven**, name it `Maven3`, and check "Install automatically".

---

### **Step 3: Add GitHub Credentials**

Jenkins needs permission to push the tag back to GitHub.

1. Go to **Manage Jenkins** > **Credentials** > **System** > **Global credentials**.
2. Click **Add Credentials**.
3. **Kind**: Username with password.
4. **Username**: Your GitHub username.
5. **Password**: Your **GitHub Personal Access Token (PAT)**.
6. **ID**: Name it `github-push-creds`.

---

### **Step 4: Create the Pipeline Job**

1. From the Jenkins Dashboard, click **New Item**.
2. Enter name: `WelcomeKit-Build-and-Tag`.
3. Select **Pipeline** and click **OK**.
4. Scroll down to **This project is parameterized** and check it.
5. Add a **String Parameter**:
* **Name**: `VERSION_TAG`
* **Description**: Enter the version (e.g., v1.0.5).



---

### **Step 5: The Jenkinsfile Script**

In the **Pipeline** section, under **Definition**, choose **Pipeline script** and paste the following. This replaces your manual shell script with a Jenkins-managed version:

```groovy
pipeline {
    agent any
    
    tools {
        maven 'Maven3' // Matches the name you gave in Step 2
        jdk 'Java17'   // Matches the name you gave in Step 2
    }

    environment {
        // Use the credentials ID created in Step 3
        GITHUB_CREDS = credentials('github-push-creds')
        REPO_URL     = "github.com/YourUser/WelcomeKitApp.git"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls the dev or main branch
                git branch: 'main', url: "https://${env.REPO_URL}"
            }
        }

        stage('Step 1: Build & Test') {
            steps {
                echo "Running Maven Build..."
                sh "mvn clean package"
            }
        }

        stage('Step 2: Tag & Push') {
            steps {
                script {
                    // Configure git identity for the commit
                    sh 'git config user.email "jenkins@yourdomain.com"'
                    sh 'git config user.name "Jenkins Build Bot"'
                    
                    // Add the remote with credentials embedded
                    sh "git remote set-url origin https://${GITHUB_CREDS_USR}:${GITHUB_CREDS_PSW}@${env.REPO_URL}"
                    
                    echo "Creating Tag: ${params.VERSION_TAG}"
                    sh "git add ."
                    sh "git commit -m 'Build and prepare for release ${params.VERSION_TAG}'"
                    sh "git tag -a ${params.VERSION_TAG} -m 'Release version ${params.VERSION_TAG}'"
                    
                    echo "Pushing to GitHub..."
                    sh "git push origin main"
                    sh "git push origin ${params.VERSION_TAG}"
                }
            }
        }

        stage('Step 3: Archive Artifact') {
            steps {
                // This makes the .war file available to download from Jenkins
                archiveArtifacts artifacts: 'target/*.war', fingerprint: true
                echo "SUCCESS: Version ${params.VERSION_TAG} tagged and pushed."
                echo "Now, download the WAR and upload it to GitHub Releases."
            }
        }
    }
}

```

---

### **How to Run It**

1. Click **Build with Parameters** in the left menu.
2. Type your version (e.g., `v1.0.5`).
3. Click **Build**.
4. Once finished, click on the build number. You will see the **Build Artifacts** at the top—this is your `.war` file.

### **Next Step**

Now that Jenkins has handled the build and tagging, you simply go to GitHub, find the tag it just pushed, click **"Create release from tag"**, and upload the `.war` you downloaded from Jenkins.

Would you like me to show you how to automate the **GitHub Release creation** itself so you don't even have to visit the GitHub website?