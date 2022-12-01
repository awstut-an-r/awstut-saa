# Read Replica and Endpoints of Aurora Cluster

https://awstut.com/en/2022/03/23/read-replica-and-endpoints-of-aurora-cluster/

# Architecture

![saa-02-006-diagram](https://user-images.githubusercontent.com/84276199/205156573-edf72eb7-5f8e-404a-91ab-029be8b9249e.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-02-006.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-02-006/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-02-006 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-02-006/saa-02-006.yaml \
--capabilities CAPABILITY_IAM
```
