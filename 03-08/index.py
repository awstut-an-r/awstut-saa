import boto3
import datetime
import json
import mysql.connector
import os


db_endpoint_address = os.environ['DB_ENDPOINT_ADDRESS']
db_proxy_endpoint_address = os.environ['DB_PROXY_ENDPOINT_ADDRESS']
db_endpoint_port = os.environ['DB_ENDPOINT_PORT']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
db_tablename = os.environ['DB_TABLENAME']
region = 'ap-northeast-1'


def lambda_handler(event, context):
    conn = mysql.connector.connect(
        #host=db_endpoint_address,
        host=db_proxy_endpoint_address,
        port=db_endpoint_port,
        user=db_user,
        password=db_password,
        database=db_name
        )
    cur = conn.cursor()
    
    table_sql = 'create table if not exists {db}.{tbl} (dt datetime);'.format(
        db=db_name,
        tbl=db_tablename
        )
    cur.execute(table_sql)
    
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    write_sql = 'insert into {tbl} values ("{now}");'.format(
        tbl=db_tablename,
        now=now_str
    )
    cur.execute(write_sql)
    
    cur.close()
    conn.commit()
    
    cur = conn.cursor()
    read_sql = 'select * from {tbl};'.format(tbl=db_tablename)
    cur.execute(read_sql)
    content = [record[0].strftime('%Y-%m-%d %H:%M:%S') for record in cur]
    
    cur.close()
    conn.close()
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(content, indent=2)
    }
