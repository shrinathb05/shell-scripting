Since you need a project that is guaranteed to work with **Maven**, **Tomcat**, and your **WAR-based pipeline**, I recommend using the **"Spring Hello World"** or **"Address Book"** sample. These are simple, stable, and perfect for demonstrating a CI/CD flow.

Here are the three best options for you to use:

### Option 1: The "Standard" Sample (Recommended)

This is a clean, simple Java Web App specifically designed for Tomcat.

* **Source:** [https://github.com/hkhajuria/AddressBook-1](https://www.google.com/search?q=https://github.com/hkhajuria/AddressBook-1)
* **Why it’s good:** It uses a standard `pom.xml` and generates a clean `AddressBook.war` file. It is very "interview-friendly."

### Option 2: The "Official" Spring Sample

* **Source:** [https://github.com/spring-projects/spring-petclinic](https://github.com/spring-projects/spring-petclinic)
* **Note:** By default, modern versions use `.jar`. To use this with your pipeline, you would look for the **legacy version** or a branch that uses **WAR** packaging.

### Option 3: Create your own in 1 minute (Safest)

If you want to ensure there are no bugs in the "online code," you can generate a perfect project yourself using the **Spring Initializr**:

1. Go to [start.spring.io](https://start.spring.io)
2. **Project:** Maven
3. **Language:** Java
4. **Packaging:** **WAR** (This is the most important step!)
5. **Dependencies:** Add "Spring Web".
6. Click **Generate**. It will download a zip file.
7. Upload this to your GitHub repo.

---

### **How to adapt your script for the new project:**

Once you pick a project, you only need to change **one variable** in your script to make it work.

If the project name is `AddressBook`:

1. Open your **Jenkinsfile** and **deploy_war.sh**.
2. Change `APP_NAME = "WelcomeKitApp"` to `APP_NAME = "AddressBook"`.

### **Steps to start right now:**

1. **Fork** one of the repositories above (or upload your generated zip to your own GitHub).
2. Run `mvn clean package` on your local machine or Jenkins to confirm it creates a `.war` file in the `target/` folder.
3. **Trigger your Jenkins Pipeline.**

**Which one would you like to try? If you give me the link to the project you pick, I can tell you the exact `APP_NAME` and `ASSET_ID` logic you will need.**




Since you need a reliable project that is ready to go, I have selected the **Address Book** project for you. It is a classic Java Web application that is perfect for DevOps demonstrations because it is lightweight and uses the standard Maven structure.

### **The Project to Use**

* **GitHub Repository:** [https://github.com/hkhajuria/AddressBook-1](https://www.google.com/search?q=https://github.com/hkhajuria/AddressBook-1)
* **Project Name:** `AddressBook`
* **Artifact Name:** `AddressBook.war`

---

### **How to Set This Up (3 Quick Steps)**

#### **Step 1: Fork the Repository**

1. Open the [AddressBook-1 link](https://www.google.com/search?q=https://github.com/hkhajuria/AddressBook-1).
2. Click the **"Fork"** button at the top right to copy it into your own GitHub account. This is important so you can create "Releases" and "Tags" for your pipeline.

#### **Step 2: Update your Jenkinsfile & Script**

You need to change the `APP_NAME` variable so the script looks for the correct file.

* **In your Jenkinsfile:**
```groovy
environment {
    APP_NAME = "AddressBook" 
    // ... rest stays the same
}

```


* **In your deploy_war.sh:**
```bash
APP_NAME="AddressBook"

```



#### **Step 3: Create your first "Release" (The Trigger)**

Your pipeline is designed to fetch from "GitHub Releases." You need to create one first:

1. Go to your forked repo on GitHub.
2. On the right side, click **"Create a new release"**.
3. Type `v1.0` as the tag.
4. **Important:** You must upload the `AddressBook.war` file (which you can get by running `mvn clean package` on your computer) to the "Assets" section of this release.

---

### **Why this project is perfect for your Resume:**

* **Clear Structure:** It has a standard `pom.xml` and `src/main/webapp` folder.
* **Tomcat Ready:** It is designed specifically to run on Apache Tomcat.
* **Easy to Explain:** In an interview, you can say: *"I used a standard Address Book Java application to demonstrate how my pipeline handles artifact versioning and automated rollbacks."*

### **Next Step for you:**

Try to run the `mvn clean package` command on this project. If you don't have Maven installed on your local machine, I can show you the Jenkins stage to do the build automatically.

**Would you like me to show you how to add a "Build" stage to your Jenkinsfile so it compiles the AddressBook code for you?**