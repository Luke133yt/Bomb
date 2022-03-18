#Cosini, Simonelli, Amerio, Angelotti

from playsound import playsound
import socket
import threading

ip = input('IP SERVER: ')   #DESKTOP-8JUD279

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #creo il socker
client.connect((ip, 25565))                                 #e mi ci connetto
def start():
    #prendo e lo mando l'input
    message = input('Codice di avvio: ')
    client.send(message.encode('utf-8'))

def recieving():
    #RECEIVE MESSAGE
    message = client.recv(1024).decode('utf-8')
    print(f'Message: {message}')    #Stampo il valore del messaggio
    
    if message == ('No Code! - Terrorist WIN!' or 'Wrong Code! - Terrorist WIN!'):
        print(r"""

     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____


            """)

        playsound('audio.mp3')
        
    if message == 'Code Correct! - Counter-terrorist WIN!':
        playsound('audio-2.mp3')

def sending():
    #prendo gli input
    message = input('Password: ')
    #mando l'input
    client.send(message.encode('utf-8'))

def main():
    try:
            
        start()

        y = threading.Thread(target = sending)
        y.start()

        x = threading.Thread(target = recieving)
        x.start()

    except Exception as e:  #catturo gli errori
        print("Errore: " + e)


if __name__ == "__main__":
    main()