Document Management with AWS

This project demonstrates how to build an efficient document management system using AWS services, including S3, Lambda, and SNS.

The system allows writers to upload documents directly to an S3 bucket and notifies the team leader of the document's word count using SNS. The word count is calculated using a Lambda function.

Prerequisites
Before running this project, you will need:

An AWS account
AWS CLI installed and configured on your local machine
Python 3.x installed on your local machine
Getting Started
To get started with this project, follow these steps:

Clone the repository to your local machine.
Create an S3 bucket and an SNS topic in your AWS account.
Update the config.py file with the S3 bucket name, SNS topic ARN, and other configurations as needed.
Install the required Python packages using pip install -r requirements.txt.
Deploy the Lambda function by running deploy_lambda.sh in the terminal.
Upload a document to the S3 bucket. The Lambda function will automatically calculate the word count and publish it to the SNS topic.
Check the SNS topic for the word count notification.

Architecture
This project uses the following AWS services:

S3: For storing the uploaded documents.
Lambda: For calculating the word count of the uploaded document.
SNS: For notifying the team leader of the word count.
Architecture Diagram

License
This project is licensed under the MIT License. See the LICENSE file for details.

References
For more information on AWS services used in this project, see the official AWS documentation:

Amazon S3 Developer Guide
AWS Lambda Developer Guide
Amazon SNS Developer Guide
