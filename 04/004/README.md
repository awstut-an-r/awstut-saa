# Three ways to start/stop EC2 instances periodically

https://awstut.com/en/2023/08/18/three-ways-to-start-stop-ec2-instances-periodically-en/

# Architecture

![saa-04-004-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/858c84fa-25e6-49c7-ae65-e603f332209d)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-04-004.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-01-004/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-04-004 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-04-004/saa-04-004.yaml \
--capabilities CAPABILITY_IAM
```
