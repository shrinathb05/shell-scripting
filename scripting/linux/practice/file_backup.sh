#!/bin/bash
set -x

path="/var/work/batch-uploads"
bkp_dir=/var/work/backup/

# Enter the directory
cd $path

# 2. Use a loop to rename and move each file
# This finds every .SAL file and processes them one by one

for file in *.SAL; do
    # Check if files actually exist to avoid errors if the folder is empty
    [ -e "$file" ] || continue

    # Rename and move in one go
    # This takes "filename.SAL" and moves it to "backup/filename_bkp.SAL"
    mv "$file" "${bkp_dir}${file%.SAL}_bkp.SAL"

    echo "Processed: $file"
done

