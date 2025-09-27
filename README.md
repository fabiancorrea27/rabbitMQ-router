# RabbitMQ con Python - Capítulo 1

Este proyecto demuestra los conceptos básicos de **RabbitMQ** utilizando **Python**, incluyendo el envío y recepción de mensajes.

## Requisitos

- Docker
- Python 3.6+
- Biblioteca `pika`

## Instalación

### 1. Ejecutar RabbitMQ con Docker

```bash
# latest RabbitMQ 4.x
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management
```

### 2. Instalar la biblioteca `pika`

```bash
python -m pip install pika --upgrade
```

> **Alternativa:** Si usas un sistema basado en Debian/Ubuntu, puedes buscar el paquete en `apt`.

## Ejecución

### Parte 1: Enviar Mensajes (`send.py`)

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='Hello World!'
)
print(" [x] Sent 'Hello World!'")
connection.close()
```

### Parte 2: Recibir Mensajes (`receive.py`)

```python
import pika
import sys
import os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
```

## Docker Compose

Se incluye un archivo `docker-compose.yml` para facilitar la ejecución de los ejemplos en un entorno contenedorizado.

```yaml
version: '3.8'

services:
  rabbitmq:
    image: rabbitmq:4-management
    ports:
      - "5672:5672"
      - "15672:15672"
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq

volumes:
  rabbitmq_data:
```

## Capturas de Pantalla

A continuación, se muestran algunas capturas del proceso:

### 1. Inicio de RabbitMQ en Docker
![RabbitMQ Docker](https://github.com/WBOK-GM/RabbitMQ_1/blob/main/images/1.png)

### 2. Interfaz de Administración de RabbitMQ
![RabbitMQ Management](https://github.com/WBOK-GM/RabbitMQ_1/blob/main/images/2.png)

### 3. Instalación de Pika
![Pika Installation](https://github.com/WBOK-GM/RabbitMQ_1/blob/main/images/3.png)

### 4. Ejecución del script de envío
![Send Script](https://github.com/WBOK-GM/RabbitMQ_1/blob/main/images/4.png)

### 5. Ejecución del script de recepción
![Receive Script](https://github.com/WBOK-GM/RabbitMQ_1/blob/main/images/5.png)

### 6. Resultado final
![Final Result](https://github.com/WBOK-GM/RabbitMQ_1/blob/main/images/6.png)

### 7. Vista desde RabbitMQ
![Final Result](https://github.com/WBOK-GM/RabbitMQ_1/blob/main/images/7.png)

### 8. Resultado Logs
![Final Result](https://github.com/WBOK-GM/RabbitMQ_1/blob/main/images/8.png)


