import boto3
import logging
import os
import time


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    queue_name = os.environ['QueueName']
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    
    while True:
        messages = queue.receive_messages(MaxNumberOfMessages=1)
        
        if len(messages) == 0:
            logging.info('no messages')
            continue
        
        for msg in messages:
            logging.info(msg.body)
            time.sleep(60)
            msg.delete()
