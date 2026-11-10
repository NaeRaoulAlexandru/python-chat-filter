import mysql.connector
import json

def createdb():

    with open("config.json", "r") as f:
        configData = json.load(f)

    connexion = mysql.connector.connect(
        host=configData["host"],
        user=configData["user"],
        password=configData["password"],
        port=configData["port"],
        database=configData["database"]
    )

    cursor = connexion.cursor()
    cursor.execute(f"CREATE DATABASE {configData['database']}")