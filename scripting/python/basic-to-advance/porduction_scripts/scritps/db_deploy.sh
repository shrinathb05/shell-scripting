
# DB Deployment script MS-SQL
# DB Backup
# Clean working directory
    erase * /q
    -------------------------------
    working directory: D:\Launch_Agent\var\work\BrakeApp2_DataPatches

    #execution
    D:\Launch_Agent\var\work\BrakeApp2_DataPatches>erase * /q 

# Download artifacts
Working directory: D:\Launch_Agent\var\work\BrakeApp2_DataPatches
Including **/*

    # Scan for 1 files complete in 0 seconds.
    # Downloading files to D:\Launch_Agent\var\work\BrakeApp2_DataPatches.
    # Downloading: BRAKE_2_PATCH_270126.sql
    # Download complete.
    # ${p:resource.id}  19a6c7a9-7de4-a9f8-e687-adaadb6a2dea
    # ${p:server.url}   https://172.26.50.130:8443

# Execute the scripts
Working directory: D:\Launch_Agent\var\work\BrakeApp_DataPatches
SQLFiles: BMS_PATCH_270126.sql
Executing : sqlcmd -b -S 172.30.86.67,5007 -U IT_CHANGE_RELEASE -P **** -d DCS -i D:\Launch_Agent\var\work\BrakeApp_DataPatches\BMS_PATCH_270126.sql
Changed database context to 'ltfcollect'.    

