# Easy to verify performance of S3 Transfer Acceleration

https://awstut.com/en/2021/12/26/easy-to-verify-performance-of-s3-transfer-acceleration/

# Architecture

![saa-02-002-diagram](https://user-images.githubusercontent.com/84276199/204647390-3507fa67-0c2c-409e-b5d9-ab86ba7b59a7.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-02-002.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-02-002/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-02-002 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-02-002/saa-02-002.yaml \
--capabilities CAPABILITY_IAM
```
