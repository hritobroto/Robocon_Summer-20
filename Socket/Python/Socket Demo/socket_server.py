import socket

def server_program():
    host = socket.gethostname();
    port = 5000;
    
    #binding hst address and the port together
    socket_server = socket.socket();
    socket_server.bind((host, port));
    
    #creating file to store client responses
    f=open("data_log.txt","a");
    
    #accept new connection
    socket_server.listen(2);
    conn, address = socket_server.accept();
    
    print("Connection from: " + str(address));
    while True:
        response = conn.recv(1024).decode();
        if not response:
            break;
        print("from connected user: " + str(response));
        f.write(str(response));
        f.write("\n")
        response = input(' -> ');
        conn.send(response.encode());

    conn.close();

#main
if __name__ == '__main__':
    server_program();
