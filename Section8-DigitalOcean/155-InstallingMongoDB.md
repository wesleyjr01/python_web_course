# Steps
* ```sudo apt install mongodb```. That's it.
* Check if it is running already: ```sudo systemctl status mongodb```. You see it is already running, that's because installing MongoDB in this way sets it as a service, that means that it will run when your server restarts. If you want to disable that do ```sudo systemctl disable mongodb```. If you do that, you will have to start and stop MongoDB manually.
* If you have MongoDB installed, you can do ```mongo``` to connec to MongoDB.