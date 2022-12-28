# Accessing DynamoDB Accelerator (DAX) with EC2/Lambda

https://awstut.com/en/2022/12/29/accessing-dynamodb-accelerator-dax-with-ec2-lambda-en/

# Architecture

![saa-02-009-diagram](https://user-images.githubusercontent.com/84276199/209882835-43769894-43fa-4a60-abee-7ac8f3bfb59e.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-02-009.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-02-009/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-02-009 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-02-009/saa-02-009.yaml \
--capabilities CAPABILITY_IAM
```
