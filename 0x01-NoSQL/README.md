# 0x01. NoSQL
An introductory project on:
- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements
### MongoDB Command File
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `MongoDB` (version 4.2)
### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7) and `PyMongo` (version 3.10)
- The first line of all your files should be exactly `#!/usr/bin/env python3`

## File Descriptions
### Mandatory
1. [0-list_databases](./0-list_databases) - a script that lists all databases in MongoDB
   
    **Execution Example**:
    ```
    guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
    MongoDB shell version v3.6.3
    connecting to: mongodb://127.0.0.1:27017
    MongoDB server version: 3.6.3
    admin        0.000GB
    config       0.000GB
    local        0.000GB
    logs         0.005GB
    bye
    guillaume@ubuntu:~/0x01$
    ```

2. [1-use_or_create_database](./1-use_or_create_database) - a script that creates or uses the database `my_db`
   
    **Execution Example**:
    ```
    guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
    MongoDB shell version v3.6.3
    connecting to: mongodb://127.0.0.1:27017
    MongoDB server version: 3.6.3
    admin        0.000GB
    config       0.000GB
    local        0.000GB
    logs         0.005GB
    bye
    guillaume@ubuntu:~/0x01$
    guillaume@ubuntu:~/0x01$ cat 1-use_or_create_database | mongo
    MongoDB shell version v3.6.3
    connecting to: mongodb://127.0.0.1:27017
    MongoDB server version: 3.6.3
    switched to db my_db
    bye
    guillaume@ubuntu:~/0x01$
    ```

3. [2-insert](./2-insert) - a script that inserts a document in the collection `school`:
    -  The document must have one attribute `name` with value “Holberton school”
    - The database name will be passed as option of `mongo` command
      
    **Execution Example**:
    ```
    guillaume@ubuntu:~/0x01$ cat 2-insert | mongo my_db
    MongoDB shell version v3.6.3
    connecting to: mongodb://127.0.0.1:27017/my_db
    MongoDB server version: 3.6.3
    WriteResult({ "nInserted" : 1 })
    bye
    guillaume@ubuntu:~/0x01$
    ```

4. [3-all](./3-all) - a script that lists all documents in the collection `school`:
      
    **Execution Example**:
   ```
   guillaume@ubuntu:~/0x01$ cat 3-all | mongo my_db
   MongoDB shell version v3.6.3
   connecting to: mongodb://127.0.0.1:27017/my_db
   MongoDB server version: 3.6.3
   { "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
   bye
   guillaume@ubuntu:~/0x01$
   ```
  
5. [4-match](./4-match) - a script that lists all documents with `name="Holberton school"` in the collection `school`:
   
   **Execution Example**:
   ```
   guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
   MongoDB shell version v3.6.3
   connecting to: mongodb://127.0.0.1:27017/my_db
   MongoDB server version: 3.6.3
   { "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
   bye
   guillaume@ubuntu:~/0x01$
   ```

6. [5-count](./5-count) - a script that displays the number of documents in the collection `school`:
   
   **Execution Example**:
   ```
   guillaume@ubuntu:~/0x01$ cat 5-count | mongo my_db
   MongoDB shell version v3.6.3
   connecting to: mongodb://127.0.0.1:27017/my_db
   MongoDB server version: 3.6.3
   1
   bye
   guillaume@ubuntu:~/0x01$
   ```

7. [6-update](./6-update) - a script that adds a new attribute to a document in the collection `school`:
   - The script should update only document with `name="Holberton school"` (all of them)
   - The update should add the attribute `address` with the value “972 Mission street”
   
   **Execution Example**:
   ```
   guillaume@ubuntu:~/0x01$ cat 6-update | mongo my_db
   MongoDB shell version v3.6.3
   connecting to: mongodb://127.0.0.1:27017/my_db
   MongoDB server version: 3.6.3
   WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
   bye
   guillaume@ubuntu:~/0x01$ 
   guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
   MongoDB shell version v3.6.3
   connecting to: mongodb://127.0.0.1:27017/my_db
   MongoDB server version: 3.6.3
   { "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school", "address" : "972 Mission street" }
   bye
   guillaume@ubuntu:~/0x01$ 
   ```

8. [7-delete](./7-delete) - a script that deletes all documents with `name="Holberton school"` in the collection `school`:

   **Execution Example**:
   ```
   guillaume@ubuntu:~/0x01$ cat 7-delete | mongo my_db
   MongoDB shell version v3.6.3
   connecting to: mongodb://127.0.0.1:27017/my_db
   MongoDB server version: 3.6.3
   { "acknowledged" : true, "deletedCount" : 1 }
   bye
   guillaume@ubuntu:~/0x01$ 
   guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
   MongoDB shell version v3.6.3
   connecting to: mongodb://127.0.0.1:27017/my_db
   MongoDB server version: 3.6.3
   bye
   guillaume@ubuntu:~/0x01$
   ```

9. [8-all.py](./8-all.py) - a Python function that lists all documents in a collection:
   - Prototype: def `list_all(mongo_collection):`
   - Return an empty list if no document in the collection
   - `mongo_collection` will be the `pymongo` collection object

   **Execution Example**:
   ```
   guillaume@ubuntu:~/0x01$ cat 8-main.py
   #!/usr/bin/env python3
   """ 8-main """
   from pymongo import MongoClient
   list_all = __import__('8-all').list_all
   
   if __name__ == "__main__":
       client = MongoClient('mongodb://127.0.0.1:27017')
       school_collection = client.my_db.school
       schools = list_all(school_collection)
       for school in schools:
           print("[{}] {}".format(school.get('_id'), school.get('name')))
   
   guillaume@ubuntu:~/0x01$ 
   guillaume@ubuntu:~/0x01$ ./8-main.py
   [5a8f60cfd4321e1403ba7ab9] Holberton school
   [5a8f60cfd4321e1403ba7aba] UCSD
   guillaume@ubuntu:~/0x01$ 
   ```
   
### Advanced
