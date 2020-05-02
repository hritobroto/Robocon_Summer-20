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
    print("Message:",m)

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

print("Publishing")
m="Working on MQTT" 
client1.publish("Technocrats",m)
time.sleep(1)

print("Publishing")
m="Summer Task CSE" 
client1.publish("Technocrats",m)
time.sleep(1)

client1.disconnect()
client1.loop_stop()


