import mysql.connector
import json

def createtable():

    with open("config.json","r") as f:
        configData = json.load(f)

    connexion = mysql.connector.connect(
        host=configData["host"],
        user=configData["user"],
        password=configData["password"],
        port=configData["port"],
        database=configData["database"]
    )

    cursor = connexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id_user INT PRIMARY KEY AUTO_INCREMENT,
            username TEXT NOT NULL,
            status INT DEFAULT 0
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_logs (
            id INT PRIMARY KEY AUTO_INCREMENT,
            id_user INT NOT NULL REFERENCES users(id_user),
            log TEXT NOT NULL,
            time DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS banned_words (
            id INT PRIMARY KEY AUTO_INCREMENT,
            bannedword TEXT
        ); 
    """)

    print("You created the tables!")
