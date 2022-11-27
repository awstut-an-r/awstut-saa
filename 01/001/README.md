# Failing over with Route53 and displaying error page

https://awstut.com/en/2021/12/11/failing-over-with-route53-and-displaying-an-error-page/

# Architecture

![saa-01-001-diagram](https://user-images.githubusercontent.com/84276199/204133753-ef4af43d-9ed6-4ea8-b891-b014b9cd4833.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-01-001.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-01-001/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-01-001 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-01-001/saa-01-001.yaml \
--capabilities CAPABILITY_IAM
```
