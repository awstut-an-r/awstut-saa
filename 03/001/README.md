# CloudFront Geographic Restriction

https://awstut.com/en/2022/04/17/cloudfront-geographic-restriction-en/

# Architecture

![saa-03-001-diagram](https://user-images.githubusercontent.com/84276199/208523419-da8fe00a-c0da-46e7-befe-19c50c5345ca.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-03-001.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-03-001/ --recursive
```

## CloudFormation Stack Creation

### Server Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-03-001 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-03-001/saa-03-001.yaml \
--capabilities CAPABILITY_IAM \
--region ap-northeast-1
```

### Test Client Stack 1 Creation

```bash
aws cloudformation create-stack \
--stack-name saa-03-001-test \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-03-001/saa-03-001-test.yaml \
--capabilities CAPABILITY_IAM \
--region ap-northeast-1
```

### Test Client Stack 2 Creation

```bash
aws cloudformation create-stack \
--stack-name saa-03-001-test \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-03-001/saa-03-001-test.yaml \
--capabilities CAPABILITY_IAM \
--region us-east-1
```
