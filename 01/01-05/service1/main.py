import boto3
import datetime
import os

from bottle import route, run

@route('/')
def hello():
    queue_name = os.environ['QueueName']
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    
    dt_now = datetime.datetime.now()
    
    message_body = 'message form service1: {now}'.format(now=dt_now)
    messages = [{
        'Id': str(dt_now.strftime('%Y%m%d%H%M%S%f')),
        'MessageBody': message_body
    }]
    response = queue.send_messages(Entries=messages)
    
    return 'hello, world !: {now}'.format(now=dt_now)
    
    
if __name__ == '__main__':
    run (host='0.0.0.0', port=8080)
