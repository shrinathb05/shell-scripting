This looks like a deployment script for a CI/CD pipeline (likely IBM UrbanCode Deploy or a similar tool given the `${p:resource/...}` syntax).

I have organized this into a clean Markdown file with clear headings, code blocks, and a logical flow to make it easier for your team to read and maintain.

---

# Deployment Documentation: Collekto CRM Frontend

This document outlines the shell operations for managing Docker services and images for the `collekto-crm-frontend` resource.

## 1. Update Image Tag in Compose File

Navigates to the project directory and updates the Docker image tag within the Compose file using `sed`.

```bash
cd ${p:resource/collekto-crm-frontend/Docker_Compose_Path}

# Updates the image tag using a regex replacement
sed -i 's/\(image: ${p:resource/collekto-crm-frontend/img_name}\)[^ ]*/\1:${p:Tag}/' ${p:resource/collekto-crm-frontend/Docker_Compose_File}

# Verify changes
cat ${p:resource/collekto-crm-frontend/Docker_Compose_File}

```

## 2. Docker Image Cleanup

Deletes the specific old image to free up disk space and avoid conflicts.

```bash
cd ${p:resource/collekto-crm-frontend/Deployment_path}

# List image to verify existence
docker images | grep ${p:resource/collekto-crm-frontend/img_name}:${p:old_image_tag}

# Force remove the old image
docker rmi -f ${p:resource/collekto-crm-frontend/img_name}:${p:old_image_tag}

```

## 3. Artifact Management & Backup

Handles the rotation of `.tar` files. It keeps the **2 most recent backups** and deletes older ones.

```bash
# 1. Clean Working Directory
rm -rf *

# 2. Rotate Backups
cd ${p:resource/collekto-crm-frontend/Backup_Path}

# Find files, sort by time, and remove all but the 2 newest
find . -type f -name "${p:resource/collekto-crm-frontend/tar_file}_*" -printf '%T@\t%p\n' | \
sort -t $'\t' -g | \
head -n -2 | \
cut -d $'\t' -f 2- | \
xargs rm -f

# 3. Move current file to backup with timestamp
mv ${p:resource/collekto-crm-frontend/tar_file} ${p:resource/collekto-crm-frontend/Backup_Path}${p:resource/collekto-crm-frontend/tar_file}_`date +%Y%m%d%H%M%S`

# 4. Deploy New Tar File from CodeStation
cd ${p:resource/collekto-crm-frontend/CodeStation_Path}
cp -r ${p:resource/collekto-crm-frontend/tar_file} ${p:resource/collekto-crm-frontend/Deployment_path}

```

## 4. Load and Deploy

Loads the image into Docker and deploys the stack.

### Load Image

```bash
cd ${p:resource/collekto-crm-frontend/Deployment_path}
docker load -i ${p:resource/collekto-crm-frontend/tar_file}

```

### Remove Existing Service

```bash
cd ${p:resource/collekto-crm-frontend/Docker_Compose_Path}
docker service ls
docker service rm ${p:resource/collekto-crm-frontend/Service_Name}

```

### Run/Deploy Stack

```bash
cd ${p:resource/collekto-crm-frontend/Docker_Compose_Path}
docker stack deploy -c ${p:resource/collekto-crm-frontend/Docker_Compose_File} ${p:resource/collekto-crm-frontend/img_name}

```

## 5. Verification

Check the status of the service to ensure it is running correctly.

```bash
# List all services
docker service ls

# Check specific service status/tasks
docker service ps ${p:resource/collekto-crm-frontend/Service_Name}

```

---

**Artifacts Directory:** `/home/ltfadmin.devops/collekto`

Would you like me to add a section for error handling or a script to verify if the Docker service is healthy after deployment?