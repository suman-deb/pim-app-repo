
import os
import logging
from azure.cosmos import CosmosClient

COSMOS_CONNECTION_STRING = os.getenv("COSMOS_DB_CONNECTION")
DATABASE_NAME = "PIMDatabase"
CONTAINER_NAME = "Products"

def get_container():
    if not COSMOS_CONNECTION_STRING:
        raise EnvironmentError("COSMOS_DB_CONNECTION is missing.")
    try:
        client = CosmosClient.from_connection_string(COSMOS_CONNECTION_STRING)
        db = client.get_database_client(DATABASE_NAME)
        return db.get_container_client(CONTAINER_NAME)
    except Exception as e:
        logging.error(f"Cosmos DB connection failed: {e}")
        raise
