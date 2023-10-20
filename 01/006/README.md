# Using CloudFormation to configure security groups for NLB

https://awstut.com/en/2023/10/21/using-cloudformation-to-configure-security-groups-for-nlb-en/

# Architecture

![saa-01-006-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/8e9708ee-4ba1-4c76-b931-cea3322b27c9)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-01-006.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-01-006/ --recursive
```

## CloudFormation Stacks Creation

```bash
aws cloudformation create-stack \
--stack-name saa-01-006 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-01-006/saa-01-006.yaml \
--capabilities CAPABILITY_IAM
```
