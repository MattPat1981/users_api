# create_api.py
import json

api_definition = json.dumps(spec_dict, indent=2)
api_gateway_client.import_rest_api(body=api_definition)

