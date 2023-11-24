# Elastic Beanstalk deployment policy: Rolling with an additional batch

https://awstut.com/en/2023/11/25/elastic-beanstalk-deployment-policy-rolling-with-an-additional-batch-en/

# Architecture

![dva-01-003-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/739d2557-1dec-4960-bb1d-455bc8f55f5e)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in dva-01-003.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/dva-01-003/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name dva-01-003 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/dva-01-003/dva-01-003.yaml \
--capabilities CAPABILITY_IAM
```
