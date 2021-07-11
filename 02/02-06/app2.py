import boto3
import datetime
import json
import os
import time


def is_odd(num):
    if num % 2 == 1:
        return True
    return False
    
def lambda_handler(event, context):
    region_name = os.environ['REGION_NAME']
    
    dynamodb_config = {
        'region_name': region_name
    }
    table_name = os.environ['TABLE_NAME']
    dynamodb = boto3.resource('dynamodb', **dynamodb_config)
    table = dynamodb.Table(table_name)
    
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    epoch_time = int(time.mktime(now.timetuple()))
    
    table.put_item(Item={
        'isOdd': str(is_odd(epoch_time)),
        'datetime': now_str
    })
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'now': now_str,
            'epoch_time': epoch_time,
            'is_odd': is_odd(epoch_time),
        }),
    }
