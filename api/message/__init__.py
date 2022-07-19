import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    
    import json
    

    if name:
        message = {'text': f"Hello, {name}. This HTTP triggered function executed successfully."}
    else:
        message = {'text': "Hello, from the API."}
    message = json.dumps(message)
    return func.HttpResponse(message)
