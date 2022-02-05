import boto3
import logging
import os
import time


logging.basicConfig(level=logging.INFO)

interval = int(os.environ['Interval'])
queue_name = os.environ['QueueName']
region_name = os.environ['RegionName']
sqs_endpoint_url = os.environ['SQSEndpointUrl']

sqs = boto3.resource('sqs',
    region_name=region_name,
    endpoint_url=sqs_endpoint_url)
queue = sqs.get_queue_by_name(QueueName=queue_name)

def is_even(num):
    if num % 2 == 0:
        return True
    return False

def main():
    while True:
        messages = queue.receive_messages(MaxNumberOfMessages=1)
        
        for msg in messages:
            # print(msg.body)
            logging.info(msg.body)
            num = int(msg.body)
            
            if is_even(num):
                logging.info('{num} is even.'.format(num=num))
            else:
                logging.info('{num} is odd.'.format(num=num))
                
            time.sleep(interval)
                
            msg.delete()
            
            
if __name__ == '__main__':
    main()
