#-*-coding:utf-8-*-

import boto3
import json
import pprint
import os


def lambda_handler(event, context):
    region_name = os.environ['REGION_NAME']
    bucket_name = os.environ['S3_BUCKET_NAME']
    img_original_folder_name = os.environ['IMG_ORIGINAL_FOLDER_NAME']
    
    s3_config = {
        'region_name': region_name
    }
    s3_client = boto3.client('s3', **s3_config)
    response = s3_client.list_objects_v2(
        Bucket=bucket_name,
        Prefix=img_original_folder_name)
    
    img_original_names = [obj['Key'] for obj in response['Contents']]
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps({
            'imgOriginals': img_original_names
        }),
    }
