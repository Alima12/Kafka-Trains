import time
from kafka.admin import KafkaAdminClient, NewTopic

TOPIC_NAME = "topic1"

admin = KafkaAdminClient(
    client_id="admin",
    bootstrap_servers=f"public-kafka-29ffb9d2-aliali-22df.aivencloud.com:27760",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key"
)

topic_name_partiotioned = TOPIC_NAME + "_" + "partitioned"
topic = NewTopic(
    name=topic_name_partiotioned,
    num_partitions=3,
    replication_factor=3
)
admin.create_topics(topic,timeout_ms=5)
