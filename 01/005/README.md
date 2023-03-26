# Automation runbook to create an AMI for an instance and copy it to another region

https://awstut.com/en/2023/03/26/automation-runbook-to-create-an-ami-for-an-instance-and-copy-it-to-another-region-en/

# Architecture

![saa-01-005-diagram](https://user-images.githubusercontent.com/84276199/227766125-00bc574e-525a-4878-b6a6-ee745415ffcb.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-01-005.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-01-005/ --recursive
```

## CloudFormation Stacks Creation

```bash
aws cloudformation create-stack \
--stack-name saa-01-005 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-01-005/saa-01-005.yaml \
--capabilities CAPABILITY_IAM
```
