from pymongo import MongoClient

uri = "mongodb+srv://forosypaginas:cySVsfpMe2glBbWC@cluster0.g6tqipp.mongodb.net/"
client = MongoClient(uri)


try:
    database = client.get_database("contacts")
    movies = database.get_collection("contact")

    # Query inserting an element that has the name 'Mi'
    query = {"Name": "Mi"}
    contacto = movies.insert_one(query)

    print(contacto)

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
