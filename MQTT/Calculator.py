import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    client1.connected_flag=True
    if(rc==0):
        print("Connected")
    else:
        print("Bad connection returned code=",rc)

def on_message(client1, userdata, message):
    m=str(message.payload.decode("utf-8"))
    print("Answer:",m)

def on_publish (client, userdata, mid):
    m="on publish callback mid "+str(mid)

def on_subscribe(client, userdata, mid, granted_qos):
    m="on_subscribe callback mid "+str(mid)
  
def on_disconnect(client,userdata,flags,rc=0):
    print("Disconnected")
    
broker_address="192.168.137.1"
client1 = mqtt.Client("Orion")    
client1.on_connect= on_connect
client1.on_message=on_message 
client1.on_publish =on_publish
client1.on_disconnect= on_disconnect

time.sleep(1)
print("Connecting to broker",broker_address)
client1.connected_flag=False
client1.connect(broker_address)
client1.loop_start()  

r=client1.subscribe("Technocrats")
while not client1.connected_flag:
    print("Waiting for connection")
    time.sleep(0.5)

while(True):
    temp4=0;
    choice=input("1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Exit: ")
    if(choice=="5"):
        break;
    temp=input("Enter two numbers separated by a space: ")
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
    client1.publish("Technocrats",str(temp4))
    time.sleep(1)

client1.disconnect()
client1.loop_stop()


