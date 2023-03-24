# Introduction to FSx for Lustre using CloudFormation

https://awstut.com/en/2023/03/25/introduction-to-fsx-for-lustre-using-cloudformation-en/

# Architecture

![saa-02-010-diagram](https://user-images.githubusercontent.com/84276199/227635509-d0be5ade-ed81-41d7-92b9-9d7513de4f39.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-02-010.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-02-010/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-02-010 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-02-010/saa-02-010.yaml \
--capabilities CAPABILITY_IAM
```
