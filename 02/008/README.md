# Create Aurora custom endpoints with CFN custom resources

https://awstut.com/en/2022/11/06/create-aurora-custom-endpoints-with-cfn-custom-resources-en/

# Architecture

![saa-02-008-diagram](https://user-images.githubusercontent.com/84276199/206928640-8e4e8de3-fe18-4e4f-a9aa-5ef2702a1348.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-02-008.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-02-008/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-02-008 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-02-008/saa-02-008.yaml \
--capabilities CAPABILITY_IAM
```
