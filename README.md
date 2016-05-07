# Daily GitHub push

If you want to appear that you are a very active user in GitHub then this is the rigth tool

This is a python version I made form the shell script of [toxtli](https://github.com/toxtli/dailypush).

Execute the following commands:

> Fork this github application

> git clone .. your fork...

> cd dailypush

> Open crontab.txt and change the location of your application i.e. /home/your_laptop/dailypush/daily.py

> In your Terminal type **crontab crontab.txt** this will add a crontab that will execute **each hour**

> chmod +x daily.py

> **python daily.py** to try it

Every dot below this line is the number of times that the tool has been executed. A push is executed every hour. You can place this script on your server but make sure to run it (python daily.py) to make sure that this application run.

. . .