# Planning 
    - Jira (issue) -> Developers (pull request) -> [approved/not approved] -> github (source code management) -> Webhook build trigger 

# Continuous Integration
    # (Build and code scan)
    -> Jenkins 
    -> sonarqube (code vulnerability & coverage scan) 
    -> [pass/fail] (fail)-> return to developers

# Continuous Deployment    
    -> (pass) -> Devops Deploy tool (create version)
    -> requestor ->  Devops Deploy tool (create version)
    -> approvals
        -> UAT (appowner)
        -> PRE-PROD (AppOwner and QA)
        -> PROD (App-Owner) (QA) (Change Management) (Release Management) (Release Executor)
        -> DR (Release Management) (Release Executor)

# Github Repo Management Form
 https://docs.google.com/forms/d/e/1FAIpQLScEjaqBxEkKSUGuQyofnoZuQLLK3tVOq0uGs9DC0hlLcuJyfQ/viewform       

# Sonarqube False Postive  
 https://forms.gle/oCKoHiUaLq4ervkR9
 https://docs.google.com/forms/d/e/1FAIpQLSdorUPV28MS6fdVpeZVU__LIkmttNPW4HbKitDu-QE7BhkVLg/viewform


 Meeting Note - SAST and SCA Scan Integration in DevOps Pipeline Overview



By Chandramitra Baruah

1 min

2

Add a reaction
spiral calendar Date
Sep 10, 2025

busts in silhouette Participants
Dhaval Shah, Pravin Singh, Laxman Kamble, Jayakrishna Yarlagadda, Divya Gupta, Aashutosh Jha, Kishor Marathe, Abhishek Verma, Surekha Daine, Sneha Ashok Alwe, Ajinkya Deshpande, Om Naik, Devyani Parmar, Aravind Surairaj, Nimesh Jain, Om Nevase, Sunil Jadhav, Leena Sakat, Anup Sakharkar, Divya Vinod, Chetan Darade, Ajinkya Rahurkar, Harshal Kolhe, Nikita Rane, Chandramitra Baruah

speaking head Points Discussed
The DevOps team provided an overview and understanding of the Snyk tool and how it will be integrated with the DevOps pipeline for SAST & SCA scans to all the developers, leads, and HOD for Brake 2.0, BMS, and Digital Servicing.

Presented an overview of report generation and accessibility through both GitHub and the CLI pipeline.

For one month, gates will not be enabled, allowing developers to familiarize themselves with the tool. Gradually, gates will be implemented, starting with high and medium vulnerabilities.

Provided access to the Snyk tool to all the developers present at the call.

A call will be scheduled with the OEM this month to give an in-depth overview of the tool and address developers' questions.

 