# Fakie

![Icon](https://github.com/daspiker/fakie/blob/main/app/static/fakie.jpg)

Fakie aims to make it easy to push logs into Azure Sentinel.  

**Built a new analytics rule and want to see if it works?**

<u>Fakie!</u>

**Laid out a rad new workbook and want to see if it populates properly?**

<u>Fakie!</u>

**Want to re-live your youth where your new Airwalks were way cooler than your actual skating ability?**

<u>Sorry, Fakie can only do so much!</u>

### Overview
 Fakie is built in Python using the Flask Web Framework and has been Dockerized for easy deployment here:
 https://hub.docker.com/r/dennispike/fakie

 The latest build can be pulled from:
 `dennispike/fakie:latest`

Fakie supports:
 - Log file upload and storage 
 - Submission of files to Azure Sentinel via 
        - Syslog and CEF formatted Syslog files to Syslog Collector (currently external only)
        - JSON formatted files to Sentinel API 
 - Saving Syslog and API Settings for ease of use

### Usage
Docker Getting Started:
https://docs.docker.com/get-started/

From Zero to Fakie: install and configure Docker and get Fakie running in Windows 10:
https://github.com/daspiker/fakie/blob/main/GettingStartedWin10.md

How to Fakie:
https://github.com/daspiker/fakie/blob/main/HowToFakie.md

### Contributing
No one wants to Fakie alone!  Please reach out via the Issues link in this repo if you find a problem, have feedback or would like to get involved in contributing.  We follow a normal Pull Request process for submissions. 

### Contributors
- Dennis Pike
- Beth Bischoff
- Umesh Nagdev
