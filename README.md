# Fakie

![Icon](https://github.com/daspiker/fakie/blob/main/app/static/fakie.jpg)

Fakie aims to make it easy to push logs into Azure Sentinel.  

Built a new analytics rule and want to see if it works?

Fakie!

Layed out a rad new workbook and want to see if it populates properly?

Fakie!

Want to re-live your youth where your new Airwalks were way cooler than your actual skating ability?

Sorry, Fakie can only do so much!

### Overview
 Fakie is built in Python using the Flask Web Framework and has been Dockerized for easy deployment here:
 https://hub.docker.com/r/dennispike/fakie
 
 The latest build can be pulled from:
 dennispike/fakie:latest

Fakie supports:
 - Log file upload and storage 
 - Submission of files to Azure Sentinel via 
        - Syslog and CEF formatted Syslog files to Syslog Collector (currently external only)
        - JSON formatted files to Sentinel API 
 - Saving Syslog and API Settings for ease of use

### Usage
Head over to the [WIKI](https://github.com/BlueTeamLabs/sentinel-attack/wiki) to learn how to deploy and run Sentinel ATT&CK.

A copy of the DEF CON 27 cloud village presentation introducing Sentinel ATT&CK can be found [here](https://2019.cloud-village.org/#talks?olafedoardo) and [here](https://github.com/BlueTeamToolkit/sentinel-attack/tree/master/docs/DEFCON_attacking_the_sentinel.pdf).

### Contributing
No one wants to fakie alone!  Please reach out via the Issues link in this repo if you find a problem, have feedback or would like to get involved in contributing.  We follow a normal Pull Request process for submissions. 

### Contributors
- Dennis Pike
- Beth Bischoff
- Umesh Nagdev
