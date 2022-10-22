from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://localhost:48621')
        #self.client = MongoClient('mongodb://%s:%s@localhost:48621/' % (username, password))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  # data should be dictionary
            
            # checking to see to see if the data stored or not
            if insert is not None:
                workPlease = True
            else:
                workPlease = False
            return workPlease
        else:
            raise Exception("Nothing to save because data parameter is empty")
            
        
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data)
        else:
            print('Nothing to read, because data parameter is empty')
            return False
    
    def read_all(self,data):
        curser = self.database.animals.find(data, {'_id':False} )
        return curser
              
        
        
    def update(self, info, newData):
        if info is not None and newData is not None:
            plsWork = self.database.animals.update_many(info, {'$set':newData})
            #self.read(newData)
            return plsWork
        else:
            raise Exception("Please enter the info")
            
            
    def delete(self, lookUp):
        if lookUp is not None:
            delete = self.database.animals.delete_many(lookUp)
            return delete
        else:
            raise Exception("Please try again")
            
