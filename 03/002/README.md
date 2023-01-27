# Access NLB in another VPC via VPC Endpoint

https://awstut.com/en/2023/01/28/access-nlb-in-another-vpc-via-vpc-endpoint-en/

# Architecture

![saa-03-002-diagram](https://user-images.githubusercontent.com/84276199/215221584-9ff00aa8-58a4-4b18-84b6-928e413645e2.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-03-002.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-03-002/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-03-002 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-03-002/saa-03-002.yaml \
--capabilities CAPABILITY_IAM
```
