import paho.mqtt.client as mqtt
broker_address="localhost"

#mqtt.eclipseprojects.io

# this is the subscriber

def on_connect(client, userdata, flags, rc) :
    print("connected with result code"+str(rc))
    client.subscribe("test",)
def on_message(client, userdata, msg):
    if msg.payload.decode() == "Hello world":
        print("Yes")
        client.disconnect()
client = mqtt.Client()
client.connect("localhost",1883)

client.subscribe("test")
client.on_connect = on_connect
client.on_message = on_message
while True:
  client.loop_forever()
