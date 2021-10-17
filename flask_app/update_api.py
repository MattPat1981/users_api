#update_api.py

api_gateway_client.put_rest_api(body=api_definition, mode='merge', restApiId=find_api_id(api_gateway_client,api_name))

