# Store data in S3 bucket received by Kinesis Data Streams via Firehose

https://awstut.com/en/2023/05/07/store-data-in-s3-bucket-received-by-kinesis-data-streams-via-firehose-en/

# Architecture

![saa-04-003-diagram](https://user-images.githubusercontent.com/84276199/236666622-0a2c7240-a060-48ec-8392-7de8b23445c9.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-04-003.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-01-003/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-04-003 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-04-003/saa-04-003.yaml \
--capabilities CAPABILITY_IAM
```
