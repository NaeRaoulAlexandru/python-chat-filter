import subprocess
import sys

while True:
    print("Welcome to this app, please choose what service you want")
    print("\nIf it's your fist time using the app, please choose option 3 and complete your setup")
    print("""
    1.Connect to a server
    2.Host a server
    3.Admin KIT 
    """)
    option = input("You chose: ")

    if option == '1':
        print("Connecting to a server")
        subprocess.run([sys.executable,"client.py"])
    elif option == '2':
        print("Hosting a server: ")
        subprocess.run([sys.executable,"server.py"])
    elif option == '3':
        print("Opening Admin KIT")
        subprocess.run([sys.executable,"adminkit.py"])
    else: print("Invalid option!")