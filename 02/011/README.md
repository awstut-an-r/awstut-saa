# Specify ALB as the origin of CloudFront

https://awstut.com/en/2023/06/04/specify-alb-as-the-origin-of-cloudfront-en/

# Architecture

![saa-02-011-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/c233949e-ec96-43ff-9cf7-483c87682a44)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-02-011.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-02-011/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-02-011 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-02-011/saa-02-011.yaml \
--capabilities CAPABILITY_IAM
```
