#-*-coding:utf-8-*-

import boto3
import datetime
import json
import pprint
import os

from PIL import Image


def lambda_handler(event, context):
    region_name = os.environ['REGION_NAME']
    bucket_name = os.environ['S3_BUCKET_NAME']
    img_original_folder_name = os.environ['IMG_ORIGINAL_FOLDER_NAME']
    img_converted_folder_name = os.environ['IMG_CONVERTED_FOLDER_NAME']
    
    params = json.loads(event['body'])
    
    s3_config = {
        'region_name': region_name
    }
    s3_client = boto3.client('s3', **s3_config)
    download_path = os.environ['IMG_DOWNLOAD_PATH'].format(
        img_file=os.path.basename(params['img']))
    
    s3_client.download_file(
        Bucket=bucket_name,
        Key=params['img'],
        Filename=download_path
        )
        
    now = datetime.datetime.now()
        
    upload_file_name = '{img_name}_{now}.{extention}'.format(
        img_name=os.path.splitext(os.path.basename(params['img']))[0],
        now=datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
        extention=os.path.splitext(os.path.basename(params['img']))[1]
        )

    upload_path = os.path.join(img_converted_folder_name, upload_file_name)
        
    image = Image.open(download_path)
    image.convert(params['mode']).save(download_path)
    
    s3_client.upload_file(
        Filename=download_path,
        Bucket=bucket_name,
        Key=upload_path
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps({
            'imgConverted': upload_path
        }),
    }
