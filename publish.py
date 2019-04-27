import paho.mqtt.client as mqttClient
import time
import random

min_temp_value = 40                                  #lower limit for temp range
max_temp_value = 50                                  #upper limit for temp range
least_count_of_temp_value = 1                        #steps for increasing temp value
time_interval = 5                                    #seconds between consecutive publish
topic_path = "zenatix/candy_factory/temperature"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                
        Connected = True                
    else:
        print("Connection failed")
 
Connected = False                       #state of the connection
 
broker_address= "test.mosquitto.org"
port = 1883
user = "fejgbbqc"
password = "wIJYTuzuQYw3"
 
client = mqttClient.Client("sensor1")               
client.on_connect= on_connect                      
client.connect(broker_address, port=port)          
 
client.loop_start()        
 
while Connected != True:    
    time.sleep(0.1)
 
try:
    while True:
        value = random.randrange(min_temp_value, max_temp_value, least_count_of_temp_value)
        time.sleep(time_interval)
        print("publishing value : " , value)
        client.publish(topic_path,value)
 
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()