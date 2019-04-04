from pymongo import MongoClient

democlient = MongoClient()
myclient = MongoClient('localhost', 27017)

# db name
mydb = myclient["demo"]

# collection name
mycoll=mydb["dbtable"]

mylist = [
	{"id": 1, "name": "Talz", "adresse": "Thiaroye"},
	{"id": 2, "name": "Razack", "adresse": "Grand Mbao"},
	{"id": 3, "name": "Ibson", "adresse": "Zack Mbao"},
	{"id": 4, "name": "Ibou", "adresse": "Rufisque"},
	{"id": 5, "name": "Rifche", "adresse": "PA"},
	{"id": 6, "name": "Kheuch", "adresse": "Medina"},
	{"id": 7, "name": "Blaa", "adresse": "Medina"},
	{"id": 8, "name": "Med", "adresse": "Ngor"},
	{"id": 9, "name": "Maf", "adresse": "Yarakh"},
	{"id": 10, "name": "Tichou", "adresse": "Grand Yoff"},
	{"id": 11, "name": "MLD", "adresse": "Fass"},
	{"id": 12, "name": "Youm", "adresse": "Plateau"},
	{"id": 13, "name": "Issa", "adresse": "TivaounePeulh"},
	{"id": 14, "name": "Moussa", "adresse": "Guediawaye"}
]

x = mycoll.insert_many(mylist)

dblist = myclient.list_database_names()

if input("Enter DB: ") in dblist:
	print("The database exists.")
else:
	print("Not present")

print(dblist)