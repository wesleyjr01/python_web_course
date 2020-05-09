# Steps
* Allow user **wesley** to temporarily become the root user, to have all the privileges: ```visudo```. Right below the line ```root ALL=(ALL:ALL) ALL``` type in ```wesley ALL=(ALL:ALL) ALL```. Save it: ```CTRL+O, ENTER, CTRL+X```.
* Now we will allow **wesley** to log in: ```vi /etc/ssh/sshd_config```. Then scroll to the line ```PasswordAuthentication yes```, and make sure it is with **yes**. Next, we are going to find ```PermitRootLogin yes```, and set it to **no**, now press ```ESC, :w``` to save the file. So now we dissallowed the root user to log in our server, for security.
* Now go to the very end of the file, press the ```I``` key and then type ```AllowUsers wesley```, now save and quit ```ESC, :wq```.
* Now in the terminal press ```service sshd reload```. Now you cant just logout ```logout```.
* To log back in just type in the terminal ```<username>@<IPv4>``` and then type in the password for the user.
* Log in as <username> and do: ```sudo apt update```.