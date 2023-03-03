# Create RDS Cross-Region Read Replica using CloudFormation

https://awstut.com/en/2023/03/04/create-rds-cross-region-read-replica-using-cloudformation-en/

# Architecture

![saa-01-004-diagram](https://user-images.githubusercontent.com/84276199/222841920-7fb7bf80-6e9d-4e23-8cb1-dc299a833909.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-01-004-1.yaml and saa-01-004-2.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-01-004/ --recursive
```

## CloudFormation Stacks Creation

```bash
aws cloudformation create-stack \
--stack-name saa-01-004-1 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-01-004/saa-01-004-1.yaml \
--capabilities CAPABILITY_IAM
--region ap-northeast-1

aws cloudformation create-stack \
--stack-name saa-01-004-2 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-01-004/saa-01-004-2.yaml \
--capabilities CAPABILITY_IAM
--region us-east-1
```
