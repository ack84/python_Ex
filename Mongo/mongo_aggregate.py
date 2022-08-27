
from pymongo import MongoClient

#MongoDB Connection
client = MongoClient (host='localhost', port=27017)

db = client.test
collection = db.drive_hyun

# MongoDB data insert
collection.agreegate([
                    {$match : {"car_id":"HYUN_AAA"}},
                    {$project: }
                    {$group: {
                    "_id":"car_id"}}
                    ])


# MongoDB Connection close
client.close()


$unwind 보다 
$facet