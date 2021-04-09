#! /bin/bash

#NOW=`date '+%F %H:%M:%S'`;
NOW=`date -u`;

###Brute Force Attack###

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000064 - user name does not exist|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start=$NOW end=$NOW suser= duser=StMarsh src=179.124.202.253 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC000006A - user name is correct but the password is wrong|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start=$NOW end=$NOW suser= duser=KyBroflovski src=113.160.112.125 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000234 - user is currently locked out|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start= end= suser= duser=KeMcCormick src=196.45.177.52 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000072- account is currently disabled|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start= end= suser= duser=BuStotch src=196.45.177.52 dst=158.81.26.141 shost= dhost= dstdestinationDnsDomain=dc.domain"

###Sleep for 5 seconds###
sleep 5s

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000064 - user name does not exist|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start=$NOW end=$NOW suser= duser=WeTestaburger src=179.124.202.253 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC000006A - user name is correct but the password is wrong|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start=$NOW end=$NOW suser= duser=TwTweak src=113.160.112.125 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000234 - user is currently locked out|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start= end= suser= duser=BeStevens src=196.45.177.52 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000072- account is currently disabled|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start= end= suser= duser=BrBiggle src=196.45.177.52 dst=158.81.26.141 shost= dhost= dstdestinationDnsDomain=dc.domain"

###Sleep for 5 seconds###
sleep 5s

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000064 - user name does not exist|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start=$NOW end=$NOW suser= duser=ClDonovan src=179.124.202.253 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC000006A - user name is correct but the password is wrong|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start=$NOW end=$NOW suser= duser=CrTucker src=113.160.112.125 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000234 - user is currently locked out|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start= end= suser= duser=JiValmer src=196.45.177.52 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000072- account is currently disabled|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start= end= suser= duser=TiBurch src=196.45.177.52 dst=158.81.26.141 shost= dhost= dstdestinationDnsDomain=dc.domain"

###Sleep for 5 seconds###
sleep 5s

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000064 - user name does not exist|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start=$NOW end=$NOW suser= duser=RaMarsh src=179.124.202.253 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC000006A - user name is correct but the password is wrong|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start=$NOW end=$NOW suser= duser=ShMarsh src=113.160.112.125 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000234 - user is currently locked out|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start= end= suser= duser=JiKern src=196.45.177.52 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000072- account is currently disabled|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start= end= suser= duser=BrBiggle src=196.45.177.52 dst=158.81.26.141 shost= dhost= dstdestinationDnsDomain=dc.domain"

###Sleep for 5 seconds###
sleep 5s

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000064 - user name does not exist|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start=$NOW end=$NOW suser= duser=GeBroflovski src=179.124.202.253 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC000006A - user name is correct but the password is wrong|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start=$NOW end=$NOW suser= duser=ShBroflovski src=113.160.112.125 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000234 - user is currently locked out|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start= end= suser= duser=KySchwartz src=196.45.177.52 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|0xC0000072- account is currently disabled|4625 - An account failed to log on.|1|act=Failure deviceExternalID=4625 start= end= suser= duser=JaTenorman src=196.45.177.52 dst=158.81.26.141 shost= dhost= dstdestinationDnsDomain=dc.domain"

###Sleep for 10 seconds###
sleep 10s

###Successful login to one of the Brute Force targeted accounts; 158.81.26.141###

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|10 - RemoteInteractive|4624 - An account was successfully logged on.|2|act=Success deviceExternalID=4624 start= end= suser= duser=ErCartman src=196.45.177.52 dst=158.81.26.141 shost= dhost= destinationDnsDomain=dc.domain"

###Sleep for 30 seconds###
sleep 30s

###Login to 172.16.1.4(DMZ_Workstation)###

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|10 - RemoteInteractive|4624 - An account was successfully logged on.|2|act=Success deviceExternalID=4624 start= end= suser= duser=ErCartman src= dst=172.16.1.4 shost= dhost=DMZ_Workstation destinationDnsDomain=dc.domain"


###Sleep for 60 seconds###
sleep 60s


###Login to AD, change an existing IOT authorised user password create new user account, added to IOT authroized user group, reset password; 172.16.16.100 (dc.domain)###

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|2019|10 - RemoteInteractive|4624 - An account was successfully logged on.|2|act=Success deviceExternalID=4624 start= end= suser=ErCartman duser=StMarsh-sa src=172.16.1.4 dst=172.16.16.100 shost=DMZ_Workstation dhost=dc.domain destinationDnsDomain=dc.domain"

