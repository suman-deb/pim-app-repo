
import logging
import json
import azure.functions as func
from shared.cosmos import get_container

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Updating product.")
    try:
        data = req.get_json()
        product_id = str(data.get("id"))
        container = get_container()
        existing = container.read_item(item=product_id, partition_key=product_id)
        existing.update(data)
        container.replace_item(item=product_id, body=existing)
        return func.HttpResponse(json.dumps({"message": "Product updated", "product": existing}),
                                 mimetype="application/json", status_code=200)
    except Exception as e:
        logging.error(f"update_product error: {e}")
        return func.HttpResponse(json.dumps({"error": str(e)}), mimetype="application/json", status_code=400)
