import os
pwd = os.getcwd()
i = pwd.find("crystal")
pwd = pwd[:i+len("crystal")]
print(pwd)
class Configurations:
    def __init__(self):
        self.kafkaconsumer = "NewUpload"
        self.kafkaproducer = "Kubeflow"
        self.brokers = ['137.184.147.128:9092']
        #self.brokers = ['localhost:9092']
        self.workin_dir = pwd
        self.n_workers = 4
        self.action_detection_chunk_time = 6 # seconds
