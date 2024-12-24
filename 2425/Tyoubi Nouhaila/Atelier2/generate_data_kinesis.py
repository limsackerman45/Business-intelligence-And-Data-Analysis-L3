import boto3
import json
import random
import time

# Initialisation du client Kinesis
kinesis_client = boto3.client('kinesis', region_name='eu-north-1')

def generate_data():
    while True:
        # Données brutes
        data = {
            "InvoiceNo": f"INV-{random.randint(1000, 9999)}",
            "StockCode": f"STK-{random.randint(100, 999)}",
            "Description": random.choice(["Laptop", "Phone", "Tablet"]),
            "Quantity": random.randint(1, 10),
            "InvoiceDate": time.strftime("%Y-%m-%d %H:%M:%S"),
            "UnitPrice": round(random.uniform(10, 500), 2),
            "CustomerID": random.randint(1000, 9999),
            "Country": random.choice(["USA", "France", "Germany"])
        }

        # Envoi des données encodées à Kinesis
        kinesis_client.put_record(
            StreamName="ecommerce-data-stream",
            Data=json.dumps(data),
            PartitionKey="partition-key"
        )

        print(f"Data sent: {data}")
        time.sleep(1)  # Envoi toutes les secondes

generate_data()
