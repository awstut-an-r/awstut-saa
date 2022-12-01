# Introduction to EFS with CFN

https://awstut.com/en/2022/06/25/introduction-to-efs-with-cloudformation-en/

# Architecture

![saa-02-007-diagram](https://user-images.githubusercontent.com/84276199/205157652-cefd8524-982a-41a1-82f5-a28604164423.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-02-007.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-02-007/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-02-007 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-02-007/saa-02-007.yaml \
--capabilities CAPABILITY_IAM
```
