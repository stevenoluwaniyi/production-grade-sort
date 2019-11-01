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
(#elastic-beanstalk)
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
1. Follow steps from Day 1 - ["Elastic Beanstalk"](#elastic-beanstalk)
2. Fork this repository
3. [Code Pipeline](http://console.aws.amazon.com/codepipeline)
4. "Create New Pipeline"
5. Name: `eb-production-sort`, Role: Create New
6. Source Provider: GitHub
7. "Connect to GitHub"
8. ![Repository: <your username>/production-grade-sort](images/github.png)
9. CodeBuild: "Create Project"
   1. Name: `eb-production-sort-build`
   2. Env: `Managed Image` > `Amazon Linux 2`
   3. Runtimes: `Standard`
   ![Use default or only options from drop downs](images/code-build.png)
   4. Use buildspec file. Location: `elasticbeanstalk/buildspec.yml`
   5. "Continue to CodePipeline"
10. Deploy to ElasticBeanstalk environment we careated in step #1
![Deploy to EB environment created in step #1](images/deploy.png)
11. "Next", "Create Pipeline"

Inspired by: https://aws.amazon.com/getting-started/tutorials/continuous-deployment-pipeline/ (uses PHP instead of Python)
### AWS Lambda
1. [Code Pipeline](http://console.aws.amazon.com/codepipeline)
2. "Create New Pipeline"
3. ![Use defaults for pipeline](images/lambda-pipeline.png)
4. Source Provdier: GitHub"
5. "Connect to GitHub"
6. 


https://docs.aws.amazon.com/lambda/latest/dg/build-pipeline.html
