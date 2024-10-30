from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

client = MongoClient('mongodb+srv://'+usuario+':'+password+'@sbd.xw6rg.mongodb.net/?retryWrites=true&w=majority&appName=SBD')

try:
    client.admin.command('ping')
    print("Conectado a la base de datos correctamente")
except Exception as e:
    print(e)