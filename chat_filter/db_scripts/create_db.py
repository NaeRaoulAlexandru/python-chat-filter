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
    )

    cursor = connexion.cursor()
    database=configData["database"]
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {configData['database']}")
