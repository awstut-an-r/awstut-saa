# AWS WAF to prevent XSS with CloudFormation

https://awstut.com/en/2024/05/02/aws-waf-to-prevent-xss-with-cloudformation-en/

# Architecture

![saa-03-006-diagram](https://github.com/awstut-an-r/awstut-fa/assets/84276199/8fdce14f-0134-43eb-b538-e667d610ddac)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-03-006.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-03-006/ --recursive
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-03-006 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-03-006/saa-03-006.yaml \
--capabilities CAPABILITY_IAM
```
