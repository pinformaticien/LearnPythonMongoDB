from pymongo import MongoClient
democlient = MongoClient()
myclient = MongoClient('localhost', 27017)

mydb = myclient["demo"]
mycoll = mydb["dbtable"]

#for finding single occurence in collection
x = mycoll.find_one()
print(x,"\n\n")

#for finding all occurences in collection
for x in mycoll.find():
	print(x)