# DB for Microblog
* In this section we will be creating a microblog, and in order to store the microblog posts, we're going to need a database, so we're going to be using MongoDB.
* Let's go to https://www.mongodb.com/download-center/community to download MongoDB.
* To start the mongodb server, and then open MongoDB:
```systemctl start mongod```  
```mongo```
* To stop the mongodb server:  
```systemctl stop mongod``` 
* You can optionally ensure that MongoDB will start following a system reboot by issuing the following command:  
```sudo systemctl enable mongod```
# Why MongoDB  
* Show databases: ```show dbs```
* Enter a database: ```use <db_name>```
* Show collections in a db: ```show collections```
* If you want to insert some data into a specific collection, in the current database \<db_name\>:  
```use <db_name>```  
```db.<collection_name>.insert(<JSON>)```  
```example: database1.students.insert({"name": "Jose", "mark": 99})```
* In order to find data:  
```<db_name>.<collection_name>.find(<JSON>), this command finds everything in the collection.```  
```example: database1.items.find({}), this command finds everything in the collection.```
* In order to remove data:  
```<db_name>.<collection_name>.remove(<JSON>)```  
```example: database1.students.remove({"item": "Chair"})```
* One problem that may happen with MongoDB is that we may insert new data that is not in the same format of the collection.