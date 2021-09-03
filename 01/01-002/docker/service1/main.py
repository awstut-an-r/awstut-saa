import boto3
import datetime
import logging
import os
import random
import time

logging.basicConfig(level=logging.INFO)

queue_name = os.environ['QueueName']
sqs = boto3.resource('sqs',
    region_name='ap-northeast-1',
    endpoint_url='https://sqs.ap-northeast-1.amazonaws.com')
queue = sqs.get_queue_by_name(QueueName=queue_name)

def main():
    while True:
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S%f')
        epoch_time = int(time.mktime(now.timetuple()))
        
        logging.info(epoch_time)
        
        messages = [{
            'Id': str(now_str),
            'MessageBody': str(epoch_time)
        }]
        response = queue.send_messages(Entries=messages)
        
        time.sleep(random.randint(10, 60))
    

if __name__ == '__main__':
    main()
