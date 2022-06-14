import os
pwd = os.getcwd()
i = pwd.find("crystal")
pwd = pwd[:i+len("SonalysisAI-V2")]
print(pwd)
class Configurations:
    def __init__(self):
        self.MONGODB_URI = "mongodb://sonauser:sona15230@api.sonalysis.io:27017/sonalysis?authSource=admin&directConnection=true&ssl=false"
        self.kafkaconsumer = "NewUpload"
        self.kafkaproducer = "Kubeflow"
        self.brokers = ['137.184.147.128:9092']
        #self.brokers = ['localhost:9092']
        self.workin_dir = pwd
        self.n_workers = 4
        self.action_detection_chunk_time = 6 # seconds
