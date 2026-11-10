import mysql.connector
import json

def verifydb():
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

    while True:
        print("""Verifica urmatoarele:
        0.Exit
        1.Check DB existance
        2.Check tables
        """)
        option = input("You chose: ")

        if option=='0': break

        elif option=='1':

            cursor.execute("SHOW DATABASES")
            result = cursor.fetchall()

            if (configData["database"],) in result: print("Exists!")
            else: print("Doesn't exist!");

        elif option=='2':
            cursor.execute(f"USE {configData['database']}")
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()

            print("The tables are:")
            for tabel in tables:
                print(tabel[0])


        else: print("Invalid answer")