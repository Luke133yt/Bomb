#Cosini, Simonelli, Amerio, Angelotti

import socket
import threading
import time

#creazione server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 25565))

#stampo l'hostname per poter far si di copiare l'hostname
print(socket.gethostname())

#metto il server in ascolto sulla porta
server.listen(5)
print('Server listening...')

clientsocket, address = server.accept() #attende la connessione
print(f'Connection from {address}') #stampa chi si connette

def winning():

    result = 'Code Correct! - Counter-terrorist WIN!' #richiama la funzione calcolo e calcola
    clientsocket.send(result.encode('utf-8'))   #manda in dietro il risultato

    print('Winner!')

    server_close()

    global cond
    cond = False

def losing():

    result = 'Wrong Code! - Terrorist WIN!' #richiama la funzione calcolo e calcola
    clientsocket.send(result.encode('utf-8'))   #manda in dietro il risultato

    print('Loser!')

    server_close()

    global cond
    cond = False

def no_code():

    result = 'No Code! - Terrorist WIN!' #richiama la funzione calcolo e calcola
    clientsocket.send(result.encode('utf-8'))   #manda in dietro il risultato

    print('Loser! No Code')

    server_close()

def server_close():
    #Chiudo il client
    print("Client closing...")
    clientsocket.close()

    #chiudo il server
    print("Server closing...")
    server.close()

def planting():
    global cond
    cond = True
    i = 10
    while cond:

        print(i)
        time.sleep(1)
        i = i - 1

        if i == 0:
            cond = False
            no_code()

def start():
    message = clientsocket.recv(1024).decode('utf-8')   #riceve il messaggio
    #print(message) #for debug

    if message == 'potato':
        x = threading.Thread(target = planting)
        x.start()

    else:
        print('Write potato!')
        server_close()

def main():
        try:

            start()

            message = clientsocket.recv(1024).decode('utf-8')   #riceve il messaggio
                    
            if message == '7355608':
                winning() #useless serve solo per non dare errore
            
            elif message != '7355608':
                losing()  #useless serve solo per non dare errore
    
        except Exception as e:  #catturo gli errori
            print("Errore: " + e)

if __name__ == "__main__":
    main()