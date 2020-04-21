import socket

def client_program():
    host = socket.gethostname()
    port = 5000;
    
    #connect to the server
    socket_client = socket.socket()  
    socket_client.connect((host, port)) 

    message = input(" -> ")  
    while message.lower().strip() != 'bye':
        socket_client.send(message.encode())  
        data = socket_client.recv(1024).decode()

        #acknowledgement 
        print("Your response has been recorded")
        print('Received from server: ' + data)  
        message = input(" -> ")  

    socket_client.close()  

#main
if __name__ == '__main__':
    client_program()
