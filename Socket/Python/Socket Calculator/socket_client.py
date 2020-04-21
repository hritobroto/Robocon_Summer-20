import socket

def client_program():
    host = socket.gethostname();
    port = 5000;
    
    #connect to the server
    socket_client = socket.socket();  
    socket_client.connect((host, port)); 

    message = input(" -> ");
    while True:
        if message=="5":
            break;
        socket_client.send(message.encode());  
        data = socket_client.recv(1024).decode();

        print('Received from server: ' + data);  
        message = input(" -> ");  

    socket_client.close();  

#main
if __name__ == '__main__':
    client_program();
