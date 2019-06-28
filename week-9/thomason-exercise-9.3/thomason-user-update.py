#/*
#============================================
#; Title: User Update
#; File Name: thomason-user-update.py
#; Author: William Thomason
#; Date:   27 July 2019
#; Description: Update User
#;===========================================
#*/

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(

    {"employee_id": "6825491"},

    {
        "$set": {
            "email": "Jesse.Freeman@me.com"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id": "6825491"}))