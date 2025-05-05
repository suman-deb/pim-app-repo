
import logging
import json
import azure.functions as func
from shared.cosmos import get_container
import os
logging.info(f"1. COSMOS_CONNECTION_STRING: {os.getenv('COSMOS_DB_CONNECTION')}")
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Adding product.")
    try:
        data = req.get_json()
        logging.info(f"Received data: {data}")
        container = get_container()
        logging.info(f"2. Using Cosmos DB connection string: {COSMOS_CONNECTION_STRING}")
        if "id" not in data or "name" not in data or "price" not in data:
            raise ValueError("Missing one or more required fields")

        data["id"] = str(data.get("id") or str(len(list(container.read_all_items())) + 1))
        container.create_item(body=data)
        return func.HttpResponse(json.dumps({"message": "Product added", "product": data}),
                                 mimetype="application/json", status_code=201)
    except Exception as e:
        logging.error(f"add_product error: {e}")
        return func.HttpResponse(json.dumps({"error": str(e)}), mimetype="application/json", status_code=400)
