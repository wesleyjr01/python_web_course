# Cron Job
* In this video we are going to create a Job that runs every hour/day, that we check our alerts, and send out emails if necessary. Basically all it's gonna do is run our alert updater, so anything that does, will do every hour/day.
* ```sudo vi /etc/crontab```, and this file is what finds jobs that run periodically.  You will see a file like this 
```
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
```
* So, in the line ```m h dom mon dow user  command``` we have **minute hour dayOfTheMonth monthNumber dayOfTheWeek user command**, a \* means all. For exampĺe ```17 *    * * *``` is a job that runs at the 17th minute of every hour, every day of the month, every month of the year and every day of the week, it is ran by the root user, and the command is ```cd / && run-parts --report /etc/cron.hourly```.
* We will run this command, to run our job every 29th minute of every hour :
```11 * * * * wesley cd /var/www/html/pricing-service && source venv/bin/activate && python alert_updater.py```