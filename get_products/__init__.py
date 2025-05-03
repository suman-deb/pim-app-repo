
import logging
import json
import azure.functions as func
from shared.cosmos import get_container

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Fetching all products.")
    try:
        container = get_container()
        products = list(container.read_all_items())
        return func.HttpResponse(json.dumps(products), mimetype="application/json", status_code=200)
    except Exception as e:
        logging.error(f"get_products error: {e}")
        return func.HttpResponse(json.dumps({"error": str(e)}), mimetype="application/json", status_code=500)
