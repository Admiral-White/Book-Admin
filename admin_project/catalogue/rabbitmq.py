import pika
import json


def publish_message(message_body):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare an exchange
    channel.exchange_declare(exchange='library', exchange_type='topic')

    # Publish the message
    channel.basic_publish(exchange='library', routing_key='book.added', body=json.dumps(message_body))

    connection.close()
