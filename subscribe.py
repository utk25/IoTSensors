import paho.mqtt.client as mqtt
import smtplib, ssl

port = 465                                           #For SSL
smtp_server = "smtp.gmail.com"
sender_email = ""                                    #Enter sender address
receiver_email = ""                                  #Enter receiver address
password =                                           #Password for sender address 
avg_temp_values=[]                                   #List to hold temperature values
max_avg_temp = 40                                    #upper limit for temperature to send email
no_of_temp_values = 12                               #Total no of temperature values to store (12 for a min since values are published at 5s interval)
topic_path = "zenatix/candy_factory/temperature"

message = """\
Subject: Hi there

The temperature in sensor 1 is more that 40 degrees for the last 1 min."""

def sendEmail():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic_path)

def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    print(msg.topic+" "+msg.payload)
    avg_temp_values.append(int(msg.payload))
    if len(avg_temp_values) == no_of_temp_values:
        if sum(avg_temp_values) / no_of_temp_values >= max_avg_temp:
            print(avg_temp_values)
            sendEmail()
        avg_temp_values.clear()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

try:
    client.loop_forever()
 
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()