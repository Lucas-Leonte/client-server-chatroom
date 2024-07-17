# AUTHOR: Lucas Antonio Leonte
# Matricola: 0001071582

import socket
import threading

# Funzione per ricevere i messaggi dal server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print("Errore nella connessione al server.")
            client.close()
            break

# Funzione per inviare i messaggi al server
def write():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))

# Creazione del socket del client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

alias = input("Scegli un nickname: ")

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
