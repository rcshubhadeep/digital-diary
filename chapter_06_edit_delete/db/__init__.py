## Our imports for the DB here
from pymongo import MongoClient
from settings import MONGO_URL, DB_NAME, COLLECTION_NAME
import datetime
import sys
from bson.objectid import ObjectId ## To convert string obejct ID to ObjectId of MongoDB

## Creating the connection globally bacause we do not want to connect 
## for each request.
try:
    client = MongoClient(MONGO_URL)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
except Exception, ex:
    sys.exit()

def add_entry(user_name="", title="", date="", entry="", private=False):
    '''adds an diary entry to the DB.'''
    create_date = None
    try: ## Extra safety because of the fact that user can override the datepicker.
        create_date = datetime.datetime.strptime(date, "%m/%d/%Y")
    except:
        create_date = datetime.datetime.today()
    
    data_to_save = {"user": user_name,
                    "title": title,
                    "date": create_date,
                    "entry": entry,
                    "is_private": private} 
                    ## Notice instead of using a character like "y" we are using Python's booolean directly here
                    ## ALSO notice that it is EASY to add a new key=>value pair in the present document 
                    ## structure. Mongo is not going to complain that we did not have this for earlier ones
    try:
        collection.insert(data_to_save) ## Pymongo's method to insert a document in MongoDB
        return True ## The save operation has completed successfully.
    except:
        return False ## OOPS! Something went worng.

def get_entries():
    '''Gets the entery from MongoDB. right now, without any conditions'''
    try:
        return collection.find().sort("date", -1) ## We are sorting by date in DESC order.Newest entry first.
    except:
        return None

def get_entry(ent_id):
    ''' Notice that instead of find we are using find_one here'''
    try:
        ## Notice the way we specify AND condition in pymongo.
        ## We can obviously do with a explicit "$and". But this is short hand 
        return collection.find_one({"_id": ObjectId(ent_id), "is_private": False}) 
    except:
        return None

def search_by_username(username):
    try:
        ## We will be filttering this data by user name. And ovbiously giving due respect to the privacy
        return collection.find({"user": username, "is_private": False})
    except:
        return None

def delete_entry(entry_id):
    '''This function will delete an entry by searching it in DB'''
    try:
        collection.remove({"_id": ObjectId(entry_id)})
        return True
    except:
        return False

def edit_entry(entry_id, body):
    try:
        ## As we are using multi=False, we have to use the MongoDB $set operator
        ## to Update the collection.
        collection.update({"_id": ObjectId(entry_id)},
                          {"$set": {"entry": body}},  multi=False)
        return True
    except Exception, ex:
        print ex
        return False