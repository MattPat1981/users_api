import json

def lambda_handler(event, context):

    #call: https://pok2uapqb2.execute-api.us-west-2.amazonaws.com/users_api_dev/myresource?user_handle=42

    import boto3
    #first_name = event['queryStringParameters']['first_name']
    #last_name = event['queryStringParameters']['last_name']



    # get the user_handle from input
    user_handle = event['queryStringParameters']['user_handle']


    app_response = {}
    #app_response['message'] = 'hello these are the 10 most similar users to user_handle: ', user_handle
    app_response['message'] = 'hello these are the 10 most similar users to user_handle: ' + user_handle
    app_response['user_handle'] = user_handle
    app_response['age'] = "10 closest listed out"

    responseObject = {}
    responseObject['statusCode']=200
    responseObject['headers'] = {}
    responseObject['headers']['Contenet-Type'] = 'application/json'
    responseObject['body'] = json.dumps(app_response)

    return responseObject
