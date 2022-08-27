from pymongo import MongoClient
import datetime
import random
import string

#MongoDB Connection
client = MongoClient (host='localhost', port=27017)

db = client.test
collection = db.drive_hyun

#x,y좌표 문자,숫자 랜덤값 생성을 위한 변수
xy_length = 12
string_pool = string.ascii_letters + string.digits

#x 좌표 문자,숫자 랜덤값 생성 함수 
def xdata ():
  insertdatax = ""
  for x in range(xy_length):
    insertdatax += random.choice(string_pool)
  return insertdatax

#y 좌표 문자,숫자 랜덤값 생성 함수
def ydata ():
  insertdatay = ""
  for x in range(xy_length):
    insertdatay += random.choice(string_pool)
  return insertdatay

# dummy insert 값 생성
testdata = {
    "car_id": "HYUN_AAAA",
    "mvmnDtlHst": [
    {
    "time": datetime.datetime.utcnow() -1,
    "speed": random.randint(1,99),
    "rpm": random.randint(1,200),
    "x": xdata(),
    "y": ydata()},
    {
    "time": datetime.datetime.utcnow() -2,
    "speed": random.randint(1,99),
    "rpm": random.randint(1,200),
    "x": xdata(),
    "y": ydata()},
    {
    "time": datetime.datetime.utcnow(),
    "speed": random.randint(1,99),
    "rpm": random.randint(1,200),
    "x": xdata(),
    "y": ydata()},
    {
    "time": datetime.datetime.utcnow(),
    "speed": random.randint(1,99),
    "rpm": random.randint(1,200),
    "x": xdata(),
    "y": ydata()}
    ]
}

# MongoDB data insert
collection.insert_one(testdata)

# MongoDB Connection close
client.close()