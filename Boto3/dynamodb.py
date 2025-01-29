import boto3
from dotenv import load_dotenv
import os

load_dotenv()

client = boto3.client(
   'dynamodb',
   aws_access_key_id=os.getenv("ACCESS_KEY"),
   aws_secret_access_key=os.getenv("SECRET_KEY"),
   aws_session_token=os.getenv("SESSION_TOKEN"),
   region_name=os.getenv("REGION")
)
print(client.list_tables().get('TableNames'))

# Función para crear una tabla
def create_table(table_name, partition_key, sort_key):
    try:
        table = client.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': partition_key, 'KeyType': 'HASH'},  # Partition key
                {'AttributeName': sort_key, 'KeyType': 'RANGE'}       # Sort key
            ],
            AttributeDefinitions=[
                {'AttributeName': partition_key, 'AttributeType': 'S'},
                {'AttributeName': sort_key, 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print(f"Tabla {table_name} creada correctamente.")
    except Exception as e:
        print(f"Error al crear la tabla {table_name}: {e}")

# Crear las tablas correctamente
create_table("Users", "UserId", "Email")
create_table("Products", "ProductId", "Category")
create_table("Orders", "OrderId", "CustomerId")
