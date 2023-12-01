# Using CloudFormation to configure security groups for NLB

https://awstut.com/en/2023/12/02/use-cloudformation-to-build-a-route53-geolocation-routing-policy-environment-en/

# Architecture

![saa-01-007-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/4a7272b4-0f27-4569-903a-b0458b0957fb)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-01-007.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-01-007/ --recursive
```

## CloudFormation Stacks Creation

```bash
aws cloudformation create-stack \
--stack-name saa-01-007 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-01-007/saa-01-007.yaml \
--capabilities CAPABILITY_NAMED_IAM
```
