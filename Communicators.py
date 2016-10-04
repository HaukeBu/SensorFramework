import threading
import time
import json
import pika
import socket


class CommunicatorDummy:
    def __init__(self):
        name = "Dummy"
        print(name + "created!")

    def setup_connection(self):
        print(self.name + "setup!")

    def close_connection(self):
        print(self.name + "close!")

    def print(self, to_send):
        print(self.name + ":" + to_send)


class RabbitMQCommunicator:
    def __init__(self, ip_address, mq_queue_name, intern_json_queue):
        self.connection = False
        self.channel = False
        self.ip_address = ip_address

        self.mq_queue_name = mq_queue_name
        self.intern_json_queue = intern_json_queue

    def setup_connection(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.ip_address))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.mq_queue_name)

    def close_connection(self):
        self.connection.close()

    def send(self, to_send):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.mq_queue_name,
                                   body=to_send)


class SocketCommunicator:
    def __init__(self, ip_address, port):
        self.client_socket = False
        self.ip_address = ip_address
        self.port = port

    def setup_connection(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.ip_address, self.port))

    def close_connection(self):
        self.client_socket.close()

    def send(self, to_send):
        self.close_connection()
        self.setup_connection()

        self.client_socket.send(to_send.encode('utf-8'))