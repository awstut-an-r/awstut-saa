import boto3
import logging
import os
import time


logging.basicConfig(level=logging.INFO)
INTERVAL = 60

queue_name = os.environ['QueueName']
sqs = boto3.resource('sqs',
    region_name='ap-northeast-1',
    endpoint_url='https://sqs.ap-northeast-1.amazonaws.com')
queue = sqs.get_queue_by_name(QueueName=queue_name)

def is_even(num):
    if num % 2 == 0:
        return True
    return False

def main():
    while True:
        messages = queue.receive_messages(MaxNumberOfMessages=1)
        
        for msg in messages:
            num = int(msg.body)
            
            if is_even(num):
                logging.info('{num} is even.'.format(num=num))
            else:
                logging.info('{num} is odd.'.format(num=num))
                
            time.sleep(INTERVAL)
                
            msg.delete()
            
            
if __name__ == '__main__':
    main()
