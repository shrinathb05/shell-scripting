#!/bin/bash

# This script automates the sequence: Build → Test → Tag → Push.

# --- CONFIGURATION ---
APP_NAME="WelcomeKitApp"
MAIN_BRANCH="main" # or 'dev' depending on your workflow

echo "Starting Release Process for $APP_NAME..."

# 1. BUILD & TEST
echo "Step 1: Running Maven Build and Tests..."
if mvn clean package; then
    echo "SUCCESS: Build and Tests passed."
else
    echo "ERROR: Build failed. Fix the code before tagging."
    exit 1
fi

# 2. VERSION INPUT
echo ""
read -p "Enter the version tag (e.g., v1.0.5): " VERSION_TAG

if [ -z "$VERSION_TAG" ]; then
    echo "ERROR: Tag name cannot be empty."
    exit 1
fi

# 3. GIT TAGGING
echo "Step 2: Creating Git Tag $VERSION_TAG..."
git add .
git commit -m "Build and prepare for release $VERSION_TAG"
git tag -a "$VERSION_TAG" -m "Release version $VERSION_TAG"

# 4. PUSH TO GITHUB
echo "Step 3: Pushing code and tags to GitHub..."
git push origin "$MAIN_BRANCH"
git push origin "$VERSION_TAG"

echo ""
echo "===================================================="
echo "DONE! Tag $VERSION_TAG is now on GitHub."
echo "1. Go to GitHub and create the Release from this tag."
echo "2. Upload target/${APP_NAME}.war to the Release."
echo "3. Trigger your Jenkins Deployment Pipeline."
echo "===================================================="