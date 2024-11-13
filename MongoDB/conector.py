from pymongo import MongoClient
from dotenv import load_dotenv
import os

class ConectorMongoDB():

    def conectarse(self):
        load_dotenv()

        usuario= os.getenv("USUARIO_MONGODB")
        password = os.getenv("PASSWORD_MONGODB")
        cluster= os.getenv("CLUSTER_MONGODB")


        client = MongoClient('mongodb+srv://'+usuario+':'+password+'@'+cluster+'.xw6rg.mongodb.net/?retryWrites=true&w=majority&appName='+cluster, maxPoolSize=50)

        return client