###Sleep for 10 seconds###
sleep 10s

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|2019||4723 - An attempt was made to change an account's password|1|act=Failure deviceExternalID=4723 start= end= suser=StMarsh-sa  duser=ErCartman-IOT src= dst=172.16.16.100 shost= dhost=dc.domain destinationDnsDomain=dc.domain"

###Sleep for 30 seconds###
sleep 30s

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|2019||4720 - A user account was created.|2|act=Success deviceExternalID=4720 start= end= suser=StMarsh-sa duser=LiCartman-IOT src= dst=172.16.16.100 shost= dhost=dc.domain destinationDnsDomain=dc.domain"

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|2019||4724 - An attempt was made to reset an account's password|2|act=Success deviceExternalID=4724 start= end= suser=StMarsh-sa duser=LiCartman-IOT src= dst=172.16.16.100 shost= dhost=dc.domain destinationDnsDomain=dc.domain"

###Sleep for 20 seconds###
sleep 20s

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|2019||4728 - A member was added to a security-enabled global group|2|act=Success deviceExternalID=4728 start= end= suser=StMarsh-sa duser=LiCartman-IOT src= dst=172.16.16.100 shost= dhost=dc.domain destinationDnsDomain=dc.domain dpriv=dc.domain\IOT-Engineering"

###Sleep for 60 seconds###
sleep 60s

###Login to Process control asset; 192.168.1.80(PCN_NTPSrvr)###

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|10 - RemoteInteractive|4624 - An account was successfully logged on.|2|act=Success deviceExternalID=4624 start= end= suser=ErCartman duser=LiCartman-IOT src=172.16.1.4 dst=192.168.1.80 shost=DMZ_Workstation dhost=PCN_NTPSrvr destinationDnsDomain=dc.domain"

###Sleep for 60 seconds###
sleep 60s

###Login to Engineering workstation; 192.168.1.81(S7EWSBldg6)###

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10|10 - RemoteInteractive|4624 - An account was successfully logged on.|2|act=Success deviceExternalID=4624 start= end= suser=LiCartman-IOT duser=S7EWSBldg6\cooladmin src=192.168.1.80 dst=192.168.1.81 shost=PCN_NTPSrvr dhost=S7EWSBldg6 destinationDnsDomain= "

###Sleep for 120 seconds###
sleep 120s

###Delete log traces - remove group membership, delete account, clear audit logs###

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10||1102 - The audit log was cleared|2|act=Success deviceExternalID=1102 start= end= suser=cooladmin duser= src= dst=192.168.1.81 shost= dhost=S7EWSBldg6 destinationDnsDomain=S7EWSBldg6"

###Sleep for 30 seconds###
sleep 30s

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10||1102 - The audit log was cleared|2|act=Success deviceExternalID=1102 start= end= suser=LiCartman-IOT duser= src= dst=192.168.1.80 shost= dhost=PCN_NTPSrvr destinationDnsDomain=dc.domain"

###Sleep for 30 seconds###
sleep 30s

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|2019||4729 - A member was removed from a security-enabled global group|2|act=Success deviceExternalID=4729 start= end= suser=StMarsh-sa duser=LiCartman-IOT src= dst=172.16.16.100 shost= dhost=dc.domain destinationDnsDomain=dc.domain dpriv=dc.domain\IOT-Engineering"

###Sleep for 30 seconds###
sleep 30s

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|2019||4726 - A user account was deleted.|2|act=Success deviceExternalID=4726 start= end= suser=StMarsh-sa duser=LiCartman-IOT src= dst=172.16.16.100 shost= dhost=dc.domain destinationDnsDomain=dc.domain"

###Sleep for 30 seconds###
sleep 30s

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|10||1102 - The audit log was cleared|2|act=Success deviceExternalID=1102 start= end= suser=ErCartman duser= src= dst=172.16.1.4 shost= dhost=DMZ_Workstation destinationDnsDomain= "

logger -p auth.info -n localhost -t CEF "CEF:0|Microsoft|Microsoft-Windows-Security-Auditing|2019||1102 - The audit log was cleared|2|act=Success deviceExternalID=1102 start= end= suser=StMarsh-sa duser= src= dst=172.16.16.100 shost= dhost=dc.domain destinationDnsDomain= "