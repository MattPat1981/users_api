import json

def lambda_handler(event, context):
    import pandas as pd
    import boto3
    import io

    #first_name = event['queryStringParameters']['first_name']
    #last_name = event['queryStringParameters']['last_name']



    # get the user_handle from input
    user_handle = event['queryStringParameters']['user_handle']


    app_response = {}
    app_response['message'] = 'hello these are the 10 most similar users to user_handle: ' + user_handle



    # Get the lookup table data and display the results
    bucket_name = 'mp-pluralsight-demo-20211016'
    filename = 'data/sims_df.csv'

    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=filename)
    sims_df = pd.read_csv(io.BytesIO(obj['Body'].read()), index_col='user_handle')

    search = 42
    print("*"*30)
    #print("You entered user handle:", search)
    print("The closest 10 user handles and their cosine similarities are:")
    print(sims_df.loc[search].sort_values(ascending=False)[1:11])
    print("*"*30)

    responseObject = {}
    responseObject['statusCode']=200
    responseObject['headers'] = {}
    responseObject['headers']['Contenet-Type'] = 'application/json'
    responseObject['body'] = json.dumps(app_response)

    return responseObject
