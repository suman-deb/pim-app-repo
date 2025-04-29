import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    products = [
        {"id": 1, "name": "Product A", "price": 19.99},
        {"id": 2, "name": "Product B", "price": 29.99}
    ]
    
    return func.HttpResponse(
        json.dumps(products),
        mimetype="application/json",
        status_code=200
    )
