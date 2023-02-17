# 3 ways to access S3 from private subnet

https://awstut.com/en/2023/02/18/3-ways-to-access-s3-from-private-subnet-en/

# Architecture

![saa-03-003-diagram](https://user-images.githubusercontent.com/84276199/219805676-d3818c86-09c2-4fee-9b18-1f7f9f6e59fb.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-03-003.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-03-003/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-03-003 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-03-003/saa-03-003.yaml \
--capabilities CAPABILITY_IAM
```
