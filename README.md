# Daily GitHub push

If you want to appear that you are a very active user in GitHub then this is the rigth tool

This is a python version I made form the shell script of [toxtli](https://github.com/toxtli/dailypush).

Execute the following commands:

> Fork this github application

> git clone .. your fork...

> cd dailypush

> Open crontab.txt and change the location of your application i.e. /home/your_laptop/dailypush/daily.py

> In your Terminal type **crontab crontab.txt** this will add a crontab that will execute **each minute**

> chmod +x daily.py

> **python daily.py** to try it

Every dot below this line is the number of times that the tool has been executed. A push is executed every minute. You can place this script on your server but make sure to run it (python daily.py) to make sure that this application run. Make sure also that you don't get a `Permission denied (publickey).` from Github. You should test this app by outputing your log to ***/1 * * * * ~/dailypush/daily.py > /var/log/daily.log 2>&1** and make sure to do a `sudo touch /var/log/daily.log && sudo chmod -R 777 /var/log/daily.log`

. . . . . . . . . . + + + + + + + + + + + + +