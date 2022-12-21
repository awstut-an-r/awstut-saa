# Introduction to Kinesis Data Analytics – Real-time analysis of streaming data

https://awstut.com/en/2022/02/11/introduction-to-kinesis-data-analytics-2/

# Architecture

![saa-04-001-diagram](https://user-images.githubusercontent.com/84276199/209002272-4ef4991f-2694-4c99-bdb2-99768f96a75a.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-04-001.yaml.

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
--stack-name saa-04-001 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-04-001/saa-04-001.yaml \
--capabilities CAPABILITY_IAM
```
