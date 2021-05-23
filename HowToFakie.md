## How To Fakie

Not this Fakie!
https://www.youtube.com/watch?v=QNO3qjNkdxc&t=97s

Once you have Fakie up and running and can reach the website, how do you use it?

**Upload Log files that you want to send into Sentinel**

There are two log files included:

- testJson.json - this is a known good test file for the API job option
- testCEF.txt - this is a known good test file for the CEF job option

The Syslog/CEF Collector will only work with syslog or CEF encoded syslog.  The API will only work with JSON encoded files.  Fakie does not verify the format of the files.  The test files will verify if things are working with a known good file.  If that works and your file doesn't then it likely isn't properly formatted logs.

This animation shows how to upload your own:

![ubuntu1](https://github.com/daspiker/fakie/blob/main/app/static/fakie_upload_animated.gif)

**Enter Syslog and/or API Settings**

You don't have to do this step but you can enter you Syslog/CEF collector IP address and/or API Log Analytics Workspace information here once and it is saved and will be the default in the Job section.

Fakie does not currently support its own Syslog/CEF collector so you will need to have one configured and working that you can reach from the machine running Fakie.

The Log Analytics Workspace Settings can be found at:

Workspace Id: Azure Sentinel > Settings >  Workspace settings > Workspace ID

Workspace Key: Azure Sentinel > Settings >  Workspace settings > Agents Management > Primary key or Secondary key

This animation shows how to put in your settings:

![ubuntu1](https://github.com/daspiker/fakie/blob/main/app/static/fakie_settings_syslog_api_animated.gif)

**Run a Job**

Now you can upload the logs to Sentinel via the Job page.  

This animation shows how to setup and run a Job::

![ubuntu1](https://github.com/daspiker/fakie/blob/main/app/static/fakie_job_animated.gif)