#!/bin/bash

# Create the deployment package
rm -rf deployment_package.zip
mkdir package
pip install -r requirements.txt --target package
cd package && zip -r9 ../deployment_package.zip . && cd ..

# Create the Lambda function
aws lambda create-function \
  --function-name $LAMBDA_FUNCTION_NAME \
  --runtime python3.8 \
  --role $LAMBDA_ROLE_ARN \
  --handler $LAMBDA_HANDLER_NAME \
  --timeout $LAMBDA_TIMEOUT \
  --memory-size $LAMBDA_MEMORY_SIZE \
  --zip-file fileb://deployment_package.zip \
  --region $REGION_NAME

# Update the Lambda function
aws lambda update-function-code \
  --function-name $LAMBDA_FUNCTION_NAME \
  --zip-file fileb://deployment_package.zip \
  --region $REGION_NAME






#Make sure to replace the variables in the script 
#with the appropriate values from your config.py file.

#This script creates a deployment package for the Lambda function, 
#installs the required dependencies, 
#and then creates or updates the Lambda function using the AWS CLI. 
#The function's code is updated with each execution of this script.
