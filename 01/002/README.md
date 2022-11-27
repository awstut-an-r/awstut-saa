# Data Linkage between Fargate Containers Using SQS

https://awstut.com/en/2022/02/06/data-linkage-between-fargate-containers-using-sqs-2/

# Architecture

![saa-01-002-diagram](https://user-images.githubusercontent.com/84276199/204133927-f4944967-cc32-47c7-b4e5-b359383b3fb9.png)

# Requirements

* AWS CLI
* S3 Bucket(Here, the bucket name is *my-bucket* and region is *ap-northeast-1*)

# Usage

## Tempalte File Modification

Modify the following locations in saa-01-002.yaml.

```yaml
Parameters:
  TemplateBucketName:
    Type: String
    Default: [bucket-name]
```

## Upload  Template Files to S3 Bucket

```bash
aws s3 cp . s3://my-bucket/saa-01-002/ --recursive
```

## Prepare ECR Repository

```bash
aws cloudformation create-stack --stack-name saa-01-002-ecr --template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-01-002/saa-01-002-ecr.yaml
```

### Push Container 1

```bash
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin [account-id].dkr.ecr.ap-northeast-1.amazonaws.com

docker build -t saa-01-002-repository1 ./service1

docker tag saa-01-002-repository1:latest [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/saa-01-002-repository1:latest

docker push [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/saa-01-002-repository1:latest
```

### Push Container 2

```bash
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin [account-id].dkr.ecr.ap-northeast-1.amazonaws.com

docker build -t saa-01-002-repository2 ./service2

docker tag saa-01-002-repository2:latest [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/saa-01-002-repository2:latest

docker push [account-id].dkr.ecr.ap-northeast-1.amazonaws.com/saa-01-002-repository2:latest
```

## CloudFormation Stack Creation

```bash
aws cloudformation create-stack \
--stack-name saa-01-002 \
--template-url https://my-bucket.s3.ap-northeast-1.amazonaws.com/saa-01-002/saa-01-002.yaml \
--capabilities CAPABILITY_IAM
```
