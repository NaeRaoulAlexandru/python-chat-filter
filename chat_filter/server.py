import socket
import json
import mysql.connector
from db_scripts import  queries

#CONNECTION IS KEY WORD, THATS WHY I PUT CONNEXION
with open("config.json", "r") as f:
    configData = json.load(f)

connexion = mysql.connector.connect(
    host=configData["host"],
    user=configData["user"],
    password=configData["password"],
    port=configData["port"],
    database=configData["database"]
)


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print(f"""
        As a client you need to connect to the server address
        which is {IPAddr}  
      """
      )

#We listen to all ip addr existing
HOST = ''
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 5000))
server_socket.listen()

while True:

    c, addr = server_socket.accept()
    print("We are connected with: ", addr)

    if queries.checkaddr(connexion,addr[0]) == 0:  queries.insertaddr(connexion, addr[0])

    if queries.checkstatus(connexion, addr[0]) == 1:
        c.send('YOU ARE BANNED FROM OUR PLATFORM!'.encode())
        c.send('Connection ended.'.encode())
        c.close()
        continue

    c.send('You contacted our support, how can we help you?'.encode())

    while queries.checkstatus(connexion, addr[0]) == 0:
        c.send(('Support: ' + input()).encode())
        decodedMessage = c.recv(1024).decode()
        print(decodedMessage)

        #Add flag to stop the next iteration
        banned = False

        wordList=decodedMessage.split()
        for word in wordList:
            if queries.searchword(connexion,word) == 1:
                queries.updatestatus(connexion, addr[0])
                queries.insertlogs(connexion, decodedMessage, addr[0])
                c.send('YOU GOT BANNED FROM OUR PLATFORM! Connection ended.'.encode())
                c.close()
                banned=True
                break

        if banned: break

    c.close()

