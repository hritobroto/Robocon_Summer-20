import socket

def server_program():
    host = socket.gethostname();
    port = 5000;
    
    #binding hst address and the port together
    socket_server = socket.socket();
    socket_server.bind((host, port));
    
    
    #accept new connection
    socket_server.listen(2);
    conn, address = socket_server.accept();
    
    x="";
    print("Connection from: " + str(address));
    while True:
        response = conn.recv(1024).decode();
        if not response:
            break;
        x=input(" -> ");
        if(response=="1" or response=="2" or response=="3" or response=="4" or response=="5"): 
            choice=response;
            response = "Enter two numbers separated by space ";
            
        else:
            s=response[0:1];
            
            if(s.isdigit()):
                temp=response;
                temp4=0;
                temp1=int(temp[0:temp.find(" ")]);
                temp2=int(temp[temp.find(" ")+1:len(temp)]);
                if(choice=="1"):
                    temp4=temp1+temp2;
                elif(choice=="2"):
                    temp4=temp1-temp2;
                elif(choice=="3"):
                    temp4=temp1*temp2;
                elif(choice=="4"):
                    temp4=temp1/temp2;
                response=str(temp4)
            else:
                response = "1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Exit ";
        conn.send(response.encode());

    conn.close();

#main
if __name__ == '__main__':
    server_program();
