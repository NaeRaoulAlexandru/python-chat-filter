from db_scripts import create_db,table_create,verify_db,queries
import mysql.connector
import json

#CONNECTION IS KEY WORD, THATS WHY I PUT CONNEXION

while True:
    while True:
        print("""Hello admin, please make your choice:
                       1 --> No existing database. Let's create one
                       2 --> Existing database. Let's analyze it
                       3 --> Enter queries menu\n""")
        start = input("You chose: ")
        if start in ['1','2','3']: break
        else: print("Invalid option")

    match start:
        case '1':
            print("1 --> No existing database. Let's create one")
            try:
                while True:
                    isMade = input("Do you have your Docker container turned on with the db? Y/n\n")
                    if isMade == 'Y':
                        host=input("Enter host: ")
                        user=input("Enter user: ")
                        password=input("Enter password: ")
                        port=input("Enter port: ")
                        break
                    elif isMade == 'n':
                         print("""Open the Docker terminal and run the command as in the ex
                         docker run --name mysql-server -e MYSQL_ROOT_PASSWORD=parola_secreta -e MYSQL_DATABASE=activitati -p 3306:3306 -d mysql
                         
                         You can change these parameters but remember them! 
                         host="localhost", user="root", password="parola_secreta",  port="3306"\n
                         """)

                         print("Please provide how you entered the parameters")
                         host = input("Enter host: ")
                         user = input("Enter user: ")
                         password = input("Enter password: ")
                         port = input("Enter port: ")
                         break
                    else: print("Invalid answer")
                print("Now that we have our Docker container configured. Lets create our database")
                nameDB = input("Enter your schema (database) name: ")

                #SAVE TO USE IN OTHER FILES
                db_config = {
                    "host": host,
                    "user": user,
                    "password": password,
                    "port": port,
                    "database": nameDB
                }

                with open("config.json", "w") as f:
                    json.dump(db_config, f, indent=4)

                create_db.createdb()
                table_create.createtable()

                print("You have saved your db config and created it(+tables).")
                print("This version has preset tables, you can see them in the analyze menu!")
            except mysql.connector.errors.InterfaceError:
                print("Your container is not working!")
        case '2':
            print("2 --> Existing database. Let's analyze it")
            try:
                verify_db.verifydb()
            except mysql.connector.Error:
                print("Docker container is not opened")
        case '3':
            try:
                with open("config.json", "r") as f:
                    configData = json.load(f)

                connexion = mysql.connector.connect(
                    host=configData["host"],
                    user=configData["user"],
                    password=configData["password"],
                    port=configData["port"],
                    database=configData["database"]
                )

                print("3 --> Enter queries menu")
                while True:
                    print(""" 
                     0.Exit
                     1.Check user status
                     2. Update user status
                     3. Check user address
                     4. Check user logs
                     5. Insert word
                     6. Delete word
                     7. Show table content""")

                    option = input("You chose: ")
                    match option:
                        case '0':
                            print("Exit")
                            break
                        case '1':
                            result = queries.checkstatus(connexion, input("Enter address: "))
                            if result == 1: print("User is BANNED!")
                            else: print("User is NOT banned!")
                        case '2': queries.adminupdatestatus(connexion, input("Update user status: "))
                        case '3':
                            result = queries.checkaddr(connexion, input("Check user address: "))
                            if result == 1: print("Address exists!")
                            else: print("Address not found! ")
                        case '4': queries.checklogs(connexion, input("Check logs for user: "))
                        case '5': queries.wordadd(connexion, input("Add word to banned_words: "))
                        case '6': queries.worddelete(connexion ,input("Delete word to banned words: "))
                        case '7': queries.showtablecontent(connexion, input("You want to see contents in table: "))
                        case '': print("Invalid option")
            except mysql.connector.Error:
                print("Docker container is not opened")
                continue
            except FileNotFoundError:
                print("config.json doesn't exist")

