import boto3
import datetime
import logging
import os
import random
import time

logging.basicConfig(level=logging.INFO)

queue_name = os.environ['QueueName']
region_name = os.environ['RegionName']
sqs_endpoint_url = os.environ['SQSEndpointUrl']

sqs = boto3.resource('sqs',
    region_name=region_name,
    endpoint_url=sqs_endpoint_url)
queue = sqs.get_queue_by_name(QueueName=queue_name)

def main():
    while True:
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S%f')
        epoch_time = int(time.mktime(now.timetuple()))
        
        logging.info(now_str)
        logging.info(epoch_time)
        
        messages = [{
            'Id': str(now_str),
            'MessageBody': str(epoch_time)
        }]
        response = queue.send_messages(Entries=messages)
        
        time.sleep(random.randint(10, 60))
    

if __name__ == '__main__':
    main()
