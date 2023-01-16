import time
from kafka import KafkaProducer

TOPIC_NAME = "alerts"

producer = KafkaProducer(
    bootstrap_servers=f"public-kafka-29ffb9d2-aliali-22df.aivencloud.com:27760",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

for i in range(3):
    message = f"Hello from Python using SSL {i + 1}!"
    producer.send(TOPIC_NAME, message.encode('utf-8'), key="red".encode("utf-8"), partition=i)
    print(f"Message sent: {message}")
    time.sleep(1)

producer.close()