#|send/app.py
import pika
import time

# Esperar a que RabbitMQ esté listo
time.sleep(15)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="rabbitmq",
        credentials=pika.PlainCredentials("admin", "admin")
    )
)
channel = connection.channel()
channel.queue_declare(queue="hello")

while True:
    channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
    print(" [x] Sent 'Hello World!'")
    time.sleep(2)
