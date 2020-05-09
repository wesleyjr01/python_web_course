# Files Location and Configuration
* **GitHub Clode Placed in**: ```mkdir -p /var/www/html/pricing-service```. Noticed that when we create this directory, it will be owned by the root user, and you can check it by doing ```ls -al /var/www/html```, and we have to change that so our user can make changes in that directory. So to change the ownership of the directory, by doing ```sudo chown wesley:wesley /var/www/html/pricing-service```, what this does is it gives permission to this directory to our user wesley an our group wesley. So now we dont have to be **sudo** in the directory.
* Now we clone the code inside this direcotory: ```git clone https://github.com/wesleyjr01/web_flask_app .```
* We also need to create a log folder to see the logs if we have any problems, ```mkdir log```.
* Now lets create a virtualenv and install everything:
```
virtualenv venv -p python3.7
source venv/bin/activate
pip install -r requirements.txt
```
* To see if everything worked, just try to run the app: ```python app.py```. If it all worked, that's all good, just press CTRL+C.