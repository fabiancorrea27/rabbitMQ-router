#|receive/app.py
import pika
import sys
import time

# Esperar a que RabbitMQ esté listo
time.sleep(15)

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="rabbitmq",
            credentials=pika.PlainCredentials("admin", "admin")
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
