# AWS configurations
REGION_NAME = 'us-east-1'

# S3 configurations
S3_BUCKET_NAME = 'your-s3-bucket-name'

# Lambda configurations
LAMBDA_FUNCTION_NAME = 'document_wordcount_lambda'
LAMBDA_HANDLER_NAME = 'lambda_function.lambda_handler'
LAMBDA_ROLE_ARN = 'arn:aws:iam::123456789012:role/lambda-execution-role'
LAMBDA_TIMEOUT = 60
LAMBDA_MEMORY_SIZE = 128

# SNS configurations
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:123456789012:document_wordcount_topic'


#Make sure to replace the AWS configurations with your own values. In this example, you'll need to replace:

            ###S3_BUCKET_NAME with the name of the S3 bucket you created.
            ###LAMBDA_ROLE_ARN with the ARN of the IAM role you created for the Lambda function to assume.
            ###SNS_TOPIC_ARN with the ARN of the SNS topic you created.
            ###You may also need to update other configurations, such as the Lambda function name and timeout, depending on your specific requirements. 
