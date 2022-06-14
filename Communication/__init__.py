from json import dumps
from kafka import KafkaProducer, KafkaConsumer
import time
import Config
from kafka.structs import TopicPartition
from json import loads
config = Config.Configurations()


class Kafka_Prod:
    def __init__(self, topic='AnalysisResult'):
        """This function is used to create a kafka producer."""
        self.topic = topic
        self.producer = None
        try:
            self.producer = KafkaProducer(
                bootstrap_servers=config.brokers,
                value_serializer=lambda x: dumps(x).encode('utf-8')  # covert the data to json and encode it
            )
        except Exception as e:
            print("An error occured while connecting Kafka")
            print(e)

    def publish_message(self, data):
        """This function is used to by the producer to publish videoURLs to the topic."""
        topic = self.topic
        try:
            print("============================sending message=============================")
            print(data)
            self.producer.send(topic, value=data)  # send the data i.e (topic, data)
            self.producer.flush()  # makes all buffered records immediately available to send
            print("============================sent message=============================")
        except Exception as e:
            print("An error occured while publishing the message")
            print(e)





class Kafka_Consumer:

    def __init__(self, topic = 'NewUpload', partition = None):

        """This function is used to create a kafka consumer."""
        self.consumer = KafkaConsumer(
            topic,  # same topic used to publish
            bootstrap_servers=config.brokers,
            auto_offset_reset='earliest',  # enables the consumer to read msgs after restarting (due to loss in connection)
            enable_auto_commit=True,
            group_id='my_group', #str(np.abs(int(np.random.randn() * 1000))),  # consumer group enables auto commit, random group_id as intege
            )
        if partition:
            self.consumer.assign([TopicPartition(topic, int(partition))])


print(config.kafkaproducer,config.kafkaconsumer, config.brokers )
producer = Kafka_Prod(topic=config.kafkaproducer)
consumer = Kafka_Consumer(topic=config.kafkaconsumer).consumer



