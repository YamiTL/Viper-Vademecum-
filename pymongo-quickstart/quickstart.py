from pymongo import MongoClient

uri = "mongodb+srv://forosypaginas:cySVsfpMe2glBbWC@cluster0.g6tqipp.mongodb.net/"
client = MongoClient(uri)

try:
    database = client.get_database("contacts")
    movies = database.get_collection("contact")

    # Query for a movie that has the title 'Back to the Future'
    query = {"Name": "Auca"}
    contacto = movies.find_one(query)

    print(contacto)

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
