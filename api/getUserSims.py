# getUserSims.py is a fast program for the CLI
# this toy program returns the data for the 
# 10 users most similar to the entered user_handle

import pandas as pd
import boto3
import io

bucket_name = 'mp-pluralsight-demo-20211016'
filename = 'data/sims_df.csv'

s3 = boto3.client('s3')
obj = s3.get_object(Bucket=bucket_name, Key=filename)
sims_df = pd.read_csv(io.BytesIO(obj['Body'].read()), index_col='user_handle')

#sims_df = pd.read_csv("s3://mp-pluralsight-demo-20211016/data/sims_df.csv")

search = 42
print("*"*30)
print("You entered user handle:", search)
print("The closest 10 user handles and their cosine similarities are:")
print(sims_df.loc[search].sort_values(ascending=False)[1:11])   
print("*"*30)
