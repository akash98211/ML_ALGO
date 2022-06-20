from typing import Collection
from pymongo import MongoClient, mongo_client
import config

database = config.DATABASE
mongodb_port = 27017

uri = f'mongodb://localhost:{mongodb_port}/'

mongo_db_client = MongoClient(uri)

db = mongo_db_client[database]

collection_user = db['user_details']

def register_user(data):
    print("***************************************")

    name = data['name']
    lastname = data['lastname']
    emailid = data['emailid']
    mobile_number = int(data['mobile_number'])
    password = data['password']

    print('name,lastname,emailid,mobile_number,password\n',name,lastname,emailid,mobile_number,password)

    response = collection_user.find_one({"Email ID":emailid, "Mobile Number ": mobile_number})
    print("Response ::::::::::::::",response)
    if not response:
        print("Response ",response)
        collection_user.insert_one({"Name":name, "Last Name": lastname, "Email ID":emailid,
                    "Mobile Number ": mobile_number,"Password": password })
        return "Registered Successfully"

    else:
        return "User already exist"


def login_user(data):

    emailid = data['emailid']
    password = data['password']
    print("******************************",data)
    response = collection_user.find_one({"Email ID":emailid, "Password": password})

    if response:
        return "Login Successful"

    else:
        return "Email id or password is incorrect"
