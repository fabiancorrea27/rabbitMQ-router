<img width="793" height="467" alt="image" src="https://github.com/user-attachments/assets/d3fb5d70-e882-43dc-b2bc-699b52d27d22" /># RabbitMQ_1
Capitulo 1 de RabbitMQ con python

Para esto se requiere tener corriendo RabbitMQ en un contenedor de docker.
# latest RabbitMQ 4.x
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management

<img width="822" height="311" alt="image" src="" />
Se requiere de la libreria pika en python: 

se puede instalar con: 
python -m pip install pika --upgrade

y si no funciona buscar si se encuentar en el administrador de paquetes (apt)
e inatalarla si no se quiere instalar en ambiente virtual.
<img width="793" height="467" alt="image" src="" />

Primera parte - Sending 

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()

<img width="655" height="123" alt="image" src="https:" />

Segunda parte - Recieve

import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

<img width="713" height="115" alt="image" src="" />

Tercera parte - Putting it all together

<img width="930" height="100" alt="image" src="" />

Cuarta parte - aplicar lo aprendido

Construimos un docker compose con estos porgramas



