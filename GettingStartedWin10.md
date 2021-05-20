## ***From Zero to Fakie: How to install and configure Docker and get Fakie running on Windows 10*** 

### Install Docker Desktop: 

-Download here: [Docker Hub](https://hub.docker.com/) (also, use this opportunity to create a Docker Hub Account, if you don’t have one) 

DON’T “try running a container” as the app suggests. We’ll get to that… 

-Install and Enable WSL2 

[Install WSL on Windows 10 | Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/install-win10) 

- -Open Powershell as admin, (to enable “Windows Subsystem for Linux”) Run: 

  `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart` 

- -Enable VM Platform: 

  `dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart` 

- -Restart! 

- -Open Powershell as admin again, then set WSL 2 as your Default version: 

  `wsl --set-default-version 2` 

 WSL 2 will now be default on any NEW Linux Distros installed. 

IF you HAD ALREADY INSTALLED prior to updating to WSL 2, then you’ll need to change your WSL version on the distro where you’ll be pulling/pushing containers. To get the details of the distributions and versions available, you can run: 

`wsl --list --verbose` 

Then you’ll be able to change to WSL 2 by running this command, grabbing the Distribution desired from above provided list: 

`wsl --set-version <distribution name> 2` 

-If you don’t already have it, download Ubuntu 18.04 from your Windows Store (which will now be installed with WSL 2 as the default): 

![ubuntu1](https://github.com/daspiker/fakie/blob/main/app/static/gswin10_ubuntu1.png)

-Run it. 

-Open Docker Desktop and log in. 

-Click Settings on the upper right 

![docker1](https://github.com/daspiker/fakie/blob/main/app/static/gswin10_docker1.png)

-Under “Resources”, Select “WSL Integration” 

![docker2](https://github.com/daspiker/fakie/blob/main/app/static/gswin10_docker2.png)

-switch on the WSL 2 integration with Ubuntu 18.04: 

![docker3](https://github.com/daspiker/fakie/blob/main/app/static/gswin10_docker3.png) 

-Apply & Restart. 

-Navigate to “Images.” (It will be empty, unless you made the mistake of running the pointless one suggested by the app). 

-Go back to your Ubuntu Terminal. (Here’s where the Magic Happens): 

-Enter pull command: 

`docker pull dennispike/fakie`  

It will tell you the default tag (latest) 

-Go back to Docker Desktop and see the container, whereby you can Run it: 

-Give it a name and tell it to use port 8000: 

![docker4](https://github.com/daspiker/fakie/blob/main/app/static/gswin10_docker4.png) 


-Navigate to: 

[http://127.0.0.1:8000](http://127.0.0.1:8000/) 

**It's Fakie Time!!!**