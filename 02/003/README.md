# Introduction to FSx for Windows

https://awstut.com/en/2022/01/19/introduction-to-fsx-for-windows-2/

# Architecture

![saa-02-003-diagram](https://user-images.githubusercontent.com/84276199/204647746-0d32a293-eb1e-4669-ba65-9c2b1a9b3b1b.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-02-003.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-02-003/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-02-003 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-02-003/saa-02-003.yaml \
--capabilities CAPABILITY_IAM
```
