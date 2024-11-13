from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

usuario= os.getenv("USUARIO_MONGODB")
password = os.getenv("PASSWORD_MONGODB")
cluster= os.getenv("CLUSTER_MONGODB")

client = MongoClient('mongodb+srv://'+usuario+':'+password+'@'+cluster+'.xw6rg.mongodb.net/?retryWrites=true&w=majority&appName='+cluster)

baseDatos = client["FedericoLuque"]

coleccion = baseDatos["mi_primera_coleccion"]

documento = {'nombre' : 'Federico','apellido' : 'Luque Santos'}

insercion = coleccion.insert_one(documento)

print(insercion)