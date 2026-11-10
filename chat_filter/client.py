import socket


PORT = 5000

serverIP = input("Enter server address: ")
if serverIP == "": serverIP = "127.0.0.1"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((serverIP,5000))
print("I connected to the server!")
print(client_socket.recv(1024).decode())

while True:
    message = client_socket.recv(1024).decode()
    if 'Support: ' in message:
        print(message)
        client_socket.send(input().encode())
    else:
        print(message)
        client_socket.close()
        break