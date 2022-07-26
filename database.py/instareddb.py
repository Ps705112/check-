import pymongo
from info import DATABASE_URI, DATABASE_NAME
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

myclient = pymongo.MongoClient(DATABASE_URI)
mydb = myclient[DATABASE_NAME]

async def add_inst_filter(fileid, links): 
    mycol = mydb["instreddb"]
    mydict = {"fileid": str(fileid), "links": str(links) }
    
    try:
        x = mycol.insert_one(mydict)
    except:
        logger.exception('Some error occured!', exc_info=True)
                
async def remove_inst(fileid):
    mycol = mydb["instreddb"]
    myquery = { "fileid": str(fileid) }
    mycol.delete_one(myquery)
    
async def get_ids(fileid):
    mycol = mydb["instreddb"]
    myquery = { "fileid": str(fileid) }
    mydoc = mycol.find(myquery)
    for x in mydoc:
      return x 

async def get(id):
    mycol = mydb["instreddb"]
    for x in mycol.find():
        return x
