from concurrent import futures
import logging

import random

from paho.mqtt import client as mqtt_client 

import grpc

import serv_pb2

import serv_pb2_grpc


broker = 'broker.emqx.io'

port = 50051

topic = "/python/mqtt"

client_id =f'python-mqtt-{random.randint(0,100)}'
username = 'emqx'
password = 'public'

class ServServs(serv_pb2_grpc.MqttservicesServicer):
    def connect_mqtt() -> mqtt_client:
        def on_connect(client,userdata,flags,rc):
            if rc==0:
                print("Connected to MQTT BROKER")
            else:
                print("Failed to connect %d",rc)
        client=mqtt_client.Client(client_id)
        client.username_pw_set(username,password)
        client.on_connect = on_connect
        client.connect(broker,port)
        return client


    def publish(client):
        msg_cnt=0
        while true:
            time.sleep(1)
            msg="messages:{msg_cnt}"
            result=client.publish(topic,msg)
            status=result[0]
            if status ==0:
               print("send`{msg}` to topic `{topic`")
            else:
                print("Failed to send message to topic {topic}")
                msg_cnt+=1
    def subscribe(client:mqtt_client):
        def on_message(client,userdata,msg):
            print("Receieved`{msg.payload.decode()}`from `{msg.topic}` topic")
    
        client.subscribe(topic)

        client.on_message=on_message

def serve():
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    serv_pb2_grpc.add_MqttservicesServicer_to_server(ServServs(),server)
    
    server.add_insecure_port('[::]:50051')
    
    server.start()
    
    
    print("Server statred")
    
   
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
    client=connect_mqtt()
    if (c==3):
      subscribe(client)
    elif (c==2):
      publish(client)
    elif (c==1):
      connect_mqtt()
    
    
    client.loop_forever()
    



