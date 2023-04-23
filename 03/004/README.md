# Two ways to access DynamoDB from private subnets

https://awstut.com/en/2023/04/23/two-ways-to-access-dynamodb-from-private-subnets-en/

# Architecture

![saa-03-004-diagram](https://user-images.githubusercontent.com/84276199/233831147-994abc9c-1406-4899-820e-ccd02c607eac.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-03-004.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-03-004/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-03-004 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-03-004/saa-03-004.yaml \
--capabilities CAPABILITY_IAM
```
