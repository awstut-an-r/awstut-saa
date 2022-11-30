# Improved Origin Server Performance with CloudFront Cache

https://awstut.com/en/2022/03/12/improved-origin-server-performance-with-cloudfront-cache/

# Architecture

![saa-02-005-diagram](https://user-images.githubusercontent.com/84276199/204907523-1f47799e-7691-4996-9bcd-2e04e604b3e2.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-02-005.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-02-005/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-02-004 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-02-005/saa-02-005.yaml \
--capabilities CAPABILITY_IAM
```
