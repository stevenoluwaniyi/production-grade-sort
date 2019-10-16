# Sorting API
## Deployed Two Ways: AWS Elastic Beanstalk and Lambda
This repo shows how to deploy the same sorting API in two different ways:
1. [AWS ElasticBeanstalk](https://aws.amazon.com/elasticbeanstalk/)
2. [AWS Lambda](https://aws.amazon.com/lambda/)

At the end you'll have two API's that sort a list of numbers:
![API with sorted numbers in browser hosted on Elastic Beanstalk](images/result-elastic-beanstalk.png)
![API with sorted numbers in browser hosted on Lambda](images/result-lambda.png)

## Prereqs
- [AWS account](https://aws.amazon.com/) with admin access
- [AWS CLI](https://aws.amazon.com/cli/) installed on laptop
- [GitHub](https://github.com/) account

## Day 1: Manual Deployment
```bash
git clone https://github.com/muymoo/production-grade-sort.git
cd production-grade-sort
```
### Elastic Beanstalk
1. `cd elasticbeanstalk`
2. Create zip: `zip -X ../elasticbeanstalk application.py requirements.txt` 
2. Create [AWS Elastic Beanstalk Environment](https://console.aws.amazon.com/elasticbeanstalk/home)
   1. Environment Tier: Web Server Environment
   2. Platform: Python
   3. Upload your code - use zip from step #1

### AWS Lambda
1. Create Lambda
   1. From Scratch
   2. Python 3.6
2. Copy handler code in from `lambda/handler.py` - rename `sort()` to `lambda_handler()`
3. Test with event:
``` 
{
  "queryStringParameters": {
      "numbers": "3,2,1,4"
  }
}
```
4. Create new AWS API Gateway REST API
5. New Method: GET
6. Lambda Function, Use Lambda Proxy Integration
7. Method Request: URL Query String Parameters - `numbers`
8. "Test"

## Day 2: Automated Pipeline 
### Elastic Beanstalk
https://aws.amazon.com/getting-started/tutorials/continuous-deployment-pipeline/

### AWS Lambda
https://docs.aws.amazon.com/lambda/latest/dg/build-pipeline.html
