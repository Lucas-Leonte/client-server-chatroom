# AUTHOR: Lucas Antonio Leonte
# Matricola: 0001071582


import socket
import threading

# Lista per memorizzare i client connessi e i loro indirizzi
clients = []
aliases = []

# Funzione per gestire i messaggi dei client
def broadcast(message):
    for client in clients:
        client.send(message)

# Funzione per gestire la comunicazione con un singolo client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} ha lasciato la chat.'.encode('utf-8'))
            aliases.remove(alias)
            break

# Funzione per ricevere le connessioni dei client
def receive():
    while True:
        client, address = server.accept()
        print(f"Connessione stabilita con {str(address)}")
        client.send('NICK'.encode('utf-8'))
        alias = client.recv(1024).decode('utf-8')
        aliases.append(alias)
        clients.append(client)
        print(f"Il nickname del client è {alias}")
        broadcast(f"{alias} si è unito alla chat.".encode('utf-8'))
        client.send('Connesso al server'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Creazione del socket del server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))
server.listen()

print("Server in ascolto...")
receive()
