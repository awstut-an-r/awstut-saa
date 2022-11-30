# EC2 Auto Scaling Scheduled Actions

https://awstut.com/en/2022/03/06/ec2-auto-scaling-scheduled-actions/

# Architecture

![saa-02-004-diagram](https://user-images.githubusercontent.com/84276199/204907075-f09587bd-1fc8-4a9d-ab03-6aec142fa557.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-02-004.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-02-004/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-02-004 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-02-004/saa-02-004.yaml \
--capabilities CAPABILITY_IAM
```
