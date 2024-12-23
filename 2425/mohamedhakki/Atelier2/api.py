from flask import Flask, jsonify 
import random, time 
from azure.eventhub import EventHubProducerClient, EventData 
 
app = Flask(__name__) 
 
# Chaîne de connexion Event Hub 
eventhub_connection_str = "Endpoint=sb://ordereventhub.servicebus.windows.net/;SharedAccessKeyName=Analyze_ecommerce_OrderEventHubInput_policy;SharedAccessKey=0OKY7AFBc1SVNtnRuO5Q5WVAYSNYLRHM3+AEhBG1Kv4=;EntityPath=ordereventhubNouha" 
eventhub_name = "ordereventhubecom" 
 
# Créer un client EventHub 
eventhub_client = EventHubProducerClient.from_connection_string( 
    eventhub_connection_str, 
    eventhub_name= eventhub_name 
) 
 
@app.route('/generate_order', methods=['GET']) 
def generate_order(): 
    order = { 
        "order_id": random.randint(1000, 9999), 
        "product_id": random.randint(1, 50), 
        "quantity": random.randint(1, 10), 
        "timestamp": time.time() 
    } 
    send_to_event_hub(order) 
    return jsonify(order) 
 
@app.route('/generate_orders_continuous', methods=['GET']) 
def generate_orders_continuous(): 
    orders = []  # Liste pour stocker les commandes envoyées (optionnel) 
    for _ in range(100):  # Nombre de commandes à générer 
        order = { 
            "order_id": random.randint(1000, 9999), 
            "product_id": random.randint(1, 50), 
            "quantity": random.randint(1, 10), 
            "timestamp": time.time() 
        } 
        send_to_event_hub(order) 
        orders.append(order)  # Ajouter à la liste (optionnel, utile pour visualiser) 
        time.sleep(1)  # Pause entre chaque commande (en secondes) 
    return jsonify({"message": f"{len(orders)} orders sent to Event Hub", "orders": orders}) 
 
def send_to_event_hub(order_data): 
    try: 
        event_data_batch = eventhub_client.create_batch() 
        event_data_batch.add(EventData(str(order_data))) 
        eventhub_client.send_batch(event_data_batch) 
        print(f"Order sent: {order_data}")  # Log dans la console 
    except Exception as e: 
        print(f"Failed to send order: {order_data} due to {str(e)}")  # Log en cas d'erreur 
 
if __name__ == "__main__": 
    app.run(debug=True)