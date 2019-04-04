from pymongo import MongoClient
democlient = MongoClient()
myclient = MongoClient('localhost', 27017)

# pour afficher la liste des differentes db on fait l'instruction suivante

print(myclient.list_database_names())
