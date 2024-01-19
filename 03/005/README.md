# Create network ACLs using CloudFormation

https://awstut.com/en/2024/01/20/create-network-acls-using-cloudformation-en/

# Architecture

![saa-03-005-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/aa111f81-96d5-490d-9cc9-e54534015462)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-03-005.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-03-005/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-03-005 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-03-005/saa-03-005.yaml \
--capabilities CAPABILITY_IAM
```
