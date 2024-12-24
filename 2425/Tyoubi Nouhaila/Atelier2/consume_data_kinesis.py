import boto3
import json
import time

# Initialisation du client Kinesis
kinesis_client = boto3.client('kinesis', region_name='eu-north-1')

# Nom du flux Kinesis
STREAM_NAME = "ecommerce-data-stream"

# Fonction pour récupérer et traiter les données du flux
def consume_kinesis_data():
    # Récupérer l'itérateur de shard
    response = kinesis_client.describe_stream(StreamName=STREAM_NAME)
    shard_id = response['StreamDescription']['Shards'][0]['ShardId']  # Utilise le premier shard disponible
    
    shard_iterator_response = kinesis_client.get_shard_iterator(
        StreamName=STREAM_NAME,
        ShardId=shard_id,
        ShardIteratorType="LATEST"  # Récupère les données les plus récentes
    )
    
    shard_iterator = shard_iterator_response['ShardIterator']
    
    print("Starting to consume data from Kinesis...")
    
    # Boucle pour récupérer et traiter les données
    while True:
        record_response = kinesis_client.get_records(
            ShardIterator=shard_iterator,
            Limit=10  # Nombre maximum d'enregistrements à récupérer par appel
        )
        
        shard_iterator = record_response['NextShardIterator']
        
        for record in record_response['Records']:
            # Les données sont encodées en UTF-8, donc on les décode
            data = json.loads(record['Data'])
            print("Data received:", data)
            
            # Ici, vous pouvez ajouter du traitement pour les données
            # Exemple : sauvegarder dans une base de données, transformer les données, etc.
        
        time.sleep(2)  # Attendre avant la prochaine récupération

consume_kinesis_data()
