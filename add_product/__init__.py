
import logging
import json
import azure.functions as func
from shared.cosmos import get_container

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Adding product.")
    try:
        data = req.get_json()
        container = get_container()
        print("Connection string is:", COSMOS_CONNECTION_STRING)

        data["id"] = str(data.get("id") or str(len(list(container.read_all_items())) + 1))
        container.create_item(body=data)
        return func.HttpResponse(json.dumps({"message": "Product added", "product": data}),
                                 mimetype="application/json", status_code=201)
    except Exception as e:
        logging.error(f"add_product error: {e}")
        return func.HttpResponse(json.dumps({"error": str(e)}), mimetype="application/json", status_code=400)
