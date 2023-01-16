from kafka import KafkaConsumer

TOPIC_NAME = "alerts"

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=f"public-kafka-29ffb9d2-aliali-22df.aivencloud.com:27760",
    client_id = "CONSUMER_CLIENT_ID",
    group_id = "CONSUMER_GROUP_ID",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

while True:
    for message in consumer.poll().values():
        for m in message:
            print("Got message using SSL: " + m.value.decode('utf-8'))