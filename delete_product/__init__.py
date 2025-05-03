
import logging
import json
import azure.functions as func
from shared.cosmos import get_container

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Deleting product.")
    try:
        data = req.get_json()
        product_id = str(data.get("id"))
        container = get_container()
        container.delete_item(item=product_id, partition_key=product_id)
        return func.HttpResponse(json.dumps({"message": f"Product {product_id} deleted."}),
                                 mimetype="application/json", status_code=200)
    except Exception as e:
        logging.error(f"delete_product error: {e}")
        return func.HttpResponse(json.dumps({"error": str(e)}), mimetype="application/json", status_code=400)
