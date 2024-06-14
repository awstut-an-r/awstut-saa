# Each time a message is added to the SQS queue, it is read by Lambda and written to RDS via RDS Proxy

https://awstut.com/en/2024/06/15/each-time-a-message-is-added-to-the-sqs-queue-it-is-read-by-lambda-and-written-to-rds-via-rds-proxy-en/

# Architecture

![saa-01-008-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/be629525-0530-46e6-bcaf-79dbed5a6d5b)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-01-008.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-01-008/ --recursive
```

## CloudFormation Stacks Creation

```bash
aws cloudformation create-stack \
--stack-name saa-01-008 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-01-008/saa-01-008.yaml \
--capabilities CAPABILITY_NAMED_IAM
```
