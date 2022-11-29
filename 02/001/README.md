# Performance Verification of Cluster Placement Group

https://awstut.com/en/2021/12/19/performance-verification-of-cluster-placement-groups/

# Architecture

![saa-02-001-diagram](https://user-images.githubusercontent.com/84276199/204646657-864b226b-1ddd-4d4a-84a8-e563b172111c.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-02-001.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-02-001/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-02-001 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-02-001/saa-02-001.yaml \
--capabilities CAPABILITY_IAM
```
