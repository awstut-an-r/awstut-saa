# Create S3 bucket with cross-region replication enabled using CFN

https://awstut.com/en/2023/01/05/create-s3-bucket-with-cross-region-replication-enabled-using-cfn-en/

# Architecture

![saa-01-003-diagram](https://user-images.githubusercontent.com/84276199/210668392-c5c28502-50ba-46e5-a8c1-c0d7d3c97dbe.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-01-003-1.yaml and saa-01-003-2.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-01-003/ --recursive
```

## CloudFormation Stacks Creation

```bash
aws cloudformation create-stack \
--stack-name saa-01-003-1 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-01-003/saa-01-003-1.yaml \
--capabilities CAPABILITY_IAM
--region us-east-1

aws cloudformation create-stack \
--stack-name saa-01-003-2 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-01-003/saa-01-003-2.yaml \
--capabilities CAPABILITY_IAM
--region ap-northeast-1
```
