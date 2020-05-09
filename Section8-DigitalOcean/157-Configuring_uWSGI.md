# Configuring uWSGI
* We will be configuring **uWSGI** so that it can run our application when **nginx** talks to it. By using **nginx** to talk to **uWSGI**, and uWSGI to talk to our app, we're going to create higher performance and more security.
* Let's begin by modifying our uwsgi.ini file. We will delete all of the lines and rewrite it, the final form is below:
```
[uwsgi]
base = /var/www/html/pricing-service
app = app
module = %(app)
home = %(base)/venv
pythonpath = %(base)
socket = %(base)/socket.sock

chmod-socket = 777

processes = 8
threads = 8

harakiri = 15

callable = app

logto = %(base)/log/%n.log
```
* **base** : the base defines where the home folder of our application is, and that's in var/www/html/pricing-service.
* **app** : it tells which file contains our app, it could be ```app = run``` the the file name to run our app was run.py.
* **module** : which module we should import in order to include our app, and that also is the app module, and here we use the ```%()``` to refer to the variable ```app```.
* **home**: now we have to tell uwsgi where our virtual environment is located. Since our virtualenvironment called venv is located in the base directory, we can use ```home = %(base)/venv```.
* **pythonpath**: the pythonpath defines where the top level of our application is, so that when we import any local files, we will look there first.
* **socket**: this is a file that contains some information so that nginx can talk to uWSGI.
* **chmod-socket** : we need to make sure that this socket can be read and written to by anybody, including the nginx users, so we set it to 777.
* **process / threads** : 8 threads and 8 processes mean a total of 64 independent instances running of our application, which means that we can serve more users at once. However, the more procesess and threads you have, the less resources each one has, by your application. 8 / 8 is a fine number. Search for **Load Testing** if you want to read more about it.
* **harakiri** : this is how many seconds we will wait before killing one of these threads, if there is an error.
* **callable** : is the anme of you Flask variable in app.py, The line usually goes: ```app = Flask(__name__)```. We don't use %(app) because we could change the file name without changing the variable name, so we want to keep them separate.
* **logto**: where we are going to log to, this is just going to create a file called uWSGI.log, and is going to write our applications output and any other Python output into it. If we do have any application erros, we will be checking uWSGI.log inside the log folder.
* Thats all for the uwsgi file!
# Create a System Daemon to start  uWSGI for us.
* ```sudo vi /etc/systemd/system/uwsgi_pricing_service.service```. Then we will write a bunch of stuff, the final code is below:
```
[Unit]
Description=uWSGI Pricing Service

[Service]
User=wesley
Group=wesley
WorkingDirectory=/var/www/html/pricing-service
Environment=MONGODB_URI=mongodb://127.0.0.1:27017/fullstack
ExecStart=/var/www/html/pricing-service/venv/bin/uwsgi --master --emperor /var/www/html/pricing-service/uwsgi.ini --die-on-term --uid wesley --gid wesley --logto /var/www/html/pricing-service/log/emperor.log
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAcess=all

[Install]
WantedBy=multi-user.target
```
* Now you can save, write and quit (ESC+:wq).
* And there is one more thing, in case we haven't done it already, which is ```touch log/emperor.log```.
* Now ```sudo systemctl daemon-reload```
* Now ```sudo systemctl start uwsgi_pricing_service```. Hopefully, nothing happened, no errors.