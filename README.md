# technical-test-python-app

#HERE ARE THE STEPS

Setup and Deployment Instructions

We will follow these steps to set up and deploy the Python application with S3 upload and DocumentDB integration via SSH tunnel using AWS App Runner YAML.

Pre-requisites:

An AWS account with appropriate permissions to create and manage resources.
Python is installed on my local machine.
AWS CLI installed and configured with appropriate IAM user credentials in my aws account.
I have access to an existing DocumentDB cluster.
Basic knowledge of AWS App Runner, S3, DocumentDB, and SSH tunneling concepts.

Step 1: Clone the Repository

git clone <repository-url>
cd <repository-directory>

Step 2: Configure AWS Credentials


aws configure
I will follow the prompts to input in my AWS IAM user credentials, including Access Key ID and Secret Access Key.

Step 3: Configure Environment Variables

cp .env.example .env
I will edit the .env file and update the placeholders with actual values for S3 bucket name, DocumentDB details, file path, and SSH tunnel parameters.

Step 4: Set Up SSH Tunneling

# Generate SSH key pair
ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa -q -N ""

# Configure SSH tunnel
ssh -N -L <local-port>:<documentdb-host>:<documentdb-port> <ec2-instance-user>@<ec2-instance-ip>
I will replace placeholders with actual values for the DocumentDB host, port, EC2 instance user, and IP.

Step 5: Deploy the Application using AWS App Runner YAML

# Deploy using AWS CLI
aws apprunner create-service --cli-input-yaml file://apprunner.yaml
I will ensure that apprunner.yaml file is properly configured with necessary settings for App Runner, S3, and DocumentDB integration.

Step 6: Access the Application
Once the deployment is successful,I will access the deployed application through the provided App Runner URL.

===============================================================================================
