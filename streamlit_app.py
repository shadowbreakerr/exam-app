# streamlit_app.py
# SAP-C02 Practice Quiz (Streamlit) – offline, embedded dataset
import streamlit as st
import random, textwrap

QUESTIONS = [
  {
    "id": "1",
    "question": "- (Exam Topic 1) A solutions architect is designing a publicly accessible web application that is on an Amazon CloudFront distribution with an Amazon S3 website endpoint as the origin. When the solution is deployed, the website returns an Error 403: Access Denied message. Which steps should the solutions architect take to correct the issue? (Select TWO.) A. Remove the S3 block public access option from the S3 bucket. B. Remove the requester pays option trom the S3 bucket. C. Remove the origin access identity (OAI) from the CloudFront distribution. D. Change the storage class from S3 Standard to S3 One Zone-Infrequent Access (S3 One Zone-IA). E. Disable S3 object versioning. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Remove the S3 block public access option from the S3 bucket.",
      "B": "Remove the requester pays option trom the S3 bucket.",
      "C": "Remove the origin access identity (OAI) from the CloudFront distribution.",
      "D": "Change the storage class from S3 Standard to S3 One Zone-Infrequent Access (S3 One Zone-IA).",
      "E": "Disable S3 object versioning. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "B"
    ],
    "select_n": 2,
    "explanation": "See using S3 to host a static website with Cloudfront: https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/\n- Using a REST API endpoint as the origin, with access restricted by an origin access identity (OAI)\n- Using a website endpoint as the origin, with anonymous (public) access allowed\n- Using a website endpoint as the origin, with access restricted by a Referer header\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "2",
    "question": "- (Exam Topic 1) A company wants to deploy an AWS WAF solution to manage AWS WAF rules across multiple AWS accounts. The accounts are managed under different OUs in AWS Organizations. Administrators must be able to add or remove accounts or OUs from managed AWS WAF rule sets as needed. Administrators also must have the ability to automatically update and remediate noncompliant AWS WAF rules in all accounts Which solution meets these requirements with the LEAST amount of operational overhead? A. Use AWS Firewall Manager to manage AWS WAF rules across accounts in the organizatio B. Use an AWS Systems Manager Parameter Store parameter to store accountnumbers and OUs to manage Update the parameter as needed to add or remove accounts or OUs Use an Amazon EventBridge (Amazon CloudWatch Events) rule to identify any changes to the parameter and to invoke an AWS Lambda function to update the security policy in the Firewall Manager administrative account C. Deploy an organization-wide AWS Conng rule that requires all resources in the selected OUs to associate the AWS WAF rule D. Deploy automated remediation actions by using AWS Lambda to fix noncompliant resource E. Deploy AWS WAF rules by using an AWS CloudFormation stack set to target the same OUs where the AWS Config rule is applied. F. Create AWS WAF rules in the management account of the organizatio G. Use AWS Lambda environment variables to store account numbers and OUs to manage Update environment variables as needed to add or remove accounts or OUs Create cross-account IAM roles in member account H. Assume the roles by using AWS Security Token Service (AWS STS) in the Lambda function to create and update AWS WAF rules in the member accounts I. Use AWS Control Tower to manage AWS WAF rules across accounts in the organizatio J. Use AWS Key Management Service (AWS KMS) to store account numbers and OUs to manage Update AWS KMS as needed to add or remove accounts or OU K. Create IAM users in member accounts Allow AWS Control Tower in the management account to use the access key and secret access key to create and update AWS WAF rules in the member accounts -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS Firewall Manager to manage AWS WAF rules across accounts in the organizatio",
      "B": "Use an AWS Systems Manager Parameter Store parameter to store accountnumbers and OUs to manage Update the parameter as needed to add or remove accounts or OUs Use an Amazon EventBridge (Amazon CloudWatch Events) rule to identify any changes to the parameter and to invoke an AWS Lambda function to update the security policy in the Firewall Manager administrative account",
      "C": "Deploy an organization-wide AWS Conng rule that requires all resources in the selected OUs to associate the AWS WAF rule",
      "D": "Deploy automated remediation actions by using AWS Lambda to fix noncompliant resource",
      "E": "Deploy AWS WAF rules by using an AWS CloudFormation stack set to target the same OUs where the AWS Config rule is applied.",
      "F": "Create AWS WAF rules in the management account of the organizatio",
      "G": "Use AWS Lambda environment variables to store account numbers and OUs to manage Update environment variables as needed to add or remove accounts or OUs Create cross-account IAM roles in member account",
      "H": "Assume the roles by using AWS Security Token Service (AWS STS) in the Lambda function to create and update AWS WAF rules in the member accounts",
      "I": "Use AWS Control Tower to manage AWS WAF rules across accounts in the organizatio",
      "J": "Use AWS Key Management Service (AWS KMS) to store account numbers and OUs to manage Update AWS KMS as needed to add or remove accounts or OU K. Create IAM users in member accounts Allow AWS Control Tower in the management account to use the access key and secret access key to create and update AWS WAF rules in the member accounts -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "3",
    "question": "- (Exam Topic 1) A company Is serving files to its customers through an SFTP server that Is accessible over the internet The SFTP server Is running on a single Amazon EC2 instance with an Elastic IP address attached Customers connect to the SFTP server through its Elastic IP address and use SSH for authentication The EC2 instance also has an attached security group that allows access from all customer IP addresses. A solutions architect must implement a solution to improve availability minimize the complexity ot infrastructure management and minimize the disruption to customers who access files. The solution must not change the way customers connect. Which solution will meet these requirements? A. Disassociate the Elastic IP address from me EC2 instance Create an Amazon S3 bucket to be used for sftp file hosting Create an AWS Transfer Family server Configure the Transfer Family server with a publicly accessible endpoin B. Associate the SFTP Elastic IP address with the new endpoin C. Point the Transfer Family server to the S3 bucket Sync all files from the SFTP server to the S3 bucket. D. Disassociate the Elastic IP address from the EC2 instanc E. Create an Amazon S3 bucket to be used for SFTP file hosting Create an AWS Transfer Family serve F. Configure the Transfer Family server with a VPC-hoste G. internet-facing endpoin H. Associate the SFTP Elastic IP address with the new endpoin I. Attach the security group with customer IP addresses to the new endpoin J. Point the Transfer Family server to the S3 bucke K. Sync all files from the SFTP server to The S3 bucket L. Disassociate the Elastic IP address from the EC2 instanc M. Create a new Amazon Elastic File System (Amazon EFS) file system to be used for SFTP file hostin N. Create an AWS Fargate task definition to run an SFTP serve O. Specify the EFS file system as a mount in the task definition Create a Fargate service by using the task definition, and place a Network Load Balancer (NLB> «i front of the service When configuring the service, attach the security group with customer IP addresses to the tasks that run the SFTP server Associate the Elastic IP address with the Nl B Sync all files from the SFTP server to the S3 bucket P. Disassociate the Elastic IP address from the EC2 instance Create a multi-attach Amazon Elastic Block Store (Amazon EBS) volume to be used to SFTP file hosting Create a Network Load Balancer (NLB) with the Elastic IP address attached Create an Auto Scaling group with EC2 instances that run an SFTP server Define in the Auto Scaling group that instances that are launched should attach the newmulti-attach EBS volume Configure the Auto Scaling group to automatically add instances behind the NLB Configure the Auto Scaling group to use the security group that allows customer IP addresses for the EC2 instances that the Auto Scaling group launches Sync all files from the SFTP server to the new multi-attach EBS volume -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Disassociate the Elastic IP address from me EC2 instance Create an Amazon S3 bucket to be used for sftp file hosting Create an AWS Transfer Family server Configure the Transfer Family server with a publicly accessible endpoin",
      "B": "Associate the SFTP Elastic IP address with the new endpoin",
      "C": "Point the Transfer Family server to the S3 bucket Sync all files from the SFTP server to the S3 bucket.",
      "D": "Disassociate the Elastic IP address from the EC2 instanc",
      "E": "Create an Amazon S3 bucket to be used for SFTP file hosting Create an AWS Transfer Family serve",
      "F": "Configure the Transfer Family server with a VPC-hoste",
      "G": "internet-facing endpoin",
      "H": "Associate the SFTP Elastic IP address with the new endpoin",
      "I": "Attach the security group with customer IP addresses to the new endpoin",
      "J": "Point the Transfer Family server to the S3 bucke K. Sync all files from the SFTP server to The S3 bucket L. Disassociate the Elastic IP address from the EC2 instanc M. Create a new Amazon Elastic File System (Amazon EFS) file system to be used for SFTP file hostin N. Create an AWS Fargate task definition to run an SFTP serve O. Specify the EFS file system as a mount in the task definition Create a Fargate service by using the task definition, and place a Network Load Balancer (NLB> «i front of the service When configuring the service, attach the security group with customer IP addresses to the tasks that run the SFTP server Associate the Elastic IP address with the Nl B Sync all files from the SFTP server to the S3 bucket P. Disassociate the Elastic IP address from the EC2 instance Create a multi-attach Amazon Elastic Block Store (Amazon EBS) volume to be used to SFTP file hosting Create a Network Load Balancer (NLB) with the Elastic IP address attached Create an Auto Scaling group with EC2 instances that run an SFTP server Define in the Auto Scaling group that instances that are launched should attach the newmulti-attach EBS volume Configure the Auto Scaling group to automatically add instances behind the NLB Configure the Auto Scaling group to use the security group that allows customer IP addresses for the EC2 instances that the Auto Scaling group launches Sync all files from the SFTP server to the new multi-attach EBS volume -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "https://aws.amazon.com/premiumsupport/knowledge-center/aws-sftp-endpoint-type/\nhttps://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html https://aws.amazon.com/premiumsupport/knowledge-center/aws-sftp-endpoint-\ntype/\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "4",
    "question": "- (Exam Topic 1) A company is running an application on several Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer. The load on the application varies throughout the day, and EC2 instances are scaled in and out on a regular basis. Log files from the EC2 instances are copied to a central Amazon S3 bucket every 15 minutes. The security team discovers that log files are missing from some of the terminated EC2 instances. Which set of actions will ensure that log files are copied to the central S3 bucket from the terminated EC2 instances? A. Create a script to copy log files to Amazon S3, and store the script in a file on the EC2 instanc B. Create an Auto Scaling lifecycle hook and an Amazon EventBridge (Amazon CloudWatch Events) rule to detect lifecycle events from the Auto Scaling grou C. Invoke an AWS Lambda function on the autoscaling:EC2_INSTANCE_TERMINATING transition to send ABANDON to the Auto Scaling group to prevent termination, run the script to copy the log files, and terminate the instance using the AWS SDK. D. Create an AWS Systems Manager document with a script to copy log files to Amazon S3. Create an Auto Scaling lifecycle hook and an Amazon EventBridge (Amazon CloudWatch Events) rule to detect lifecycle events from the Auto Scaling grou E. Invoke an AWS Lambda function on the autoscaling:EC2_INSTANCE_TERMINATING transition to call the AWS Systems Manager API SendCommand operation to run the document to copy the log files and send CONTINUE to the Auto Scaling group to terminate the instance. F. Change the log delivery rate to every 5 minute G. Create a script to copy log files to Amazon S3, and add the script to EC2 instance user dat H. Create an Amazon EventBridge (Amazon CloudWatch Events) rule to detect EC2 instance terminatio I. Invoke an AWS Lambda function from the EventBridge (CloudWatch Events) rule that uses the AWS CLI to run the user-data script to copy the log files and terminate the instance. J. Create an AWS Systems Manager document with a script to copy log files to Amazon S3. Create an Auto Scaling lifecycle hook that publishes a message to an Amazon Simple Notification Service (Amazon SNS) topi K. From the SNS notification, call the AWS Systems Manager API SendCommand operation to run the document to copy the log files and send ABANDON to the Auto Scaling group to terminate the instance. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a script to copy log files to Amazon S3, and store the script in a file on the EC2 instanc",
      "B": "Create an Auto Scaling lifecycle hook and an Amazon EventBridge (Amazon CloudWatch Events) rule to detect lifecycle events from the Auto Scaling grou",
      "C": "Invoke an AWS Lambda function on the autoscaling:EC2_INSTANCE_TERMINATING transition to send ABANDON to the Auto Scaling group to prevent termination, run the script to copy the log files, and terminate the instance using the AWS SDK.",
      "D": "Create an AWS Systems Manager document with a script to copy log files to Amazon S3. Create an Auto Scaling lifecycle hook and an Amazon EventBridge (Amazon CloudWatch Events) rule to detect lifecycle events from the Auto Scaling grou",
      "E": "Invoke an AWS Lambda function on the autoscaling:EC2_INSTANCE_TERMINATING transition to call the AWS Systems Manager API SendCommand operation to run the document to copy the log files and send CONTINUE to the Auto Scaling group to terminate the instance.",
      "F": "Change the log delivery rate to every 5 minute",
      "G": "Create a script to copy log files to Amazon S3, and add the script to EC2 instance user dat",
      "H": "Create an Amazon EventBridge (Amazon CloudWatch Events) rule to detect EC2 instance terminatio",
      "I": "Invoke an AWS Lambda function from the EventBridge (CloudWatch Events) rule that uses the AWS CLI to run the user-data script to copy the log files and terminate the instance.",
      "J": "Create an AWS Systems Manager document with a script to copy log files to Amazon S3. Create an Auto Scaling lifecycle hook that publishes a message to an Amazon Simple Notification Service (Amazon SNS) topi K. From the SNS notification, call the AWS Systems Manager API SendCommand operation to run the document to copy the log files and send ABANDON to the Auto Scaling group to terminate the instance. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/autoscaling/ec2/userguide/adding-lifecycle-hooks.html\n- Refer to Default Result section - If the instance is terminating, both abandon and continue allow the instance\nto terminate. However, abandon stops any remaining actions, such as other lifecycle hooks, and continue allows any other lifecycle hooks to complete.\nhttps://aws.amazon.com/blogs/infrastructure-and-automation/run-code-before-terminating-an-ec2-auto-scaling-i https://github.com/aws-samples/aws-lambda-\nlifecycle-hooks-function\nhttps://github.com/aws-samples/aws-lambda-lifecycle-hooks-function/blob/master/cloudformation/template.yam\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "5",
    "question": "- (Exam Topic 1) A development team has created a new flight tracker application that provides near-real-time data to users. The application has a front end that consists of an Application Load Balancer (ALB) in front of two large Amazon EC2 instances in a single Availability Zone. Data is stored in a single Amazon RDS MySQL DB instance. An Amazon Route 53 DNS record points to the ALB. Management wants the development team to improve the solution to achieve maximum reliability with the least amount of operational overhead. Which set of actions should the team take? A. Create RDS MySQL read replica B. Deploy the application to multiple AWS Region C. Use a Route 53 latency-based routing policy to route to the application. D. Configure the DB instance as Multi-A E. Deploy the application to two additional EC2 instances in different Availability Zones behind an ALB. F. Replace the DB instance with Amazon DynamoDB global table G. Deploy the application in multiple AWS Region H. Use a Route 53 latency-based routing policy to route to the application. I. Replace the DB instance with Amazon Aurora with Aurora Replica J. Deploy the application to mulliple smaller EC2 instances across multiple Availability Zones in an Auto Scaling group behind an ALB.",
    "options": {
      "A": "Create RDS MySQL read replica",
      "B": "Deploy the application to multiple AWS Region",
      "C": "Use a Route 53 latency-based routing policy to route to the application.",
      "D": "Configure the DB instance as Multi-A",
      "E": "Deploy the application to two additional EC2 instances in different Availability Zones behind an ALB.",
      "F": "Replace the DB instance with Amazon DynamoDB global table",
      "G": "Deploy the application in multiple AWS Region",
      "H": "Use a Route 53 latency-based routing policy to route to the application.",
      "I": "Replace the DB instance with Amazon Aurora with Aurora Replica",
      "J": "Deploy the application to mulliple smaller EC2 instances across multiple Availability Zones in an Auto Scaling group behind an ALB."
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "Multi AZ ASG + ALB + Aurora = Less over head and automatic scaling\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "6",
    "question": "- (Exam Topic 1) A company has developed an application that is running Windows Server on VMware vSphere VMs that the company hosts or premises. The application data is stored in a proprietary format that must be read through the application. The company manually provisioned the servers and the application. As pan of us disaster recovery plan, the company warns the ability to host its application on AWS temporarily me company's on-premises environment becomes unavailable The company wants the application to return to on-premises hosting after a disaster recovery event is complete The RPO 15 5 minutes. Which solution meets these requirements with the LEAST amount of operational overhead? A. Configure AWS DataSyn B. Replicate the data lo Amazon Elastic Block Store (Amazon EBS) volumes When the on-premises environment is unavailable, use AWS CloudFormation templates to provision Amazon EC2 instances and attach the EBS volumes C. Configure CloudEndure Disaster Recovery Replicate the data to replication Amazon EC2 instances that are attached to Amazon Elastic Block Store (Amazon EBS) volumes When the on-premises environment is unavailable, use CloudEndure to launch EC2 instances that use the replicated volumes. D. Provision an AWS Storage Gateway We gatewa E. Recreate the data lo an Amazon S3 bucke F. When the on-premises environment is unavailable, use AWS Backup to restore the data to Amazon Elastic Block Store (Amazon EBS) volumes and launch Amazon EC2 instances from these EBS volumes G. Provision an Amazon FS* for Windows File Server file system on AWS Replicate :ne data to the «e system When the on-premoes environment is unavailable, use AWS CloudFormation templates to provision Amazon EC2 instances and use AWS :CloudFofmation::lnit commands to mount the Amazon FSx file shares -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure AWS DataSyn",
      "B": "Replicate the data lo Amazon Elastic Block Store (Amazon EBS) volumes When the on-premises environment is unavailable, use AWS CloudFormation templates to provision Amazon EC2 instances and attach the EBS volumes",
      "C": "Configure CloudEndure Disaster Recovery Replicate the data to replication Amazon EC2 instances that are attached to Amazon Elastic Block Store (Amazon EBS) volumes When the on-premises environment is unavailable, use CloudEndure to launch EC2 instances that use the replicated volumes.",
      "D": "Provision an AWS Storage Gateway We gatewa",
      "E": "Recreate the data lo an Amazon S3 bucke",
      "F": "When the on-premises environment is unavailable, use AWS Backup to restore the data to Amazon Elastic Block Store (Amazon EBS) volumes and launch Amazon EC2 instances from these EBS volumes",
      "G": "Provision an Amazon FS* for Windows File Server file system on AWS Replicate :ne data to the «e system When the on-premoes environment is unavailable, use AWS CloudFormation templates to provision Amazon EC2 instances and use AWS :CloudFofmation::lnit commands to mount the Amazon FSx file shares -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "7",
    "question": "- (Exam Topic 1) A company wants to retire its Oracle Solaris NFS storage arrays. The company requires rapid data migration over its internet network connection to a combination of destinations for Amazon S3. Amazon Elastic File System (Amazon EFS), and Amazon FSx lor Windows File Server. The company also requires a full initial copy, as well as incremental transfers of changes until the retirement of the storage arrays. All data must be encrypted and checked for integrity. What should a solutions architect recommend to meet these requirements? A. Configure CloudEndur B. Create a project and deploy the CloudEndure agent and token to the storage arra C. Run the migration plan to start the transfer. D. Configure AWS DataSyn E. Configure the DataSync agent and deploy it to the local networ F. Create a transfer task and start the transfer. G. Configure the aws S3 sync comman H. Configure the AWS client on the client side with credential I. Run the sync command to start the transfer. J. Configure AWS Transfer (or FT K. Configure the FTP client with credential L. Script the client to connect and sync to start the transfer. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure CloudEndur",
      "B": "Create a project and deploy the CloudEndure agent and token to the storage arra",
      "C": "Run the migration plan to start the transfer.",
      "D": "Configure AWS DataSyn",
      "E": "Configure the DataSync agent and deploy it to the local networ",
      "F": "Create a transfer task and start the transfer.",
      "G": "Configure the aws S3 sync comman",
      "H": "Configure the AWS client on the client side with credential",
      "I": "Run the sync command to start the transfer.",
      "J": "Configure AWS Transfer (or FT K. Configure the FTP client with credential L. Script the client to connect and sync to start the transfer. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "8",
    "question": "- (Exam Topic 1) A company has a three-tier application running on AWS with a web server, an application server, and an Amazon RDS MySQL DB instance. A solutions architect is designing a disaster recovery (OR) solution with an RPO of 5 minutes. Which solution will meet the company's requirements? A. Configure AWS Backup to perform cross-Region backups of all servers every 5 minute B. Reprovision the three tiers in the DR Region from the backups using AWS CloudFormation in the event of a disaster. C. Maintain another running copy of the web and application server stack in the DR Region using AWS CloudFormation drill detectio D. Configure cross-Region snapshots ol the DB instance to the DR Region every 5 minute E. In the event of a disaster, restore the DB instance using the snapshot in the DR Region. F. Use Amazon EC2 Image Builder to create and copy AMIs of the web and application server to both the primary and DR Region G. Create a cross-Region read replica of the DB instance in the DR Regio H. In the event of a disaster, promote the read replica to become the master and reprovision the servers with AWS CloudFormation using the AMIs. I. Create AMts of the web and application servers in the DR Regio J. Use scheduled AWS Glue jobs to synchronize the DB instance with another DB instance in the DR Regio K. In the event of a disaster, switch to the DB instance in the DR Region and reprovision the servers with AWS CloudFormation using the AMIs. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure AWS Backup to perform cross-Region backups of all servers every 5 minute",
      "B": "Reprovision the three tiers in the DR Region from the backups using AWS CloudFormation in the event of a disaster.",
      "C": "Maintain another running copy of the web and application server stack in the DR Region using AWS CloudFormation drill detectio",
      "D": "Configure cross-Region snapshots ol the DB instance to the DR Region every 5 minute",
      "E": "In the event of a disaster, restore the DB instance using the snapshot in the DR Region.",
      "F": "Use Amazon EC2 Image Builder to create and copy AMIs of the web and application server to both the primary and DR Region",
      "G": "Create a cross-Region read replica of the DB instance in the DR Regio",
      "H": "In the event of a disaster, promote the read replica to become the master and reprovision the servers with AWS CloudFormation using the AMIs.",
      "I": "Create AMts of the web and application servers in the DR Regio",
      "J": "Use scheduled AWS Glue jobs to synchronize the DB instance with another DB instance in the DR Regio K. In the event of a disaster, switch to the DB instance in the DR Region and reprovision the servers with AWS CloudFormation using the AMIs. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "deploying a brand new RDS instance will take >30 minutes. You will use EC2 Image builder to put the AMIs into the new region, but not use image builder to\nLAUNCH them.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "9",
    "question": "- (Exam Topic 1) A company has 50 AWS accounts that are members of an organization in AWS Organizations Each account contains multiple VPCs The company wants to use AWS Transit Gateway to establish connectivity between the VPCs in each member account Each time a new member account is created, the company wants to automate the process of creating a new VPC and a transit gateway attachment. Which combination of steps will meet these requirements? (Select TWO) A. From the management account, share the transit gateway with member accounts by using AWS Resource Access Manager B. Prom the management account, share the transit gateway with member accounts by using an AWS Organizations SCP C. Launch an AWS CloudFormation stack set from the management account that automatical^/ creates a new VPC and a VPC transit gateway attachment in a member accoun D. Associate the attachment with the transit gateway in the management account by using the transit gateway ID. E. Launch an AWS CloudFormation stack set from the management account that automatical^ creates a new VPC and a peering transit gateway attachment in a member accoun F. Share the attachment with the transit gateway in the management account by using a transit gateway service-linked role. G. From the management account, share the transit gateway with member accounts by using AWS Service Catalog -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "From the management account, share the transit gateway with member accounts by using AWS Resource Access Manager",
      "B": "Prom the management account, share the transit gateway with member accounts by using an AWS Organizations SCP",
      "C": "Launch an AWS CloudFormation stack set from the management account that automatical^/ creates a new VPC and a VPC transit gateway attachment in a member accoun",
      "D": "Associate the attachment with the transit gateway in the management account by using the transit gateway ID.",
      "E": "Launch an AWS CloudFormation stack set from the management account that automatical^ creates a new VPC and a peering transit gateway attachment in a member accoun",
      "F": "Share the attachment with the transit gateway in the management account by using a transit gateway service-linked role.",
      "G": "From the management account, share the transit gateway with member accounts by using AWS Service Catalog -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "10",
    "question": "- (Exam Topic 1) A company has multiple AWS accounts as part of an organization created with AWS Organizations. Each account has a VPC in the us-east-2 Region and is used for either production or development workloads. Amazon EC2 instances across production accounts need to communicate with each other, and EC2 instances across development accounts need to communicate with each other, but production and development instances should not be able to communicate with each other. To facilitate connectivity, the company created a common network account. The company used AWS Transit Gateway to create a transit gateway in the us-east-2 Region in the network account and shared the transit gateway with the entire organization by using AWS Resource Access Manager. Network administrators then attached VPCs in each account to the transit gateway, after which the EC2 instances were able to communicate across accounts. However, production and development accounts were also able to communicate with one another. Which set of steps should a solutions architect take to ensure production traffic and development traffic are completely isolated? A. Modify the security groups assigned to development EC2 instances to block traffic from production EC2 instance B. Modify the security groups assigned to production EC2 instances to block traffic from development EC2 instances. C. Create a tag on each VPC attachment with a value of either production or development, according to the type of account being attache D. Using the Network Manager feature of AWS Transit Gateway, create policies that restrict traffic between VPCs based on the value of this tag. E. Create separate route tables for production and development traffi F. Delete each account's association and route propagation to the default AWS Transit Gateway route tabl G. Attach development VPCs to the development AWS Transit Gateway route table and production VPCs to the production route table, and enable automatic route propagation on each attachment. H. Create a tag on each VPC attachment with a value of either production or development, according to the type of account being attache I. Modify the AWS Transit Gateway routing table to route production tagged attachments to one another and development tagged attachments to one another. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Modify the security groups assigned to development EC2 instances to block traffic from production EC2 instance",
      "B": "Modify the security groups assigned to production EC2 instances to block traffic from development EC2 instances.",
      "C": "Create a tag on each VPC attachment with a value of either production or development, according to the type of account being attache",
      "D": "Using the Network Manager feature of AWS Transit Gateway, create policies that restrict traffic between VPCs based on the value of this tag.",
      "E": "Create separate route tables for production and development traffi",
      "F": "Delete each account's association and route propagation to the default AWS Transit Gateway route tabl",
      "G": "Attach development VPCs to the development AWS Transit Gateway route table and production VPCs to the production route table, and enable automatic route propagation on each attachment.",
      "H": "Create a tag on each VPC attachment with a value of either production or development, according to the type of account being attache",
      "I": "Modify the AWS Transit Gateway routing table to route production tagged attachments to one another and development tagged attachments to one another. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/vpc/latest/tgw/vpc-tgw.pdf\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "10.2",
    "question": "- (Exam Topic 1) A finance company is running its business-critical application on current-generation Linux EC2 instances The application includes a self-managed MySQL database performing heavy I/O operations. The application is working fine to handle a moderate amount of traffic during the month. However, it slows down during the final three days of each month due to month-end reporting, even though the company is using Elastic Load Balancers and Auto Scaling within its infrastructure to meet the increased demand. Which of the following actions would allow the database to handle the month-end load with the LEAST impact on performance? A. Pre-warming Elastic Load Balancers, using a bigger instance type, changing all Amazon EBS volumes to GP2 volumes. B. Performing a one-time migration of the database cluster to Amazon RD C. and creating several additional read replicas to handle the load during end of month D. Using Amazon CioudWatch with AWS Lambda to change the typ E. size, or IOPS of Amazon EBS volumes in the cluster based on a specific CloudWatch metric F. Replacing all existing Amazon EBS volumes with new PIOPS volumes that have the maximum available storage size and I/O per second by taking snapshots before the end of the month and reverting back afterwards. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Pre-warming Elastic Load Balancers, using a bigger instance type, changing all Amazon EBS volumes to GP2 volumes.",
      "B": "Performing a one-time migration of the database cluster to Amazon RD",
      "C": "and creating several additional read replicas to handle the load during end of month",
      "D": "Using Amazon CioudWatch with AWS Lambda to change the typ",
      "E": "size, or IOPS of Amazon EBS volumes in the cluster based on a specific CloudWatch metric",
      "F": "Replacing all existing Amazon EBS volumes with new PIOPS volumes that have the maximum available storage size and I/O per second by taking snapshots before the end of the month and reverting back afterwards. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "In this scenario, the Amazon EC2 instances are in an Auto Scaling group already which means that the database read operations is the possible bottleneck\nespecially during the month-end wherein the reports are generated. This can be solved by creating RDS read replicas.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "13",
    "question": "- (Exam Topic 1) A company is deploying a new cluster for big data analytics on AWS. The cluster will run across many Linux Amazon EC2 instances that are spread across multiple Availability Zones. All of the nodes in the cluster must have read and write access to common underlying file storage. The file storage must be highly available, must be resilient, must be compatible with the Portable Operating System Interface (POSIX), and must accommodate high levels of throughput. Which storage solution will meet these requirements? A. Provision an AWS Storage Gateway file gateway NFS file share that is attached to an Amazon S3 bucke B. Mount the NFS file share on each EC2 instance In the cluster. C. Provision a new Amazon Elastic File System (Amazon EFS) file system that uses General Purpose performance mod D. Mount the EFS file system on each EC2 instance in the cluster. E. Provision a new Amazon Elastic Block Store (Amazon EBS) volume that uses the lo2 volume type.Attach the EBS volume to all of the EC2 instances in the cluster. F. Provision a new Amazon Elastic File System (Amazon EFS) file system that uses Max I/O performance mod G. Mount the EFS file system on each EC2 instance in the cluster. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Provision an AWS Storage Gateway file gateway NFS file share that is attached to an Amazon S3 bucke",
      "B": "Mount the NFS file share on each EC2 instance In the cluster.",
      "C": "Provision a new Amazon Elastic File System (Amazon EFS) file system that uses General Purpose performance mod",
      "D": "Mount the EFS file system on each EC2 instance in the cluster.",
      "E": "Provision a new Amazon Elastic Block Store (Amazon EBS) volume that uses the lo2 volume type.Attach the EBS volume to all of the EC2 instances in the cluster.",
      "F": "Provision a new Amazon Elastic File System (Amazon EFS) file system that uses Max I/O performance mod",
      "G": "Mount the EFS file system on each EC2 instance in the cluster. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "16",
    "question": "- (Exam Topic 1) A large payroll company recently merged with a small staffing company. The unified company now has multiple business units, each with its own existing AWS account. A solutions architect must ensure that the company can centrally manage the billing and access policies for all the AWS accounts. The solutions architect configures AWS Organizations by sending an invitation to all member accounts of the company from a centralized management account. What should the solutions architect do next to meet these requirements? A. Create the OrganizationAccountAccess IAM group in each member accoun B. Include the necessary IAM roles for each administrator. C. Create the OrganizationAccountAccessPolicy IAM policy in each member accoun D. Connect the member accounts to the management account by using cross-account access. E. Create the OrganizationAccountAccessRole IAM role in each member accoun F. Grant permission to the management account to assume the IAM role. G. Create the OrganizationAccountAccessRole IAM role in the management account Attach the Administrator Access AWS managed policy to the IAM rol H. Assign the IAM role to the administrators in each member account. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create the OrganizationAccountAccess IAM group in each member accoun",
      "B": "Include the necessary IAM roles for each administrator.",
      "C": "Create the OrganizationAccountAccessPolicy IAM policy in each member accoun",
      "D": "Connect the member accounts to the management account by using cross-account access.",
      "E": "Create the OrganizationAccountAccessRole IAM role in each member accoun",
      "F": "Grant permission to the management account to assume the IAM role.",
      "G": "Create the OrganizationAccountAccessRole IAM role in the management account Attach the Administrator Access AWS managed policy to the IAM rol",
      "H": "Assign the IAM role to the administrators in each member account. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "18",
    "question": "- (Exam Topic 1) A company runs an e-commerce platform with front-end and e-commerce tiers. Both tiers run on LAMP stacks with the front-end instances running behind a load balancing appliance that has a virtual offering on AWS Current*/, the operations team uses SSH to log in to the instances to maintain patches and address other concerns. The platform has recently been the target of multiple attacks, including. • A DDoS attack. • An SOL injection attack • Several successful dictionary attacks on SSH accounts on the web servers The company wants to improve the security of the e-commerce platform by migrating to AWS. The company's solutions architects have decided to use the following approach; • Code review the existing application and fix any SQL injection issues. • Migrate the web application to AWS and leverage the latest AWS Linux AMI to address initial security patching. • Install AWS Systems Manager to manage patching and allow the system administrators to run commands on all instances, as needed. What additional steps will address all of the identified attack types while providing high availability and minimizing risk? A. Enable SSH access to the Amazon EC2 instances using a security group that limits access to specific IP B. Migrate on-premises MySQL to Amazon RDS Multi-AZ Install the third-party load balancer from the AWS Marketplace and migrate the existing rules to the load balancer's AWS instances Enable AWS Shield Standard for DDoS protection C. Disable SSH access to the Amazon EC2 instance D. Migrate on-premises MySQL to Amazon RDS Multi-AZ Leverage an Elastic Load Balancer to spread the load and enable AWS Shield Advanced for protectio E. Add an Amazon CloudFront distribution in front of the website Enable AWS WAF on the distribution to manage the rules. F. Enable SSH access to the Amazon EC2 instances through a bastion host secured by limiting access to specific IP addresse G. Migrate on-premises MySQL to a self-managed EC2 instanc H. Leverage an AWS Elastic Load Balancer to spread the load, and enable AWS Shield Standard for DDoS protection Add an Amazon CloudFront distribution in front of the website. I. Disable SSH access to the EC2 instance J. Migrate on-premises MySQL to Amazon RDS Single-A K. Leverage an AWS Elastic Load Balancer to spread the load Add an Amazon CloudFront distribution in front of the website Enable AWS WAF on the distribution to manage the rules. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Enable SSH access to the Amazon EC2 instances using a security group that limits access to specific IP",
      "B": "Migrate on-premises MySQL to Amazon RDS Multi-AZ Install the third-party load balancer from the AWS Marketplace and migrate the existing rules to the load balancer's AWS instances Enable AWS Shield Standard for DDoS protection",
      "C": "Disable SSH access to the Amazon EC2 instance",
      "D": "Migrate on-premises MySQL to Amazon RDS Multi-AZ Leverage an Elastic Load Balancer to spread the load and enable AWS Shield Advanced for protectio",
      "E": "Add an Amazon CloudFront distribution in front of the website Enable AWS WAF on the distribution to manage the rules.",
      "F": "Enable SSH access to the Amazon EC2 instances through a bastion host secured by limiting access to specific IP addresse",
      "G": "Migrate on-premises MySQL to a self-managed EC2 instanc",
      "H": "Leverage an AWS Elastic Load Balancer to spread the load, and enable AWS Shield Standard for DDoS protection Add an Amazon CloudFront distribution in front of the website.",
      "I": "Disable SSH access to the EC2 instance",
      "J": "Migrate on-premises MySQL to Amazon RDS Single-A K. Leverage an AWS Elastic Load Balancer to spread the load Add an Amazon CloudFront distribution in front of the website Enable AWS WAF on the distribution to manage the rules. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "20",
    "question": "- (Exam Topic 1) A company is using AWS Organizations lo manage multiple accounts. Due to regulatory requirements, the company wants to restrict specific member accounts to certain AWS Regions, where they are permitted to deploy resources. The resources in the accounts must be tagged, enforced based on a group standard, and centrally managed with minimal configuration. What should a solutions architect do to meet these requirements? A. Create an AWS Config rule in the specific member accounts to limit Regions and apply a tag policy. B. From the AWS Billing and Cost Management console, in the master account, disable Regions for the specific member accounts and apply a tag policy on the root. C. Associate the specific member accounts with the roo D. Apply a tag policy and an SCP using conditions to limit Regions. E. Associate the specific member accounts with a new O F. Apply a tag policy and an SCP using conditions to limit Regions. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an AWS Config rule in the specific member accounts to limit Regions and apply a tag policy.",
      "B": "From the AWS Billing and Cost Management console, in the master account, disable Regions for the specific member accounts and apply a tag policy on the root.",
      "C": "Associate the specific member accounts with the roo",
      "D": "Apply a tag policy and an SCP using conditions to limit Regions.",
      "E": "Associate the specific member accounts with a new O",
      "F": "Apply a tag policy and an SCP using conditions to limit Regions. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "23",
    "question": "- (Exam Topic 1) A web application is hosted in a dedicated VPC that is connected to a company's on-premises data center over a Site-to-Site VPN connection. The application is accessible from the company network only. This is a temporary non-production application that is used during business hours. The workload is generally low with occasional surges. The application has an Amazon Aurora MySQL provisioned database cluster on the backend. The VPC has an internet gateway and a NAT gateways attached. The web servers are in private subnets in an Auto Scaling group behind an Elastic Load Balancer. The web servers also upload data to an Amazon S3 bucket through the internet. A solutions architect needs to reduce operational costs and simplify the architecture. Which strategy should the solutions architect use? A. Review the Auto Scaling group settings and ensure the scheduled actions are specified to operate the Amazon EC2 instances during business hours onl B. Use 3-year scheduled Reserved Instances for the web server EC2 instance C. Detach the internet gateway and remove the NAT gateways from the VP D. Use an Aurora Servertess database and set up a VPC endpoint for the S3 bucket. E. Review the Auto Scaling group settings and ensure the scheduled actions are specified to operate the Amazon EC2 instances during business hours onl F. Detach the internet gateway and remove the NAT gateways from the VP G. Use an Aurora Servertess database and set up a VPC endpoint for the S3 bucket, then update the network routing and security rules and policies related to the changes. H. Review the Auto Scaling group settings and ensure the scheduled actions are specified to operate the Amazon EC2 instances during business hours onl I. Detach the internet gateway from the VPC, and use an Aurora Servertess databas J. Set up a VPC endpoint for the S3 bucket, then update the network routing and security rules and policies related to the changes. K. Use 3-year scheduled Reserved Instances for the web server Amazon EC2 instance L. Remove the NAT gateways from the VPC, and set up a VPC endpoint for the S3 bucke M. Use Amazon N. CloudWatch and AWS Lambda to stop and start the Aurora DB cluster so it operates during business hours onl O. Update the network routing and security rules and policies related to the changes. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Review the Auto Scaling group settings and ensure the scheduled actions are specified to operate the Amazon EC2 instances during business hours onl",
      "B": "Use 3-year scheduled Reserved Instances for the web server EC2 instance",
      "C": "Detach the internet gateway and remove the NAT gateways from the VP",
      "D": "Use an Aurora Servertess database and set up a VPC endpoint for the S3 bucket.",
      "E": "Review the Auto Scaling group settings and ensure the scheduled actions are specified to operate the Amazon EC2 instances during business hours onl",
      "F": "Detach the internet gateway and remove the NAT gateways from the VP",
      "G": "Use an Aurora Servertess database and set up a VPC endpoint for the S3 bucket, then update the network routing and security rules and policies related to the changes.",
      "H": "Review the Auto Scaling group settings and ensure the scheduled actions are specified to operate the Amazon EC2 instances during business hours onl",
      "I": "Detach the internet gateway from the VPC, and use an Aurora Servertess databas",
      "J": "Set up a VPC endpoint for the S3 bucket, then update the network routing and security rules and policies related to the changes. K. Use 3-year scheduled Reserved Instances for the web server Amazon EC2 instance L. Remove the NAT gateways from the VPC, and set up a VPC endpoint for the S3 bucke M. Use Amazon N. CloudWatch and AWS Lambda to stop and start the Aurora DB cluster so it operates during business hours onl O. Update the network routing and security rules and policies related to the changes. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "The application is accessible from the company network only remove NAT and IGW, application - S3 with VPC endpoint. Non-Production application no need to go\nfor Reserved instances\nTo build site-to-site vpn, you don't need internet gateway. Instead, customer gateway is needed.\nhttps://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-create-cgw\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "28",
    "question": "- (Exam Topic 1) An education company is running a web application used by college students around the world. The application runs in an Amazon Elastic Container Service {Amazon ECS) cluster in an Auto Scaling group behind an Application Load Balancer (ALB). A system administrator detects a weekly spike in the number of failed login attempts, which overwhelm the application's authentication service. All the failed login attempts originate from about 500 different IP addresses that change each week, A solutions architect must prevent the failed login attempts from overwhelming the authentication service. Which solution meets these requirements with the MOST operational efficiency? A. Use AWS Firewall Manager to create a security group and security group policy to deny access from the IP addresses. B. Create an AWS WAF web ACL with a rate-based rule, and set the rule action to Bloc C. Connect theweb ACL to the ALB. D. Use AWS Firewall Manager to create a security group and security group policy to allow access only to specific CIOR ranges. E. Create an AWS WAF web ACL with an IP set match rule, and set the rule action to Bloc F. Connect the web ACL to the ALB. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS Firewall Manager to create a security group and security group policy to deny access from the IP addresses.",
      "B": "Create an AWS WAF web ACL with a rate-based rule, and set the rule action to Bloc",
      "C": "Connect theweb ACL to the ALB.",
      "D": "Use AWS Firewall Manager to create a security group and security group policy to allow access only to specific CIOR ranges.",
      "E": "Create an AWS WAF web ACL with an IP set match rule, and set the rule action to Bloc",
      "F": "Connect the web ACL to the ALB. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html\nThe IP set match statement inspects the IP address of a web request against a set of IP addresses and address ranges. Use this to allow or block web requests\nbased on the IP addresses that the requests originate from. By default, AWS WAF uses the IP address from the web request origin, but you can configure the rule\nto use an HTTP header like X-Forwarded-For instead.\nhttps://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-ipset-match.html\nhttps://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "29",
    "question": "- (Exam Topic 1) A company has a photo sharing social networking application. To provide a consistent experience for users, the company performs some image processing on the photos uploaded by users before publishing on the application. The image processing is implemented using a set of Python libraries. The current architecture is as follows: • The image processing Python code runs in a single Amazon EC2 instance and stores the processed images in an Amazon S3 bucket named ImageBucket. • The front-end application, hosted in another bucket, loads the images from ImageBucket to display to users. With plans for global expansion, the company wants to implement changes in its existing architecture to be able to scale for increased demand on the application and reduce management complexity as the application scales. Which combination of changes should a solutions architect make? (Select TWO.) A. Place the image processing EC2 instance into an Auto Scaling group. B. Use AWS Lambda to run the image processing tasks. C. Use Amazon Rekognition for image processing. D. Use Amazon CloudFront in front of ImageBucket. E. Deploy the applications in an Amazon ECS cluster and apply Service Auto Scaling. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Place the image processing EC2 instance into an Auto Scaling group.",
      "B": "Use AWS Lambda to run the image processing tasks.",
      "C": "Use Amazon Rekognition for image processing.",
      "D": "Use Amazon CloudFront in front of ImageBucket.",
      "E": "Deploy the applications in an Amazon ECS cluster and apply Service Auto Scaling. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "D"
    ],
    "select_n": 2,
    "explanation": "https://prismatic.io/blog/why-we-moved-from-lambda-to-ecs/\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "34",
    "question": "- (Exam Topic 1) A company is developing and hosting several projects in the AWS Cloud. The projects are developed across multiple AWS accounts under the same organization in AWS Organizations. The company requires the cost lor cloud infrastructure to be allocated to the owning project. The team responsible for all of the AWS accounts has discovered that several Amazon EC2 instances are lacking the Project tag used for cost allocation. Which actions should a solutions architect take to resolve the problem and prevent it from happening in the future? (Select THREE.) A. Create an AWS Config rule in each account to find resources with missing tags. B. Create an SCP in the organization with a deny action for ec2:Runlnstances if the Project tag is missing. C. Use Amazon Inspector in the organization to find resources with missing tags. D. Create an IAM policy in each account with a deny action for ec2:RunInstances if the Project tag is missing. E. Create an AWS Config aggregator for the organization to collect a list of EC2 instances with the missing Project tag. F. Use AWS Security Hub to aggregate a list of EC2 instances with the missing Project tag. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an AWS Config rule in each account to find resources with missing tags.",
      "B": "Create an SCP in the organization with a deny action for ec2:Runlnstances if the Project tag is missing.",
      "C": "Use Amazon Inspector in the organization to find resources with missing tags.",
      "D": "Create an IAM policy in each account with a deny action for ec2:RunInstances if the Project tag is missing.",
      "E": "Create an AWS Config aggregator for the organization to collect a list of EC2 instances with the missing Project tag.",
      "F": "Use AWS Security Hub to aggregate a list of EC2 instances with the missing Project tag. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "D",
      "E"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "39",
    "question": "- (Exam Topic 1) A media company uses Amazon DynamoDB to store metadata for its catalog of movies that are available to stream. Each media item Contains user-facing content that concludes a description of the media, a list of search tags, and similar data. In addition, media items include a list of Amazon S3 key names that relate to movie files. The company stores these movie files in a single S3 bucket that has versioning enable. The company uses Amazon CloudFront to serve these movie files. The company has 100.000 media items, and each media item can have many different S3 objects that represent different encodings of the same media S3 objects that belong to the same media item are grouped together under the same key prefix, which is a random unique ID Because of an expiring contract with a media provider, the company must remove 2.000 media Items. The company must completely delete all DynamoDB keys and movie files on Amazon S3 that are related to these media items within 36 hours The company must ensure that the content cannot be recovered. Which combination of actions will meet these requirements? (Select TWO.) A. Configure the dynamoDB table with a TTL fiel B. Create and invoke an AWS Lambda function to perform a conditional update Set the TTL field to the time of the contract's expiration on every affected media item. C. Configure an S3 Lifecycle object expiration rule that is based on the contract's expiration date D. Write a script to perform a conditional delete on all the affected DynamoDB records E. Temporarily suspend versioning on the S3 bucke F. Create and invoke an AWS Lambda function that deletes affected objects Reactivate versioning when the operation is complete G. Write a script to delete objects from Amazon S3 Specify in each request a NoncurrentVersionExpiration property with a NoncurrentDays attribute set to 0. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure the dynamoDB table with a TTL fiel",
      "B": "Create and invoke an AWS Lambda function to perform a conditional update Set the TTL field to the time of the contract's expiration on every affected media item.",
      "C": "Configure an S3 Lifecycle object expiration rule that is based on the contract's expiration date",
      "D": "Write a script to perform a conditional delete on all the affected DynamoDB records",
      "E": "Temporarily suspend versioning on the S3 bucke",
      "F": "Create and invoke an AWS Lambda function that deletes affected objects Reactivate versioning when the operation is complete",
      "G": "Write a script to delete objects from Amazon S3 Specify in each request a NoncurrentVersionExpiration property with a NoncurrentDays attribute set to 0. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C",
      "E"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "43",
    "question": "- (Exam Topic 1) A company built an ecommerce website on AWS using a three-tier web architecture. The application is Java-based and composed of an Amazon CloudFront distribution, an Apache web server layer of Amazon EC2 instances in an Auto Scaling group, and a backend Amazon Aurora MySQL database. Last month, during a promotional sales event, users reported errors and timeouts while adding items to their shopping carts. The operations team recovered the logs created by the web servers and reviewed Aurora DB cluster performance metrics. Some of the web servers were terminated before logs could be collected and the Aurora metrics were not sufficient for query performance analysis. Which combination of steps must the solutions architect take to improve application performance visibility during peak traffic events? (Select THREE.) A. Configure the Aurora MySQL DB cluster to publish slow query and error logs to Amazon CloudWatch Logs. B. Implement the AWS X-Ray SDK to trace incoming HTTP requests on the EC2 instances and implement tracing of SQL queries with the X-Ray SDK for Java. C. Configure the Aurora MySQL DB cluster to stream slow query and error logs to Amazon Kinesis. D. Install and configure an Amazon CloudWatch Logs agent on the EC2 instances to send the Apache logsto CloudWatch Logs. E. Enable and configure AWS CloudTrail to collect and analyze application activity from Amazon EC2 and Aurora. F. Enable Aurora MySQL DB cluster performance benchmarking and publish the stream to AWS X-Ray. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure the Aurora MySQL DB cluster to publish slow query and error logs to Amazon CloudWatch Logs.",
      "B": "Implement the AWS X-Ray SDK to trace incoming HTTP requests on the EC2 instances and implement tracing of SQL queries with the X-Ray SDK for Java.",
      "C": "Configure the Aurora MySQL DB cluster to stream slow query and error logs to Amazon Kinesis.",
      "D": "Install and configure an Amazon CloudWatch Logs agent on the EC2 instances to send the Apache logsto CloudWatch Logs.",
      "E": "Enable and configure AWS CloudTrail to collect and analyze application activity from Amazon EC2 and Aurora.",
      "F": "Enable Aurora MySQL DB cluster performance benchmarking and publish the stream to AWS X-Ray. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "B",
      "D"
    ],
    "select_n": 3,
    "explanation": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.Concepts.MySQL.html# https://aws.amazon.com/blogs/mt/simplifying-\napache-server-logs-with-amazon-cloudwatch-logs-insights/ https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-dotnet-messagehandler.html\nhttps://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-sqlclients.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "48",
    "question": "- (Exam Topic 1) A large company in Europe plans to migrate its applications to the AWS Cloud. The company uses multiple AWS accounts for various business groups. A data privacy law requires the company to restrict developers' access to AWS European Regions only. What should the solutions architect do to meet this requirement with the LEAST amount of management overhead^ A. Create IAM users and IAM groups in each accoun B. Create IAM policies to limit access to non-European Regions Attach the IAM policies to the IAM groups C. Enable AWS Organizations, attach the AWS accounts, and create OUs for European Regions andnon-European Region D. Create SCPs to limit access to non-European Regions and attach the policies to the OUs. E. Set up AWS Single Sign-On and attach AWS account F. Create permission sets with policies to restrict access to non-European Regions Create IAM users and IAM groups in each account. G. Enable AWS Organizations, attach the AWS accounts, and create OUs for European Regions andnon-European Region H. Create permission sets with policies to restrict access to non-European Region I. Create IAM users and IAM groups in the primary account. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create IAM users and IAM groups in each accoun",
      "B": "Create IAM policies to limit access to non-European Regions Attach the IAM policies to the IAM groups",
      "C": "Enable AWS Organizations, attach the AWS accounts, and create OUs for European Regions andnon-European Region",
      "D": "Create SCPs to limit access to non-European Regions and attach the policies to the OUs.",
      "E": "Set up AWS Single Sign-On and attach AWS account",
      "F": "Create permission sets with policies to restrict access to non-European Regions Create IAM users and IAM groups in each account.",
      "G": "Enable AWS Organizations, attach the AWS accounts, and create OUs for European Regions andnon-European Region",
      "H": "Create permission sets with policies to restrict access to non-European Region",
      "I": "Create IAM users and IAM groups in the primary account. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "\"This policy uses the Deny effect to deny access to all requests for operations that don't target one of the two approved regions (eu-central-1 and eu-west-1).\"\nhttps://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.htm\nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "53",
    "question": "- (Exam Topic 1) A company stores sales transaction data in Amazon DynamoDB tables. To detect anomalous behaviors and respond quickly, all changes lo the items stored in the DynamoDB tables must be logged within 30 minutes. Which solution meets the requirements? A. Copy the DynamoDB tables into Apache Hive tables on Amazon EMR every hour and analyze them (or anomalous behavior B. Send Amazon SNS notifications when anomalous behaviors are detected. C. Use AWS CloudTrail to capture all the APIs that change the DynamoDB table D. Send SNS notifications when anomalous behaviors are detected using CloudTrail event filtering. E. Use Amazon DynamoDB Streams to capture and send updates to AWS Lambd F. Create a Lambda function to output records lo Amazon Kinesis Data Stream G. Analyze any anomalies with Amazon Kinesis Data Analytic H. Send SNS notifications when anomalous behaviors are detected. I. Use event patterns in Amazon CloudWatch Events to capture DynamoDB API call events with an AWS Lambda (unction as a target to analyze behavio J. Send SNS notifications when anomalous behaviors are detected. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Copy the DynamoDB tables into Apache Hive tables on Amazon EMR every hour and analyze them (or anomalous behavior",
      "B": "Send Amazon SNS notifications when anomalous behaviors are detected.",
      "C": "Use AWS CloudTrail to capture all the APIs that change the DynamoDB table",
      "D": "Send SNS notifications when anomalous behaviors are detected using CloudTrail event filtering.",
      "E": "Use Amazon DynamoDB Streams to capture and send updates to AWS Lambd",
      "F": "Create a Lambda function to output records lo Amazon Kinesis Data Stream",
      "G": "Analyze any anomalies with Amazon Kinesis Data Analytic",
      "H": "Send SNS notifications when anomalous behaviors are detected.",
      "I": "Use event patterns in Amazon CloudWatch Events to capture DynamoDB API call events with an AWS Lambda (unction as a target to analyze behavio",
      "J": "Send SNS notifications when anomalous behaviors are detected. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "https://aws.amazon.com/blogs/database/dynamodb-streams-use-cases-and-design-patterns/#:~:text=DynamoDB DynamoDb Stream to capture DynamoDB\nupdate. And Kinesis Data Analytics for anomaly detection (it uses AWS proprietary Random Cut Forest Algorithm)\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "58",
    "question": "- (Exam Topic 1) A solutions architect works for a government agency that has strict disaster recovery requirements All Amazon Elastic Block Store (Amazon EBS) snapshots are required to be saved in at least two additional AWS Regions. The agency also is required to maintain the lowest possible operational overhead. Which solution meets these requirements? A. Configure a policy in Amazon Data Lifecycle Manager (Amazon DLMJ to run once daily to copy the EBS snapshots to the additional Regions. B. Use Amazon EventBridge (Amazon CloudWatch Events) to schedule an AWS Lambda function to copy the EBS snapshots to the additional Regions. C. Set up AWS Backup to create the EBS snapshot D. Configure Amazon S3 cross-Region replication to copy the EBS snapshots to the additional Regions. E. Schedule Amazon EC2 Image Builder to run once daily to create an AMI and copy the AMI to the additional Regions. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure a policy in Amazon Data Lifecycle Manager (Amazon DLMJ to run once daily to copy the EBS snapshots to the additional Regions.",
      "B": "Use Amazon EventBridge (Amazon CloudWatch Events) to schedule an AWS Lambda function to copy the EBS snapshots to the additional Regions.",
      "C": "Set up AWS Backup to create the EBS snapshot",
      "D": "Configure Amazon S3 cross-Region replication to copy the EBS snapshots to the additional Regions.",
      "E": "Schedule Amazon EC2 Image Builder to run once daily to create an AMI and copy the AMI to the additional Regions. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "62",
    "question": "- (Exam Topic 1) A company with global offices has a single 1 Gbps AWS Direct Connect connection to a single AWS Region. The company's on-premises network uses the connection to communicate with the company's resources in the AWS Cloud. The connection has a single private virtual interface that connects to a single VPC. A solutions architect must implement a solution that adds a redundant Direct Connect connection in the same Region. The solution also must provide connectivity to other Regions through the same pair of Direct Connect connections as the company expands into other Regions. Which solution meets these requirements? A. Provision a Direct Connect gatewa B. Delete the existing private virtual interface from the existing connectio C. Create the second Direct Connect connectio D. Create a new private virtual interlace on each connection, and connect both private victual interfaces to the Direct Connect gatewa E. Connect the Direct Connect gateway to the single VPC. F. Keep the existing private virtual interfac G. Create the second Direct Connect connectio H. Create a new private virtual interface on the new connection, and connect the new private virtual interface to the single VPC. I. Keep the existing private virtual interfac J. Create the second Direct Connect connectio K. Create a new public virtual interface on the new connection, and connect the new public virtual interface to the single VPC. L. Provision a transit gatewa M. Delete the existing private virtual interface from the existing connection.Create the second Direct Connect connectio N. Create a new private virtual interface on each connection, and connect both private virtual interfaces to the transit gatewa O. Associate the transit gateway with the single VPC. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Provision a Direct Connect gatewa",
      "B": "Delete the existing private virtual interface from the existing connectio",
      "C": "Create the second Direct Connect connectio",
      "D": "Create a new private virtual interlace on each connection, and connect both private victual interfaces to the Direct Connect gatewa",
      "E": "Connect the Direct Connect gateway to the single VPC.",
      "F": "Keep the existing private virtual interfac",
      "G": "Create the second Direct Connect connectio",
      "H": "Create a new private virtual interface on the new connection, and connect the new private virtual interface to the single VPC.",
      "I": "Keep the existing private virtual interfac",
      "J": "Create the second Direct Connect connectio K. Create a new public virtual interface on the new connection, and connect the new public virtual interface to the single VPC. L. Provision a transit gatewa M. Delete the existing private virtual interface from the existing connection.Create the second Direct Connect connectio N. Create a new private virtual interface on each connection, and connect both private virtual interfaces to the transit gatewa O. Associate the transit gateway with the single VPC. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": "A Direct Connect gateway is a globally available resource. You can create the Direct Connect gateway in any Region and access it from all other Regions. The\nfollowing describe scenarios where you can use a Direct Connect gateway.\nhttps://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "67",
    "question": "- (Exam Topic 1) A company has a project that is launching Amazon EC2 instances that are larger than required. The project's account cannot be part of the company's organization in AWS Organizations due to policy restrictions to keep this activity outside of corporate IT. The company wants to allow only the launch of t3.small EC2 instances by developers in the project's account. These EC2 instances must be restricted to the us-east-2 Region. What should a solutions architect do to meet these requirements? A. Create a new developer accoun B. Move all EC2 instances, users, and assets into us-east-2. Add the account to the company's organization in AWS Organization C. Enforce a tagging policy that denotes Region affinity. D. Create an SCP that denies the launch of all EC2 instances except I3.small EC2 instances in us-east-2.Attach the SCP to the project's account. E. Create and purchase a t3.small EC2 Reserved Instance for each developer in us-east-2. Assign each developer a specific EC2 instance with their name as the tag. F. Create an IAM policy than allows the launch of only t3.small EC2 instances in us-east-2. Attach the policy to the roles and groups that the developers use in the project's account. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a new developer accoun",
      "B": "Move all EC2 instances, users, and assets into us-east-2. Add the account to the company's organization in AWS Organization",
      "C": "Enforce a tagging policy that denotes Region affinity.",
      "D": "Create an SCP that denies the launch of all EC2 instances except I3.small EC2 instances in us-east-2.Attach the SCP to the project's account.",
      "E": "Create and purchase a t3.small EC2 Reserved Instance for each developer in us-east-2. Assign each developer a specific EC2 instance with their name as the tag.",
      "F": "Create an IAM policy than allows the launch of only t3.small EC2 instances in us-east-2. Attach the policy to the roles and groups that the developers use in the project's account. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "71",
    "question": "- (Exam Topic 1) A solution architect needs to deploy an application on a fleet of Amazon EC2 instances. The EC2 instances run in private subnets in An Auto Scaling group. The application is expected to generate logs at a rate of 100 MB each second on each of the EC2 instances. The logs must be stored in an Amazon S3 bucket so that an Amazon EMR cluster can consume them for further processing The logs must be quickly accessible for the first 90 days and should be retrievable within 48 hours thereafter. What is the MOST cost-effective solution that meets these requirements? A. Set up an S3 copy job to write logs from each EC2 instance to the S3 bucket with S3 Standard storage Use a NAT instance within the private subnets to connect to Amazon S3. Create S3 Lifecycle policies to move logs that are older than 90 days to S3 Glacier. B. Set up an S3 sync job to copy logs from each EC2 instance to the S3 bucket with S3 Standard storage Use a gateway VPC endpoint for Amazon S3 to connect to Amazon S3. Create S3 Lifecycle policies to move logs that are older than 90 days to S3 Glacier Deep Archive C. Set up an S3 batch operation to copy logs from each EC2 instance to the S3 bucket with S3 Standardstorage Use a NAT gateway with the private subnets to connect to Amazon S3 Create S3 Lifecycle policies to move logs that are older than 90 days to S3 Glacier Deep Archive D. Set up an S3 sync job to copy logs from each EC2 instance to the S3 bucket with S3 Standard storage Use a gateway VPC endpoint for Amazon S3 to connect to Amazon S3. Create S3 Lifecycle policies to move logs that are older than 90 days to S3 Glacier -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Set up an S3 copy job to write logs from each EC2 instance to the S3 bucket with S3 Standard storage Use a NAT instance within the private subnets to connect to Amazon S3. Create S3 Lifecycle policies to move logs that are older than 90 days to S3 Glacier.",
      "B": "Set up an S3 sync job to copy logs from each EC2 instance to the S3 bucket with S3 Standard storage Use a gateway VPC endpoint for Amazon S3 to connect to Amazon S3. Create S3 Lifecycle policies to move logs that are older than 90 days to S3 Glacier Deep Archive",
      "C": "Set up an S3 batch operation to copy logs from each EC2 instance to the S3 bucket with S3 Standardstorage Use a NAT gateway with the private subnets to connect to Amazon S3 Create S3 Lifecycle policies to move logs that are older than 90 days to S3 Glacier Deep Archive",
      "D": "Set up an S3 sync job to copy logs from each EC2 instance to the S3 bucket with S3 Standard storage Use a gateway VPC endpoint for Amazon S3 to connect to Amazon S3. Create S3 Lifecycle policies to move logs that are older than 90 days to S3 Glacier -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "73",
    "question": "- (Exam Topic 1) A company needs to run a software package that has a license that must be run on the same physical host for the duration of Its use. The software package is only going to be used for 90 days The company requires patching and restarting of all instances every 30 days How can these requirements be met using AWS? A. Run a dedicated instance with auto-placement disabled. B. Run the instance on a dedicated host with Host Affinity set to Host. C. Run an On-Demand Instance with a Reserved Instance to ensure consistent placement. D. Run the instance on a licensed host with termination set for 90 days. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Run a dedicated instance with auto-placement disabled.",
      "B": "Run the instance on a dedicated host with Host Affinity set to Host.",
      "C": "Run an On-Demand Instance with a Reserved Instance to ensure consistent placement.",
      "D": "Run the instance on a licensed host with termination set for 90 days. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "Host Affinity is configured at the instance level. It establishes a launch relationship between an instance and a Dedicated Host. (This set which host the instance\ncan run on) Auto-placement allows you to manage whether instances that you launch are launched onto a specific host, or onto any available host that has\nmatching configurations. Auto-placement must be configured at the host level. (This sets which instance the host can run.) When affinity is set to Host, an instance\nlaunched onto a specific host always restarts on the same host if stopped. This applies to both targeted and untargeted launches.\nhttps://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html\nWhen affinity is set to Off, and you stop and restart the instance, it can be restarted on any available host. However, it tries to launch back onto the last Dedicated\nHost on which it ran (on a best-effort basis).\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "76",
    "question": "- (Exam Topic 1) A company's AWS architecture currently uses access keys and secret access keys stored on each instance to access AWS services. Database credentials are hard-coded on each instance. SSH keys for command-tine remote access are stored in a secured Amazon S3 bucket. The company has asked its solutions architect to improve the security posture of the architecture without adding operational complexity. Which combination of steps should the solutions architect take to accomplish this? (Select THREE.) A. Use Amazon EC2 instance profiles with an IAM role. B. Use AWS Secrets Manager to store access keys and secret access keys. C. Use AWS Systems Manager Parameter Store to store database credentials. D. Use a secure fleet of Amazon EC2 bastion hosts (or remote access. E. Use AWS KMS to store database credentials. F. Use AWS Systems Manager Session Manager tor remote access -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use Amazon EC2 instance profiles with an IAM role.",
      "B": "Use AWS Secrets Manager to store access keys and secret access keys.",
      "C": "Use AWS Systems Manager Parameter Store to store database credentials.",
      "D": "Use a secure fleet of Amazon EC2 bastion hosts (or remote access.",
      "E": "Use AWS KMS to store database credentials.",
      "F": "Use AWS Systems Manager Session Manager tor remote access -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C",
      "F"
    ],
    "select_n": 3,
    "explanation": "https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "79",
    "question": "- (Exam Topic 1) A company runs a popular public-facing ecommerce website. Its user base is growing quickly from a local market to a national market. The website is hosted in an on-premises data center with web servers and a MySQL database. The company wants to migrate its workload (o AWS. A solutions architect needs to create a solution to: • Improve security • Improve reliability Improve availability • Reduce latency • Reduce maintenance Which combination of steps should the solutions architect take to meet these requirements? (Select THREE.) A. Use Amazon EC2 instances in two Availability Zones for the web servers in an Auto Scaling group behind an Application Load Balancer. B. Migrate the database to a Multi-AZ Amazon Aurora MySQL DB cluster. C. Use Amazon EC2 instances in two Availability Zones to host a highly available MySQL database cluster. D. Host static website content in Amazon S3. Use S3 Transfer Acceleration to reduce latency while serving webpage E. Use AWS WAF to improve website security. F. Host static website content in Amazon S3. Use Amazon CloudFronl to reduce latency while serving webpage G. Use AWS WAF to improve website security H. Migrate the database to a single-AZ Amazon RDS for MySQL DB instance. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use Amazon EC2 instances in two Availability Zones for the web servers in an Auto Scaling group behind an Application Load Balancer.",
      "B": "Migrate the database to a Multi-AZ Amazon Aurora MySQL DB cluster.",
      "C": "Use Amazon EC2 instances in two Availability Zones to host a highly available MySQL database cluster.",
      "D": "Host static website content in Amazon S3. Use S3 Transfer Acceleration to reduce latency while serving webpage",
      "E": "Use AWS WAF to improve website security.",
      "F": "Host static website content in Amazon S3. Use Amazon CloudFronl to reduce latency while serving webpage",
      "G": "Use AWS WAF to improve website security",
      "H": "Migrate the database to a single-AZ Amazon RDS for MySQL DB instance. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "B",
      "E"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "82",
    "question": "- (Exam Topic 1) A company wants to control its cost of Amazon Athena usage The company has allocated a specific monthly budget for Athena usage A solutions architect must design a solution that will prevent the company from exceeding the budgeted amount Which solution will moot these requirements? A. Use AWS Budget B. Create an alarm (or when the cost of Athena usage reaches the budgeted amount for the mont C. Configure AWS Budgets actions to deactivate Athena until the end of the month. D. Use Cost Explorer to create an alert for when the cost of Athena usage reaches the budgeted amount for the mont E. Configure Cost Explorer to publish notifications to an Amazon Simple Notification Service (Amazon SNS) topic. F. Use AWS Trusted Advisor to track the cost of Athena usag G. Configure an Amazon EventBridge (Amazon CloudWatch Events) rule to deactivate Athena until the end of the month whenever the cost reaches the budgeted amount for the month H. Use Athena workgroups to set a limit on the amount of data that can be scanne I. Set a limit that is appropriate for the monthly budget and the current pricing for Athena. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS Budget",
      "B": "Create an alarm (or when the cost of Athena usage reaches the budgeted amount for the mont",
      "C": "Configure AWS Budgets actions to deactivate Athena until the end of the month.",
      "D": "Use Cost Explorer to create an alert for when the cost of Athena usage reaches the budgeted amount for the mont",
      "E": "Configure Cost Explorer to publish notifications to an Amazon Simple Notification Service (Amazon SNS) topic.",
      "F": "Use AWS Trusted Advisor to track the cost of Athena usag",
      "G": "Configure an Amazon EventBridge (Amazon CloudWatch Events) rule to deactivate Athena until the end of the month whenever the cost reaches the budgeted amount for the month",
      "H": "Use Athena workgroups to set a limit on the amount of data that can be scanne",
      "I": "Set a limit that is appropriate for the monthly budget and the current pricing for Athena. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "85",
    "question": "- (Exam Topic 1) A company is migrating applications from on premises to the AWS Cloud. These applications power the company's internal web forms. These web forms collect data for specific events several times each quarter. The web forms use simple SQL statements to save the data to a local relational database. Data collection occurs for each event, and the on-premises servers are idle most of the time. The company needs to minimize the amount of idle infrastructure that supports the web forms. Which solution will meet these requirements? A. Use Amazon EC2 Image Builder to create AMIs for the legacy server B. Use the AMIs to provision EC2 instances to recreate the applications in the AWS.Clou C. Place an Application Load Balancer (ALB) in front of the EC2 instance D. Use Amazon Route 53 to point the DNS names of the web forms to the ALB. E. Create one Amazon DynamoDB table to store data for all the data input Use the application form name as the table key to distinguish data item F. Create an Amazon Kinesis data stream to receive the data input and store the input in DynamoD G. Use Amazon Route 53 to point the DNS names of the web forms to the Kinesis data stream's endpoint. H. Create Docker images for each server of the legacy web form application I. Create an Amazon Elastic Container Service (Amazon ECS) cluster on AWS Fargat J. Place an Application Load Balancer in front of the ECS cluste K. Use Fargate task storage to store the web form data. L. Provision an Amazon Aurora Serverless cluste M. Build multiple schemas for each web form's data storag N. Use Amazon API Gateway and an AWS Lambda function to recreate the data input form O. Use Amazon Route 53 to point the DNS names of the web forms to their corresponding API Gateway endpoint. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use Amazon EC2 Image Builder to create AMIs for the legacy server",
      "B": "Use the AMIs to provision EC2 instances to recreate the applications in the AWS.Clou",
      "C": "Place an Application Load Balancer (ALB) in front of the EC2 instance",
      "D": "Use Amazon Route 53 to point the DNS names of the web forms to the ALB.",
      "E": "Create one Amazon DynamoDB table to store data for all the data input Use the application form name as the table key to distinguish data item",
      "F": "Create an Amazon Kinesis data stream to receive the data input and store the input in DynamoD",
      "G": "Use Amazon Route 53 to point the DNS names of the web forms to the Kinesis data stream's endpoint.",
      "H": "Create Docker images for each server of the legacy web form application",
      "I": "Create an Amazon Elastic Container Service (Amazon ECS) cluster on AWS Fargat",
      "J": "Place an Application Load Balancer in front of the ECS cluste K. Use Fargate task storage to store the web form data. L. Provision an Amazon Aurora Serverless cluste M. Build multiple schemas for each web form's data storag N. Use Amazon API Gateway and an AWS Lambda function to recreate the data input form O. Use Amazon Route 53 to point the DNS names of the web forms to their corresponding API Gateway endpoint. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "Provision an Amazon Aurora Serverless cluster. Build multiple schemas for each web forms data storage. Use Amazon API Gateway and an AWS Lambda\nfunction to recreate the data input forms. Use Amazon Route 53 to point the DNS names of the web forms to their corresponding API Gateway endpoint.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "90",
    "question": "- (Exam Topic 1) A finance company hosts a data lake in Amazon S3. The company receives financial data records over SFTP each night from several third parties. The company runs its own SFTP server on an Amazon EC2 instance in a public subnet of a VPC. After the files ate uploaded, they are moved to the data lake by a cron job that runs on the same instance. The SFTP server is reachable on DNS sftp.examWe.com through the use of Amazon Route 53. What should a solutions architect do to improve the reliability and scalability of the SFTP solution? A. Move the EC2 instance into an Auto Scaling grou B. Place the EC2 instance behind an Application Load Balancer (ALB). Update the DNS record sftp.example.com in Route 53 to point to the ALB. C. Migrate the SFTP server to AWS Transfer for SFT D. Update the DNS record sftp.example.com in Route 53 to point to the server endpoint hostname. E. Migrate the SFTP server to a file gateway in AWS Storage Gatewa F. Update the DNS record sflp.example.com in Route 53 to point to the file gateway endpoint. G. Place the EC2 instance behind a Network Load Balancer (NLB). Update the DNS record sftp.example.com in Route 53 to point to the NLB. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Move the EC2 instance into an Auto Scaling grou",
      "B": "Place the EC2 instance behind an Application Load Balancer (ALB). Update the DNS record sftp.example.com in Route 53 to point to the ALB.",
      "C": "Migrate the SFTP server to AWS Transfer for SFT",
      "D": "Update the DNS record sftp.example.com in Route 53 to point to the server endpoint hostname.",
      "E": "Migrate the SFTP server to a file gateway in AWS Storage Gatewa",
      "F": "Update the DNS record sflp.example.com in Route 53 to point to the file gateway endpoint.",
      "G": "Place the EC2 instance behind a Network Load Balancer (NLB). Update the DNS record sftp.example.com in Route 53 to point to the NLB. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "94",
    "question": "- (Exam Topic 1) A solutions architect at a largo company needs to set up network security for outbound traffic to the internet from all AWS accounts within an organization m AWS Organizations The organization has more than 100 AWS accounts, and the accounts route to each other by using a centralized AWS Transit Gateway. Each account has both an internet gateway and a NAT gateway for outbound traffic to the interne) The company deploys resources only Into a single AWS Region The company needs the ability to add centrally managed rule-based filtering on all outbound traffic to the internet for all AWS accounts in the organization The peak load of outbound traffic will not exceed 25 Gbps in each Availability Zone Which solution meets these requirements? A. Creates a new VPC for outbound traffic to the internet Connect the existing transit gateway to the new VPC Configure a new NAT gateway Create an Auto Scaling group of Amazon EC2 Instances that run an open-source internet proxy for rule-based filtering across all Availability Zones in the Region Modify all default routes to point to the proxy's Auto Scaling group B. Create a new VPC for outbound traffic to the internet Connect the existing transit gateway to the new VPC Configure a new NAT gateway Use an AWS Network Firewall firewall for rule-based filtering Create Network Firewall endpoints In each Availability Zone Modify all default routes to point to the Network Firewall endpoints C. Create an AWS Network Firewall firewal for rule-based filtering in each AWS account Modify all default routes to point to the Network Firewall firewalls in each account. D. In each AWS account, create an Auto Scaling group of network-optimized Amazon EC2 instances that run an open-source internet proxy for rule-based filtering Modify all default routes to point to the proxy's Auto Scaling group. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Creates a new VPC for outbound traffic to the internet Connect the existing transit gateway to the new VPC Configure a new NAT gateway Create an Auto Scaling group of Amazon EC2 Instances that run an open-source internet proxy for rule-based filtering across all Availability Zones in the Region Modify all default routes to point to the proxy's Auto Scaling group",
      "B": "Create a new VPC for outbound traffic to the internet Connect the existing transit gateway to the new VPC Configure a new NAT gateway Use an AWS Network Firewall firewall for rule-based filtering Create Network Firewall endpoints In each Availability Zone Modify all default routes to point to the Network Firewall endpoints",
      "C": "Create an AWS Network Firewall firewal for rule-based filtering in each AWS account Modify all default routes to point to the Network Firewall firewalls in each account.",
      "D": "In each AWS account, create an Auto Scaling group of network-optimized Amazon EC2 instances that run an open-source internet proxy for rule-based filtering Modify all default routes to point to the proxy's Auto Scaling group. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/\nhttps://aws.amazon.com/blogs/networking-and-content-delivery/deploy-centralized-traffic-filtering-using-aws-n\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "99",
    "question": "- (Exam Topic 1) A company is hosting a single-page web application in the AWS Cloud. The company is using Amazon CloudFront to reach its goal audience. The CloudFront distribution has an Amazon S3 bucket that is configured as its origin. The static files for the web application are stored in this S3 bucket. The company has used a simple routing policy to configure an Amazon Route 53 A record The record points to the CloudFront distribution The company wants to use a canary deployment release strategy for new versions of the application. What should a solutions architect recommend to meet these requirements? A. Create a second CloudFront distribution for the new version of the applicatio B. Update the Route 53 record to use a weighted routing policy. C. Create a Lambda@Edge functio D. Configure the function to implement a weighting algorithm and rewrite the URL to direct users to a new version of the application. E. Create a second S3 bucket and a second CloudFront origin for the new S3 bucket Create a CloudFrontorigin group that contains both origins Configure origin weighting for the origin group. F. Create two Lambda@Edge function G. Use each function to serve one of the application versions Set up a CloudFront weighted Lambda@Edge invocation policy -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a second CloudFront distribution for the new version of the applicatio",
      "B": "Update the Route 53 record to use a weighted routing policy.",
      "C": "Create a Lambda@Edge functio",
      "D": "Configure the function to implement a weighting algorithm and rewrite the URL to direct users to a new version of the application.",
      "E": "Create a second S3 bucket and a second CloudFront origin for the new S3 bucket Create a CloudFrontorigin group that contains both origins Configure origin weighting for the origin group.",
      "F": "Create two Lambda@Edge function",
      "G": "Use each function to serve one of the application versions Set up a CloudFront weighted Lambda@Edge invocation policy -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "53.2",
    "question": "- (Exam Topic 2) A company hosts a blog post application on AWS using Amazon API Gateway. Amazon DynamoDB, and AWS Lambda The application currently does not use API keys to authorize requests The API model is as follows: GET /posts/Jpostld) to get post details GET /users/{userld}. to get user details GET /comments/{commentld}: to get comments details The company has noticed users are actively discussing topics in the comments section, and the company wants to increase user engagement by making the comments appear in real time Which design should be used to reduce comment latency and improve user experience? A. Use edge-optimized API with Amazon CloudFront to cache API responses. B. Modify the blog application code to request GET/commentsV{commentld} every 10 seconds C. Use AWS AppSync and leverage WebSockets to deliver comments D. Change the concurrency limit of the Lambda functions to lower the API response time. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use edge-optimized API with Amazon CloudFront to cache API responses.",
      "B": "Modify the blog application code to request GET/commentsV{commentld} every 10 seconds",
      "C": "Use AWS AppSync and leverage WebSockets to deliver comments",
      "D": "Change the concurrency limit of the Lambda functions to lower the API response time. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "49",
    "question": "- (Exam Topic 2) A life sciences company is using a combination of open source tools to manage data analysis workflows and Docker containers running on servers in its on- premises data center to process genomics data Sequencing data is generated and stored on a local storage area network (SAN), and then the data is processed. The research and development teams are running into capacity issues and have decided to re-architect their genomics analysis platform on AWS to scale based on workload demands and reduce the turnaround time from weeks to days The company has a high-speed AWS Direct Connect connection Sequencers will generate around 200 GB of data for each genome, and individual jobs can take several hours to process the data with ideal compute capacity. The end result will be stored in Amazon S3. The company is expecting 10-15 job requests each day Which solution meets these requirements? A. Use regularly scheduled AWS Snowball Edge devices to transfer the sequencing data into AWS When AWS receives the Snowball Edge device and the data is loaded into Amazon S3 use S3 events to trigger an AWS Lambda function to process the data B. Use AWS Data Pipeline to transfer the sequencing data to Amazon S3 Use S3 events to trigger an Amazon EC2 Auto Scaling group to launch custom-AMI EC2 instances running the Docker containers to process the data C. Use AWS DataSync to transfer the sequencing data to Amazon S3 Use S3 events to trigger an AWS Lambda function that starts an AWS Step Functions workflow Store the Docker images in Amazon Elastic Container Registry (Amazon ECR) and trigger AWS Batch to run the container and process the sequencing data D. Use an AWS Storage Gateway file gateway to transfer the sequencing data to Amazon S3 Use S3 events to trigger an AWS Batch job that runs on Amazon EC2 instances running the Docker containers to process the data -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use regularly scheduled AWS Snowball Edge devices to transfer the sequencing data into AWS When AWS receives the Snowball Edge device and the data is loaded into Amazon S3 use S3 events to trigger an AWS Lambda function to process the data",
      "B": "Use AWS Data Pipeline to transfer the sequencing data to Amazon S3 Use S3 events to trigger an Amazon EC2 Auto Scaling group to launch custom-AMI EC2 instances running the Docker containers to process the data",
      "C": "Use AWS DataSync to transfer the sequencing data to Amazon S3 Use S3 events to trigger an AWS Lambda function that starts an AWS Step Functions workflow Store the Docker images in Amazon Elastic Container Registry (Amazon ECR) and trigger AWS Batch to run the container and process the sequencing data",
      "D": "Use an AWS Storage Gateway file gateway to transfer the sequencing data to Amazon S3 Use S3 events to trigger an AWS Batch job that runs on Amazon EC2 instances running the Docker containers to process the data -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "101",
    "question": "- (Exam Topic 2) A finance company is storing financial records in an Amazon S3 bucket. The company persists a record for every financial transaction. According to regulatory requirements, the records cannot be modified for at least 1 year after they are written. The records are read on a regular basis and must be immediately accessible. Which solution will meet these requirements? A. Create a new S3 bucke B. Turn on S3 Object Lock, set a default retention period of 1 year, and set the retention mode to compliance mod C. Store all records inthe new S3 bucket. D. Create an S3 Lifecycle rule to immediately transfer new objects to the S3 Glacier storage tier Create an S3 Glacier Vault Lock policy that has a retention period of 1 year. E. Create an S3 Lifecycle rule to immediately transfer new objects to the S3 Intelligent-Tiering storage tier.Set a retention period of 1 year. F. Create an S3 bucket policy with a Deny action for PutObject operations with a condition where the s3:x-amz-object-retention header is not equal to 1 year. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a new S3 bucke",
      "B": "Turn on S3 Object Lock, set a default retention period of 1 year, and set the retention mode to compliance mod",
      "C": "Store all records inthe new S3 bucket.",
      "D": "Create an S3 Lifecycle rule to immediately transfer new objects to the S3 Glacier storage tier Create an S3 Glacier Vault Lock policy that has a retention period of 1 year.",
      "E": "Create an S3 Lifecycle rule to immediately transfer new objects to the S3 Intelligent-Tiering storage tier.Set a retention period of 1 year.",
      "F": "Create an S3 bucket policy with a Deny action for PutObject operations with a condition where the s3:x-amz-object-retention header is not equal to 1 year. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "103",
    "question": "- (Exam Topic 2) A company that runs applications on AWS recently subscribed to a new software-as-a-service (SaaS) data vendor. The vendor provides the data by way of a REST API that the vendor hosts in its AWS environment The vendor offers multiple options for connectivity to the API and Is working with the company to find the best way to connect. The company's AWS account does not allow outbound internet access from Its AWS environment The vendor's services run on AWS in the same AWS Region as the company's applications A solutions architect must Implement connectivity to the vendor's API so that the API is highly available In the company's VPC. Which solution will meet these requirements? A. Connect to the vendor's public API address for the data service. B. Connect to the vendor by way of a VPC peering connection between the vendor's VPC and the company's VPC C. Connect to the vendor by way of a VPC endpoint service that uses AWS PrivateLink D. Connect to a public bastion host that the vendor provides Tunnel the API traffic. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Connect to the vendor's public API address for the data service.",
      "B": "Connect to the vendor by way of a VPC peering connection between the vendor's VPC and the company's VPC",
      "C": "Connect to the vendor by way of a VPC endpoint service that uses AWS PrivateLink",
      "D": "Connect to a public bastion host that the vendor provides Tunnel the API traffic. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "105",
    "question": "- (Exam Topic 2) A company runs a proprietary stateless ETL application on an Amazon EC2 Linux instance. The application is a Linux binary, and the source code cannot be modified. The application is single-threaded, uses 2 GB of RAM. and is highly CPU intensive The application is scheduled to run every 4 hours and runs for up to 20 minutes A solutions architect wants to revise the architecture for the solution. Which strategy should the solutions architect use? A. Use AWS Lambda to run the applicatio B. Use Amazon CloudWatch Logs to invoke the Lambda function every 4 hours C. Use AWS Batch to run the application Use an AWS Step Functions state machine to invoke the AWS Batch job every 4 hours D. Use AWS Fargate to run the application Use Amazon EventBridge (Amazon CloudWatch Events) to invoke the Fargate task every 4 hours E. Use Amazon 6C2 Spot Instances to run the application Use AWS CodeDeptoy to deploy and run the application every 4 hours. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS Lambda to run the applicatio",
      "B": "Use Amazon CloudWatch Logs to invoke the Lambda function every 4 hours",
      "C": "Use AWS Batch to run the application Use an AWS Step Functions state machine to invoke the AWS Batch job every 4 hours",
      "D": "Use AWS Fargate to run the application Use Amazon EventBridge (Amazon CloudWatch Events) to invoke the Fargate task every 4 hours",
      "E": "Use Amazon 6C2 Spot Instances to run the application Use AWS CodeDeptoy to deploy and run the application every 4 hours. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "109",
    "question": "- (Exam Topic 2) A company wants to migrate its website from an on-premises data center onto AWS At the same time it wants to migrate the website to a containerized microservice-based architecture to improve the availability and cost efficiency The company's security policy states that privileges and network permissions must be configured according to best practice, using least privilege A solutions architect must create a containerized architecture that meets the security requirements and has deployed the application to an Amazon ECS cluster What steps are required after the deployment to meet the requirements'? (Select TWO.) A. Create tasks using the bridge network mode B. Create tasks using the awsvpc network mode C. Apply security groups to Amazon EC2 instances and use IAM roles for EC2 instances to access other resources D. Apply security groups to the tasks, and pass IAM credentials into the container at launch time to access other resources E. Apply security groups to the tasks; and use IAM roles for tasks to access other resources -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create tasks using the bridge network mode",
      "B": "Create tasks using the awsvpc network mode",
      "C": "Apply security groups to Amazon EC2 instances and use IAM roles for EC2 instances to access other resources",
      "D": "Apply security groups to the tasks, and pass IAM credentials into the container at launch time to access other resources",
      "E": "Apply security groups to the tasks; and use IAM roles for tasks to access other resources -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "E"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "62.2",
    "question": "- (Exam Topic 2) A company has a new security policy. The policy requires the company to log any event that retrieves data from Amazon S3 buckets. The company must save these audit logs in a dedicated S3 bucket. The company created the audit logs S3 bucket in an AWS account that is designated for centralized logging. The S3 bucket has a bucket policy that allows write-only cross-account access A solutions architect must ensure that all S3 object-level access is being logged for current S3 buckets and future S3 buckets. Which solution will meet these requirements? A. Enable server access logging for all current S3 bucket B. Use the audit logs S3 bucket as a destination foraudit logs C. Enable replication between all current S3 buckets and the audit logs S3 bucket Enable S3 Versioning in the audit logs S3 bucket D. Configure S3 Event Notifications for all current S3 buckets to invoke an AWS Lambda function every time objects are accessed . Store Lambda logs in the audit logs S3 bucket. E. Enable AWS CloudTrai F. and use the audit logs S3 bucket to store logs Enable data event logging for S3 event sources, current S3 buckets, and future S3 buckets. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Enable server access logging for all current S3 bucket",
      "B": "Use the audit logs S3 bucket as a destination foraudit logs",
      "C": "Enable replication between all current S3 buckets and the audit logs S3 bucket Enable S3 Versioning in the audit logs S3 bucket",
      "D": "Configure S3 Event Notifications for all current S3 buckets to invoke an AWS Lambda function every time objects are accessed . Store Lambda logs in the audit logs S3 bucket.",
      "E": "Enable AWS CloudTrai",
      "F": "and use the audit logs S3 bucket to store logs Enable data event logging for S3 event sources, current S3 buckets, and future S3 buckets. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "113",
    "question": "- (Exam Topic 2) A company has more than 10.000 sensors that send data to an on-premises Apache Kafka server by using the Message Queuing Telemetry Transport (MQTT) protocol . The on-premises Kafka server transforms the data and then stores the results as objects in an Amazon S3 bucket Recently, the Kafka server crashed. The company lost sensor data while the server was being restored A solutions architect must create a new design on AWS that is highly available and scalable to prevent a similar occurrence Which solution will meet these requirements? A. Launch two Amazon EC2 instances to host the Kafka server in an active/standby configuration across two Availability Zone B. Create a domain name in Amazon Route 53 Create a Route 53 failover policy Route the sensors to send the data to the domain name C. Migrate the on-premises Kafka server to Amazon Managed Streaming for Apache Kafka (Amazon MSK). Create a Network Load Balancer (NLB) that points to the Amazon MSK broke D. Enable NLB health checks Route the sensors to send the data to the NLB. E. Deploy AWS loT Core, and connect it to an Amazon Kinesis Data Firehose delivery stream Use an AWS Lambda function to handle data transformation Route the sensors to send the data to AWS loT Core F. Deploy AWS loT Core, and launch an Amazon EC2 instance to host the Kafka server Configure AWS loT Core to send the data to the EC2 instance Route the sensors to send the data to AWSIoT Core. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Launch two Amazon EC2 instances to host the Kafka server in an active/standby configuration across two Availability Zone",
      "B": "Create a domain name in Amazon Route 53 Create a Route 53 failover policy Route the sensors to send the data to the domain name",
      "C": "Migrate the on-premises Kafka server to Amazon Managed Streaming for Apache Kafka (Amazon MSK). Create a Network Load Balancer (NLB) that points to the Amazon MSK broke",
      "D": "Enable NLB health checks Route the sensors to send the data to the NLB.",
      "E": "Deploy AWS loT Core, and connect it to an Amazon Kinesis Data Firehose delivery stream Use an AWS Lambda function to handle data transformation Route the sensors to send the data to AWS loT Core",
      "F": "Deploy AWS loT Core, and launch an Amazon EC2 instance to host the Kafka server Configure AWS loT Core to send the data to the EC2 instance Route the sensors to send the data to AWSIoT Core. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "116",
    "question": "- (Exam Topic 2) A development team s Deploying new APIs as serverless applications within a company. The team is currently using the AWS Maragement Console to provision Amazon API Gateway. AWS Lambda, and Amazon DynamoDB resources A solutions architect has been tasked with automating the future deployments of these serveriess APIs How can this be accomplished? A. Use AWS CloudFonTiation with a Lambda-backed custom resource to provision API Gateway Use the MfS: :OynMoDB::Table and AWS::Lambda::Function resources to create the Amazon DynamoOB table and Lambda functions Write a script to automata the deployment of the CloudFormation template. B. Use the AWS Serverless Application Model to define the resources Upload a YAML template and application files to the code repository Use AWS CodePipeline to conned to the code repository and to create an action to build using AWS CodeBuil C. Use the AWS CloudFormabon deployment provider m CodePipeline to deploy the solution. D. Use AWS CloudFormation to define the serverless applicatio E. Implement versioning on the Lambda functions and create aliases to point to the version F. When deploying, configure weights to implement shifting traffic to the newest version, and gradually update the weights as traffic moves over G. Commit the application code to the AWS CodeCommit code repositor H. Use AWS CodePipeline and connect to the CodeCommit code repository Use AWS CodeBuild to build and deploy the Lambda functions using AWS CodeDeptoy Specify the deployment preference type in CodeDeploy to gradually shift traffic over to the new version. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS CloudFonTiation with a Lambda-backed custom resource to provision API Gateway Use the MfS: :OynMoDB::Table and AWS::Lambda::Function resources to create the Amazon DynamoOB table and Lambda functions Write a script to automata the deployment of the CloudFormation template.",
      "B": "Use the AWS Serverless Application Model to define the resources Upload a YAML template and application files to the code repository Use AWS CodePipeline to conned to the code repository and to create an action to build using AWS CodeBuil",
      "C": "Use the AWS CloudFormabon deployment provider m CodePipeline to deploy the solution.",
      "D": "Use AWS CloudFormation to define the serverless applicatio",
      "E": "Implement versioning on the Lambda functions and create aliases to point to the version",
      "F": "When deploying, configure weights to implement shifting traffic to the newest version, and gradually update the weights as traffic moves over",
      "G": "Commit the application code to the AWS CodeCommit code repositor",
      "H": "Use AWS CodePipeline and connect to the CodeCommit code repository Use AWS CodeBuild to build and deploy the Lambda functions using AWS CodeDeptoy Specify the deployment preference type in CodeDeploy to gradually shift traffic over to the new version. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "118",
    "question": "- (Exam Topic 2) A company uses AWS Organizations with a single OU named Production to manage multiple accounts All accounts are members of the Production OU Administrators use deny list SCPs in the root of the organization to manage access to restricted services. The company recently acquired a new business unit and invited the new unit's existing AWS account to the organization Once onboarded the administrators of the new business unit discovered that they are not able to update existing AWS Config rules to meet the company's policies. Which option will allow administrators to make changes and continue to enforce the current policies without introducing additional long-term maintenance? A. Remove the organization's root SCPs that limit access to AWS Config Create AWS Service Catalog products for the company's standard AWS Config rules and deploy them throughout the organization, including the new account. B. Create a temporary OU named Onboarding for the new account Apply an SCP to the Onboarding OU to allow AWS Config actions Move the new account to the Production OU when adjustments to AWS Config are complete C. Convert the organization's root SCPs from deny list SCPs to allow list SCPs to allow the required services only Temporarily apply an SCP to the organization's root that allows AWS Config actions for principals only in the new account. D. Create a temporary OU named Onboarding for the new account Apply an SCP to the Onboarding OU to allow AWS Config action E. Move the organization's root SCP to the Production O F. Move the new account to the Production OU when adjustments to AWS Config are complete. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Remove the organization's root SCPs that limit access to AWS Config Create AWS Service Catalog products for the company's standard AWS Config rules and deploy them throughout the organization, including the new account.",
      "B": "Create a temporary OU named Onboarding for the new account Apply an SCP to the Onboarding OU to allow AWS Config actions Move the new account to the Production OU when adjustments to AWS Config are complete",
      "C": "Convert the organization's root SCPs from deny list SCPs to allow list SCPs to allow the required services only Temporarily apply an SCP to the organization's root that allows AWS Config actions for principals only in the new account.",
      "D": "Create a temporary OU named Onboarding for the new account Apply an SCP to the Onboarding OU to allow AWS Config action",
      "E": "Move the organization's root SCP to the Production O",
      "F": "Move the new account to the Production OU when adjustments to AWS Config are complete. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "122",
    "question": "- (Exam Topic 2) A company is using a lift-and-shift strategy to migrate applications from several on-premises Windows servers to AWS. The Windows servers will be hosted on Amazon EC2 instances in the us-east-1 Region. The company's security policy allows the installation of migration tools on servers. The migration data must be encrypted in transit and encrypted at rest. The applications are business critical. The company needs to minimize the cutover window and minimize the downtime that results from the migration. The company wants to use Amazon CloudWatch and AWS CloudTrail for monitoring. Which solution will meet these requirements? A. Use AWS Application Migration Service (CloudEnsure Migration) to migrate the Windows servers to AW B. Create a Replication Settings templat C. Install the AWS Replication Agent on the source servers D. Use AWS DataSync to migrate the Windows servers to AW E. Install the DataSync agent on the source server F. Configure a blueprint for the target server G. Begin the replication process. H. Use AWS Server Migration Service (AWS SMS) to migrate the Windows servers to AW I. Install the SMS Connector on the source server J. Replicate the source servers to AW K. Convert the replicated volumes to AMIs to launch EC2 instances. L. Use AWS Migration Hub to migrate the Windows servers to AW M. Create a project in Migration Hub.Track the progress of server migration by using the built-in dashboard. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS Application Migration Service (CloudEnsure Migration) to migrate the Windows servers to AW",
      "B": "Create a Replication Settings templat",
      "C": "Install the AWS Replication Agent on the source servers",
      "D": "Use AWS DataSync to migrate the Windows servers to AW",
      "E": "Install the DataSync agent on the source server",
      "F": "Configure a blueprint for the target server",
      "G": "Begin the replication process.",
      "H": "Use AWS Server Migration Service (AWS SMS) to migrate the Windows servers to AW",
      "I": "Install the SMS Connector on the source server",
      "J": "Replicate the source servers to AW K. Convert the replicated volumes to AMIs to launch EC2 instances. L. Use AWS Migration Hub to migrate the Windows servers to AW M. Create a project in Migration Hub.Track the progress of server migration by using the built-in dashboard. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "123",
    "question": "- (Exam Topic 2) A company is migrating its infrastructure to the AW5 Cloud. The company must comply with a variety of regulatory standards for different projects. The company needs a multi-account environment. A solutions architect needs to prepare the baseline infrastructure The solution must provide a consistent baseline of management and security but it must allow flexibility for different compliance requirements within various AWS accounts. The solution also needs to integrate with the existing on-premises Active Directory Federation Services (AD FS) server. Which solution meets these requirements with the LEAST amount of operational overhead? A. Create an organization In AWS Organizations Create a single SCP for least privilege access across all accounts Create a single OU for all accounts Configure an IAM identity provider tor federation with the on-premises AD FS server Configure a central togging account with a defined process for log generating services to send log events to the central accoun B. Enable AWS Config in the central account with conformance packs for all accounts. C. Create an organization In AWS Organizations Enable AWS Control Tower on the organizatio D. Review included guardrails for SCP E. Check AWS Config for areas that require additions Add OUs as necessary Connect AWS Single Sign-On to the on-premises AD FS server F. Create an organization in AWS Organizations Create SCPs for least privilege access Create an OU structure, and use it to group AWS accounts Connect AWS Single Sign-On to the on-premises AD FS serve G. Configure a central logging account with a defined process for tog generating services to send log events to the central account Enable AWS Config in the central account with aggregators and conformance packs. H. Create an organization in AWS Organizations Enable AWS Control Tower on the organization Review included guardrails for SCP I. Check AWS Config for areas that require additions Configure an IAM identity provider for federation with the on-premises AD FS server. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an organization In AWS Organizations Create a single SCP for least privilege access across all accounts Create a single OU for all accounts Configure an IAM identity provider tor federation with the on-premises AD FS server Configure a central togging account with a defined process for log generating services to send log events to the central accoun",
      "B": "Enable AWS Config in the central account with conformance packs for all accounts.",
      "C": "Create an organization In AWS Organizations Enable AWS Control Tower on the organizatio",
      "D": "Review included guardrails for SCP",
      "E": "Check AWS Config for areas that require additions Add OUs as necessary Connect AWS Single Sign-On to the on-premises AD FS server",
      "F": "Create an organization in AWS Organizations Create SCPs for least privilege access Create an OU structure, and use it to group AWS accounts Connect AWS Single Sign-On to the on-premises AD FS serve",
      "G": "Configure a central logging account with a defined process for tog generating services to send log events to the central account Enable AWS Config in the central account with aggregators and conformance packs.",
      "H": "Create an organization in AWS Organizations Enable AWS Control Tower on the organization Review included guardrails for SCP",
      "I": "Check AWS Config for areas that require additions Configure an IAM identity provider for federation with the on-premises AD FS server. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "124",
    "question": "- (Exam Topic 2) A company has multiple business units Each business unit has its own AWS account and runs a single website within that account. The company also has a single logging account. Logs from each business unit website are aggregated into a single Amazon S3 bucket in the logging account. The S3 bucket policy provides each business unit with access to write data into the bucket and requires data to be encrypted. The company needs to encrypt logs uploaded into the bucket using a Single AWS Key Management Service {AWS KMS) CMK The CMK that protects the data must be rotated once every 365 days Which strategy is the MOST operationally efficient for the company to use to meet these requirements? A. Create a customer managed CMK ri the logging account Update the CMK key policy to provide access to the logging account only Manually rotate the CMK every 365 days. B. Create a customer managed CMK in the logging accoun C. Update the CMK key policy to provide access to the logging account and business unit account D. Enable automatic rotation of the CMK E. Use an AWS managed CMK m the togging accoun F. Update the CMK key policy to provide access to the logging account and business unit accounts Manually rotate the CMK every 365 days. G. Use an AWS managed CMK in the togging account Update the CMK key policy to provide access to the togging account onl H. Enable automatic rotation of the CMK. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a customer managed CMK ri the logging account Update the CMK key policy to provide access to the logging account only Manually rotate the CMK every 365 days.",
      "B": "Create a customer managed CMK in the logging accoun",
      "C": "Update the CMK key policy to provide access to the logging account and business unit account",
      "D": "Enable automatic rotation of the CMK",
      "E": "Use an AWS managed CMK m the togging accoun",
      "F": "Update the CMK key policy to provide access to the logging account and business unit accounts Manually rotate the CMK every 365 days.",
      "G": "Use an AWS managed CMK in the togging account Update the CMK key policy to provide access to the togging account onl",
      "H": "Enable automatic rotation of the CMK. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "128",
    "question": "- (Exam Topic 2) A large company recently experienced an unexpected increase in Amazon RDS and Amazon DynamoDB costs The company needs to increase visibility into details of AWS Billing and Cost Management There are various accounts associated with AWS Organizations, including many development and production accounts. There is no consistent tagging strategy across the organization, but there are guidelines in place that require all infrastructure to be deployed using AWS Cloud Formation with consistent tagging Management requires cost center numbers and project ID numbers for all existing and future DynamoDB tables and RDS instances Which strategy should the solutions architect provide to meet these requirements? A. Use Tag Editor to tag existing resources Create cost allocation tags to define the cost center and project ID and allow 24 hours for tags to propagate to existing resources B. Use an AWS Config rule to alert the finance team of untagged resources Create a centralized AWS Lambda based solution to tag untagged RDS databases and DynamoDB resources every hour using a cross-account rote. C. Use Tag Editor to tag existing resources Create cost allocation tags to define the cost center and project ID Use SCPs to restrict resource creation that do not have the cost center and project ID on the resource. D. Create cost allocation tags to define the cost center and project ID and allow 24 hours for tags to propagate to existing resources Update existing federated roles to restrict privileges to provision resources that do not include the cost center and project ID on the resource -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use Tag Editor to tag existing resources Create cost allocation tags to define the cost center and project ID and allow 24 hours for tags to propagate to existing resources",
      "B": "Use an AWS Config rule to alert the finance team of untagged resources Create a centralized AWS Lambda based solution to tag untagged RDS databases and DynamoDB resources every hour using a cross-account rote.",
      "C": "Use Tag Editor to tag existing resources Create cost allocation tags to define the cost center and project ID Use SCPs to restrict resource creation that do not have the cost center and project ID on the resource.",
      "D": "Create cost allocation tags to define the cost center and project ID and allow 24 hours for tags to propagate to existing resources Update existing federated roles to restrict privileges to provision resources that do not include the cost center and project ID on the resource -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "130",
    "question": "- (Exam Topic 2) A solutions architect needs to provide AWS Cost and Usage Report data from a company's AWS Organizations management account The company already has an Amazon S3 bucket to store the reports The reports must be automatically ingested into a database that can be visualized with other toots. Which combination of steps should the solutions architect take to meet these requirements? (Select THREE ) A. Create an Amazon EventBridge (Amazon CloudWatch Events) rule that a new object creation in the S3 bucket will trigger B. Create an AWS Cost and Usage Report configuration to deliver the data into the S3 bucket C. Configure an AWS Glue crawler that a new object creation in the S3 bucket will trigger. D. Create an AWS Lambda function that a new object creation in the S3 bucket will trigger E. Create an AWS Glue crawler that me AWS Lambda function will trigger to crawl objects in me S3 bucket F. Create an AWS Glue crawler that the Amazon EventBridge (Amazon CloudWatCh Events) rule will trigger to crawl objects m the S3 bucket -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an Amazon EventBridge (Amazon CloudWatch Events) rule that a new object creation in the S3 bucket will trigger",
      "B": "Create an AWS Cost and Usage Report configuration to deliver the data into the S3 bucket",
      "C": "Configure an AWS Glue crawler that a new object creation in the S3 bucket will trigger.",
      "D": "Create an AWS Lambda function that a new object creation in the S3 bucket will trigger",
      "E": "Create an AWS Glue crawler that me AWS Lambda function will trigger to crawl objects in me S3 bucket",
      "F": "Create an AWS Glue crawler that the Amazon EventBridge (Amazon CloudWatCh Events) rule will trigger to crawl objects m the S3 bucket -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "D",
      "F"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "133",
    "question": "- (Exam Topic 2) A company owns a chain of travel agencies and is running an application in the AWS Cloud. Company employees use the application to search (or Information about travel destinations. Destination content is updated four times each year. Two fixed Amazon EC2 instances serve the application. The company uses an Amazon Route 53 public hosted zone with a multivalue record of travel.example.com that returns the Elastic IP addresses for the EC2 instances. The application uses Amazon DynamoDB as its primary data store. The company uses a self-hosted Redis instance as a caching solution. During content updates, the load on the EC2 instances and the caching solution increases drastically. This increased load has led to downtime on several occasions. A solutions architect must update the application so that the application is highly available and can handle the load that is generated by the content updates. Which solution will meet these requirements? A. Set up DynamoDB Accelerator (DAX} as in-memory cach B. Update the application to use DA C. Create an Auto Scaling group for the EC2 instance D. Create an Application Load Balancer (ALB). Set the Auto Scaling group as a target for the AL E. Update the Route 53 record to use a simple routing policy that targets the ALB's DNS alia F. Configure scheduled scaling for the EC2 instances before the content updates. G. Set up Amazon ElastiCache for Redi H. Update the application to use ElastiCach I. Create an Auto Scaling group for the EC2 instance J. Create an AmazonCloudFront distnbutio K. and set the Auto Scaling group as an origin for the distributio L. Update the Route 53 record to use a simple routing policy that targets the CloudFront distribution's DNS alias Manually scale up EC2 instances before the content updates M. Set up Amazon ElastiCache for Memcache N. Update the application to use ElastiCach O. Create an Auto Scaling group for the EC2 instances Create an Application Load Balancer (ALB). Set the Auto Scaling group as a target for the AL P. Update the Route 53 record to use a simple routing policy that targets the ALB's DNS alia Q. Configure scheduled scaling for the application before the content updates. R. Set up DynamoDB Accelerator (DAX) as in-memory cach S. Update the application to use DA T. Create an Auto Scaling group for the EC2 instance . Create an Amazon CloudFront distribution, and set the Auto Scaling group as an origin for the distributio . Update the Route 53 record to use a simple routing policy that targets the CloudFront distribution's DNS alia . Manually scale up EC2 instances before the content updates. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Set up DynamoDB Accelerator (DAX} as in-memory cach",
      "B": "Update the application to use DA",
      "C": "Create an Auto Scaling group for the EC2 instance",
      "D": "Create an Application Load Balancer (ALB). Set the Auto Scaling group as a target for the AL",
      "E": "Update the Route 53 record to use a simple routing policy that targets the ALB's DNS alia",
      "F": "Configure scheduled scaling for the EC2 instances before the content updates.",
      "G": "Set up Amazon ElastiCache for Redi",
      "H": "Update the application to use ElastiCach",
      "I": "Create an Auto Scaling group for the EC2 instance",
      "J": "Create an AmazonCloudFront distnbutio K. and set the Auto Scaling group as an origin for the distributio L. Update the Route 53 record to use a simple routing policy that targets the CloudFront distribution's DNS alias Manually scale up EC2 instances before the content updates M. Set up Amazon ElastiCache for Memcache N. Update the application to use ElastiCach O. Create an Auto Scaling group for the EC2 instances Create an Application Load Balancer (ALB). Set the Auto Scaling group as a target for the AL P. Update the Route 53 record to use a simple routing policy that targets the ALB's DNS alia Q. Configure scheduled scaling for the application before the content updates. R. Set up DynamoDB Accelerator (DAX) as in-memory cach S. Update the application to use DA T. Create an Auto Scaling group for the EC2 instance . Create an Amazon CloudFront distribution, and set the Auto Scaling group as an origin for the distributio . Update the Route 53 record to use a simple routing policy that targets the CloudFront distribution's DNS alia . Manually scale up EC2 instances before the content updates. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "138",
    "question": "- (Exam Topic 2) A large company runs workloads in VPCs that are deployed across hundreds of AWS accounts Each VPC consists of public subnets and private subnets that span across multiple Availability Zones NAT gateways are deployed in the public subnets and allow outbound connectivity to the internet from the private subnets. A solutions architect is working on a hub-and-spoke design. All private subnets in the spoke VPCs must route traffic to the internet through an egress VPC The solutions architect already has deployed a NAT gateway in an egress VPC in a central AWS account Which set of additional steps should the solutions architect take to meet these requirements? A. Create peering connections between the egress VPC and the spoke VPCs Configure the required routing to allow access to the internet B. Create a transit gateway and share it with the existing AWS accounts Attach existing VPCs to the transit gateway Configure the required routing to allow access to the internet C. Create a transit gateway in every account Attach the NAT gateway to the transit gateways Configure the required routing to allow access to the internet D. Create an AWS PrivateLink connection between the egress VPC and the spoke VPCs Configure the required routing to allow access to the internet -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create peering connections between the egress VPC and the spoke VPCs Configure the required routing to allow access to the internet",
      "B": "Create a transit gateway and share it with the existing AWS accounts Attach existing VPCs to the transit gateway Configure the required routing to allow access to the internet",
      "C": "Create a transit gateway in every account Attach the NAT gateway to the transit gateways Configure the required routing to allow access to the internet",
      "D": "Create an AWS PrivateLink connection between the egress VPC and the spoke VPCs Configure the required routing to allow access to the internet -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "139",
    "question": "- (Exam Topic 2) A company has an organization that has many AWS accounts in AWS Organizations A solutions architect must improve how the company manages common security group rules for the AWS accounts in the organization. The company has a common set of IP CIDR ranges in an allow list in each AWS account lo allow access to and from the company's on-premises network Developers within each account are responsible for adding new IP CIDR ranges to their security groups. The security team has its own AWS account. Currently, the security team notifies the owners of the other AWS accounts when changes are made to the allow list. The solutions architect must design a solution that distributes the common set of CIDR ranges across all accounts Which solution meets these requirements with the LEAST amount of operational overhead. A. Set up an Amazon Simple Notification Service (Amazon SNS) topic in the security team's AWS account Deploy an AWS Lambda function in each AWS account Configure the Lambda function to run every time an SNS topic receives a message Configure the Lambda function to take an IP address as input and add it to a list of security groups in the account Instruct the security team to distribute changes by publishing messages to its SNS topic B. Create new customer-managed prefix lists in each AWS account within the organization Populate theprefix lists in each account with all internal CIDR ranges Notify the owner of each AWS account to allow the new customer-managed prefix list IDs in their accounts in their security groups Instruct the security team to share updates with each AWS account owner. C. Create a new customer-managed prefix list in the security team's AWS account Populate thecustomer-managed prefix list with all internal CIDR range D. Share the customer-managed prefix list.... organization by using AWS Resource Access Manager Notify the owner of each AWS account to allow the new customer-managed prefix list ID in their security groups -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Set up an Amazon Simple Notification Service (Amazon SNS) topic in the security team's AWS account Deploy an AWS Lambda function in each AWS account Configure the Lambda function to run every time an SNS topic receives a message Configure the Lambda function to take an IP address as input and add it to a list of security groups in the account Instruct the security team to distribute changes by publishing messages to its SNS topic",
      "B": "Create new customer-managed prefix lists in each AWS account within the organization Populate theprefix lists in each account with all internal CIDR ranges Notify the owner of each AWS account to allow the new customer-managed prefix list IDs in their accounts in their security groups Instruct the security team to share updates with each AWS account owner.",
      "C": "Create a new customer-managed prefix list in the security team's AWS account Populate thecustomer-managed prefix list with all internal CIDR range",
      "D": "Share the customer-managed prefix list.... organization by using AWS Resource Access Manager Notify the owner of each AWS account to allow the new customer-managed prefix list ID in their security groups -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "144",
    "question": "- (Exam Topic 2) A company is configuring connectivity to a multi-account AWS environment to support application workloads fiat serve users in a single geographic region. The workloads depend on a highly available, on-premises legacy system deployed across two locations It is critical for the AWS workloads to manias connectivity to the legacy system, and a minimum of 5 Gbps of bandwidth is required All application workloads within AWS must have connectivity with one another. Which solution will meet these requirements? A. Configure multiple AWS Direct Connect (OX) 10 Gbps dedicated connections from a DX partner for each on-premises location Create private virtual interfaces on each connection for each AWS account VPC Associate me private virtual interface with a virtual private gateway attached to each VPC B. Configure multiple AWS Direct Connect (DX) 10 Gbps dedicated connections from two DX partners for each on-premises location Create and attach a virtual private gateway for each AWS account VP C. Create a DX gateway m a central network account and associate it with the virtual private gateways Create a public virtual interface on each DX connection and associate the interface with me DX gateway. D. Configure multiple AWS Direct Connect (DX) 10 Gbps dedicated connections from two DX partners for each on-premises location Create a transit gateway and a DX gateway in a central network accoun E. Create a transit virtual interface for each DX interlace and associate them with the DX gatewa F. Create a gateway association between the DX gateway and the transit gateway G. Configure multiple AWS Direct Connect (DX) 10 Gbps dedicated connections from a DX partner for each on-premises location Create and attach a virtual private gateway for each AWS account VP H. Create a transit gateway in a central network account and associate It with the virtual private gateways Create a transit virtual interface on each DX connection and attach the interface to the transit gateway. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure multiple AWS Direct Connect (OX) 10 Gbps dedicated connections from a DX partner for each on-premises location Create private virtual interfaces on each connection for each AWS account VPC Associate me private virtual interface with a virtual private gateway attached to each VPC",
      "B": "Configure multiple AWS Direct Connect (DX) 10 Gbps dedicated connections from two DX partners for each on-premises location Create and attach a virtual private gateway for each AWS account VP",
      "C": "Create a DX gateway m a central network account and associate it with the virtual private gateways Create a public virtual interface on each DX connection and associate the interface with me DX gateway.",
      "D": "Configure multiple AWS Direct Connect (DX) 10 Gbps dedicated connections from two DX partners for each on-premises location Create a transit gateway and a DX gateway in a central network accoun",
      "E": "Create a transit virtual interface for each DX interlace and associate them with the DX gatewa",
      "F": "Create a gateway association between the DX gateway and the transit gateway",
      "G": "Configure multiple AWS Direct Connect (DX) 10 Gbps dedicated connections from a DX partner for each on-premises location Create and attach a virtual private gateway for each AWS account VP",
      "H": "Create a transit gateway in a central network account and associate It with the virtual private gateways Create a transit virtual interface on each DX connection and attach the interface to the transit gateway. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "146",
    "question": "- (Exam Topic 2) A company's CI SO has asked a solutions architect to re-engineer the company's current CI/CD practices to make sure patch deployments to its application can happen as quickly as possible with minimal downtime if vulnerabilities are discovered The company must also be able to quickly roll back a change in case of errors. The web application is deployed in a fleet of Amazon EC2 instances behind an Application Load Balancer The company is currently using GitHub to host the application source code. and has configured an AWS CodeBuild project to build the application The company also intends to use AWS CodePipeline to trigger builds from GitHub commits using the existing CodeBuild project. What CI/CD configuration meets all of the requirements? A. Configure CodePipeline with a deploy stage using AWS CodeDeploy configured for in-place deployment Monitor the newly deployed code, and, if there are any issues, push another code update B. Configure CodePipeline with a deploy stage using AWS CodeDeploy configured for blue/green deployments Monitor the newly deployed code and if there are any issues, trigger a manual rollback using CodeDeploy C. Configure CodePipeline with a deploy stage using AWS CloudFormation to create a pipeline for test and production stacks Monitor the newly deployed code, and, if there are any issues, push another code update D. Configure the CodePipeline with a deploy stage using AWS OpsWorks and m-place deployments Monitor the newly deployed code an E. if there are any issues, push another code update -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure CodePipeline with a deploy stage using AWS CodeDeploy configured for in-place deployment Monitor the newly deployed code, and, if there are any issues, push another code update",
      "B": "Configure CodePipeline with a deploy stage using AWS CodeDeploy configured for blue/green deployments Monitor the newly deployed code and if there are any issues, trigger a manual rollback using CodeDeploy",
      "C": "Configure CodePipeline with a deploy stage using AWS CloudFormation to create a pipeline for test and production stacks Monitor the newly deployed code, and, if there are any issues, push another code update",
      "D": "Configure the CodePipeline with a deploy stage using AWS OpsWorks and m-place deployments Monitor the newly deployed code an",
      "E": "if there are any issues, push another code update -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "151",
    "question": "- (Exam Topic 2) A new startup is running a serverless application using AWS Lambda as the primary source of compute New versions of the application must be made available to a subset of users before deploying changes to all users Developers should also have the ability to stop the deployment and have access to an easy rollback mechanism A solutions architect decides to use AWS CodeDeploy to deploy changes when a new version is available. Which CodeDeploy configuration should the solutions architect use? A. A blue/green deployment B. A linear deployment C. A canary deployment D. An all-at-once deployment -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "A blue/green deployment",
      "B": "A linear deployment",
      "C": "A canary deployment",
      "D": "An all-at-once deployment -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "99.2",
    "question": "- (Exam Topic 2) A company runs an loT platform on AWS loT sensors in various locations send data to the company's Node js API servers on Amazon EC2 instances running behind an Application Load Balancer The data is stored in an Amazon RDS MySQL DB instance that uses a 4 TB General Purpose SSD volume The number of sensors the company has deployed in the field has increased over time and is expected to grow significantly The API servers are consistently overloaded and RDS metrics show high write latency Which of the following steps together will resolve the issues permanently and enable growth as new sensors are provisioned, while keeping this platform cost- efficient? {Select TWO.) A. Resize the MySQL General Purpose SSD storage to 6 TB to improve the volume's IOPS B. Re-architect the database tier to use Amazon Aurora instead of an RDS MySQL DB instance and add read replicas C. Leverage Amazon Kinesis Data Streams and AWS Lambda to ingest and process the raw data D. Use AWS X-Ray to analyze and debug application issues and add more API servers to match the load E. Re-architect the database tier to use Amazon DynamoDB instead of an RDS MySQL DB instance -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Resize the MySQL General Purpose SSD storage to 6 TB to improve the volume's IOPS",
      "B": "Re-architect the database tier to use Amazon Aurora instead of an RDS MySQL DB instance and add read replicas",
      "C": "Leverage Amazon Kinesis Data Streams and AWS Lambda to ingest and process the raw data",
      "D": "Use AWS X-Ray to analyze and debug application issues and add more API servers to match the load",
      "E": "Re-architect the database tier to use Amazon DynamoDB instead of an RDS MySQL DB instance -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C",
      "E"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "156",
    "question": "- (Exam Topic 2) A company's solutions architect is reviewing a web application that runs on AWS. The application references static assets in an Amazon S3 bucket in the us-east-1 Region. The company needs resiliency across multiple AWS Regions. The company already has created an S3 bucket in a second Region. Which solution will meet these requirements with the LEAST operational overhead? A. Configure the application to write each object to both S3 bucket B. Set up an Amazon Route 53 public hosted zone with a record set by using a weighted routing policy for each S3 bucke C. Configure the application to reference the objects by using the Route 53 DNS name. D. Create an AWS Lambda function to copy objects from the S3 bucket in us-east-1 to the S3 bucket in the second Regio E. Invoke the Lambda function each time an object is written to the S3 bucket in us-east-1. Set up an Amazon CloudFront distribution with an origin group that contains the two S3 buckets as origins. F. Configure replication on the S3 bucket in us-east-1 to replicate objects to the S3 bucket in the second Region Set up an Amazon CloudFront distribution with an origin group that contains the two S3 bucketsas origins. G. Configure replication on the S3 bucket in us-east-1 to replicate objects to the S3 bucket in the second Regio H. If failover is required, update the application code to load S3 objects from the S3 bucket in the second Region. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure the application to write each object to both S3 bucket",
      "B": "Set up an Amazon Route 53 public hosted zone with a record set by using a weighted routing policy for each S3 bucke",
      "C": "Configure the application to reference the objects by using the Route 53 DNS name.",
      "D": "Create an AWS Lambda function to copy objects from the S3 bucket in us-east-1 to the S3 bucket in the second Regio",
      "E": "Invoke the Lambda function each time an object is written to the S3 bucket in us-east-1. Set up an Amazon CloudFront distribution with an origin group that contains the two S3 buckets as origins.",
      "F": "Configure replication on the S3 bucket in us-east-1 to replicate objects to the S3 bucket in the second Region Set up an Amazon CloudFront distribution with an origin group that contains the two S3 bucketsas origins.",
      "G": "Configure replication on the S3 bucket in us-east-1 to replicate objects to the S3 bucket in the second Regio",
      "H": "If failover is required, update the application code to load S3 objects from the S3 bucket in the second Region. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "161",
    "question": "- (Exam Topic 2) A retail company runs a business-critical web service on an Amazon Elastic Container Service (Amazon ECS) cluster that runs on Amazon EC2 instances The web service receives POST requests from end users and writes data to a MySQL database that runs on a separate EC2 instance The company needs to ensure that data loss does not occur. The current code deployment process includes manual updates of the ECS service During a recent deployment, end users encountered intermittent 502 Bad Gateway errors in response to valid web requests The company wants to implement a reliable solution to prevent this issue from recurring. The company also wants to automate code deployments. The solution must be highly available and must optimize cost-effectiveness A. Run the web service on an ECS cluster that has a Fargate launch type Use AWS CodePipeline and AWS CodeDeploy to perform a blue/green deployment with validation testing to update the ECS service. B. Migrate the MySQL database to run on an Amazon RDS for MySQL Multi-AZ DB instance that uses Provisioned IOPS SSD (io2) storage C. Configure an Amazon Simple Queue Service (Amazon SQS) queue as an event source to receive the POST requests from the web service Configure an AWS Lambda function to poll the queue Write the data to the database. D. Run the web service on an ECS cluster that has a Fargate launch type Use AWS CodePipeline and AWS CodeDeploy to perform a canary deployment to update the ECS service. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Run the web service on an ECS cluster that has a Fargate launch type Use AWS CodePipeline and AWS CodeDeploy to perform a blue/green deployment with validation testing to update the ECS service.",
      "B": "Migrate the MySQL database to run on an Amazon RDS for MySQL Multi-AZ DB instance that uses Provisioned IOPS SSD (io2) storage",
      "C": "Configure an Amazon Simple Queue Service (Amazon SQS) queue as an event source to receive the POST requests from the web service Configure an AWS Lambda function to poll the queue Write the data to the database.",
      "D": "Run the web service on an ECS cluster that has a Fargate launch type Use AWS CodePipeline and AWS CodeDeploy to perform a canary deployment to update the ECS service. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C",
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "162",
    "question": "- (Exam Topic 2) A company's solution architect is designing a diasaster recovery (DR) solution for an application that runs on AWS. The application uses PostgreSQL 11.7 as its database. The company has an PRO of 30 seconds. The solutions architect must design a DR solution with the primary database in the us-east-1 Region and the database in the us-west-2 Region. What should the solution architect do to meet these requirements with minimum application change? A. Migrate the database to Amazon RDS for PostgreSQL in us-east-1. Set up a read replica up a read replica in us-west-2. Set the managed PRO for the RDS database to 30 seconds. B. Migrate the database to Amazon for PostgreSQL in us-east-1. Set up a standby replica in an Availability Zone in us-west-2, Set the managed PRO for the RDS database to 30 seconds. C. Migrate the database to an Amazon Aurora PostgreSQL global database with the primary Region as us-east-1 and the secondary Region as us-west-2. Set the managed PRO for the Aurora database to 30 seconds. D. Migrate the database to Amazon DynamoDB in us-east-1. Set up global tables with replica tables that are created in us-west-2. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Migrate the database to Amazon RDS for PostgreSQL in us-east-1. Set up a read replica up a read replica in us-west-2. Set the managed PRO for the RDS database to 30 seconds.",
      "B": "Migrate the database to Amazon for PostgreSQL in us-east-1. Set up a standby replica in an Availability Zone in us-west-2, Set the managed PRO for the RDS database to 30 seconds.",
      "C": "Migrate the database to an Amazon Aurora PostgreSQL global database with the primary Region as us-east-1 and the secondary Region as us-west-2. Set the managed PRO for the Aurora database to 30 seconds.",
      "D": "Migrate the database to Amazon DynamoDB in us-east-1. Set up global tables with replica tables that are created in us-west-2. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "56",
    "question": "- (Exam Topic 2) A company is using an Amazon CloudFront distribution to distribute both static and dynamic content from a web application running behind an Application Load Balancer The web application requires user authorization and session tracking tor dynamic content The CloudFront distribution has a single cache behavior configured to forward the Authorization, Host, and Agent HTTP allow list headers and a session cookie to the origin All other cache behavior settings are set to their default value A valid ACM certificate is applied to the CloudFront distribution with a matching CNAME in the distribution settings The ACM certificate is also applied to the HTTPS listener for the Application Load Balancer The CloudFront origin protocol policy is set to HTTPS only Analysis of the cache statistics report shows that the miss rate for this distribution is very high What can the solutions architect do to improve the cache hit rate for this distribution without causing the SSL/TLS handshake between CloudFront and the Application Load Balancer to fail? A. Create two cache behaviors for static and dynamic content Remove the user-Agent and Host HTTP headers from the allow list headers section on both of the cache behaviors Remove the session cookie from the allow list cookies section and the Authorization HTTP header from the allow list headers section for cache behavior configured for static content B. Remove the user-Agent and Authorization HTTP headers from the allow list headers section of the cache behaviou C. Then update the cache behaviour to use resigned cookies for authorization D. Remove the Host HTTP header from the allow list headers section and remove the session cookie from the allow list cookies section for the default cache behaviour Enable automatic object compression and use Lambda@Edge viewer request events for user authorization E. Create two cache behaviours for static and dynamic content Remove the User-Agent HTTP header from the allow list headers section on both of the cache behavioursRemove the session cookie from the allow list cookies section and the Authorization HTTP header from the allow list headers section for cache behaviour configured for static content -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create two cache behaviors for static and dynamic content Remove the user-Agent and Host HTTP headers from the allow list headers section on both of the cache behaviors Remove the session cookie from the allow list cookies section and the Authorization HTTP header from the allow list headers section for cache behavior configured for static content",
      "B": "Remove the user-Agent and Authorization HTTP headers from the allow list headers section of the cache behaviou",
      "C": "Then update the cache behaviour to use resigned cookies for authorization",
      "D": "Remove the Host HTTP header from the allow list headers section and remove the session cookie from the allow list cookies section for the default cache behaviour Enable automatic object compression and use Lambda@Edge viewer request events for user authorization",
      "E": "Create two cache behaviours for static and dynamic content Remove the User-Agent HTTP header from the allow list headers section on both of the cache behavioursRemove the session cookie from the allow list cookies section and the Authorization HTTP header from the allow list headers section for cache behaviour configured for static content -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-the-cache-key.html Removing the host header will result in failed flow\nbetween CloudFront and ALB, because they have same certificate.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "166",
    "question": "- (Exam Topic 2) A company used Amazon EC2 instances to deploy a web fleet to host a blog site The EC2 instances are behind an Application Load Balancer (ALB) and are configured in an Auto ScaSng group The web application stores all blog content on an Amazon EFS volume. The company recently added a feature 'or Moggers to add video to their posts, attracting 10 times the previous user traffic At peak times of day. users report buffering and timeout issues while attempting to reach the site or watch videos Which is the MOST cost-efficient and scalable deployment that win resolve the issues for users? A. Reconfigure Amazon EFS to enable maximum I/O. B. Update the Nog site to use instance store volumes tor storag C. Copy the site contents to the volumes at launch and to Amazon S3 al shutdown. D. Configure an Amazon CloudFront distributio E. Point the distribution to an S3 bucket, and migrate the videos from EFS to Amazon S3. F. Set up an Amazon CloudFront distribution for all site contents, and point the distribution at the ALB. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Reconfigure Amazon EFS to enable maximum I/O.",
      "B": "Update the Nog site to use instance store volumes tor storag",
      "C": "Copy the site contents to the volumes at launch and to Amazon S3 al shutdown.",
      "D": "Configure an Amazon CloudFront distributio",
      "E": "Point the distribution to an S3 bucket, and migrate the videos from EFS to Amazon S3.",
      "F": "Set up an Amazon CloudFront distribution for all site contents, and point the distribution at the ALB. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "168",
    "question": "- (Exam Topic 2) A company is using multiple AWS accounts. The company has a shared services account and several other accounts (or different projects. A team has a VPC in a project account. The team wants to connect this VPC to a corporate network through an AWS Direct Connect gateway that exists in the shared services account. The team wants to automatically perform a virtual private gateway association with the Direct Connect gateway by using an already- tested AWS Lambda function while deploying its VPC networking stack. The Lambda function code can assume a role by using AWS Security Token Service (AWS STS). The team is using AWS Cloud Formation to deploy its infrastructure. A. Deploy the Lambda function to the project accoun B. Update the Lambda function's 1AM role with the directconnect:* permission C. Create a cross-account 1AM role in the shared services account that grants the Lambda function the directconnect:\" permissio D. Add the sts:AssumeRo!epermission to the 1AM role that is associated with the Lambda function in the shared services account. E. Add a custom resource to the Cloud Formation networking stack that references the Lambda function in the project account. F. Deploy the Lambda function that is performing the association to the shared services accoun G. Update the Lambda function's 1AM role with the directconnect:' permission. H. Create a cross-account 1AM role in the shared services account that grants the sts: Assume Role permission to the Lambda function with the directconnect:\"permission acting as a resourc I. Add the sts AssumeRole permission with this cross-account 1AM role as a resource to the 1AM role that belongs to the Lambda function in the project account. J. Add a custom resource to the Cloud Formation networking stack that references the Lambda function in the shared services account. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy the Lambda function to the project accoun",
      "B": "Update the Lambda function's 1AM role with the directconnect:* permission",
      "C": "Create a cross-account 1AM role in the shared services account that grants the Lambda function the directconnect:\" permissio",
      "D": "Add the sts:AssumeRo!epermission to the 1AM role that is associated with the Lambda function in the shared services account.",
      "E": "Add a custom resource to the Cloud Formation networking stack that references the Lambda function in the project account.",
      "F": "Deploy the Lambda function that is performing the association to the shared services accoun",
      "G": "Update the Lambda function's 1AM role with the directconnect:' permission.",
      "H": "Create a cross-account 1AM role in the shared services account that grants the sts: Assume Role permission to the Lambda function with the directconnect:\"permission acting as a resourc",
      "I": "Add the sts AssumeRole permission with this cross-account 1AM role as a resource to the 1AM role that belongs to the Lambda function in the project account.",
      "J": "Add a custom resource to the Cloud Formation networking stack that references the Lambda function in the shared services account. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "C",
      "E"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "169",
    "question": "- (Exam Topic 2) A company is launching a web-based application in multiple regions around the world The application consists of both static content stored in a private Amazon S3 bucket and dyna ECS containers behind an Application Load Balancer (ALB) The company requires that the static and dynamic application content be accessible through Amazon CloudFront only Which combination of steps should a solutions architect recommend to restrict direct content access to CloudFront? (Select THREE) A. Create a web ACL in AWS WAF with a rule to validate the presence of a custom header and associate the web ACL with the ALB B. Create a web ACL in AWS WAF with a rule to validate the presence of a custom header and associate the web ACL with the CloudFront distribution C. Configure CloudFront to add a custom header to origin requests D. Configure the ALB to add a custom header to HTTP requests E. Update the S3 bucket ACL to allow access from the CloudFront distribution only F. Create a CloudFront Origin Access Identity (OAI) and add it to the CloudFront distribution Update the S3 bucket policy to allow access to the OAI only -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a web ACL in AWS WAF with a rule to validate the presence of a custom header and associate the web ACL with the ALB",
      "B": "Create a web ACL in AWS WAF with a rule to validate the presence of a custom header and associate the web ACL with the CloudFront distribution",
      "C": "Configure CloudFront to add a custom header to origin requests",
      "D": "Configure the ALB to add a custom header to HTTP requests",
      "E": "Update the S3 bucket ACL to allow access from the CloudFront distribution only",
      "F": "Create a CloudFront Origin Access Identity (OAI) and add it to the CloudFront distribution Update the S3 bucket policy to allow access to the OAI only -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C",
      "F"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "170",
    "question": "- (Exam Topic 2) A company has loT sensors that monitor traffic patterns throughout a large city. The company wants to read and collect data from the sensors and perform aggregations on the data. A solutions architect designs a solution in which the loT devices are streaming to Amazon Kinesis Data Streams. Several applications are reading from the stream. However, several consumers are experiencing throttling and are periodically encountering a ReadProvisionedThroughputExceeded error. Which actions should the solutions architect take to resolve this issue? (Select THREE.) A. Reshard the stream to increase the number of shards in the stream. B. Use the Kinesis Producer Library (KPL). Adjust the polling frequency. C. Use consumers with the enhanced fan-out feature. D. Reshard the stream to reduce the number of shards in the stream. E. Use an error retry and exponential backoff mechanism in the consumer logic. F. Configure the stream to use dynamic partitioning. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Reshard the stream to increase the number of shards in the stream.",
      "B": "Use the Kinesis Producer Library (KPL). Adjust the polling frequency.",
      "C": "Use consumers with the enhanced fan-out feature.",
      "D": "Reshard the stream to reduce the number of shards in the stream.",
      "E": "Use an error retry and exponential backoff mechanism in the consumer logic.",
      "F": "Configure the stream to use dynamic partitioning. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C",
      "D"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "175",
    "question": "- (Exam Topic 2) A company has used infrastructure as code (laC) to provision a set of two Amazon EC2 instances. The instances have remained the same tor several years. The company's business has grown rapidly in the past few months. In response, the company's operations team has implemented an Auto Scaling group to manage the sudden increases in traffic Company policy requires a monthly installation of security updates on all operating systems that are running. The most recent security update required a reboot. As a result the Auto Scaling group terminated the instances and replaced them with new, unpatched instances. Which combination of steps should a sol-tons architect recommend to avoid a recurrence of this issue? (Select TWO ) A. Modify the Auto Scaling group by setting the Update policy to target the oldest launch configuration for replacement. B. Create a new Auto Scaling group before the next patch maintenance During the maintenance window patch both groups and reboot the instances. C. Create an Elastic Load Balancer in front of the Auto Scaling group Configure monitoring to ensure that target group health checks return healthy after the Auto Scaling group replaces the terminated instances D. Create automation scripts to patch an AM E. update the launch configuration, and invoke an Auto Scaling instance refresh. F. Create an Elastic Load Balancer in front of the Auto Scaling group Configure termination protection on the instances. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Modify the Auto Scaling group by setting the Update policy to target the oldest launch configuration for replacement.",
      "B": "Create a new Auto Scaling group before the next patch maintenance During the maintenance window patch both groups and reboot the instances.",
      "C": "Create an Elastic Load Balancer in front of the Auto Scaling group Configure monitoring to ensure that target group health checks return healthy after the Auto Scaling group replaces the terminated instances",
      "D": "Create automation scripts to patch an AM",
      "E": "update the launch configuration, and invoke an Auto Scaling instance refresh.",
      "F": "Create an Elastic Load Balancer in front of the Auto Scaling group Configure termination protection on the instances. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "178",
    "question": "- (Exam Topic 2) A media company has a 30-TB repository of digital news videos These videos are stored on tape in an on-premises tape library and referenced by a Media Asset Management (MAM) system The company wants to enrich the metadata for these videos in an automated fashion and put them into a searchable catalog by using a MAM feature The company must be able to search based on information in the video such as objects scenery items or people's faces A catalog is available that contains faces of people who have appeared in the videos that include an image of each person The company would like to migrate these videos to AWS The company has a high-speed AWS Direct Connect connection with AWS and would like to move the MAM solution video content directly from its current file system How can these requirements be met by using the LEAST amount of ongoing management overhead and causing MINIMAL disruption to the existing system\"' A. Set up an AWS Storage Gateway file gateway appliance on-premise B. Use the MAM solution to extract the videos from the current archive and push them into the file gateway Use the catalog of faces to build a collection in Amazon Rekognition Build an AWS Lambda function that invokes the Rekognition Javascript SDK to have Rekognition pull the video from the Amazon S3 files backing the file gateway, retrieve the required metadata and push the metadata into the MAM solution C. Set up an AWS Storage Gateway tape gateway appliance on-premises Use the MAM solution to extract the videos from the current archive and push them into the tape gateway Use the catalog of faces to build a collection in Amazon Rekognition Build an AWS Lambda function that invokes the Rekognition Javascript SDK to have Amazon Rekognition process the video in the tape gateway retrieve the required metadata, and push the metadata into the MAM solution D. Configure a video ingestion stream by using Amazon Kinesis Video Streams Use the catalog of faces to build a collection in Amazon Rekognition Stream the videos from the MAM solution into Kinesis Video Streams Configure Amazon Rekognition to process the streamed videos Then, use a stream consumer to retrieve the required metadata and push the metadata into the MAM solution Configure the stream to store the videos in Amazon S3 E. Set up an Amazon EC2 instance that runs the OpenCV libranes Copy the videos, images, and facecatalog from the on-premises library into an Amazon EBS volumemounted on this EC2 instance Process the videos to retrieve the required metadata, and push the metadata into the MAM solution, while also copying the video files to an Amazon S3 bucket -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Set up an AWS Storage Gateway file gateway appliance on-premise",
      "B": "Use the MAM solution to extract the videos from the current archive and push them into the file gateway Use the catalog of faces to build a collection in Amazon Rekognition Build an AWS Lambda function that invokes the Rekognition Javascript SDK to have Rekognition pull the video from the Amazon S3 files backing the file gateway, retrieve the required metadata and push the metadata into the MAM solution",
      "C": "Set up an AWS Storage Gateway tape gateway appliance on-premises Use the MAM solution to extract the videos from the current archive and push them into the tape gateway Use the catalog of faces to build a collection in Amazon Rekognition Build an AWS Lambda function that invokes the Rekognition Javascript SDK to have Amazon Rekognition process the video in the tape gateway retrieve the required metadata, and push the metadata into the MAM solution",
      "D": "Configure a video ingestion stream by using Amazon Kinesis Video Streams Use the catalog of faces to build a collection in Amazon Rekognition Stream the videos from the MAM solution into Kinesis Video Streams Configure Amazon Rekognition to process the streamed videos Then, use a stream consumer to retrieve the required metadata and push the metadata into the MAM solution Configure the stream to store the videos in Amazon S3",
      "E": "Set up an Amazon EC2 instance that runs the OpenCV libranes Copy the videos, images, and facecatalog from the on-premises library into an Amazon EBS volumemounted on this EC2 instance Process the videos to retrieve the required metadata, and push the metadata into the MAM solution, while also copying the video files to an Amazon S3 bucket -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "179",
    "question": "- (Exam Topic 2) A company has an application that uses Amazon EC2 instances in an Auto Scaling group. The quality assurance (QA) department needs to launch a large number of short-lived environments to test the application. The application environments are currently launched by the manager of the department using an AWS CloudFormation template To launch the stack, the manager uses a role with permission to use CloudFormation EC2. and Auto Scaling APIs. The manager wants to allow testers to launch their own environments, but does not want to grant broad permissions to each user Which set up would achieve these goals? A. Upload the AWS CloudFormation template to Amazon S3. Give users in the QA department permission to assume the manager's role and add a policy that restricts the permissions to the template and the resources it creates Train users to launch the template from the CloudFormation console B. Create an AWS Service Catalog product from the environment template Add a launch constraint to the product with the existing role Give users in the QA department permission to use AWS Service Catalog APIs only_ Train users to launch the template from the AWS Service Catalog console. C. Upload the AWS CloudFormation template to Amazon S3 Give users in the QA department permission to use CloudFormation and S3 APIs, with conditions that restrict the permissions to the template and the resources it creates Train users to launch the template from the CloudFormation console. D. Create an AWS Elastic Beanstalk application from the environment template Give users in the QA department permission to use Elastic Beanstalk permissions only Train users to launch Elastic Beanstalk environments with the Elastic Beanstalk CLI, passing the existing role to the environment as a service role -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Upload the AWS CloudFormation template to Amazon S3. Give users in the QA department permission to assume the manager's role and add a policy that restricts the permissions to the template and the resources it creates Train users to launch the template from the CloudFormation console",
      "B": "Create an AWS Service Catalog product from the environment template Add a launch constraint to the product with the existing role Give users in the QA department permission to use AWS Service Catalog APIs only_ Train users to launch the template from the AWS Service Catalog console.",
      "C": "Upload the AWS CloudFormation template to Amazon S3 Give users in the QA department permission to use CloudFormation and S3 APIs, with conditions that restrict the permissions to the template and the resources it creates Train users to launch the template from the CloudFormation console.",
      "D": "Create an AWS Elastic Beanstalk application from the environment template Give users in the QA department permission to use Elastic Beanstalk permissions only Train users to launch Elastic Beanstalk environments with the Elastic Beanstalk CLI, passing the existing role to the environment as a service role -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "180",
    "question": "- (Exam Topic 2) A solutions architect needs to review the design of an Amazon EMR cluster that is using the EMR File System (EMRFS). The cluster performs tasks that are critical to business needs. The cluster is running Amazon EC2 On-Demand Instances at all times for all task, master, and core nodes The EMR tasks run each morning, starting at 1:00 AM, and take 6 hours to finish running. The amount of time to complete the processing is not a priority because the data is not referenced until late in the day. The solutions architect must review the architecture and suggest a solution to minimize the compute costs Which solution should the solutions architect recommend to meet these requirements? A. Launch all task, master, and core nodes on Spot Instances in an instance flee B. Terminate the cluster, including all instances, when the processing is completed. C. Launch the master and core nodes on On-Demand Instance D. Launch the task nodes on Spot Instances In an instance flee E. Terminate the cluster, including all instances, when the processing is complete F. Purchase Compute Savings Plans to cover the On-Demand Instance usage. G. Continue to launch all nodes on On-Demand Instance H. Terminate the cluste I. Including all instances, when the processing Is complete J. Purchase Compute Savings Plans to cover the On-Demand Instance usage. K. Launch the master and core nodes on On-Demand Instance L. Launch the task nodes on Spot Instances In an instance flee M. Terminate only the task node Instances when the processing is completed Purchase Compute Savings Plans to cover the On-Demand Instance usage. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Launch all task, master, and core nodes on Spot Instances in an instance flee",
      "B": "Terminate the cluster, including all instances, when the processing is completed.",
      "C": "Launch the master and core nodes on On-Demand Instance",
      "D": "Launch the task nodes on Spot Instances In an instance flee",
      "E": "Terminate the cluster, including all instances, when the processing is complete",
      "F": "Purchase Compute Savings Plans to cover the On-Demand Instance usage.",
      "G": "Continue to launch all nodes on On-Demand Instance",
      "H": "Terminate the cluste",
      "I": "Including all instances, when the processing Is complete",
      "J": "Purchase Compute Savings Plans to cover the On-Demand Instance usage. K. Launch the master and core nodes on On-Demand Instance L. Launch the task nodes on Spot Instances In an instance flee M. Terminate only the task node Instances when the processing is completed Purchase Compute Savings Plans to cover the On-Demand Instance usage. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "149",
    "question": "- (Exam Topic 2) A company is collecting a large amount of data from a fleet of loT devices. Data is stored as Optimized Row Columnar (ORC) files in the Hadoop Distributed File System (HDFS) on a persistent Amazon EMR cluster. The company's data analytics team queries the data by using SQL in Apache Presto deployed on the same EMR cluster Queries scan large amounts of data always run for less than 15 minutes, and run only between 5 PM and 10 PM. The company is concerned about the high cost associated with the current solution A solutions architect must propose the most cost-effective solution that will allow SQL data queries. Which solution will meet these requirements? A. Store data m Amazon S3 Use Amazon Redshift Spectrum to query data. B. Store data m Amazon S3 Use the AWS Glue Data Catalog and Amazon Athena to query data. C. Store data in EMR File System (EMRFS). Use Presto n Amazon EMR to query data. D. Store data in Amazon Redshift Use Amazon Redshift to query data -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Store data m Amazon S3 Use Amazon Redshift Spectrum to query data.",
      "B": "Store data m Amazon S3 Use the AWS Glue Data Catalog and Amazon Athena to query data.",
      "C": "Store data in EMR File System (EMRFS). Use Presto n Amazon EMR to query data.",
      "D": "Store data in Amazon Redshift Use Amazon Redshift to query data -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "153",
    "question": "- (Exam Topic 2) A company is using an existing orchestration tool to manage thousands of Amazon EC2 instances. A recent penetration test found a vulnerability in the company's software stack. This vulnerability has prompted the company to perform a full evaluated of its current production environment The analysts determined that the following vulnerabilities exist within the environment: • Operating systems with outdated libraries and known vulnerabilities are being used in production • Relational databases hosted and managed by the company are running unsupported versions with known vulnerabilities • Data stored in databases Is not encrypted. The solutions architect intends to use AWS Config to continuously audit and assess the compliance of the company's AWS resource configurations with the company's polices and guidelines What additional steps will enable the company to secure its environments and track resources while adhering to best practices? A. Use AWS Application Discovery Service to evaluate at running EC2 instances Use the AWS CLI lo modify each instance, and use EC2 user data to install the AWS SystemsManager Agent during boot Schedule patching to run as a Systems Manager Maintenance Windowstas B. Migrate all relational databases lo Amazon RDS and enable AWS KMS encryption C. Create an AWS CloudFormation template for the EC2 instances Use EC2 user data in the CloudFormation template to install the AWS Systems Manager Agent, and enable AWS KMS encryption on all Amazon EBS volume D. Have CloudFormation replace al running instance E. Use Systems Manager Patch Manager to establish a patch baseline and deploy a Systems Manager Maintenance Windows task to run AWS-RunPatchBaseline using the patch baseline F. Install the AWS Systems Manager Agent on all existing instances using the company's current orchestration tool Use the Systems Manager Run Command to run a list of commands to upgrade software on each instance using operating system-specific tool G. Enable AWS KMS encryption on all Amazon EBS volumes. H. install the AWS Systems Manager Agent on all existing instances using the company's current orchestration too I. Migrate al relational databases to Amazon RDS and enable AWS KMS encryption Use Systems Manager Patch Manager to establish a patch baseline and deploy a Systems Manager Maintenance Windows task to run AWS-RunPatchBaseline using the patch baseline. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS Application Discovery Service to evaluate at running EC2 instances Use the AWS CLI lo modify each instance, and use EC2 user data to install the AWS SystemsManager Agent during boot Schedule patching to run as a Systems Manager Maintenance Windowstas",
      "B": "Migrate all relational databases lo Amazon RDS and enable AWS KMS encryption",
      "C": "Create an AWS CloudFormation template for the EC2 instances Use EC2 user data in the CloudFormation template to install the AWS Systems Manager Agent, and enable AWS KMS encryption on all Amazon EBS volume",
      "D": "Have CloudFormation replace al running instance",
      "E": "Use Systems Manager Patch Manager to establish a patch baseline and deploy a Systems Manager Maintenance Windows task to run AWS-RunPatchBaseline using the patch baseline",
      "F": "Install the AWS Systems Manager Agent on all existing instances using the company's current orchestration tool Use the Systems Manager Run Command to run a list of commands to upgrade software on each instance using operating system-specific tool",
      "G": "Enable AWS KMS encryption on all Amazon EBS volumes.",
      "H": "install the AWS Systems Manager Agent on all existing instances using the company's current orchestration too",
      "I": "Migrate al relational databases to Amazon RDS and enable AWS KMS encryption Use Systems Manager Patch Manager to establish a patch baseline and deploy a Systems Manager Maintenance Windows task to run AWS-RunPatchBaseline using the patch baseline. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "156.2",
    "question": "- (Exam Topic 2) A new application is running on Amazon Elastic Container Service (Amazon ECS) with AWS Fargate The application uses an Amazon Aurora MySQL database The application and the database run m the same subnets of a VPC with distinct security groups that are configured. The password (or the database is stored m AWS Secrets Manager and is passed to the application through the D8_PASSWORD environment variable The hostname of the database is passed to the application through the DB_HOST environment variable The application Is failing to access the database. Which combination of actions should a solutions architect take to resolve this error? (Select THREE ) A. Ensure that the container has the environment variable with name \"DB_PASSWORD\" specified with a \"ValueFrom\" and the ARN of the secret B. Ensure that the container has the environment variable with name *D8_PASSWORD\" specified with a\"ValueFrom\" and the secret name of the secret. C. Ensure that the Fargate service security group allows inbound network traffic from the Aurora MySQL database on the MySQL TCP port 3306. D. Ensure that the Aurora MySQL database security group allows inbound network traffic from the Fargate service on the MySQL TCP port 3306. E. Ensure that the container has the environment variable with name \"D8_HOST\" specified with the hostname of a DB instance endpoint. F. Ensure that the container has the environment variable with name \"DB_HOST\" specified with the hostname of the OB duster endpoint. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Ensure that the container has the environment variable with name \"DB_PASSWORD\" specified with a \"ValueFrom\" and the ARN of the secret",
      "B": "Ensure that the container has the environment variable with name *D8_PASSWORD\" specified with a\"ValueFrom\" and the secret name of the secret.",
      "C": "Ensure that the Fargate service security group allows inbound network traffic from the Aurora MySQL database on the MySQL TCP port 3306.",
      "D": "Ensure that the Aurora MySQL database security group allows inbound network traffic from the Fargate service on the MySQL TCP port 3306.",
      "E": "Ensure that the container has the environment variable with name \"D8_HOST\" specified with the hostname of a DB instance endpoint.",
      "F": "Ensure that the container has the environment variable with name \"DB_HOST\" specified with the hostname of the OB duster endpoint. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "D",
      "E"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "161.2",
    "question": "- (Exam Topic 2) A large company has a business-critical application that runs in a single AWS Region The application consists of multiple Amazon EC2 instances and an Amazon RDS Multi-AZ DB instance The EC2 instances run In an Amazon EC2 Auto Scaling group across multiple Availability Zones A solutions architect is implementing a disaster recovery (DR) plan for the application The solutions architect has created a pilot light application deployment in a new Region, which is referred to as the DR Region The DR environment has an Auto Scaling group with a single EC2 instance and a read replica of the RDS DB instance The solutions architect must automate a failover from the primary application environment to the pilot light environment in the DR Region Which solution meets these requirements with the MOST operational efficiency'' A. Publish an application availability metric to Amazon CloudWatch in the DR Region from the application environment in the primary Region Create a CloudWatch alarm in the DR Region that is invoked when the application availability metric stops being delivered Configure the CloudWatch alarm to send a notification to an Amazon Simple Notification Service (Amazon SNS> topic in the DR Region Add an email subscription to the SNS topic that sends messages to the application owner upon notification, instruct a systems operator to sign in to the AWS Management Console and initiate failover operations for the application B. Create a cron task that runs every 5 minutes by using one of the application's EC2 instances in the primary Region Configure the cron task to check whether the application is available Upon failure, the cron task notifies a systems operator and attempts to restart the application services C. Create a cron task that runs every 5 minutes by using one of the application's EC2 instances in the primary Region Configure the cron task to check whether the application is available Upon failure, the cron task modifies the DR environment by promoting the read replica and by adding EC2 instances to the Auto Scaling group D. Publish an application availability metric to Amazon CloudWatch in the DR Region from the application environment in the primary Region Create a CloudWatch alarm in the DR Region that is invoked when the application availability metric stops being delivered Configure the CloudWatch alarm to send a notification to an Amazon Simple Notification Service (Amazon SNS) topic in the DR Region Use an AWS Lambda function that is invoked by Amazon SNS in the DR Region to promote the read replica and to add EC2 instances to the Auto Scaling group -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Publish an application availability metric to Amazon CloudWatch in the DR Region from the application environment in the primary Region Create a CloudWatch alarm in the DR Region that is invoked when the application availability metric stops being delivered Configure the CloudWatch alarm to send a notification to an Amazon Simple Notification Service (Amazon SNS> topic in the DR Region Add an email subscription to the SNS topic that sends messages to the application owner upon notification, instruct a systems operator to sign in to the AWS Management Console and initiate failover operations for the application",
      "B": "Create a cron task that runs every 5 minutes by using one of the application's EC2 instances in the primary Region Configure the cron task to check whether the application is available Upon failure, the cron task notifies a systems operator and attempts to restart the application services",
      "C": "Create a cron task that runs every 5 minutes by using one of the application's EC2 instances in the primary Region Configure the cron task to check whether the application is available Upon failure, the cron task modifies the DR environment by promoting the read replica and by adding EC2 instances to the Auto Scaling group",
      "D": "Publish an application availability metric to Amazon CloudWatch in the DR Region from the application environment in the primary Region Create a CloudWatch alarm in the DR Region that is invoked when the application availability metric stops being delivered Configure the CloudWatch alarm to send a notification to an Amazon Simple Notification Service (Amazon SNS) topic in the DR Region Use an AWS Lambda function that is invoked by Amazon SNS in the DR Region to promote the read replica and to add EC2 instances to the Auto Scaling group -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "163",
    "question": "- (Exam Topic 2) A company is running an application in the AWS Cloud. The company has several third-party services that integrate with the application through a RESTful API. The API is a serverless implementation with an Amazon API Gateway regional API endpoint that integrates with several different AWS Lambda functions. The application's data is nonrelational and is stored in an Amazon DynamoDB table. The application and the API are running in the eu-west-1 Region. The company needs the API to also be available in the us-east-1 Region. All data must be available in both Regions. A solutions architect already has deployed all the Lambda functions in us-east-1 Which additional steps should the solutions architect take to meet these requirements? (Select TWO.) A. Deploy a second API Gateway regional API endpoint in us-east-1. Create Lambda integration with the functions in us-east-1. B. Enable DynamoDB Streams on the table in eu-west-1. Replicate all changes to a DynamoDB table in us-east-1 C. Modify the DynamoDB table to be a global table in eu-west-1 and in us-east-1. D. Change the API Gateway API endpoint in eu-west-1 to an edge-optimized endpoin E. Create Lambda integration with the functions in both Regions. F. Create a DynamoDB read replica in us-east-1. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy a second API Gateway regional API endpoint in us-east-1. Create Lambda integration with the functions in us-east-1.",
      "B": "Enable DynamoDB Streams on the table in eu-west-1. Replicate all changes to a DynamoDB table in us-east-1",
      "C": "Modify the DynamoDB table to be a global table in eu-west-1 and in us-east-1.",
      "D": "Change the API Gateway API endpoint in eu-west-1 to an edge-optimized endpoin",
      "E": "Create Lambda integration with the functions in both Regions.",
      "F": "Create a DynamoDB read replica in us-east-1. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "166.2",
    "question": "- (Exam Topic 2) A company is finalizing the architecture for its backup solution for applications running on AWS. All of the applications run on AWS and use at least two Availability Zones in each tier. Company policy requires IT to durably store nightly backups of all its data in at least two locations: production and disaster recovery. The locations must be m different geographic regions. The company also needs the backup to be available to restore immediately at the production data center, and within 24 hours at the disaster recovery location backup processes must be fully automated. What is the MOST cost-effective backup solution that will meet all requirements? A. Back up all the data to a large Amazon EBS volume attached to the backup media server m the production regio B. Run automated scripts to snapshot these volumes nightl C. and copy these snapshots to the disaster recovery region. D. Back up all the data to Amazon S3 in the disaster recovery region Use a Lifecycle policy to move this data to Amazon Glacier in the production region immediately Only the data is replicated: remove the data from the S3 bucket in the disaster recovery region. E. Back up all the data to Amazon Glacier in the production regio F. Set up cross-region replication of this data to Amazon Glacier in the disaster recovery regio G. Set up a lifecycle policy to delete any data o der than 60 days. H. Back up all the data to Amazon S3 in the production regio I. Set up cross-region replication of this S3 bucket to another region and set up a lifecycle policy in the second region to immediately move this data to Amazon Glacier -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Back up all the data to a large Amazon EBS volume attached to the backup media server m the production regio",
      "B": "Run automated scripts to snapshot these volumes nightl",
      "C": "and copy these snapshots to the disaster recovery region.",
      "D": "Back up all the data to Amazon S3 in the disaster recovery region Use a Lifecycle policy to move this data to Amazon Glacier in the production region immediately Only the data is replicated: remove the data from the S3 bucket in the disaster recovery region.",
      "E": "Back up all the data to Amazon Glacier in the production regio",
      "F": "Set up cross-region replication of this data to Amazon Glacier in the disaster recovery regio",
      "G": "Set up a lifecycle policy to delete any data o der than 60 days.",
      "H": "Back up all the data to Amazon S3 in the production regio",
      "I": "Set up cross-region replication of this S3 bucket to another region and set up a lifecycle policy in the second region to immediately move this data to Amazon Glacier -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "182",
    "question": "- (Exam Topic 2) A company wants to deploy an API to AWS. The company plans to run the API on AWS Fargate behind a load balancer. The API requires the use of header- based routing and must be accessible from on-premises networks through an AWS Direct Connect connection and a private VIF. The company needs to add the client IP addresses that connect to the API to an allow list in AWS. The company also needs to add the IP addresses of the API to the allow list. The company's security team will allow /27 CIDR ranges to be added to the allow list. The solution must minimize complexity and operational overhead. Which solution will meet these requirements? A. Create a new Network Load Balancer (NLB) in the same subnets as the Fargate task deployments.Create a security group that includes only the client IP addresses that need access to the AP B. Attach the new security group to the Fargate task C. Provide the security team with the NLB's IP addresses for the allow list. D. Create two new /27 subnet E. Create a new Application Load Balancer (ALB) that extends across the new subnet F. Create a security group that includes only the client IP addresses that need access to the AP G. Attach the security group to the AL H. Provide the security team with the new subnet IP ranges for the allow list. I. Create two new '27 subnet J. Create a new Network Load Balancer (NLB) that extends across the new subnet K. Create a new Application Load Balancer (ALB) within the new subnet L. Create a security group that includes only the client IP addresses that need access to the AP M. Attach the security group to the AL N. Add the ALB's IP addresses as targets behind the NL O. Provide the security team with the NLB's IP addresses for the allow list. P. Create a new Application Load Balancer (ALB) in the same subnets as the Fargate task deployments.Create a security group that includes only the client IP addresses that need access to the AP Q. Attach the security group to the AL R. Provide the security team with the ALB's IP addresses for the allow list. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a new Network Load Balancer (NLB) in the same subnets as the Fargate task deployments.Create a security group that includes only the client IP addresses that need access to the AP",
      "B": "Attach the new security group to the Fargate task",
      "C": "Provide the security team with the NLB's IP addresses for the allow list.",
      "D": "Create two new /27 subnet",
      "E": "Create a new Application Load Balancer (ALB) that extends across the new subnet",
      "F": "Create a security group that includes only the client IP addresses that need access to the AP",
      "G": "Attach the security group to the AL",
      "H": "Provide the security team with the new subnet IP ranges for the allow list.",
      "I": "Create two new '27 subnet",
      "J": "Create a new Network Load Balancer (NLB) that extends across the new subnet K. Create a new Application Load Balancer (ALB) within the new subnet L. Create a security group that includes only the client IP addresses that need access to the AP M. Attach the security group to the AL N. Add the ALB's IP addresses as targets behind the NL O. Provide the security team with the NLB's IP addresses for the allow list. P. Create a new Application Load Balancer (ALB) in the same subnets as the Fargate task deployments.Create a security group that includes only the client IP addresses that need access to the AP Q. Attach the security group to the AL R. Provide the security team with the ALB's IP addresses for the allow list. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "119",
    "question": "- (Exam Topic 2) An AWS partner company is building a service in AWS Organizations using Its organization named org. This service requires the partner company to have access to AWS resources in a customer account, which is in a separate organization named org2 The company must establish least privilege security access using an API or command line tool to the customer account What is the MOST secure way to allow org1 to access resources h org2? A. The customer should provide the partner company with their AWS account access keys to log in and perform the required tasks B. The customer should create an IAM user and assign the required permissions to the IAM user The customer should then provide the credentials to the partner company to log In and perform the required tasks. C. The customer should create an IAM role and assign the required permissions to the IAM rol D. The partner company should then use the IAM rote's Amazon Resource Name (ARN) when requesting access to perform the required tasks E. The customer should create an IAM rote and assign the required permissions to the IAM rot F. The partner company should then use the IAM rote's Amazon Resource Name (ARN). Including the external ID in the IAM role's trust pokey, when requesting access to perform the required tasks -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "The customer should provide the partner company with their AWS account access keys to log in and perform the required tasks",
      "B": "The customer should create an IAM user and assign the required permissions to the IAM user The customer should then provide the credentials to the partner company to log In and perform the required tasks.",
      "C": "The customer should create an IAM role and assign the required permissions to the IAM rol",
      "D": "The partner company should then use the IAM rote's Amazon Resource Name (ARN) when requesting access to perform the required tasks",
      "E": "The customer should create an IAM rote and assign the required permissions to the IAM rot",
      "F": "The partner company should then use the IAM rote's Amazon Resource Name (ARN). Including the external ID in the IAM role's trust pokey, when requesting access to perform the required tasks -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "184",
    "question": "- (Exam Topic 2) A solutions architect has implemented a SAML 2.0 federated identity solution with their company's on-premises identity provider (IdP) to authenticate users' access to the AWS environment. When the solutions architect tests authentication through the federated identity web portal access to the AWS environment is granted However, when test users attempt to authenticate through the federated identity web portal, they are not able to access the AWS environment. Which items should the solutions architect check to ensure identity federation is property configured? (Select THREE) A. The IAM user's permissions pokey has allowed the use of SAML federation for that user B. The IAM roles created for the federated users' or federated groups' trust policy have set the SAML provider as the principle. C. Test users are not in the AWSFederatedUsers group in the company's IdP D. The web portal calls the AWS STS AssumeRoleWithSAML API with the ARN of the SAML provider the ARN of the IAM role, and the SAML assertion from IdP E. The on-premises IdP's DNS hostname is reachable from the AWS environment VPCs. F. The company's IdP defines SAML assertions that property map users or groups m the company to IAM roles with appropriate permissions -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "The IAM user's permissions pokey has allowed the use of SAML federation for that user",
      "B": "The IAM roles created for the federated users' or federated groups' trust policy have set the SAML provider as the principle.",
      "C": "Test users are not in the AWSFederatedUsers group in the company's IdP",
      "D": "The web portal calls the AWS STS AssumeRoleWithSAML API with the ARN of the SAML provider the ARN of the IAM role, and the SAML assertion from IdP",
      "E": "The on-premises IdP's DNS hostname is reachable from the AWS environment VPCs.",
      "F": "The company's IdP defines SAML assertions that property map users or groups m the company to IAM roles with appropriate permissions -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "C",
      "F"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "127",
    "question": "- (Exam Topic 2) A company is using an Amazon EMR cluster to run its big data jobs The cluster's jobs are invoked by AWS Step Functions Express Workflows that consume various Amazon Simple Queue Service (Amazon SQS) queues The workload of this solution is variable and unpredictable Amazon CloudWatch metrics show that the cluster's peak utilization is only 25% at times and that the cluster sits idle the rest of the time A solutions architect must optimize the costs of the cluster without negatively impacting the time it takes to run the various jobs What is the MOST cost-effective solution that meets these requirements? A. Modify the EMR cluster by turning on automatic scaling of the core nodes and task nodes with a custom policy that is based on cluster utilization Purchase Reserved Instance capacity to cover the master node. B. Modify the EMR cluster to use an instance fleet of Dedicated On-Demand Instances for the master node and core nodes, and to use Spot Instances for the task node C. Define target capacity for each node type to cover the load. D. Purchase Reserved Instances for the master node and core nodes Terminate all existing task nodes in the EMR cluster E. Modify the EMR cluster to use capacity-optimized Spot Instances and a diversified task flee F. Define target capacity for each node type with a mix of On-Demand Instances and Spot Instances. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Modify the EMR cluster by turning on automatic scaling of the core nodes and task nodes with a custom policy that is based on cluster utilization Purchase Reserved Instance capacity to cover the master node.",
      "B": "Modify the EMR cluster to use an instance fleet of Dedicated On-Demand Instances for the master node and core nodes, and to use Spot Instances for the task node",
      "C": "Define target capacity for each node type to cover the load.",
      "D": "Purchase Reserved Instances for the master node and core nodes Terminate all existing task nodes in the EMR cluster",
      "E": "Modify the EMR cluster to use capacity-optimized Spot Instances and a diversified task flee",
      "F": "Define target capacity for each node type with a mix of On-Demand Instances and Spot Instances. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "130.2",
    "question": "- (Exam Topic 2) A data analytics company has an Amazon Redshift cluster that consists of several reserved nodes. The duster is experiencing unexpected bursts of usage because a team of employees is compiling a deep audit analysis report The queries to generate the report are complex read queries and are CPU intensive. Business requirements dictate that the cluster must be able to service read and write queries at at) times A solutions architect must devise a solution that accommodates the bursts of usage Which solution meets these requirements MOST cost-effectively? A. Provision an Amazon EMR duster Offload the complex data processing tasks B. Deploy an AWS Lambda function to add capacity to the Amazon Redshift cluster by using a classic resize operation when the duster's CPU metrics in Amazon CloudWatch reach 80%. C. Deploy an AWS Lambda function to add capacity to the Amazon Redshift duster by using an elastic resize operation when the duster's CPU metrics in Amazon CloudWatch leach 80%. D. Turn on the Concurrency Scaling feature for the Amazon Redshift duster -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Provision an Amazon EMR duster Offload the complex data processing tasks",
      "B": "Deploy an AWS Lambda function to add capacity to the Amazon Redshift cluster by using a classic resize operation when the duster's CPU metrics in Amazon CloudWatch reach 80%.",
      "C": "Deploy an AWS Lambda function to add capacity to the Amazon Redshift duster by using an elastic resize operation when the duster's CPU metrics in Amazon CloudWatch leach 80%.",
      "D": "Turn on the Concurrency Scaling feature for the Amazon Redshift duster -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "126",
    "question": "- (Exam Topic 2) A company wants to improve cost awareness for its Amazon EMR platform The company has aWocated budgets for each team's Amazon EMR usage When a budgetary threshold is reached a notification should be sent by email to the budget office's distribution list Teams should be able lo view their EMR cluster expenses to date A solutions architect needs to create a solution that ensures this policy is proactively and centrally enforced in a multi-account environment Which combination of steps should the solutions architect take to meet these requirements? (Select TWO.) A. Update the AWS CloudFormation template to include the AWS Budgets Budget resource with the NotificationsWithSubscnbers property B. Implement Amazon CloudWatch dashboards for Amazon EMR usage C. Create an EMR bootstrap action that runs at startup that calls the Cost Explorer API to set the budget onthe cluster with the GetCostForecast and NotificationsWithSubscnbers actions D. Create an AWS Service Catalog portfolio for each tea E. Add each team's Amazon EMR cluster as an AWS CloudFormation template to their Service Catalog portfolio as a Product F. Create an Amazon CloudWatch metric for billing Create a custom alert when costs exceed the budgetary threshold. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Update the AWS CloudFormation template to include the AWS Budgets Budget resource with the NotificationsWithSubscnbers property",
      "B": "Implement Amazon CloudWatch dashboards for Amazon EMR usage",
      "C": "Create an EMR bootstrap action that runs at startup that calls the Cost Explorer API to set the budget onthe cluster with the GetCostForecast and NotificationsWithSubscnbers actions",
      "D": "Create an AWS Service Catalog portfolio for each tea",
      "E": "Add each team's Amazon EMR cluster as an AWS CloudFormation template to their Service Catalog portfolio as a Product",
      "F": "Create an Amazon CloudWatch metric for billing Create a custom alert when costs exceed the budgetary threshold. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "E"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "187",
    "question": "- (Exam Topic 2) A company is creating a sequel for a popular online game. A large number of users from all over the world will play the game within the first week after launch. Currently, the game consists of the following components deployed in a single AWS Region: • Amazon S3 bucket that stores game assets • Amazon DynamoDB table that stores player scores A solutions architect needs to design a multi-Region solution that will reduce latency improve reliability, and require the least effort to implement What should the solutions architect do to meet these requirements? A. Create an Amazon CloudFront distribution to serve assets from the S3 bucket Configure S3Cross-Region Replication Create a new DynamoDB able in a new Region Use the new table as a replica target tor DynamoDB global tables. B. Create an Amazon CloudFront distribution to serve assets from the S3 bucke C. Configure S3Same-Region Replicatio D. Create a new DynamoDB able m a new Regio E. Configure asynchronous replication between the DynamoDB tables by using AWS Database Migration Service (AWS DMS) with change data capture (CDC) F. Create another S3 bucket in a new Region and configure S3 Cross-Region Replication between the buckets Create an Amazon CloudFront distribution and configure origin failover with two origins accessing the S3 buckets in each Regio G. Configure DynamoDB global tables by enabling Amazon DynamoDB Streams, and add a replica table in a new Region. H. Create another S3 bucket in the same Region, and configure S3 Same-Region Replication between the buckets- Create an Amazon CloudFront distribution and configure origin failover with two origin accessing the S3 buckets Create a new DynamoDB table m a new Region Use the new table as a replica target for DynamoDB global tables. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an Amazon CloudFront distribution to serve assets from the S3 bucket Configure S3Cross-Region Replication Create a new DynamoDB able in a new Region Use the new table as a replica target tor DynamoDB global tables.",
      "B": "Create an Amazon CloudFront distribution to serve assets from the S3 bucke",
      "C": "Configure S3Same-Region Replicatio",
      "D": "Create a new DynamoDB able m a new Regio",
      "E": "Configure asynchronous replication between the DynamoDB tables by using AWS Database Migration Service (AWS DMS) with change data capture (CDC)",
      "F": "Create another S3 bucket in a new Region and configure S3 Cross-Region Replication between the buckets Create an Amazon CloudFront distribution and configure origin failover with two origins accessing the S3 buckets in each Regio",
      "G": "Configure DynamoDB global tables by enabling Amazon DynamoDB Streams, and add a replica table in a new Region.",
      "H": "Create another S3 bucket in the same Region, and configure S3 Same-Region Replication between the buckets- Create an Amazon CloudFront distribution and configure origin failover with two origin accessing the S3 buckets Create a new DynamoDB table m a new Region Use the new table as a replica target for DynamoDB global tables. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "192",
    "question": "- (Exam Topic 2) An auction website enables users to bid on collectible items The auction rules require that each bid is processed only once and in the order it was received The current implementation is based on a fleet of Amazon EC2 web servers that write bid records into Amazon Kinesis Data Streams A single 12 large instance has a cron job that runs the bid processor, which reads incoming bids from Kinesis Data Streams and processes each bid The auction site is growing in popularity, but users are complaining that some bids are not registering Troubleshooting indicates that the bid processor is too slow during peak demand hours sometimes crashes while processing and occasionally loses track of which record is being processed What changes should make the bid processing more reliable? A. Refactor the web application to use the Amazon Kinesis Producer Library (KPL) when posting bids to Kinesis Data Streams Refactor the bid processor to flag each record in Kinesis Data Streams as being unread processing and processed At the start of each bid processing run; scan Kinesis Data Streams for unprocessed records B. Refactor the web application to post each incoming bid to an Amazon SNS topic in place of Kinesis Data Streams Configure the SNS topic to trigger an AWS Lambda function that C. processes each bid as soon as a user submits it D. Refactor the web application to post each incoming bid to an Amazon SQS FIFO queue in place of Kinesis Data Streams Refactor the bid processor to continuously consume the SQS queue Place the bid processing EC2 instance in an Auto Scaling group with a minimum and a maximum size of 1 E. Switch the EC2 instance type from t2 large to a larger general compute instance type Put the bid processor EC2 instances in an Auto Scaling group that scales out the number of EC2 instances running the bid processor based on the incomingRecords metric in Kinesis Data Streams -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Refactor the web application to use the Amazon Kinesis Producer Library (KPL) when posting bids to Kinesis Data Streams Refactor the bid processor to flag each record in Kinesis Data Streams as being unread processing and processed At the start of each bid processing run; scan Kinesis Data Streams for unprocessed records",
      "B": "Refactor the web application to post each incoming bid to an Amazon SNS topic in place of Kinesis Data Streams Configure the SNS topic to trigger an AWS Lambda function that",
      "C": "processes each bid as soon as a user submits it",
      "D": "Refactor the web application to post each incoming bid to an Amazon SQS FIFO queue in place of Kinesis Data Streams Refactor the bid processor to continuously consume the SQS queue Place the bid processing EC2 instance in an Auto Scaling group with a minimum and a maximum size of 1",
      "E": "Switch the EC2 instance type from t2 large to a larger general compute instance type Put the bid processor EC2 instances in an Auto Scaling group that scales out the number of EC2 instances running the bid processor based on the incomingRecords metric in Kinesis Data Streams -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "https://aws.amazon.com/sqs/faqs/#:~:text=A%20single%20Amazon%20SQS%20message,20%2C000%20for%2\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "135",
    "question": "- (Exam Topic 2) A retail company needs to provide a series of data files to another company. which is its business partner. These files are saved in an Amazon S3 bucket under Account A. which belongs to the retail company. The business partner company wants one of its IAM users User_DataProcessor to access the files from its own AWS account (Account B) Which combination of steps must the companies take so that User_DataProcessor can access the S3 bucket successfully? (Select TWO.) A. Turn on the cross-origin resource sharing (CORS) feature for the S3 bucket in Account A. B. In Account B set the S3 bucket policy to the following. { \"Effect\": \"Allow\", \"Action\": [ \"s3:GetObject\", \"s3:ListBucket\" ], \"Resource\": \"arn:aws:s3:::AccountABucketName/*\" } C. In Account A, set the S3 bucket policy to the following: { \"Effect\": \"Allow\", \"Principal\": { \"AWS\": \"arn:aws:iam::AccountB:user/User_DataProcessor\" }, \"Action\": [ \"s3:GetObject\", \"s3:ListBucket\" ], \"Resource\": [ \"arn:aws:s3:::AccountABucketName/*\" ] } D. InAccount B, set the permissions of User_DataProcessor to the following: { \"Effect\": \"Allow\", \"Principal\": { \"AWS\": \"arn:aws:iam::AccountB:user/User_DataProcessor\" }, \"Action\": [ \"s3:GetObject\", \"s3:ListBucket\" ], \"Resource\": [ \"arn:aws:s3:::AccountABucketName/*\" ] } E. InAccount B, set the permissions of User_DataProcessor to the following: { \"Effect\": \"Allow\", \"Principal\": { \"AWS\": \"arn:aws:iam::AccountB:user/User_DataProcessor\" }, \"Action\": [ \"s3:GetObject\", \"s3:ListBucket\" ], \"Resource\": [ \"arn:aws:s3:::AccountABucketName/*\" ] } -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Turn on the cross-origin resource sharing (CORS) feature for the S3 bucket in Account A.",
      "B": "In Account B set the S3 bucket policy to the following. { \"Effect\": \"Allow\", \"Action\": [ \"s3:GetObject\", \"s3:ListBucket\" ], \"Resource\": \"arn:aws:s3:::AccountABucketName/*\" }",
      "C": "In Account A, set the S3 bucket policy to the following: { \"Effect\": \"Allow\", \"Principal\": { \"AWS\": \"arn:aws:iam::AccountB:user/User_DataProcessor\" }, \"Action\": [ \"s3:GetObject\", \"s3:ListBucket\" ], \"Resource\": [ \"arn:aws:s3:::AccountABucketName/*\" ] }",
      "D": "InAccount B, set the permissions of User_DataProcessor to the following: { \"Effect\": \"Allow\", \"Principal\": { \"AWS\": \"arn:aws:iam::AccountB:user/User_DataProcessor\" }, \"Action\": [ \"s3:GetObject\", \"s3:ListBucket\" ], \"Resource\": [ \"arn:aws:s3:::AccountABucketName/*\" ] }",
      "E": "InAccount B, set the permissions of User_DataProcessor to the following: { \"Effect\": \"Allow\", \"Principal\": { \"AWS\": \"arn:aws:iam::AccountB:user/User_DataProcessor\" }, \"Action\": [ \"s3:GetObject\", \"s3:ListBucket\" ], \"Resource\": [ \"arn:aws:s3:::AccountABucketName/*\" ] } -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "D"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "137",
    "question": "- (Exam Topic 2) During an audit, a security team discovered that a development team was putting IAM user secret access keys in their code and then committing it to an AWS CodeCommit repository . The security team wants to automatically find and remediate instances of this security vulnerability Which solution will ensure that the credentials are appropriately secured automatically? A. Run a script nightly using AWS Systems Manager Run Command to search for credentials on the development instances If found use AWS Secrets Manager to rotate the credentials. B. Use a scheduled AWS Lambda function to download and scan the application code from CodeCommit If credentials are found, generate new credentials and store them in AWS KMS C. Configure Amazon Macie to scan for credentials in CodeCommit repositories If credentials are found, trigger an AWS Lambda function to disable the credentials and notify the user D. Configure a CodeCommit trigger to invoke an AWS Lambda function to scan new code submissions for credentials If credentials are found, disable them in AWS IAM and notify the user. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Run a script nightly using AWS Systems Manager Run Command to search for credentials on the development instances If found use AWS Secrets Manager to rotate the credentials.",
      "B": "Use a scheduled AWS Lambda function to download and scan the application code from CodeCommit If credentials are found, generate new credentials and store them in AWS KMS",
      "C": "Configure Amazon Macie to scan for credentials in CodeCommit repositories If credentials are found, trigger an AWS Lambda function to disable the credentials and notify the user",
      "D": "Configure a CodeCommit trigger to invoke an AWS Lambda function to scan new code submissions for credentials If credentials are found, disable them in AWS IAM and notify the user. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "141",
    "question": "- (Exam Topic 2) A solutions architect is designing a solution to connect a company's on-premises network with all the company's current and future VPCs on AWS The company is running VPCs in five different AWS Regions and has at least 15 VPCs in each Region. The company's AWS usage is constantly increasing and will continue to grow Additionally, all the VPCs throughout all five Regions must be able to communicate with each other The solution must maximize scalability and ease of management Which solution meets these requirements'? A. Set up a transit gateway in each Region Establish a redundant AWS Site-to-Site VPN connection between the on-premises firewalls and the transit gateway in the Region that is closest to theon-premises network Peer all the transit gateways with each other Connect all the VPCs to the transitgateway in their Region B. Create an AWS CloudFormation template for a redundant AWS Site-to-Site VPN tunnel to theon-premises network Deploy the CloudFormation template for each VPC Set up VPC peering between all the VPCs for VPC-to-VPC communication C. Set up a transit gateway in each Region Establish a redundant AWS Site-to-Site VPN connection between the on-premises firewalls and each transit gateway Route traffic between the different Regions through the company's on-premises firewalls Connect all the VPCs to the transit gateway in their Region D. Create an AWS CloudFormation template for a redundant AWS Site-to-Site VPN tunnel to theon-premises network Deploy the CloudFormation template for each VPC Route traffic between the different Regions through the company's on-premises firewalls -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Set up a transit gateway in each Region Establish a redundant AWS Site-to-Site VPN connection between the on-premises firewalls and the transit gateway in the Region that is closest to theon-premises network Peer all the transit gateways with each other Connect all the VPCs to the transitgateway in their Region",
      "B": "Create an AWS CloudFormation template for a redundant AWS Site-to-Site VPN tunnel to theon-premises network Deploy the CloudFormation template for each VPC Set up VPC peering between all the VPCs for VPC-to-VPC communication",
      "C": "Set up a transit gateway in each Region Establish a redundant AWS Site-to-Site VPN connection between the on-premises firewalls and each transit gateway Route traffic between the different Regions through the company's on-premises firewalls Connect all the VPCs to the transit gateway in their Region",
      "D": "Create an AWS CloudFormation template for a redundant AWS Site-to-Site VPN tunnel to theon-premises network Deploy the CloudFormation template for each VPC Route traffic between the different Regions through the company's on-premises firewalls -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "145",
    "question": "- (Exam Topic 2) A solutions architect is importing a VM from an on-premises environment by using the Amazon EC2 VM Import feature of AWS Import/Export The solutions architect has created an AMI and has provisioned an Amazon EC2 instance that is based on that AMI The EC2 instance runs inside a public subnet in a VPC and has a public IP address assigned The EC2 instance does not appear as a managed instance in the AWS Systems Manager console Which combination of steps should the solutions architect take to troubleshoot this issue\"? (Select TWO ) A. Verify that Systems Manager Agent is installed on the instance and is running B. Verify that the instance is assigned an appropriate IAM role for Systems Manager C. Verify the existence of a VPC endpoint on the VPC D. Verify that the AWS Application Discovery Agent is configured E. Verify the correct configuration of service-linked roles for Systems Manager -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Verify that Systems Manager Agent is installed on the instance and is running",
      "B": "Verify that the instance is assigned an appropriate IAM role for Systems Manager",
      "C": "Verify the existence of a VPC endpoint on the VPC",
      "D": "Verify that the AWS Application Discovery Agent is configured",
      "E": "Verify the correct configuration of service-linked roles for Systems Manager -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "B",
      "D"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "194",
    "question": "- (Exam Topic 2) A company uses AWS Organizations to manage more than 1.000 AWS accounts. The company has created a new developer organization. There are 540 developer member accounts that must be moved to the new developer organization All accounts are set up with all the required Information so mat each account can be operated as a standalone account Which combination of steps should a solutions architect take to move all of the developer accounts to the new developer organization? (Select THREE ) A. Call the MoveAccount operation In the Organizations API from the old organization's management account to migrate the developer accounts to the new developer organization B. From the management account remove each developer account from the old organization using the RemoveAccountFromOrganization operation in the Organizations API C. From each developer account, remove the account from the old organization using the RemoveAccounrFromOrganization operation in the Organizations API D. Sign in to the new developer organization's management account and create a placeholder member account that acts as a target for the developer account migration E. Call the InviteAccountToOrganzation operation in the Organizations API from the new developer organization's management account to send invitations to the developer accounts. F. Have each developer sign in to their account and confirm to join the new developer organization. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Call the MoveAccount operation In the Organizations API from the old organization's management account to migrate the developer accounts to the new developer organization",
      "B": "From the management account remove each developer account from the old organization using the RemoveAccountFromOrganization operation in the Organizations API",
      "C": "From each developer account, remove the account from the old organization using the RemoveAccounrFromOrganization operation in the Organizations API",
      "D": "Sign in to the new developer organization's management account and create a placeholder member account that acts as a target for the developer account migration",
      "E": "Call the InviteAccountToOrganzation operation in the Organizations API from the new developer organization's management account to send invitations to the developer accounts.",
      "F": "Have each developer sign in to their account and confirm to join the new developer organization. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "D",
      "E"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "198",
    "question": "- (Exam Topic 2) A mobile gaming company is expanding into the global market. The company's game servers run in the us-east-1 Region. The game's client application uses UDP to communicate with the game servers and needs to be able to connect to a set of static IP addresses. The company wants its game to be accessible on multiple continents. The company also wants the game to maintain its network performance and global availability. Which solution meets these requirements? A. Provision an Application Load Balancer (ALB) in front of the game servers Create an Amazon CloudFront distribution that has no geographical restrictions Set the ALB as the origin Perform DNS lookups for the cloudfront net domain name Use the resulting IP addresses in the game's client application. B. Provision game servers in each AWS Regio C. Provision an Application Load Balancer in front of the game server D. Create an Amazon Route 53 latency-based routing policy for the game's client application to use with DNS lookups E. Provision game servers in each AWS Region Provision a Network Load Balancer (NLB) in front of the game servers Create an accelerator in AWS Global Accelerator, and configure endpoint groups in each Region Associate the NLBs with the corresponding Regional endpoint groups Point the game client's application to the Global Accelerator endpoints F. Provision game servers in each AWS Region Provision a Network Load Balancer (NLB) in front of the game servers Create an Amazon CloudFront distribution that has no geographical restrictions Set the NLB as the origin Perform DNS lookups for the cloudfront net domain nam G. Use the resulting IP addresses in the game's client application -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Provision an Application Load Balancer (ALB) in front of the game servers Create an Amazon CloudFront distribution that has no geographical restrictions Set the ALB as the origin Perform DNS lookups for the cloudfront net domain name Use the resulting IP addresses in the game's client application.",
      "B": "Provision game servers in each AWS Regio",
      "C": "Provision an Application Load Balancer in front of the game server",
      "D": "Create an Amazon Route 53 latency-based routing policy for the game's client application to use with DNS lookups",
      "E": "Provision game servers in each AWS Region Provision a Network Load Balancer (NLB) in front of the game servers Create an accelerator in AWS Global Accelerator, and configure endpoint groups in each Region Associate the NLBs with the corresponding Regional endpoint groups Point the game client's application to the Global Accelerator endpoints",
      "F": "Provision game servers in each AWS Region Provision a Network Load Balancer (NLB) in front of the game servers Create an Amazon CloudFront distribution that has no geographical restrictions Set the NLB as the origin Perform DNS lookups for the cloudfront net domain nam",
      "G": "Use the resulting IP addresses in the game's client application -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "202",
    "question": "- (Exam Topic 2) A company has automated the nightly retraining ot its machine learning models by using AWS Step Functions. The workflow consists of multiple steps that use AWS Lambda. Each step can fail for various reasons, and any failure causes a failure of the overall workflow. A review reveals that the retraining has failed multiple nights in a row without the company noticing the failure. A solutions architect needs to improve the workflow so that notifications are sent for all types of failures in the retraining process. Which combination of steps should the solutions architect take to meet these requirements? (Select THREE.) A. Create an Amazon Simple Notification Service {Amazon SNS) topic with a subscription of type\"Email\" that targets the team's mailing list. B. Create a task named \"Email\" that forwards the input arguments to the SNS topic C. Add a Catch field to all Tas D. Ma E. and Parallel states that have a statement of \"ErrorEquals\": [ \"states.all\" ] and \"Next\": \"Email\". F. Add a new email address to Amazon Simple Email Service (Amazon SES). Verify the email address. G. Create a task named \"Email\" that forwards the input arguments to the SES email address H. Add a Catch field to all Task, Map, and Parallel states that have a statement of \"ErrorEquals\": [ \"states.Bun time\" ] and \"Next\": \"Email\". -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an Amazon Simple Notification Service {Amazon SNS) topic with a subscription of type\"Email\" that targets the team's mailing list.",
      "B": "Create a task named \"Email\" that forwards the input arguments to the SNS topic",
      "C": "Add a Catch field to all Tas",
      "D": "Ma",
      "E": "and Parallel states that have a statement of \"ErrorEquals\": [ \"states.all\" ] and \"Next\": \"Email\".",
      "F": "Add a new email address to Amazon Simple Email Service (Amazon SES). Verify the email address.",
      "G": "Create a task named \"Email\" that forwards the input arguments to the SES email address",
      "H": "Add a Catch field to all Task, Map, and Parallel states that have a statement of \"ErrorEquals\": [ \"states.Bun time\" ] and \"Next\": \"Email\". -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "C",
      "D"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "207",
    "question": "- (Exam Topic 2) A company is refactoring its on-premises order-processing platform in the AWS Cloud. The platform includes a web front end that is hosted on a fleet of VMs RabbitMQ to connect the front end to the backend, and a Kubernetes cluster to run a containerized backend system to process the orders. The company does not want to make any major changes to the application Which solution will meet these requirements with the LEAST operational overhead? A. Create an AMI of the web server VM Create an Amazon EC2 Auto Scaling group that uses the AMI and an Application Load Balancer Set up Amazon MQ to replace the on-premises messaging queue Configure Amazon Elastic Kubernetes Service (Amazon EKS) to host the order-processing backend B. Create a custom AWS Lambda runtime to mimic the web server environment Create an Amazon API Gateway API to replace the front-end web servers Set up Amazon MQ to replace the on-premises messaging queue Configure Amazon Elastic Kubernetes Service (Amazon EKS) to host theorder-processing backend C. Create an AMI of the web server VM Create an Amazon EC2 Auto Scaling group that uses the AMI and an Application Load Balancer Set up Amazon MQ to replace the on-premises messaging queue Install Kubernetes on a fleet of different EC2 instances to host the order-processing backend D. Create an AMI of the web server VM Create an Amazon EC2 Auto Scaling group that uses the AMI and an Application Load Balancer Set up an Amazon Simple Queue Service (Amazon SQS) queue to replace the on-premises messaging queue Configure Amazon Elastic Kubernetes Service (Amazon EKS) to host the order-processing backend -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an AMI of the web server VM Create an Amazon EC2 Auto Scaling group that uses the AMI and an Application Load Balancer Set up Amazon MQ to replace the on-premises messaging queue Configure Amazon Elastic Kubernetes Service (Amazon EKS) to host the order-processing backend",
      "B": "Create a custom AWS Lambda runtime to mimic the web server environment Create an Amazon API Gateway API to replace the front-end web servers Set up Amazon MQ to replace the on-premises messaging queue Configure Amazon Elastic Kubernetes Service (Amazon EKS) to host theorder-processing backend",
      "C": "Create an AMI of the web server VM Create an Amazon EC2 Auto Scaling group that uses the AMI and an Application Load Balancer Set up Amazon MQ to replace the on-premises messaging queue Install Kubernetes on a fleet of different EC2 instances to host the order-processing backend",
      "D": "Create an AMI of the web server VM Create an Amazon EC2 Auto Scaling group that uses the AMI and an Application Load Balancer Set up an Amazon Simple Queue Service (Amazon SQS) queue to replace the on-premises messaging queue Configure Amazon Elastic Kubernetes Service (Amazon EKS) to host the order-processing backend -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "175.2",
    "question": "- (Exam Topic 2) A company is currently using AWS CodeCommit for its source control and AWS CodePipeline for continuous integration The pipeline has a build stage for building the artifacts, which is then staged in an Amazon S3 bucket. The company has identified various improvement opportunities in the existing process and a solutions architect has been given the following requirements • Create a new pipeline to support feature development • Support feature development without impacting production applications • Incorporate continuous testing with unit tests • Isolate development and production artifacts • Support the capability to merge tested code into production code How should the solutions architect achieve these requirements? A. Trigger a separate pipeline from CodeCommit feature branches Use AWS CodeBuild for running unit tests Use CodeBuild to stage the artifacts within an S3 bucket in a separate testing account B. Trigger a separate pipeline from CodeCommit feature branches Use AWS Lambda for running unit tests Use AWS CodeDeploy to stage the artifacts within an S3 bucket in a separate testing account C. Trigger a separate pipeline from CodeCommit tags Use Jenkins for running unit tests Create a stage in the pipeline with S3 as the target for staging the artifacts within an S3 bucket in a separate testing account. D. Create a separate CodeCommit repository for feature development and use it to trigger the pipeline Use AWS Lambda for running unit tests Use AWS CodeBuild to stage the artifacts within different S3 buckets in the same production account -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Trigger a separate pipeline from CodeCommit feature branches Use AWS CodeBuild for running unit tests Use CodeBuild to stage the artifacts within an S3 bucket in a separate testing account",
      "B": "Trigger a separate pipeline from CodeCommit feature branches Use AWS Lambda for running unit tests Use AWS CodeDeploy to stage the artifacts within an S3 bucket in a separate testing account",
      "C": "Trigger a separate pipeline from CodeCommit tags Use Jenkins for running unit tests Create a stage in the pipeline with S3 as the target for staging the artifacts within an S3 bucket in a separate testing account.",
      "D": "Create a separate CodeCommit repository for feature development and use it to trigger the pipeline Use AWS Lambda for running unit tests Use AWS CodeBuild to stage the artifacts within different S3 buckets in the same production account -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "179.2",
    "question": "- (Exam Topic 2) A company is migrating an on-premises content management system (CMS) to AWS Fargate. The company uses the CMS for blog posts that include text, images, and videos. The company has observed that traffic to blog posts drops by more than 80% after the posts are more than 30 days old The CMS runs on multiple VMs and stores application state on disk This application state is shared across all instances across multiple Availability Zones Images and other media are stored on a separate NFS file share. The company needs to reduce the costs of the existing solution while minimizing the impact on performance. Which combination of steps will meet these requirements MOST cost-effectively? (Select TWO.) A. Store media in an Amazon S3 Standard bucket Create an S3 Lifecycle configuration that transitions objects that are older than 30 days to the S3 Standard- Infrequent Access (S3 Standard-IA) storage class. B. Store media on an Amazon Elastic File System (Amazon EFS) volume Attach the EFS volume to all Fargate instances. C. Store application state on an Amazon Elastic File System (Amazon EFS) volume Attach the EFS volume to all Fargate instances. D. Store application state on an Amazon Elastic Block Store (Amazon EBS) volume Attach the EBS volume to all Fargate instances. E. Store media in an Amazon S3 Standard bucket Create an S3 Lifecycle configuration that transitions objects that are older than 30 days to the S3 Glacier storage class -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Store media in an Amazon S3 Standard bucket Create an S3 Lifecycle configuration that transitions objects that are older than 30 days to the S3 Standard- Infrequent Access (S3 Standard-IA) storage class.",
      "B": "Store media on an Amazon Elastic File System (Amazon EFS) volume Attach the EFS volume to all Fargate instances.",
      "C": "Store application state on an Amazon Elastic File System (Amazon EFS) volume Attach the EFS volume to all Fargate instances.",
      "D": "Store application state on an Amazon Elastic Block Store (Amazon EBS) volume Attach the EBS volume to all Fargate instances.",
      "E": "Store media in an Amazon S3 Standard bucket Create an S3 Lifecycle configuration that transitions objects that are older than 30 days to the S3 Glacier storage class -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "180.2",
    "question": "- (Exam Topic 2) A medical company is running an application in the AWS Cloud. The application simulates the effect of medical drugs in development. The application consists of two parts configuration and simulation The configuration part runs in AWS Fargate containers in an Amazon Elastic Container Service (Amazon ECS) cluster. The simulation part runs on large, compute optimized Amazon EC2 instances Simulations can restart if they are interrupted The configuration part runs 24 hours a day with a steady load. The simulation part runs only for a few hours each night with a variable load. The company stores simulation results in Amazon S3, and researchers use the results for 30 days. The company must store simulations for 10 years and must be able to retrieve the simulations within 5 hours Which solution meets these requirements MOST cost-effectively? A. Purchase an EC2 Instance Savings Plan to cover the usage for the configuration part Run the simulation part by using EC2 Spot Instances Create an S3 Lifecycle policy to transition objects that are older than 30 days to S3 Intelligent-Tiering B. Purchase an EC2 Instance Savings Plan to cover the usage for the configuration part and the simulation part Create an S3 Lifecycle policy to transition objects that are older than 30 days to S3 Glacier C. Purchase Compute Savings Plans to cover the usage for the configuration part Run the simulation part by using EC2 Spot instances Create an S3 Lifecycle policy to transition objects that are older than 30 days to S3 Glacier D. Purchase Compute Savings Plans to cover the usage for the configuration part Purchase EC2 Reserved Instances for the simulation part Create an S3 Lifecycle policy to transition objects that are older than 30 days to S3 Glacier Deep Archive -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Purchase an EC2 Instance Savings Plan to cover the usage for the configuration part Run the simulation part by using EC2 Spot Instances Create an S3 Lifecycle policy to transition objects that are older than 30 days to S3 Intelligent-Tiering",
      "B": "Purchase an EC2 Instance Savings Plan to cover the usage for the configuration part and the simulation part Create an S3 Lifecycle policy to transition objects that are older than 30 days to S3 Glacier",
      "C": "Purchase Compute Savings Plans to cover the usage for the configuration part Run the simulation part by using EC2 Spot instances Create an S3 Lifecycle policy to transition objects that are older than 30 days to S3 Glacier",
      "D": "Purchase Compute Savings Plans to cover the usage for the configuration part Purchase EC2 Reserved Instances for the simulation part Create an S3 Lifecycle policy to transition objects that are older than 30 days to S3 Glacier Deep Archive -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "210",
    "question": "- (Exam Topic 2) A solutions architect wants to make sure that only AWS users or roles with suitable permissions can access a new Amazon API Gateway endpoint The solutions architect wants an end-to-end view of each request to analyze the latency of the request and create service maps How can the solutions architect design the API Gateway access control and perform request inspections'' A. For the API Gateway method, set the authorization to AWSJAM Then, give the IAM user or role execute-api Invoke permission on the REST API resource Enable the API caller to sign requests with AWS Signature when accessing the endpoint Use AWS X-Ray to trace and analyze user requests to APIGateway B. For the API Gateway resource set CORS to enabled and only return the company's domain inAccess-Control-Allow-Origin headers Then give the IAM user or role execute-api Invoke permission on the REST API resource Use Amazon CloudWatch to trace and analyze user requests to API Gateway C. Create an AWS Lambda function as the custom authorizer ask the API client to pass the key and secret when making the call, and then use Lambda to validate the key/secret pair against the IAM system Use AWS X-Ray to trace and analyze user requests to API Gateway D. Create a client certificate for API Gateway Distribute the certificate to the AWS users and roles that need to access the endpoint Enable the API caller to pass the client certificate when accessing the endpoin E. Use Amazon CloudWatch to trace and analyze user requests to API Gateway. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "For the API Gateway method, set the authorization to AWSJAM Then, give the IAM user or role execute-api Invoke permission on the REST API resource Enable the API caller to sign requests with AWS Signature when accessing the endpoint Use AWS X-Ray to trace and analyze user requests to APIGateway",
      "B": "For the API Gateway resource set CORS to enabled and only return the company's domain inAccess-Control-Allow-Origin headers Then give the IAM user or role execute-api Invoke permission on the REST API resource Use Amazon CloudWatch to trace and analyze user requests to API Gateway",
      "C": "Create an AWS Lambda function as the custom authorizer ask the API client to pass the key and secret when making the call, and then use Lambda to validate the key/secret pair against the IAM system Use AWS X-Ray to trace and analyze user requests to API Gateway",
      "D": "Create a client certificate for API Gateway Distribute the certificate to the AWS users and roles that need to access the endpoint Enable the API caller to pass the client certificate when accessing the endpoin",
      "E": "Use Amazon CloudWatch to trace and analyze user requests to API Gateway. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "2.2",
    "question": "- (Exam Topic 1) A company is running an application distributed over several Amazon EC2 instances in an Auto Scaling group behind an Application Load Balancer The security team requires that all application access attempts be made available for analysis Information about the client IP address, connection type, and user agent must be included. Which solution will meet these requirements? A. Enable EC2 detailed monitoring, and include network logs Send all logs through Amazon Kinesis Data Firehose to an Amazon ElasDcsearch Service (Amazon ES) cluster that the security team uses for analysis. B. Enable VPC Flow Logs for all EC2 instance network interfaces Publish VPC Flow Logs to an Amazon S3 bucket Have the security team use Amazon Athena to query and analyze the logs C. Enable access logs for the Application Load Balancer, and publish the logs to an Amazon S3 bucket Have the security team use Amazon Athena to query and analyze the logs D. Enable Traffic Mirroring and specify all EC2 instance network interfaces as the sourc E. Send all traffic information through Amazon Kinesis Data Firehose to an Amazon Elastic search Service (Amazon ES) cluster that the security team uses for analysis. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Enable EC2 detailed monitoring, and include network logs Send all logs through Amazon Kinesis Data Firehose to an Amazon ElasDcsearch Service (Amazon ES) cluster that the security team uses for analysis.",
      "B": "Enable VPC Flow Logs for all EC2 instance network interfaces Publish VPC Flow Logs to an Amazon S3 bucket Have the security team use Amazon Athena to query and analyze the logs",
      "C": "Enable access logs for the Application Load Balancer, and publish the logs to an Amazon S3 bucket Have the security team use Amazon Athena to query and analyze the logs",
      "D": "Enable Traffic Mirroring and specify all EC2 instance network interfaces as the sourc",
      "E": "Send all traffic information through Amazon Kinesis Data Firehose to an Amazon Elastic search Service (Amazon ES) cluster that the security team uses for analysis. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "1.2",
    "question": "- (Exam Topic 1) A startup company recently migrated a large ecommerce website to AWS. The website has experienced a 70% increase in sales. Software engineers are using a private GitHub repository to manage code. The DevOps learn is using Jenkins for builds and unit testing. The engineers need to receive notifications for bad builds and zero downtime during deployments. The engineers also need to ensure any changes to production are seamless for users and can be rolled back in the event of a major issue. The software engineers have decided to use AWS CodePipeline to manage their build and deployment process. Which solution will meet these requirements? A. Use GitHub websockets to trigger the CodePipeline pipelin B. Use the Jenkins plugin for AWS CodeBuild to conduct unit testin C. Send alerts to an Amazon SNS topic for any bad build D. Deploy in an in-plac E. all-at-once deployment configuration using AWS CodeDeploy. F. Use GitHub webhooks to trigger the CodePipeline pipelin G. Use the Jenkins plugin for AWS CodeBuild to conduct unit testin H. Send alerts to an Amazon SNS topic for any bad build I. Deploy in a blue/green deployment using AWS CodeDeploy. J. Use GitHub websockets to trigger the CodePipeline pipelin K. Use AWS X-Ray for unit testing and static code analysi L. Send alerts to an Amazon SNS topic for any bad build M. Deploy in a blue/green deployment using AWS CodeDeploy. N. Use GitHub webhooks to trigger the CodePipeline pipelin O. Use AWS X-Ray for unit testing and static code analysi P. Send alerts to an Amazon SNS topic for any bad build Q. Deploy in an in-place, all-at-once deployment configuration using AWS CodeDeploy. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use GitHub websockets to trigger the CodePipeline pipelin",
      "B": "Use the Jenkins plugin for AWS CodeBuild to conduct unit testin",
      "C": "Send alerts to an Amazon SNS topic for any bad build",
      "D": "Deploy in an in-plac",
      "E": "all-at-once deployment configuration using AWS CodeDeploy.",
      "F": "Use GitHub webhooks to trigger the CodePipeline pipelin",
      "G": "Use the Jenkins plugin for AWS CodeBuild to conduct unit testin",
      "H": "Send alerts to an Amazon SNS topic for any bad build",
      "I": "Deploy in a blue/green deployment using AWS CodeDeploy.",
      "J": "Use GitHub websockets to trigger the CodePipeline pipelin K. Use AWS X-Ray for unit testing and static code analysi L. Send alerts to an Amazon SNS topic for any bad build M. Deploy in a blue/green deployment using AWS CodeDeploy. N. Use GitHub webhooks to trigger the CodePipeline pipelin O. Use AWS X-Ray for unit testing and static code analysi P. Send alerts to an Amazon SNS topic for any bad build Q. Deploy in an in-place, all-at-once deployment configuration using AWS CodeDeploy. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "3.2",
    "question": "- (Exam Topic 1) A financial services company logs personally identifiable information 10 its application logs stored in Amazon S3. Due to regulatory compliance requirements, the log files must be encrypted at rest. The security team has mandated that the company's on-premises hardware security modules (HSMs) be used to generate the CMK material. Which steps should the solutions architect take to meet these requirements? A. Create an AWS CloudHSM cluste B. Create a new CMK in AWS KMS using AWS_CloudHSM as the source (or the key material and an origin of AWS_CLOUDHS C. Enable automatic key rotation on the CMK with a duration of 1 yea D. Configure a bucket policy on the togging bucket thai disallows uploads of unencrypted data and requires that the encryption source be AWS KMS. E. Provision an AWS Direct Connect connection, ensuring there is no overlap of the RFC 1918 address space between on-premises hardware and the VPC F. Configure an AWS bucket policy on the logging bucket that requires all objects to be encrypte G. Configure the logging application to query theon-premises HSMs from the AWS environment for the encryption key material, and create a unique CMK for each logging event. H. Create a CMK in AWS KMS with no key material and an origin of EXTERNA I. Import the key material generated from the on-premises HSMs into the CMK using the public key and import token provided by AW J. Configure a bucket policy on the logging bucket that disallows uploads ofnon-encrypted data and requires that the encryption source be AWS KMS. K. Create a new CMK in AWS KMS with AWS-provided key material and an origin of AWS_KM L. Disable this CM M. and overwrite the key material with the key material from the on-premises HSM using the public key and import token provided by AW N. Re-enable the CM O. Enable automatic key rotation on the CMK with a duration of 1 yea P. Configure a bucket policy on the logging bucket that disallows uploads of non-encrypted data and requires that the encryption source be AWS KMS. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an AWS CloudHSM cluste",
      "B": "Create a new CMK in AWS KMS using AWS_CloudHSM as the source (or the key material and an origin of AWS_CLOUDHS",
      "C": "Enable automatic key rotation on the CMK with a duration of 1 yea",
      "D": "Configure a bucket policy on the togging bucket thai disallows uploads of unencrypted data and requires that the encryption source be AWS KMS.",
      "E": "Provision an AWS Direct Connect connection, ensuring there is no overlap of the RFC 1918 address space between on-premises hardware and the VPC",
      "F": "Configure an AWS bucket policy on the logging bucket that requires all objects to be encrypte",
      "G": "Configure the logging application to query theon-premises HSMs from the AWS environment for the encryption key material, and create a unique CMK for each logging event.",
      "H": "Create a CMK in AWS KMS with no key material and an origin of EXTERNA",
      "I": "Import the key material generated from the on-premises HSMs into the CMK using the public key and import token provided by AW",
      "J": "Configure a bucket policy on the logging bucket that disallows uploads ofnon-encrypted data and requires that the encryption source be AWS KMS. K. Create a new CMK in AWS KMS with AWS-provided key material and an origin of AWS_KM L. Disable this CM M. and overwrite the key material with the key material from the on-premises HSM using the public key and import token provided by AW N. Re-enable the CM O. Enable automatic key rotation on the CMK with a duration of 1 yea P. Configure a bucket policy on the logging bucket that disallows uploads of non-encrypted data and requires that the encryption source be AWS KMS. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "https://aws.amazon.com/blogs/security/how-to-byok-bring-your-own-key-to-aws-kms-for-less-than-15-00-a-yea\nhttps://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-create-cmk.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "4.2",
    "question": "- (Exam Topic 1) An enterprise runs 103 line-of-business applications on virtual machines in an on-premises data center. Many of the applications are simple PHP. Java, or Ruby web applications, are no longer actively developed, and serve little traffic. Which approach should be used to migrate these applications to AWS with the LOWEST infrastructure costs? A. Deploy the applications lo single-instance AWS Elastic Beanstalk environments without a load balancer. B. Use AWS SMS to create AMls for each virtual machine and run them in Amazon EC2. C. Convert each application to a Docker image and deploy to a small Amazon ECS cluster behind an Application Load Balancer. D. Use VM Import/Export to create AMls for each virtual machine and run them in single-instance AWS Elastic Beanstalk environments by configuring a custom image. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy the applications lo single-instance AWS Elastic Beanstalk environments without a load balancer.",
      "B": "Use AWS SMS to create AMls for each virtual machine and run them in Amazon EC2.",
      "C": "Convert each application to a Docker image and deploy to a small Amazon ECS cluster behind an Application Load Balancer.",
      "D": "Use VM Import/Export to create AMls for each virtual machine and run them in single-instance AWS Elastic Beanstalk environments by configuring a custom image. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "5.2",
    "question": "- (Exam Topic 1) A company has an application that sells tickets online and experiences bursts of demand every 7 days. The application has a stateless presentation layer running on Amazon EC2. an Oracle database to store unstructured data catalog information, and a backend API layer. The front-end layer uses an Elastic Load Balancer to distribute the load across nine On-Demand Instances over three Availability Zones (AZs). The Oracle database is running on a single EC2 instance. The company is experiencing performance issues when running more than two concurrent campaigns. A solutions architect must design a solution that meets the following requirements: • Address scalability issues. • Increase the level of concurrency. • Eliminate licensing costs. • Improve reliability. Which set of steps should the solutions architect take? A. Create an Auto Scaling group for the front end with a combination of On-Demand and Spot Instances to reduce cost B. Convert the Oracle database into a single Amazon RDS reserved DB instance. C. Create an Auto Scaling group for the front end with a combination of On-Demand and Spot Instances to reduce cost D. Create two additional copies of the database instance, then distribute the databases in separate AZs. E. Create an Auto Scaling group for the front end with a combination of On-Demand and Spot Instances to reduce cost F. Convert the tables in the Oracle database into Amazon DynamoDB tables. G. Convert the On-Demand Instances into Spot Instances to reduce costs for the front en H. Convert the tables in the Oracle database into Amazon DynamoDB tables. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an Auto Scaling group for the front end with a combination of On-Demand and Spot Instances to reduce cost",
      "B": "Convert the Oracle database into a single Amazon RDS reserved DB instance.",
      "C": "Create an Auto Scaling group for the front end with a combination of On-Demand and Spot Instances to reduce cost",
      "D": "Create two additional copies of the database instance, then distribute the databases in separate AZs.",
      "E": "Create an Auto Scaling group for the front end with a combination of On-Demand and Spot Instances to reduce cost",
      "F": "Convert the tables in the Oracle database into Amazon DynamoDB tables.",
      "G": "Convert the On-Demand Instances into Spot Instances to reduce costs for the front en",
      "H": "Convert the tables in the Oracle database into Amazon DynamoDB tables. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "Combination of On-Demand and Spot Instances + DynamoDB.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "6.2",
    "question": "- (Exam Topic 1) A company wants to deploy an AWS WAF solution to manage AWS WAF rules across multiple AWS accounts. The accounts are managed under different OUs in AWS Organizations. Administrators must be able to add or remove accounts or OUs from managed AWS WAF rule sets as needed Administrators also must have the ability to automatically update and remediate noncompliant AWS WAF rules in all accounts Which solution meets these requirements with the LEAST amount of operational overhead? A. Use AWS Firewall Manager to manage AWS WAF rules across accounts in the organizatio B. Use an AWS Systems Manager Parameter Store parameter to store account numbers and OUs to manage Update the parameter as needed to add or remove accounts or OUs Use an Amazon EventBridge (Amazon CloudWatch Events) rule to identify any changes to the parameter and to invoke an AWS Lambda function to update the security policy in the Firewall Manager administrative account C. Deploy an organization-wide AWS Config rule that requires all resources in the selected OUs to associate the AWS WAF rule D. Deploy automated remediation actions by using AWS Lambda to fix noncompliant resources Deploy AWS WAF rules by using an AWS CloudFormation stack set to target the same OUs where the AWS Config rule is applied. E. Create AWS WAF rules in the management account of the organization Use AWS Lambda environment variables to store account numbers and OUs to manage Update environment variables as needed to add or remove accounts or OUs Create cross-account IAM roles in member accounts Assume the rotes by using AWS Security Token Service (AWS STS) in the Lambda function to create and update AWS WAF rules in the member accounts. F. Use AWS Control Tower to manage AWS WAF rules across accounts in the organization Use AWS Key Management Service (AWS KMS) to store account numbers and OUs to manage Update AWS KMS as needed to add or remove accounts or OUs Create IAM users in member accounts Allow AWS Control Tower in the management account to use the access key and secret access key to create and update AWS WAF rules in the member accounts -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS Firewall Manager to manage AWS WAF rules across accounts in the organizatio",
      "B": "Use an AWS Systems Manager Parameter Store parameter to store account numbers and OUs to manage Update the parameter as needed to add or remove accounts or OUs Use an Amazon EventBridge (Amazon CloudWatch Events) rule to identify any changes to the parameter and to invoke an AWS Lambda function to update the security policy in the Firewall Manager administrative account",
      "C": "Deploy an organization-wide AWS Config rule that requires all resources in the selected OUs to associate the AWS WAF rule",
      "D": "Deploy automated remediation actions by using AWS Lambda to fix noncompliant resources Deploy AWS WAF rules by using an AWS CloudFormation stack set to target the same OUs where the AWS Config rule is applied.",
      "E": "Create AWS WAF rules in the management account of the organization Use AWS Lambda environment variables to store account numbers and OUs to manage Update environment variables as needed to add or remove accounts or OUs Create cross-account IAM roles in member accounts Assume the rotes by using AWS Security Token Service (AWS STS) in the Lambda function to create and update AWS WAF rules in the member accounts.",
      "F": "Use AWS Control Tower to manage AWS WAF rules across accounts in the organization Use AWS Key Management Service (AWS KMS) to store account numbers and OUs to manage Update AWS KMS as needed to add or remove accounts or OUs Create IAM users in member accounts Allow AWS Control Tower in the management account to use the access key and secret access key to create and update AWS WAF rules in the member accounts -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "8.2",
    "question": "- (Exam Topic 1) A company has an Amazon VPC that is divided into a public subnet and a pnvate subnet. A web application runs in Amazon VPC. and each subnet has its own NACL The public subnet has a CIDR of 10.0.0 0/24 An Application Load Balancer is deployed to the public subnet The private subnet has a CIDR of 10.0.1.0/24. Amazon EC2 instances that run a web server on port 80 are launched into the private subnet Onty network traffic that is required for the Application Load Balancer to access the web application can be allowed to travel between the public and private subnets What collection of rules should be written to ensure that the private subnet's NACL meets the requirement? (Select TWO.) A. An inbound rule for port 80 from source 0.0 0.0/0 B. An inbound rule for port 80 from source 10.0 0 0/24 C. An outbound rule for port 80 to destination 0.0.0.0/0 D. An outbound rule for port 80 to destination 10.0.0.0/24 E. An outbound rule for ports 1024 through 65535 to destination 10.0.0.0/24 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "An inbound rule for port 80 from source 0.0 0.0/0",
      "B": "An inbound rule for port 80 from source 10.0 0 0/24",
      "C": "An outbound rule for port 80 to destination 0.0.0.0/0",
      "D": "An outbound rule for port 80 to destination 10.0.0.0/24",
      "E": "An outbound rule for ports 1024 through 65535 to destination 10.0.0.0/24 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "E"
    ],
    "select_n": 2,
    "explanation": "Ephemeral ports are not covered in the syllabus so be careful that you don't confuse day to day best practise with what is required for the exam. Link to an\nexplanation on Ephemeral ports here. https://acloud.guru/forums/aws-certified-solutions-architect-associate/discussion/-KUbcwo4lXefMl7janaK/netw\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "9.2",
    "question": "- (Exam Topic 1) A travel company built a web application that uses Amazon Simple Email Service (Amazon SES) to send email notifications to users. The company needs to enable logging to help troubleshoot email delivery issues. The company also needs the ability to do searches that are based on recipient, subject, and time sent. Which combination of steps should a solutions architect take to meet these requirements? (Select TWO.) A. Create an Amazon SES configuration set with Amazon Kinesis Data Firehose as the destinatio B. Choose to send logs to an Amazon S3 bucket. C. Enable AWS CloudTrail loggin D. Specify an Amazon S3 bucket as the destination for the logs. E. Use Amazon Athena to query the fogs in the Amazon S3 bucket for recipient, subject, and time sent. F. Create an Amazon CloudWatch log grou G. Configure Amazon SES to send logs to the log group H. Use Amazon Athena to query the logs in Amazon CloudWatch for recipient, subject, and time sent. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an Amazon SES configuration set with Amazon Kinesis Data Firehose as the destinatio",
      "B": "Choose to send logs to an Amazon S3 bucket.",
      "C": "Enable AWS CloudTrail loggin",
      "D": "Specify an Amazon S3 bucket as the destination for the logs.",
      "E": "Use Amazon Athena to query the fogs in the Amazon S3 bucket for recipient, subject, and time sent.",
      "F": "Create an Amazon CloudWatch log grou",
      "G": "Configure Amazon SES to send logs to the log group",
      "H": "Use Amazon Athena to query the logs in Amazon CloudWatch for recipient, subject, and time sent. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C"
    ],
    "select_n": 2,
    "explanation": "https://docs.aws.amazon.com/ses/latest/dg/event-publishing-retrieving-firehose.html\nTo enable you to track your email sending at a granular level, you can set up Amazon SES to publish email sending events to Amazon CloudWatch, Amazon\nKinesis Data Firehose, or Amazon Simple Notification Service based on characteristics that you define.\nhttps://docs.aws.amazon.com/ses/latest/dg/monitor-using-event-publishing.html\nhttps://aws.amazon.com/getting-started/hands-on/build-serverless-real-time-data-processing-app-lambda-kinesis\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "16.2",
    "question": "- (Exam Topic 1) A company is running a web application on Amazon EC2 instances in a production AWS account. The company requires all logs generated from the web application to be copied to a central AWS account (or analysis and archiving. The company's AWS accounts are currently managed independently. Logging agents are configured on the EC2 instances to upload the tog files to an Amazon S3 bucket in the central AWS account. A solutions architect needs to provide access for a solution that will allow the production account to store log files in the central account. The central account also needs to have read access to the tog files. What should the solutions architect do to meet these requirements? A. Create a cross-account role in the central accoun B. Assume the role from the production account when the logs are being copied. C. Create a policy on the S3 bucket with the production account ID as the principa D. Allow S3 access from a delegated user. E. Create a policy on the S3 bucket with access from only the CIDR range of the EC2 instances in the production accoun F. Use the production account ID as the principal. G. Create a cross-account role in the production accoun H. Assume the role from the production account when the logs are being copied. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a cross-account role in the central accoun",
      "B": "Assume the role from the production account when the logs are being copied.",
      "C": "Create a policy on the S3 bucket with the production account ID as the principa",
      "D": "Allow S3 access from a delegated user.",
      "E": "Create a policy on the S3 bucket with access from only the CIDR range of the EC2 instances in the production accoun",
      "F": "Use the production account ID as the principal.",
      "G": "Create a cross-account role in the production accoun",
      "H": "Assume the role from the production account when the logs are being copied. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "18.2",
    "question": "- (Exam Topic 1) A large company with hundreds of AWS accounts has a newly established centralized internal process for purchasing new or modifying existing Reserved Instances. This process requires all business units that want to purchase or modify Reserved Instances to submit requests to a dedicated team for procurement or execution. Previously, business units would directly purchase or modify Reserved Instances in their own respective AWS accounts autonomously. Which combination of steps should be taken to proactively enforce the new process in the MOST secure way possible? (Select TWO.) A. Ensure all AWS accounts are part of an AWS Organizations structure operating in all features mode. B. Use AWS Contig lo report on the attachment of an IAM policy that denies access to the ec2:PurchaseReservedlnstancesOffering and ec2:ModifyReservedlnstances actions. C. In each AWS account, create an IAM policy with a DENY rule to the ec2:PurchaseReservedlnstancesOffering and ec2:ModifyReservedInstances actions. D. Create an SCP that contains a deny rule to the ec2:PurchaseReservedlnstancesOffering and ec2: Modify Reserved Instances action E. Attach the SCP to each organizational unit (OU) of the AWS Organizations structure. F. Ensure that all AWS accounts are part of an AWS Organizations structure operating in consolidated billing features mode. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Ensure all AWS accounts are part of an AWS Organizations structure operating in all features mode.",
      "B": "Use AWS Contig lo report on the attachment of an IAM policy that denies access to the ec2:PurchaseReservedlnstancesOffering and ec2:ModifyReservedlnstances actions.",
      "C": "In each AWS account, create an IAM policy with a DENY rule to the ec2:PurchaseReservedlnstancesOffering and ec2:ModifyReservedInstances actions.",
      "D": "Create an SCP that contains a deny rule to the ec2:PurchaseReservedlnstancesOffering and ec2: Modify Reserved Instances action",
      "E": "Attach the SCP to each organizational unit (OU) of the AWS Organizations structure.",
      "F": "Ensure that all AWS accounts are part of an AWS Organizations structure operating in consolidated billing features mode. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "D"
    ],
    "select_n": 2,
    "explanation": "https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAllFeatures.html\nhttps://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scp-strategies.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "23.2",
    "question": "- (Exam Topic 1) A company has a new application that needs to run on five Amazon EC2 instances in a single AWS Region. The application requires high-throughput, low-latency network connections between all of the EC2 instances where the application will run. There is no requirement for the application to be fault tolerant. Which solution will meet these requirements? A. Launch five new EC2 instances into a cluster placement grou B. Ensure that the EC2 instance type supports enhanced networking. C. Launch five new EC2 instances into an Auto Scaling group in the same Availability Zon D. Attach an extra elastic network interface to each EC2 instance. E. Launch five new EC2 instances into a partition placement grou F. Ensure that the EC2 instance type supports enhanced networking. G. Launch five new EC2 instances into a spread placement grou H. Attach an extra elastic network interface to each EC2 instance. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Launch five new EC2 instances into a cluster placement grou",
      "B": "Ensure that the EC2 instance type supports enhanced networking.",
      "C": "Launch five new EC2 instances into an Auto Scaling group in the same Availability Zon",
      "D": "Attach an extra elastic network interface to each EC2 instance.",
      "E": "Launch five new EC2 instances into a partition placement grou",
      "F": "Ensure that the EC2 instance type supports enhanced networking.",
      "G": "Launch five new EC2 instances into a spread placement grou",
      "H": "Attach an extra elastic network interface to each EC2 instance. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": "When you launch EC2 instances in a cluster they benefit from performance and low latency. No redundancy though as per the question\nhttps://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "24",
    "question": "- (Exam Topic 1) A company is running a data-intensive application on AWS. The application runs on a cluster of hundreds of Amazon EC2 instances. A shared file system also runs on several EC2 instances that store 200 TB of data. The application reads and modifies the data on the shared file system and generates a report. The job runs once monthly, reads a subset of the files from the shared file system, and takes about 72 hours to complete. The compute instances scale in an Auto Scaling group, but the instances that host the shared file system run continuously. The compute and storage instances are all in the same AWS Region. A solutions architect needs to reduce costs by replacing the shared file system instances. The file system must provide high performance access to the needed data for the duration of the 72-hour run. Which solution will provide the LARGEST overall cost reduction while meeting these requirements? A. Migrate the data from the existing shared file system to an Amazon S3 bucket that uses the S3 Intelligent-Tiering storage clas B. Before the job runs each month, use Amazon FSx for Lustre to create a new file system with the data from Amazon S3 by using lazy loadin C. Use the new file system as the shared storage for the duration of the jo D. Delete the file system when the job is complete. E. Migrate the data from the existing shared file system to a large Amazon Elastic Block Store (Amazon EBS) volume with Multi-Attach enable F. Attach the EBS volume to each of the instances by using a user data script in the Auto Scaling group launch templat G. Use the EBS volume as the shared storage for the duration of the jo H. Detach the EBS volume when the job is complete. I. Migrate the data from the existing shared file system to an Amazon S3 bucket that uses the S3 Standard storage clas J. Before the job runs each month, use Amazon FSx for Lustre to create a new file system with the data from Amazon S3 by using batch loadin K. Use the new file system as the shared storage for the duration of the jo L. Delete the file system when the job is complete. M. Migrate the data from the existing shared file system to an Amazon S3 bucke N. Before the job runs each month, use AWS Storage Gateway to create a file gateway with the data from Amazon S3. Use the file gateway as the shared storage for the jo O. Delete the file gateway when the job is complete. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Migrate the data from the existing shared file system to an Amazon S3 bucket that uses the S3 Intelligent-Tiering storage clas",
      "B": "Before the job runs each month, use Amazon FSx for Lustre to create a new file system with the data from Amazon S3 by using lazy loadin",
      "C": "Use the new file system as the shared storage for the duration of the jo",
      "D": "Delete the file system when the job is complete.",
      "E": "Migrate the data from the existing shared file system to a large Amazon Elastic Block Store (Amazon EBS) volume with Multi-Attach enable",
      "F": "Attach the EBS volume to each of the instances by using a user data script in the Auto Scaling group launch templat",
      "G": "Use the EBS volume as the shared storage for the duration of the jo",
      "H": "Detach the EBS volume when the job is complete.",
      "I": "Migrate the data from the existing shared file system to an Amazon S3 bucket that uses the S3 Standard storage clas",
      "J": "Before the job runs each month, use Amazon FSx for Lustre to create a new file system with the data from Amazon S3 by using batch loadin K. Use the new file system as the shared storage for the duration of the jo L. Delete the file system when the job is complete. M. Migrate the data from the existing shared file system to an Amazon S3 bucke N. Before the job runs each month, use AWS Storage Gateway to create a file gateway with the data from Amazon S3. Use the file gateway as the shared storage for the jo O. Delete the file gateway when the job is complete. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "26",
    "question": "- (Exam Topic 1) An e-commerce company is revamping its IT infrastructure and is planning to use AWS services. The company's CIO has asked a solutions architect to design a simple, highly available, and loosely coupled order processing application. The application is responsible (or receiving and processing orders before storing them in an Amazon DynamoDB table. The application has a sporadic traffic pattern and should be able to scale during markeling campaigns to process the orders with minimal delays. Which of the following is the MOST reliable approach to meet the requirements? A. Receive the orders in an Amazon EC2-hosted database and use EC2 instances to process them. B. Receive the orders in an Amazon SOS queue and trigger an AWS Lambda function lo process them. C. Receive the orders using the AWS Step Functions program and trigger an Amazon ECS container lo process them. D. Receive the orders in Amazon Kinesis Data Streams and use Amazon EC2 instances to process them. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Receive the orders in an Amazon EC2-hosted database and use EC2 instances to process them.",
      "B": "Receive the orders in an Amazon SOS queue and trigger an AWS Lambda function lo process them.",
      "C": "Receive the orders using the AWS Step Functions program and trigger an Amazon ECS container lo process them.",
      "D": "Receive the orders in Amazon Kinesis Data Streams and use Amazon EC2 instances to process them. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "Q: How does Amazon Kinesis Data Streams differ from Amazon SQS?\nAmazon Kinesis Data Streams enables real-time processing of streaming big data. It provides ordering of records, as well as the ability to read and/or replay\nrecords in the same order to multiple Amazon Kinesis Applications. The Amazon Kinesis Client Library (KCL) delivers all records for a given partition key to the\nsame record processor, making it easier to build multiple applications reading from the same Amazon Kinesis data stream (for example, to perform counting,\naggregation, and filtering).\nhttps://aws.amazon.com/kinesis/data-streams/faqs/\nhttps://aws.amazon.com/blogs/big-data/unite-real-time-and-batch-analytics-using-the-big-data-lambda-architect\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "31",
    "question": "- (Exam Topic 1) A company has application services that have been containerized and deployed on multiple Amazon EC2 instances with public IPs. An Apache Kafka cluster has been deployed to the EC2 instances. A PostgreSQL database has been migrated to Amazon RDS lor PostgreSQL. The company expects a significant increase of orders on its platform when a new version of its flagship product is released. What changes to the current architecture will reduce operational overhead and support the product release? A. Create an EC2 Auto Scaling group behind an Application Load Balance B. Create additional read replicas for the DB instanc C. Create Amazon Kinesis data streams and configure the application services lo use the data stream D. Store and serve static content directly from Amazon S3. E. Create an EC2 Auto Scaling group behind an Application Load Balance F. Deploy the DB instance in Multi-AZ mode and enable storage auto scalin G. Create Amazon Kinesis data streams and configure the application services to use the data stream H. Store and serve static content directly from Amazon S3. I. Deploy the application on a Kubernetes cluster created on the EC2 instances behind an Application Load Balance J. Deploy the DB instance in Multi-AZ mode and enable storage auto scalin K. Create an Amazon Managed Streaming for Apache Kafka cluster and configure the application services to use the cluste L. Store static content in Amazon S3 behind an Amazon CloudFront distribution. M. Deploy the application on Amazon Elastic Kubernetes Service (Amazon EKS) with AWS Fargate and enable auto scaling behind an Application Load Balance N. Create additional read replicas for the DB instanc O. Create an Amazon Managed Streaming for Apache Kafka cluster and configure the application services to use the cluste P. Store static content in Amazon S3 behind an Amazon CloudFront distribution. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an EC2 Auto Scaling group behind an Application Load Balance",
      "B": "Create additional read replicas for the DB instanc",
      "C": "Create Amazon Kinesis data streams and configure the application services lo use the data stream",
      "D": "Store and serve static content directly from Amazon S3.",
      "E": "Create an EC2 Auto Scaling group behind an Application Load Balance",
      "F": "Deploy the DB instance in Multi-AZ mode and enable storage auto scalin",
      "G": "Create Amazon Kinesis data streams and configure the application services to use the data stream",
      "H": "Store and serve static content directly from Amazon S3.",
      "I": "Deploy the application on a Kubernetes cluster created on the EC2 instances behind an Application Load Balance",
      "J": "Deploy the DB instance in Multi-AZ mode and enable storage auto scalin K. Create an Amazon Managed Streaming for Apache Kafka cluster and configure the application services to use the cluste L. Store static content in Amazon S3 behind an Amazon CloudFront distribution. M. Deploy the application on Amazon Elastic Kubernetes Service (Amazon EKS) with AWS Fargate and enable auto scaling behind an Application Load Balance N. Create additional read replicas for the DB instanc O. Create an Amazon Managed Streaming for Apache Kafka cluster and configure the application services to use the cluste P. Store static content in Amazon S3 behind an Amazon CloudFront distribution. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "Deploy the application on Amazon Elastic Kubernetes Service (Amazon EKS) with AWS Fargate and enable auto scaling behind an Application Load Balancer.\nCreate additional read replicas for the DB instance. Create an Amazon Managed Streaming for Apache Kafka cluster and configure the application services to use\nthe cluster. Store static content in Amazon S3 behind an Amazon CloudFront distribution.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "34.2",
    "question": "- (Exam Topic 1) A company standardized its method of deploying applications to AWS using AWS CodePipeline and AWS Cloud Formation. The applications are in Typescript and Python. The company has recently acquired another business that deploys applications to AWS using Python scripts. Developers from the newly acquired company are hesitant to move their applications under CloudFormation because it would require than they learn a new domain-specific language and eliminate their access to language features, such as looping. How can the acquired applications quickly be brought up to deployment standards while addressing the developers' concerns? A. Create CloudFormation templates and re-use parts of the Python scripts as instance user dat B. Use the AWS Cloud Development Kit (AWS CDK) to deploy the application using these template C. Incorporate the AWS CDK into CodePipeline and deploy the application to AWS using these templates. D. Use a third-party resource provisioning engine inside AWS CodeBuild to standardize the deployment processes of the existing and acquired compan E. Orchestrate the CodeBuild job using CodePipeline. F. Standardize on AWS OpsWork G. Integrate OpsWorks with CodePipelin H. Have the developers create Chef recipes to deploy their applications on AWS. I. Define the AWS resources using Typescript or Pytho J. Use the AWS Cloud Development Kit (AWS CDK) to create CloudFormation templates from the developers' code, and use the AWS CDK to create CloudFormation stack K. Incorporate the AWS CDK as a CodeBuild job in CodePipeline. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create CloudFormation templates and re-use parts of the Python scripts as instance user dat",
      "B": "Use the AWS Cloud Development Kit (AWS CDK) to deploy the application using these template",
      "C": "Incorporate the AWS CDK into CodePipeline and deploy the application to AWS using these templates.",
      "D": "Use a third-party resource provisioning engine inside AWS CodeBuild to standardize the deployment processes of the existing and acquired compan",
      "E": "Orchestrate the CodeBuild job using CodePipeline.",
      "F": "Standardize on AWS OpsWork",
      "G": "Integrate OpsWorks with CodePipelin",
      "H": "Have the developers create Chef recipes to deploy their applications on AWS.",
      "I": "Define the AWS resources using Typescript or Pytho",
      "J": "Use the AWS Cloud Development Kit (AWS CDK) to create CloudFormation templates from the developers' code, and use the AWS CDK to create CloudFormation stack K. Incorporate the AWS CDK as a CodeBuild job in CodePipeline. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "35",
    "question": "- (Exam Topic 1) A solutions architect is designing an application to accept timesheet entries from employees on their mobile devices. Timesheets will be submitted weekly, with most of the submissions occurring on Friday. The data must be stored in a format that allows payroll administrators to run monthly reports. The infrastructure must be highly available and scale to match the rate of incoming data and reporting requests. Which combination of steps meets these requirements while minimizing operational overhead? (Select TWO.) A. Deploy the application to Amazon EC2 On-Demand Instances With load balancing across multiple Availability Zone B. Use scheduled Amazon EC2 Auto Scaling to add capacity before the high volume of submissions on Fridays. C. Deploy the application in a container using Amazon Elastic Container Service (Amazon ECS) with load balancing across multiple Availability Zone D. Use scheduled Service Auto Scaling to add capacity before the high volume of submissions on Fridays. E. Deploy the application front end to an Amazon S3 bucket served by Amazon CloudFron F. Deploy the application backend using Amazon API Gateway with an AWS Lambda proxy integration. G. Store the timesheet submission data in Amazon Redshif H. Use Amazon OuickSight to generate the reports using Amazon Redshift as the data source. I. Store the timesheet submission data in Amazon S3. Use Amazon Athena and Amazon OuickSight to generate the reports using Amazon S3 as the data source. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy the application to Amazon EC2 On-Demand Instances With load balancing across multiple Availability Zone",
      "B": "Use scheduled Amazon EC2 Auto Scaling to add capacity before the high volume of submissions on Fridays.",
      "C": "Deploy the application in a container using Amazon Elastic Container Service (Amazon ECS) with load balancing across multiple Availability Zone",
      "D": "Use scheduled Service Auto Scaling to add capacity before the high volume of submissions on Fridays.",
      "E": "Deploy the application front end to an Amazon S3 bucket served by Amazon CloudFron",
      "F": "Deploy the application backend using Amazon API Gateway with an AWS Lambda proxy integration.",
      "G": "Store the timesheet submission data in Amazon Redshif",
      "H": "Use Amazon OuickSight to generate the reports using Amazon Redshift as the data source.",
      "I": "Store the timesheet submission data in Amazon S3. Use Amazon Athena and Amazon OuickSight to generate the reports using Amazon S3 as the data source. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "E"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "50",
    "question": "- (Exam Topic 1) A company is building a hybrid solution between its existing on-premises systems and a new backend in AWS. The company has a management application to monitor the state of its current IT infrastructure and automate responses to issues. The company wants to incorporate the status of its consumed AWS services into the application. The application uses an HTTPS endpoint to receive updates. Which approach meets these requirements with the LEAST amount of operational overhead? A. Configure AWS Systems Manager OpsCenter to ingest operational events from the on-premises systems Retire the on-premises management application and adopt OpsCenter as the hub B. Configure Amazon EventBridge (Amazon CloudWatch Events) to detect and react to changes for AWS Health events from the AWS Personal Health Dashboard Configure the EventBridge (CloudWatch Events) event to publish a message to an Amazon Simple Notification Service (Amazon SNS) topic and subscribe the topic to the HTTPS endpoint of the management application C. Modify the on-premises management application to call the AWS Health API to poll for status events of AWS services. D. Configure Amazon EventBridge (Amazon CloudWatch Events) to detect and react to changes for AWS Health events from the AWS Service Health Dashboard Configure the EventBridge (CloudWatch Events) event to publish a message to an Amazon Simple Notification Service (Amazon SNS) topic and subscribe the topic to an HTTPS endpoint for the management application with a topic filter corresponding to the services being used -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure AWS Systems Manager OpsCenter to ingest operational events from the on-premises systems Retire the on-premises management application and adopt OpsCenter as the hub",
      "B": "Configure Amazon EventBridge (Amazon CloudWatch Events) to detect and react to changes for AWS Health events from the AWS Personal Health Dashboard Configure the EventBridge (CloudWatch Events) event to publish a message to an Amazon Simple Notification Service (Amazon SNS) topic and subscribe the topic to the HTTPS endpoint of the management application",
      "C": "Modify the on-premises management application to call the AWS Health API to poll for status events of AWS services.",
      "D": "Configure Amazon EventBridge (Amazon CloudWatch Events) to detect and react to changes for AWS Health events from the AWS Service Health Dashboard Configure the EventBridge (CloudWatch Events) event to publish a message to an Amazon Simple Notification Service (Amazon SNS) topic and subscribe the topic to an HTTPS endpoint for the management application with a topic filter corresponding to the services being used -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": "ALB & NLB both supports IPs as targets. Questions is based on TCP traffic over VPN to on-premise. TCP is layer 4 and the , load balancer should be NLB. Then\nnext questions does NLB supports loadbalcning traffic over VPN. And answer is YEs based on below URL.\nhttps://aws.amazon.com/about-aws/whats-new/2018/09/network-load-balancer-now-supports-aws-vpn/\nTarget as IPs for NLB & ALB: https://aws.amazon.com/elasticloadbalancing/faqs/?nc=sn&loc=5 https://aws.amazon.com/elasticloadbalancing/application-load-\nbalancer/\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "57",
    "question": "- (Exam Topic 1) A solutions architect is responsible (or redesigning a legacy Java application to improve its availability, data durability, and scalability. Currently, the application runs on a single high-memory Amazon EC2 instance. It accepts HTTP requests from upstream clients, adds them to an in-memory queue, and responds with a 200 status. A separate application thread reads items from the queue, processes them, and persists the results to an Amazon RDS MySQL instance. The processing time for each item takes 90 seconds on average, most of which is spent waiting on external service calls, but the application is written to process multiple items in parallel. Traffic to this service is unpredictable. During periods of high load, items may sit in the internal queue for over an hour while the application processes the backlog. In addition, the current system has issues with availability and data loss if the single application node fails. Clients that access this service cannot be modified. They expect to receive a response to each HTTP request they send within 10 seconds before they will time out and retry the request. Which approach would improve the availability and durability of (he system while decreasing the processing latency and minimizing costs? A. Create an Amazon API Gateway REST API that uses Lambda proxy integration to pass requests to an AWS Lambda functio B. Migrate the core processing code to a Lambda function and write a wrapper class that provides a handler method that converts the proxy events to the internal application data model and invokes the processing module. C. Create an Amazon API Gateway REST API that uses a service proxy to put items in an Amazon SOS queu D. Extract the core processing code from the existing application and update it to pull items from Amazon SOS instead of an in-memory queu E. Deploy the new processing application to smaller EC2 instances within an Auto Scaling group that scales dynamically based on the approximate number of messages in the Amazon SOS queue. F. Modify the application to use Amazon DynamoDB instead of Amazon RD G. Configure Auto Scaling for the DynamoDB tabl H. Deploy the application within an Auto Scaling group with a scaling policy based on CPU utilizatio I. Back the in-memory queue with a memory-mapped file to an instance store volume and periodically write that file to Amazon S3. J. Update the application to use a Redis task queue instead of the in-memory queu K. 8uild a Docker container image for the applicatio L. Create an Amazon ECS task definition that includes the application container and a separate container to host Redi M. Deploy the new task definition as an ECS service using AWS Fargate, and enable Auto Scaling. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an Amazon API Gateway REST API that uses Lambda proxy integration to pass requests to an AWS Lambda functio",
      "B": "Migrate the core processing code to a Lambda function and write a wrapper class that provides a handler method that converts the proxy events to the internal application data model and invokes the processing module.",
      "C": "Create an Amazon API Gateway REST API that uses a service proxy to put items in an Amazon SOS queu",
      "D": "Extract the core processing code from the existing application and update it to pull items from Amazon SOS instead of an in-memory queu",
      "E": "Deploy the new processing application to smaller EC2 instances within an Auto Scaling group that scales dynamically based on the approximate number of messages in the Amazon SOS queue.",
      "F": "Modify the application to use Amazon DynamoDB instead of Amazon RD",
      "G": "Configure Auto Scaling for the DynamoDB tabl",
      "H": "Deploy the application within an Auto Scaling group with a scaling policy based on CPU utilizatio",
      "I": "Back the in-memory queue with a memory-mapped file to an instance store volume and periodically write that file to Amazon S3.",
      "J": "Update the application to use a Redis task queue instead of the in-memory queu K. 8uild a Docker container image for the applicatio L. Create an Amazon ECS task definition that includes the application container and a separate container to host Redi M. Deploy the new task definition as an ECS service using AWS Fargate, and enable Auto Scaling. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "The obvious challenges here are long workloads, scalability based on queue load, and reliability. Almost always the defacto answer to queue related workload is\nSQS. Since the workloads are very long (90 minutes) Lambdas cannot be used (15 mins max timeout). So, autoscaled smaller EC2 nodes that wait on external\nservices to complete the task makes more sense. If the task fails, the message is returned to the queue and retried.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "22",
    "question": "- (Exam Topic 1) A solutions architect is building a web application that uses an Amazon RDS for PostgreSQL DB instance The DB instance is expected to receive many more reads than writes. The solutions architect needs to ensure that the large amount of read traffic can be accommodated and that the DB instance is highly available. Which steps should the solutions architect take to meet these requirements? (Select THREE) A. Create multiple read replicas and put them into an Auto Scaling group. B. Create multiple read replicas in different Availability Zones. C. Create an Amazon Route 53 hosted zone and a record set for each read replica with a TTL and a weighted routing policy. D. Create an Application Load Balancer (ALB) and put the read replicas behind the ALB. E. Configure an Amazon CloudWatch alarm to detect a failed read replic F. Set the alarm to directly invoke an AWS Lambda function to delete its Route 53 record set. G. Configure an Amazon Route 53 health check for each read replica using its endpoint -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create multiple read replicas and put them into an Auto Scaling group.",
      "B": "Create multiple read replicas in different Availability Zones.",
      "C": "Create an Amazon Route 53 hosted zone and a record set for each read replica with a TTL and a weighted routing policy.",
      "D": "Create an Application Load Balancer (ALB) and put the read replicas behind the ALB.",
      "E": "Configure an Amazon CloudWatch alarm to detect a failed read replic",
      "F": "Set the alarm to directly invoke an AWS Lambda function to delete its Route 53 record set.",
      "G": "Configure an Amazon Route 53 health check for each read replica using its endpoint -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "C",
      "F"
    ],
    "select_n": 3,
    "explanation": "https://aws.amazon.com/premiumsupport/knowledge-center/requests-rds-read-replicas/\nYou can use Amazon Route 53 weighted record sets to distribute requests across your read replicas. Within a Route 53 hosted zone, create individual record sets\nfor each DNS endpoint associated with your read replicas and give them the same weight. Then, direct requests to the endpoint of the record set. You can\nincorporate Route 53 health checks to be sure that Route 53 directs traffic away from unavailable read replicas\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "19",
    "question": "- (Exam Topic 1) A company is migrating an application to AWS. It wants to use fully managed services as much as possible during the migration. The company needs to store large, important documents within the application with the following requirements: * 1. The data must be highly durable and available. * 2. The data must always be encrypted at rest and in transit. * 3. The encryption key must be managed by the company and rotated periodically. Which of the following solutions should the solutions architect recommend? A. Deploy the storage gateway to AWS in file gateway mod B. Use Amazon EBS volume encryption using an AWS KMS key to encrypt the storage gateway volumes. C. Use Amazon S3 with a bucket policy to enforce HTTPS for connections to the bucket and to enforce server-side encryption and AWS KMS for object encryption. D. Use Amazon DynamoDB with SSL to connect to DynamoD E. Use an AWS KMS key to encrypt DynamoDB objects at rest. F. Deploy instances with Amazon EBS volumes attached to store this dat G. Use E8S volume encryption using an AWS KMS key to encrypt the data. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy the storage gateway to AWS in file gateway mod",
      "B": "Use Amazon EBS volume encryption using an AWS KMS key to encrypt the storage gateway volumes.",
      "C": "Use Amazon S3 with a bucket policy to enforce HTTPS for connections to the bucket and to enforce server-side encryption and AWS KMS for object encryption.",
      "D": "Use Amazon DynamoDB with SSL to connect to DynamoD",
      "E": "Use an AWS KMS key to encrypt DynamoDB objects at rest.",
      "F": "Deploy instances with Amazon EBS volumes attached to store this dat",
      "G": "Use E8S volume encryption using an AWS KMS key to encrypt the data. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "Use Amazon S3 with a bucket policy to enforce HTTPS for connections to the bucket and to enforce server-side encryption and AWS KMS for object encryption.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "14",
    "question": "- (Exam Topic 1) A company provides a centralized Amazon EC2 application hosted in a single shared VPC. The centralized application must be accessible from client applications running in the VPCs of other business units. The centralized application front end is configured with a Network Load Balancer (NLB) for scalability. Up to 10 business unit VPCs will need to be connected to the shared VPC. Some of the business unit VPC CIDR blocks overlap with the shared VPC. and some overlap with each other. Network connectivity to the centralized application in the shared VPC should be allowed from authorized business unit VPCs only. Which network configuration should a solutions architect use to provide connectivity from the client applications in the business unit VPCs to the centralized application in the shared VPC? A. Create an AW5 Transit Gatewa B. Attach the shared VPC and the authorized business unit VPCs to the transit gatewa C. Create a single transit gateway route table and associate it with all of the attached VPC D. Allow automatic propagation of routes from the attachments into the route tabl E. Configure VPC routing tables to send traffic to the transit gateway. F. Create a VPC endpoint service using the centralized application NLB and enable (he option to require endpoint acceptanc G. Create a VPC endpoint in each of the business unit VPCs using the service name of the endpoint servic H. Accept authorized endpoint requests from the endpoint service console. I. Create a VPC peering connection from each business unit VPC to Ihe shared VP J. Accept the VPC peering connections from the shared VPC consol K. Configure VPC routing tables to send traffic to the VPC peering connection. L. Configure a virtual private gateway for the shared VPC and create customer gateways for each of theauthorized business unit VPC M. Establish a Sile-to-Site VPN connection from the business unit VPCs to the shared VP N. Configure VPC routing tables to send traffic to the VPN connection. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an AW5 Transit Gatewa",
      "B": "Attach the shared VPC and the authorized business unit VPCs to the transit gatewa",
      "C": "Create a single transit gateway route table and associate it with all of the attached VPC",
      "D": "Allow automatic propagation of routes from the attachments into the route tabl",
      "E": "Configure VPC routing tables to send traffic to the transit gateway.",
      "F": "Create a VPC endpoint service using the centralized application NLB and enable (he option to require endpoint acceptanc",
      "G": "Create a VPC endpoint in each of the business unit VPCs using the service name of the endpoint servic",
      "H": "Accept authorized endpoint requests from the endpoint service console.",
      "I": "Create a VPC peering connection from each business unit VPC to Ihe shared VP",
      "J": "Accept the VPC peering connections from the shared VPC consol K. Configure VPC routing tables to send traffic to the VPC peering connection. L. Configure a virtual private gateway for the shared VPC and create customer gateways for each of theauthorized business unit VPC M. Establish a Sile-to-Site VPN connection from the business unit VPCs to the shared VP N. Configure VPC routing tables to send traffic to the VPN connection. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "Amazon Transit Gateway doesn’t support routing between Amazon VPCs with overlapping CIDRs. If you attach a new Amazon VPC that has a CIDR which\noverlaps with an already attached Amazon VPC, Amazon Transit Gateway will not propagate the new Amazon VPC route into the Amazon Transit Gateway route\ntable.\nhttps://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#client-ip-pre\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "12",
    "question": "- (Exam Topic 1) A company runs an application that gives users the ability to search for videos and related information by using keywords that are curated from content providers. The application data is stored in an on-premises Oracle database that is 800 GB in size. The company wants to migrate the data to an Amazon Aurora MySQL DB instance. A solutions architect plans to use the AWS Schema Conversion Tool and AWS Database Migration Service (AWS DMS) for the migration. During the migration, the existing database must serve ongoing requests. The migration must be completed with minimum downtime Which solution will meet these requirements? A. Create primary key indexes, secondary indexes, and referential integrity constraints in the target database before starting the migration process B. Use AWS DMS to run the conversion report for Oracle to Aurora MySQ C. Remediate any issues Then use AWS DMS to migrate the data D. Use the M5 or CS DMS replication instance type for ongoing replication E. Turn off automatic backups and logging of the target database until the migration and cutover processes are complete -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create primary key indexes, secondary indexes, and referential integrity constraints in the target database before starting the migration process",
      "B": "Use AWS DMS to run the conversion report for Oracle to Aurora MySQ",
      "C": "Remediate any issues Then use AWS DMS to migrate the data",
      "D": "Use the M5 or CS DMS replication instance type for ongoing replication",
      "E": "Turn off automatic backups and logging of the target database until the migration and cutover processes are complete -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "11",
    "question": "- (Exam Topic 1) A large company is running a popular web application. The application runs on several Amazon EC2 Linux Instances in an Auto Scaling group in a private subnet. An Application Load Balancer is targeting the Instances In the Auto Scaling group in the private subnet. AWS Systems Manager Session Manager Is configured, and AWS Systems Manager Agent is running on all the EC2 instances. The company recently released a new version of the application Some EC2 instances are now being marked as unhealthy and are being terminated As a result, the application is running at reduced capacity A solutions architect tries to determine the root cause by analyzing Amazon CloudWatch logs that are collected from the application, but the logs are inconclusive How should the solutions architect gain access to an EC2 instance to troubleshoot the issue1? A. Suspend the Auto Scaling group's HealthCheck scaling proces B. Use Session Manager to log in to an instance that is marked as unhealthy C. Enable EC2 instance termination protection Use Session Manager to log In to an instance that is marked as unhealthy. D. Set the termination policy to Oldestinstance on the Auto Scaling grou E. Use Session Manager to log in to an instance that is marked as unhealthy F. Suspend the Auto Scaling group's Terminate proces G. Use Session Manager to log in to an instance that is marked as unhealthy -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Suspend the Auto Scaling group's HealthCheck scaling proces",
      "B": "Use Session Manager to log in to an instance that is marked as unhealthy",
      "C": "Enable EC2 instance termination protection Use Session Manager to log In to an instance that is marked as unhealthy.",
      "D": "Set the termination policy to Oldestinstance on the Auto Scaling grou",
      "E": "Use Session Manager to log in to an instance that is marked as unhealthy",
      "F": "Suspend the Auto Scaling group's Terminate proces",
      "G": "Use Session Manager to log in to an instance that is marked as unhealthy -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html\nit shows For Amazon EC2 Auto Scaling, there are two primary process types: Launch and Terminate. The Launch process adds a new Amazon EC2 instance to\nan Auto Scaling group, increasing its capacity. The Terminate process removes an Amazon EC2 instance from the group, decreasing its capacity. HealthCheck\nprocess for EC2 autoscaling is not a primary process! It is a process along with the following AddToLoadBalancer AlarmNotification AZRebalance HealthCheck\nInstanceRefresh ReplaceUnhealthy ScheduledActions From the requirements, Some EC2 instances are now being marked as unhealthy and are being\nterminated. Application is running at reduced capacity not because instances are marked unhealthy but because they are being terminated.\nhttps://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html#choosing-suspend-r\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "62.3",
    "question": "- (Exam Topic 1) A team collects and routes behavioral data for an entire company. The company runs a Multi-AZ VPC environment with public subnets, private subnets, and in internet gateway Each public subnet also contains a NAT gateway Most of the company's applications read from and write to Amazon Kinesis Data Streams. Most of the workloads run in private subnets. A solutions architect must review the infrastructure The solutions architect needs to reduce costs and maintain the function of the applications. The solutions architect uses Cost Explorer and notices that the cost in the EC2-Other category is consistently high A further review shows that NatGateway-Bytes charges are increasing the cost in the EC2-Other category. What should the solutions architect do to meet these requirements? A. Enable VPC Flow Log B. Use Amazon Athena to analyze the logs for traffic that can be remove C. Ensure that security groups are blocking traffic that is responsible for high costs. D. Add an interface VPC endpoint for Kinesis Data Streams to the VP E. Ensure that applications have thecorrect IAM permissions to use the interface VPC endpoint. F. Enable VPC Flow Logs and Amazon Detectiv G. Review Detective findings for traffic that is not related to Kinesis Data Streams Configure security groups to block that traffic H. Add an interface VPC endpoint for Kinesis Data Streams to the VPC Ensure that the VPC endpoint policy allows traffic from the applications -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Enable VPC Flow Log",
      "B": "Use Amazon Athena to analyze the logs for traffic that can be remove",
      "C": "Ensure that security groups are blocking traffic that is responsible for high costs.",
      "D": "Add an interface VPC endpoint for Kinesis Data Streams to the VP",
      "E": "Ensure that applications have thecorrect IAM permissions to use the interface VPC endpoint.",
      "F": "Enable VPC Flow Logs and Amazon Detectiv",
      "G": "Review Detective findings for traffic that is not related to Kinesis Data Streams Configure security groups to block that traffic",
      "H": "Add an interface VPC endpoint for Kinesis Data Streams to the VPC Ensure that the VPC endpoint policy allows traffic from the applications -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html https://aws.amazon.com/premiumsupport/knowledge-center/vpc-reduce-nat-\ngateway-transfer-costs/\nVPC endpoint policies enable you to control access by either attaching a policy to a VPC endpoint or by using additional fields in a policy that is attached to an IAM\nuser, group, or role to restrict access to only occur via the specified VPC endpoint\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "65",
    "question": "- (Exam Topic 1) A solutions architect is evaluating the reliability of a recently migrated application running on AWS. The front end is hosted on Amazon S3 and accelerated by Amazon CloudFront. The application layer is running in a stateless Docker container on an Amazon EC2 On-Demand Instance with an Elastic IP address. The storage layer is a MongoDB database running on an EC2 Reserved Instance in the same Availability Zone as the application layer. Which combination of steps should the solutions architect take to eliminate single points of failure with minimal application code changes? (Select TWO.) A. Create a REST API in Amazon API Gateway and use AWS Lambda functions as the application layer. B. Create an Application Load Balancer and migrate the Docker container to AWS Fargate. C. Migrate the storage layer to Amazon DynamoD8. D. Migrate the storage layer to Amazon DocumentD8 (with MongoDB compatibility). E. Create an Application Load Balancer and move the storage layer to an EC2 Auto Scaling group. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a REST API in Amazon API Gateway and use AWS Lambda functions as the application layer.",
      "B": "Create an Application Load Balancer and migrate the Docker container to AWS Fargate.",
      "C": "Migrate the storage layer to Amazon DynamoD8.",
      "D": "Migrate the storage layer to Amazon DocumentD8 (with MongoDB compatibility).",
      "E": "Create an Application Load Balancer and move the storage layer to an EC2 Auto Scaling group. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "D"
    ],
    "select_n": 2,
    "explanation": "https://aws.amazon.com/documentdb/?nc1=h_ls\nhttps://aws.amazon.com/blogs/containers/using-alb-ingress-controller-with-amazon-eks-on-fargate/\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "69",
    "question": "- (Exam Topic 1) A company needs to create and manage multiple AWS accounts for a number of departments from a central location. The security team requires read-only access to all accounts from its own AWs account. The company is using AWS Organizations and created an account tor the security team. How should a solutions architect meet these requirements? A. Use the OrganizationAccountAccessRole IAM role to create a new IAM policy wilh read-only access in each member accoun B. Establish a trust relationship between the IAM policy in each member account and the security accoun C. Ask the security team lo use the IAM policy to gain access. D. Use the OrganizationAccountAccessRole IAM role to create a new IAM role with read-only access in each member accoun E. Establish a trust relationship between the IAM role in each member account and the security accoun F. Ask the security team lo use the IAM role to gain access. G. Ask the security team to use AWS Security Token Service (AWS STS) to call the AssumeRole API for the OrganizationAccountAccessRole IAM role in the master account from the security accoun H. Use the generated temporary credentials to gain access. I. Ask the security team to use AWS Security Token Service (AWS STS) to call the AssumeRole API for the OrganizationAccountAccessRole IAM role in the member account from the security accoun J. Use the generated temporary credentials to gain access. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use the OrganizationAccountAccessRole IAM role to create a new IAM policy wilh read-only access in each member accoun",
      "B": "Establish a trust relationship between the IAM policy in each member account and the security accoun",
      "C": "Ask the security team lo use the IAM policy to gain access.",
      "D": "Use the OrganizationAccountAccessRole IAM role to create a new IAM role with read-only access in each member accoun",
      "E": "Establish a trust relationship between the IAM role in each member account and the security accoun",
      "F": "Ask the security team lo use the IAM role to gain access.",
      "G": "Ask the security team to use AWS Security Token Service (AWS STS) to call the AssumeRole API for the OrganizationAccountAccessRole IAM role in the master account from the security accoun",
      "H": "Use the generated temporary credentials to gain access.",
      "I": "Ask the security team to use AWS Security Token Service (AWS STS) to call the AssumeRole API for the OrganizationAccountAccessRole IAM role in the member account from the security accoun",
      "J": "Use the generated temporary credentials to gain access. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "78",
    "question": "- (Exam Topic 1) A company hosts a web application that tuns on a group of Amazon EC2 instances that ate behind an Application Load Balancer (ALB) in a VPC. The company wants to analyze the network payloads lo reverse-engineer a sophisticated attack of the application. Which approach should the company take to achieve this goal? A. Enable VPC Flow Log B. Store the flow logs in an Amazon S3 bucket for analysis. C. Enable Traffic Mirroring on the network interface of the EC2 instance D. Send the mirrored traffic lo a target for storage and analysis. E. Create an AWS WAF web AC F. and associate it with the AL G. Configure AWS WAF logging. H. Enable logging for the AL I. Store the logs in an Amazon S3 bucket for analysis. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Enable VPC Flow Log",
      "B": "Store the flow logs in an Amazon S3 bucket for analysis.",
      "C": "Enable Traffic Mirroring on the network interface of the EC2 instance",
      "D": "Send the mirrored traffic lo a target for storage and analysis.",
      "E": "Create an AWS WAF web AC",
      "F": "and associate it with the AL",
      "G": "Configure AWS WAF logging.",
      "H": "Enable logging for the AL",
      "I": "Store the logs in an Amazon S3 bucket for analysis. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "79.2",
    "question": "- (Exam Topic 1) An AWS customer has a web application that runs on premises. The web application fetches data from a third-party API that is behind a firewall. The third party accepts only one public CIDR block in each client's allow list. The customer wants to migrate their web application to the AWS Cloud. The application will be hosted on a set of Amazon EC2 instances behind an Application Load Balancer (ALB) in a VPC. The ALB is located in public subnets. The EC2 instances are located in private subnets. NAT gateways provide internet access to the private subnets. How should a solutions architect ensure that the web application can continue to call the third-parly API after the migration? A. Associate a block of customer-owned public IP addresses to the VP B. Enable public IP addressing for public subnets in the VPC. C. Register a block of customer-owned public IP addresses in the AWS accoun D. Create Elastic IP addresses from the address block and assign them lo the NAT gateways in the VPC. E. Create Elastic IP addresses from the block of customer-owned IP addresse F. Assign the static Elastic IP addresses to the ALB. G. Register a block of customer-owned public IP addresses in the AWS accoun H. Set up AWS Global Accelerator to use Elastic IP addresses from the address bloc I. Set the ALB as the accelerator endpoint. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Associate a block of customer-owned public IP addresses to the VP",
      "B": "Enable public IP addressing for public subnets in the VPC.",
      "C": "Register a block of customer-owned public IP addresses in the AWS accoun",
      "D": "Create Elastic IP addresses from the address block and assign them lo the NAT gateways in the VPC.",
      "E": "Create Elastic IP addresses from the block of customer-owned IP addresse",
      "F": "Assign the static Elastic IP addresses to the ALB.",
      "G": "Register a block of customer-owned public IP addresses in the AWS accoun",
      "H": "Set up AWS Global Accelerator to use Elastic IP addresses from the address bloc",
      "I": "Set the ALB as the accelerator endpoint. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "When EC2 instances reach third-party API through internet, their privates IP addresses will be masked by NAT Gateway public IP address.\nhttps://aws.amazon.com/blogs/networking-and-content-delivery/introducing-bring-your-own-ip-byoip-for-amaz\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "84",
    "question": "- (Exam Topic 1) A company requires that all internal application connectivity use private IP addresses. To facilitate this policy, a solutions architect has created interface endpoints to connect to AWS public services. Upon testing, the solutions architect notices that the service names are resolving to public IP addresses, and that internal services cannot connect to the interface endpoints. Which step should the solutions architect take to resolve this issue? A. Update the subnet route table with a route to the interface endpoint. B. Enable the private DNS option on the VPC attributes. C. Configure the security group on the interface endpoint to allow connectivity to the AWS services. D. Configure an Amazon Route 53 private hosted zone with a conditional forwarder for the internal application. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Update the subnet route table with a route to the interface endpoint.",
      "B": "Enable the private DNS option on the VPC attributes.",
      "C": "Configure the security group on the interface endpoint to allow connectivity to the AWS services.",
      "D": "Configure an Amazon Route 53 private hosted zone with a conditional forwarder for the internal application. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "92",
    "question": "- (Exam Topic 1) A company is planning on hosting its ecommerce platform on AWS using a multi-tier web application designed for a NoSQL database. The company plans to use the us-west-2 Region as its primary Region. The company want to ensure that copies of the application and data are available in a second Region, us-west-1, for disaster recovery. The company wants to keep the time to fail over as low as possible. Failing back to the primary Region should be possible without administrative interaction after the primary service is restored. Which design should the solutions architect use? A. Use AWS Cloud Formation StackSets lo create the stacks in both Regions with Auto Scaling groups for the web and application tier B. Asynchronously replicate static content between Regions using Amazon S3 cross-Region replicatio C. Use an Amazon Route 53 DNS failover routing policy to direct users to the secondary site in us-west-1 in the event of an outag D. Use Amazon DynamoDB global tables for the database tier. E. Use AWS Cloud Formation StackSets to create the stacks in both Regions with Auto Scaling groups for the web and application tier F. Asynchronously replicate static content between Regions using AmazonS3 cross-Region replicatio G. Use an Amazon Route 53 DNS failover routing policy to direct users to the secondary site in us-west-1 in the event of an outag H. Deploy an Amazon Aurora global database for the database tier. I. Use AWS Service Catalog to deploy the web and application servers in both Region J. Asynchronously replicate static content between the two Regions using Amazon S3 cross-Region replicatio K. Use Amazon Route 53 health checks to identify a primary Region failure and update the public DNS entry listing to the secondary Region in the event of an outag L. Use Amazon RDS for MySQL withcross-Region replication for the database tier. M. Use AWS CloudFormation StackSets to create the stacks in both Regions using Auto Scaling groups for the web and application tier N. Asynchronously replicate static content between Regions using Amazon S3 cross-Region replicatio O. Use Amazon CloudFront with static files in Amazon S3, and multi-Region origins for the front-end web tie P. Use Amazon DynamoD8 tables in each Region with scheduled backups to Amazon S3. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS Cloud Formation StackSets lo create the stacks in both Regions with Auto Scaling groups for the web and application tier",
      "B": "Asynchronously replicate static content between Regions using Amazon S3 cross-Region replicatio",
      "C": "Use an Amazon Route 53 DNS failover routing policy to direct users to the secondary site in us-west-1 in the event of an outag",
      "D": "Use Amazon DynamoDB global tables for the database tier.",
      "E": "Use AWS Cloud Formation StackSets to create the stacks in both Regions with Auto Scaling groups for the web and application tier",
      "F": "Asynchronously replicate static content between Regions using AmazonS3 cross-Region replicatio",
      "G": "Use an Amazon Route 53 DNS failover routing policy to direct users to the secondary site in us-west-1 in the event of an outag",
      "H": "Deploy an Amazon Aurora global database for the database tier.",
      "I": "Use AWS Service Catalog to deploy the web and application servers in both Region",
      "J": "Asynchronously replicate static content between the two Regions using Amazon S3 cross-Region replicatio K. Use Amazon Route 53 health checks to identify a primary Region failure and update the public DNS entry listing to the secondary Region in the event of an outag L. Use Amazon RDS for MySQL withcross-Region replication for the database tier. M. Use AWS CloudFormation StackSets to create the stacks in both Regions using Auto Scaling groups for the web and application tier N. Asynchronously replicate static content between Regions using Amazon S3 cross-Region replicatio O. Use Amazon CloudFront with static files in Amazon S3, and multi-Region origins for the front-end web tie P. Use Amazon DynamoD8 tables in each Region with scheduled backups to Amazon S3. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "96",
    "question": "- (Exam Topic 1) A team collects and routes behavioral data for an entire company The company runs a Multi-AZ VPC environment with public subnets, private subnets, and in internet gateway Each public subnet also contains a NAT gateway Most of the company's applications read from and write to Amazon Kinesis Data Streams. Most of the workloads am in private subnets. A solutions architect must review the infrastructure The solutions architect needs to reduce costs and maintain the function of the applications The solutions architect uses Cost Explorer and notices that the cost in the EC2-Other category is consistently high A further review shows that NatGateway-Bytes charges are increasing the cost in the EC2-Other category. What should the solutions architect do to meet these requirements? A. Enable VPC Flow Log B. Use Amazon Athena to analyze the logs for traffic that can be remove C. Ensure that security groups are Mocking traffic that is responsible for high costs. D. Add an interface VPC endpoint for Kinesis Data Streams to the VP E. Ensure that applications have the correct IAM permissions to use the interface VPC endpoint. F. Enable VPC Flow Logs and Amazon Detective Review Detective findings for traffic that is not related to Kinesis Data Streams Configure security groups to block that traffic G. Add an interface VPC endpoint for Kinesis Data Streams to the VP H. Ensure that the VPC endpoint policy allows traffic from the applications. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Enable VPC Flow Log",
      "B": "Use Amazon Athena to analyze the logs for traffic that can be remove",
      "C": "Ensure that security groups are Mocking traffic that is responsible for high costs.",
      "D": "Add an interface VPC endpoint for Kinesis Data Streams to the VP",
      "E": "Ensure that applications have the correct IAM permissions to use the interface VPC endpoint.",
      "F": "Enable VPC Flow Logs and Amazon Detective Review Detective findings for traffic that is not related to Kinesis Data Streams Configure security groups to block that traffic",
      "G": "Add an interface VPC endpoint for Kinesis Data Streams to the VP",
      "H": "Ensure that the VPC endpoint policy allows traffic from the applications. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html\nhttps://aws.amazon.com/premiumsupport/knowledge-center/vpc-reduce-nat-gateway-transfer-costs/\nVPC endpoint policies enable you to control access by either attaching a policy to a VPC endpoint or by using additional fields in a policy that is attached to an IAM\nuser, group, or role to restrict access to only occur via the specified VPC endpoint\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "98",
    "question": "- (Exam Topic 1) A company has an internal application running on AWS that is used to track and process shipments in the company's warehouse. Currently, after the system receives an order, it emails the staff the information needed to ship a package. Once the package is shipped, the staff replies to the email and the order is marked as shipped. The company wants to stop using email in the application and move to a serverless application model. Which architecture solution meets these requirements? A. Use AWS Batch to configure the different tasks required lo ship a packag B. Have AWS Batch trigger an AWS Lambda function that creates and prints a shipping labe C. Once that label is scanne D. as it leaves the warehouse, have another Lambda function move the process to the next step in the AWS Batch job.B. E. When a new order is created, store the order information in Amazon SQ F. Have AWS Lambda check the queue every 5 minutes and process any needed wor G. When an order needs to be shipped, have Lambda print the label in the warehous H. Once the label has been scanned, as it leaves the warehouse, have an Amazon EC2 instance update Amazon SOS. I. Update the application to store new order information in Amazon DynamoD J. When a new order is created, trigger an AWS Step Functions workflow, mark the orders as \"in progress,\" and print a package label to the warehous K. Once the label has been scanned and fulfilled, the application will trigger an AWS Lambda function that will mark the order as shipped and complete the workflow. L. Store new order information in Amazon EF M. Have instances pull the new information from the NFS and send that information to printers in the warehous N. Once the label has been scanned, as it leaves the warehouse, have Amazon API Gateway call the instances to remove the order information from Amazon EFS. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS Batch to configure the different tasks required lo ship a packag",
      "B": "Have AWS Batch trigger an AWS Lambda function that creates and prints a shipping labe",
      "C": "Once that label is scanne",
      "D": "as it leaves the warehouse, have another Lambda function move the process to the next step in the AWS Batch job.B.",
      "E": "When a new order is created, store the order information in Amazon SQ",
      "F": "Have AWS Lambda check the queue every 5 minutes and process any needed wor",
      "G": "When an order needs to be shipped, have Lambda print the label in the warehous",
      "H": "Once the label has been scanned, as it leaves the warehouse, have an Amazon EC2 instance update Amazon SOS.",
      "I": "Update the application to store new order information in Amazon DynamoD",
      "J": "When a new order is created, trigger an AWS Step Functions workflow, mark the orders as \"in progress,\" and print a package label to the warehous K. Once the label has been scanned and fulfilled, the application will trigger an AWS Lambda function that will mark the order as shipped and complete the workflow. L. Store new order information in Amazon EF M. Have instances pull the new information from the NFS and send that information to printers in the warehous N. Once the label has been scanned, as it leaves the warehouse, have Amazon API Gateway call the instances to remove the order information from Amazon EFS. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "36",
    "question": "- (Exam Topic 1) A start up company hosts a fleet of Amazon EC2 instances in private subnets using the latest Amazon Linux 2 AMI. The company's engineers rely heavily on SSH access to the instances for troubleshooting. The company's existing architecture includes the following: • A VPC with private and public subnets, and a NAT gateway • Site-to-Site VPN for connectivity with the on-premises environment • EC2 security groups with direct SSH access from the on-premises environment The company needs to increase security controls around SSH access and provide auditing of commands executed by the engineers. Which strategy should a solutions architect use? A. Install and configure EC2 instance Connect on the fleet of EC2 instance B. Remove all security group rules attached to EC2 instances that allow inbound TCP on port 22. Advise the engineers to remotely access the instances by using the EC2 Instance Connect CLI. C. Update the EC2 security groups to only allow inbound TCP on port 22 to the IP addresses of the engineer's device D. Install the Amazon CloudWatch agent on all EC2 instances and send operating system audit logs to CloudWatch Logs. E. Update the EC2 security groups to only allow inbound TCP on port 22 to the IP addresses of the engineer's device F. Enable AWS Config for EC2 security group resource change G. Enable AWS Firewall Manager and apply a security group policy that automatically remediates changes to rules. H. Create an IAM role with the Ama2onSSMManagedlnstanceCore managed policy attache I. Attach the IAM role to all the EC2 instance J. Remove all security group rules attached to the EC2 K. instances that allow inbound TCP on port 22. Have the engineers install the AWS Systems Manager Session Manager plugin for their devices and remotely access the instances by using the start-session API call from Systems Manager. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Install and configure EC2 instance Connect on the fleet of EC2 instance",
      "B": "Remove all security group rules attached to EC2 instances that allow inbound TCP on port 22. Advise the engineers to remotely access the instances by using the EC2 Instance Connect CLI.",
      "C": "Update the EC2 security groups to only allow inbound TCP on port 22 to the IP addresses of the engineer's device",
      "D": "Install the Amazon CloudWatch agent on all EC2 instances and send operating system audit logs to CloudWatch Logs.",
      "E": "Update the EC2 security groups to only allow inbound TCP on port 22 to the IP addresses of the engineer's device",
      "F": "Enable AWS Config for EC2 security group resource change",
      "G": "Enable AWS Firewall Manager and apply a security group policy that automatically remediates changes to rules.",
      "H": "Create an IAM role with the Ama2onSSMManagedlnstanceCore managed policy attache",
      "I": "Attach the IAM role to all the EC2 instance",
      "J": "Remove all security group rules attached to the EC2 K. instances that allow inbound TCP on port 22. Have the engineers install the AWS Systems Manager Session Manager plugin for their devices and remotely access the instances by using the start-session API call from Systems Manager. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "101.2",
    "question": "- (Exam Topic 1) A company wants to migrate a 30 TB Oracle data warehouse from on premises to Amazon Redshift The company used the AWS Schema Conversion Tool (AWS SCT) to convert the schema of the existing data warehouse to an Amazon Redshift schema The company also used a migration assessment report to identify manual tasks to complete. The company needs to migrate the data to the new Amazon Redshift cluster during an upcoming data freeze period of 2 weeks The only network connection between the on-premises data warehouse and AWS is a 50 Mops internet connection Which migration strategy meets these requirements? A. Create an AWS Database Migration Service (AWS DMS) replication instanc B. Authorize the public IP address of the replication instance to reach the data warehouse through the corporate firewall Create a migration task to run at the beginning of the data freeze period. C. Install the AWS SCT extraction agents on the on-premises server D. Define the extract, upload, and copy tasks to send the data to an Amazon S3 bucke E. Copy the data into the Amazon Redshift cluste F. Run the tasks at the beginning of the data freeze period. G. install the AWS SCT extraction agents on the on-premises server H. Create a Site-to-Site VPN connection Create an AWS Database Migration Service (AWS DMS) replication instance that is the appropriate size Authorize the IP address of the replication instance to be able to access the on-premises data warehouse through the VPN connection I. Create a job in AWS Snowball Edge to import data into Amazon S3 Install AWS SCT extraction agents on the on-premises servers Define the local and AWS Database Migration Service (AWS DMS) tasks to send the data to the Snowball Edge device When the Snowball Edge device is returned to AWS and the data is available in Amazon S3, run the AWS DMS subtask to copy the data to Amazon Redshift. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an AWS Database Migration Service (AWS DMS) replication instanc",
      "B": "Authorize the public IP address of the replication instance to reach the data warehouse through the corporate firewall Create a migration task to run at the beginning of the data freeze period.",
      "C": "Install the AWS SCT extraction agents on the on-premises server",
      "D": "Define the extract, upload, and copy tasks to send the data to an Amazon S3 bucke",
      "E": "Copy the data into the Amazon Redshift cluste",
      "F": "Run the tasks at the beginning of the data freeze period.",
      "G": "install the AWS SCT extraction agents on the on-premises server",
      "H": "Create a Site-to-Site VPN connection Create an AWS Database Migration Service (AWS DMS) replication instance that is the appropriate size Authorize the IP address of the replication instance to be able to access the on-premises data warehouse through the VPN connection",
      "I": "Create a job in AWS Snowball Edge to import data into Amazon S3 Install AWS SCT extraction agents on the on-premises servers Define the local and AWS Database Migration Service (AWS DMS) tasks to send the data to the Snowball Edge device When the Snowball Edge device is returned to AWS and the data is available in Amazon S3, run the AWS DMS subtask to copy the data to Amazon Redshift. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "AWS Database Migration Service (AWS DMS) can use Snowball Edge and Amazon S3 to migrate large databases more quickly than by other methods\nhttps://docs.aws.amazon.com/dms/latest/userguide/CHAP_LargeDBs.html\nhttps://www.calctool.org/CALC/prof/computing/transfer_time\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "106",
    "question": "- (Exam Topic 1) A company runs an application on AWS. An AWS Lambda function uses credentials to authenticate to an Amazon RDS tor MySQL DB instance. A security risk assessment identified that these credentials are not frequently rotated. Also, encryption at rest is not enabled for the DB instance. The security team requires that both of these issues be resolved. Which strategy should a solutions architect recommend to remediate these security risks? A. Configure the Lambda function to store and retrieve the database credentials in AWS Secrets Manager and enable rotation of the credential B. Take a snapshot ol the DB instance and encrypt a copy of that snapsho C. Replace the DB instance with a new DB instance that is based on the encrypted snapshot. D. Enable IAM DB authentication on the DB instanc E. Grant the Lambda execution role access to the DB instanc F. Modify the DB instance and enable encryption. G. Enable IAM DB authentication on the DB instanc H. Grant the Lambda execution role access to the DB instanc I. Create an encrypted read replica of the DB instanc J. Promote Ihe encrypted read replica to be the new primary node. K. Configure the Lambda function to store and retrieve the database credentials as encrypted AWS Systems Manager Parameter Store parameter L. Create another Lambda function to automatically rotate the credential M. Create an encrypted read replica of the DB instanc N. Promote the encrypted read replica to be the new primary node. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure the Lambda function to store and retrieve the database credentials in AWS Secrets Manager and enable rotation of the credential",
      "B": "Take a snapshot ol the DB instance and encrypt a copy of that snapsho",
      "C": "Replace the DB instance with a new DB instance that is based on the encrypted snapshot.",
      "D": "Enable IAM DB authentication on the DB instanc",
      "E": "Grant the Lambda execution role access to the DB instanc",
      "F": "Modify the DB instance and enable encryption.",
      "G": "Enable IAM DB authentication on the DB instanc",
      "H": "Grant the Lambda execution role access to the DB instanc",
      "I": "Create an encrypted read replica of the DB instanc",
      "J": "Promote Ihe encrypted read replica to be the new primary node. K. Configure the Lambda function to store and retrieve the database credentials as encrypted AWS Systems Manager Parameter Store parameter L. Create another Lambda function to automatically rotate the credential M. Create an encrypted read replica of the DB instanc N. Promote the encrypted read replica to be the new primary node. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": "Parameter store can store DB credentials as secure string but CANNOT rotate secrets, hence, go with A + Cannot enable encryption on existing MySQL RDS\ninstance, must create a new encrypted one from unencrypted snapshot.\nhttps://aws.amazon.com/blogs/security/rotate-amazon-rds-database-credentials-automatically-with-aws-secrets- Encrypting a unencrypted instance of DB or\ncreating a encrypted replica of an un encrypted DB instance are not possible Hence A is the only solution possible.\nhttps://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html#Overview.Encryption.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "109.2",
    "question": "- (Exam Topic 1) A company needs to implement a patching process for its servers. The on-premises servers and Amazon EC2 instances use a variety of tools to perform patching. Management requires a single report showing the patch status of all the servers and instances. Which set of actions should a solutions architect take to meet these requirements? A. Use AWS Systems Manager to manage patches on the on-premises servers and EC2 instance B. Use Systems Manager to generate patch compliance reports. C. Use AWS OpsWorks to manage patches on the on-premises servers and EC2 instance D. Use Amazon OuickSight integration with OpsWorks to generate patch compliance reports. E. Use an Amazon EventBridge (Amazon CloudWatch Events) rule to apply patches by scheduling an AWS Systems Manager patch remediation jo F. Use Amazon Inspector to generate patch compliance reports. G. Use AWS OpsWorks to manage patches on the on-premises servers and EC2 instance H. Use AWS X-Ray to post the patch status to AWS Systems Manager OpsCenter to generate patch compliance reports. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS Systems Manager to manage patches on the on-premises servers and EC2 instance",
      "B": "Use Systems Manager to generate patch compliance reports.",
      "C": "Use AWS OpsWorks to manage patches on the on-premises servers and EC2 instance",
      "D": "Use Amazon OuickSight integration with OpsWorks to generate patch compliance reports.",
      "E": "Use an Amazon EventBridge (Amazon CloudWatch Events) rule to apply patches by scheduling an AWS Systems Manager patch remediation jo",
      "F": "Use Amazon Inspector to generate patch compliance reports.",
      "G": "Use AWS OpsWorks to manage patches on the on-premises servers and EC2 instance",
      "H": "Use AWS X-Ray to post the patch status to AWS Systems Manager OpsCenter to generate patch compliance reports. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "110",
    "question": "- (Exam Topic 2) A company is in the process of implementing AWS Organizations to constrain its developers to use only Amazon EC2. Amazon S3 and Amazon DynamoDB. The developers account resides In a dedicated organizational unit (OU). The solutions architect has implemented the following SCP on the developers account: { \"Version\": \"2012-10-17\", \"Statement\": [ { \"Sid\": \"AllowEC2\", \"Effect\": \"Allow\", \"Action\": \"ec2:*\", \"Resource\": \"*\" }, { \"Sid\": \"AllowDynamoDB\", \"Effect\": \"Allow\", \"Action\": \"dynamodb:*\", \"Resource\": \"*\" }, { \"Sid\": \"AllowS3\", \"Effect\": \"Allow\", \"Action\": \"s3:*\", \"Resource\": \"*\" } ] } When this policy is deployed, IAM users in the developers account are still able to use AWS services that are not listed in the policy. What should the solutions architect do to eliminate the developers' ability to use services outside the scope of this policy? A. Create an explicit deny statement for each AWS service that should be constrained B. Remove the Full AWS Access SCP from the developer account's OU C. Modify the Full AWS Access SCP to explicitly deny all services D. Add an explicit deny statement using a wildcard to the end of the SCP -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an explicit deny statement for each AWS service that should be constrained",
      "B": "Remove the Full AWS Access SCP from the developer account's OU",
      "C": "Modify the Full AWS Access SCP to explicitly deny all services",
      "D": "Add an explicit deny statement using a wildcard to the end of the SCP -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "111",
    "question": "- (Exam Topic 2) A company is migrating its marketing website and content management system from an on-premises data center to AWS. The company wants the AWS application to be deployed in a VPC with Amazon EC2 instances used for the web servers and an Amazon RDS instance for the database. The company has a runbook document that describes the installation process of the on-premises system. The company would like to base the AWS system on the processes referenced in the runbook document. The runbook document describes the installation and configuration of the operating systems, network settings, the website, and content management system software on the servers After the migration is complete, the company wants to be able to make changes quickly to take advantage of other AWS features. How can the application and environment be deployed and automated m AWS. while allowing for future changes? A. Update the runbook to describe how to create the VP B. the EC2 instances and the RDS instance for the application by using the AWS Console Make sure that the rest of the steps in the runbook are updated to reflect any changes that may come from the AWS migration C. Write a Python script that uses the AWS API to create the VP D. the EC2 instances and the RDS instance for the application Write shell scripts that implement the rest of the steps in the runbook Have the Python script copy and run the shell scripts on the newly created instances to complete the installation E. Write an AWS Cloud Formation template that creates the VPC, the EC2 instances, and the RDS instance for the application Ensure that the rest of the steps in the runbook are updated to reflect any changes that may come from the AWS migration F. Write an AWS CloudFormation template that creates the VPC the EC2 instances, and the RDS instance for the application Include EC2 user data in the AWS Cloud Formation template to install and configure the software. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Update the runbook to describe how to create the VP",
      "B": "the EC2 instances and the RDS instance for the application by using the AWS Console Make sure that the rest of the steps in the runbook are updated to reflect any changes that may come from the AWS migration",
      "C": "Write a Python script that uses the AWS API to create the VP",
      "D": "the EC2 instances and the RDS instance for the application Write shell scripts that implement the rest of the steps in the runbook Have the Python script copy and run the shell scripts on the newly created instances to complete the installation",
      "E": "Write an AWS Cloud Formation template that creates the VPC, the EC2 instances, and the RDS instance for the application Ensure that the rest of the steps in the runbook are updated to reflect any changes that may come from the AWS migration",
      "F": "Write an AWS CloudFormation template that creates the VPC the EC2 instances, and the RDS instance for the application Include EC2 user data in the AWS Cloud Formation template to install and configure the software. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "115",
    "question": "- (Exam Topic 2) A company that develops consumer electronics with offices in Europe and Asia has 60 TB of software images stored on premises in Europe. The company wants to transfer the images to an Amazon S3 bucket in the ap-northeast-1 Region. New software images are created daily and must be encrypted in transit. The company needs a solution that does not require custom development to automatically transfer all existing and new software images to Amazon S3. What is the next step in the transfer process? A. Deploy an AWS DataSync agent and configure a task to transfer the images to the S3 bucket. B. Configure Amazon Kinesis Data Firehose to transfer the images using S3 Transfer Acceleration. C. Use an AWS Snowball device to transfer the images with the S3 bucket as the target. D. Transfer the images over a Site-to-Site VPN connection using the S3 API with multipart upload. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy an AWS DataSync agent and configure a task to transfer the images to the S3 bucket.",
      "B": "Configure Amazon Kinesis Data Firehose to transfer the images using S3 Transfer Acceleration.",
      "C": "Use an AWS Snowball device to transfer the images with the S3 bucket as the target.",
      "D": "Transfer the images over a Site-to-Site VPN connection using the S3 API with multipart upload. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "119.2",
    "question": "- (Exam Topic 2) A company has developed a new billing application that will be released in two weeks. Developers are testing the application running on 10 EC2 instances managed by an Auto Scaling group in subnet 172.31.0.0/24 within VPC A with CIDR block 172.31.0.0/16. The developers noticed connection timeout errors in the application logs while connecting to an Oracle database running on an Amazon EC2 instance in the same region within VPC B with CIDR block 172.50.0.0/16. The IP of the database instance is hard-coded in the application instances. Which recommendations should a solutions architect present to the developers to solve the problem in a secure way with minimal maintenance and overhead'' A. Disable the SrcDestCheck attribute for all instances running the application and Oracle Database.Change the default route of VPC A to point ENI of the Oracle Database that has an IP address assigned within the range of 172.50.0.0/16 B. Create and attach internet gateways for both VPC C. Configure default routes to the internet gateways for both VPC D. Assign an Elastic IP for each Amazon EC2 instance in VPC A E. Create a VPC peering connection between the two VPCs and add a route to the routing table of VPC A that points to the IP address range of 172.50.0.0/16 F. Create an additional Amazon EC2 instance for each VPC as a customer gateway; create one virtual private gateway (VGW) for each VP G. configure an end-to-end VPC, and advertise the routes for 172.50.0.0/16 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Disable the SrcDestCheck attribute for all instances running the application and Oracle Database.Change the default route of VPC A to point ENI of the Oracle Database that has an IP address assigned within the range of 172.50.0.0/16",
      "B": "Create and attach internet gateways for both VPC",
      "C": "Configure default routes to the internet gateways for both VPC",
      "D": "Assign an Elastic IP for each Amazon EC2 instance in VPC A",
      "E": "Create a VPC peering connection between the two VPCs and add a route to the routing table of VPC A that points to the IP address range of 172.50.0.0/16",
      "F": "Create an additional Amazon EC2 instance for each VPC as a customer gateway; create one virtual private gateway (VGW) for each VP",
      "G": "configure an end-to-end VPC, and advertise the routes for 172.50.0.0/16 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "124.2",
    "question": "- (Exam Topic 2) A company is running a two-tier web-based application in an on-premises data center. The application layer consists of a single server running a stateful application. The application connects to a PostgreSQL database running on a separate server The application's user base is expected to grow significantly, so the company is migrating the application and database to AWS The solution will use Amazon Aurora PostgreSQL. Amazon EC2 Auto Scaling, and Elastic Load Balancing. Which solution will provide a consistent user experience that will allow the application and database tiers to scale? A. Enable Aurora Auto Scaling for Aurora Replica B. Use a Network Load Balancer with the least outstanding requests routing algorithm and sticky sessions enabled C. Enable Aurora Auto Scaling for Aurora writer D. Use an Application Load Balancer with the round robin routing algorithm and sticky sessions enabled E. Aurora Auto Scaling for Aurora Replica F. Use an Application Load Balancer with the round robin routing algorithm and sticky sessions enabled. G. Aurora Auto Scaling for Aurora writer H. Use a Network Load Balancer with the least outstanding requests routing algorithm and sticky sessions enabled. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Enable Aurora Auto Scaling for Aurora Replica",
      "B": "Use a Network Load Balancer with the least outstanding requests routing algorithm and sticky sessions enabled",
      "C": "Enable Aurora Auto Scaling for Aurora writer",
      "D": "Use an Application Load Balancer with the round robin routing algorithm and sticky sessions enabled",
      "E": "Aurora Auto Scaling for Aurora Replica",
      "F": "Use an Application Load Balancer with the round robin routing algorithm and sticky sessions enabled.",
      "G": "Aurora Auto Scaling for Aurora writer",
      "H": "Use a Network Load Balancer with the least outstanding requests routing algorithm and sticky sessions enabled. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "136",
    "question": "- (Exam Topic 2) A company wants to use Amazon Workspaces in combination with thin client devices to replace aging desktops Employees use the desktops to access applications that work with clinical trial data Corporate security policy states that access to the applications must be restricted to only company branch office locations. The company is considering adding an additional branch office in the next 6 months. Which solution meets these requirements with the MOST operational efficiency? A. Create an IP access control group rule with the list of public addresses from the branch offices Associate the IP access control group with the Workspaces directory B. Use AWS Firewall Manager to create a web ACL rule with an IPSet with the list of public addresses from the branch office locations Associate the web ACL with the Workspaces directory C. Use AWS Certificate Manager (ACM) to issue trusted device certificates to the machines deployed in the branch office locations Enable restricted access on the Workspaces directory D. Create a custom Workspace image with Windows Firewall configured to restrict access to the public addresses of the branch offices Use the image to deploy the Workspaces. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an IP access control group rule with the list of public addresses from the branch offices Associate the IP access control group with the Workspaces directory",
      "B": "Use AWS Firewall Manager to create a web ACL rule with an IPSet with the list of public addresses from the branch office locations Associate the web ACL with the Workspaces directory",
      "C": "Use AWS Certificate Manager (ACM) to issue trusted device certificates to the machines deployed in the branch office locations Enable restricted access on the Workspaces directory",
      "D": "Create a custom Workspace image with Windows Firewall configured to restrict access to the public addresses of the branch offices Use the image to deploy the Workspaces. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "139.2",
    "question": "- (Exam Topic 2) A retail company is running an application that stores invoice files in an Amazon S3 bucket and metadata about the files in an Amazon DynamoDB table. The application software runs in both us-east-1 and eu-west-1 The S3 bucket and DynamoDB table are in us-east-1. The company wants to protect itself from data corruption and loss of connectivity to either Region Which option meets these requirements? A. Create a DynamoDB global table to replicate data between us-east-1 and eu-west-1. Enable continuous backup on the DynamoDB table in us-east-1. Enable versioning on the S3 bucket B. Create an AWS Lambda function triggered by Amazon CloudWatch Events to make regular backups of the DynamoDB table Set up S3 cross-region replication from us-east-1 to eu-west-1 Set up MFA delete on the S3 bucket in us-east-1. C. Create a DynamoDB global table to replicate data between us-east-1 and eu-west-1. Enable versioning on the S3 bucket Implement strict ACLs on the S3 bucket D. Create a DynamoDB global table to replicate data between us-east-1 and eu-west-1. Enable continuous backup on the DynamoDB table in us-east-1. Set up S3 cross-region replication from us-east-1 toeu-west-1. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a DynamoDB global table to replicate data between us-east-1 and eu-west-1. Enable continuous backup on the DynamoDB table in us-east-1. Enable versioning on the S3 bucket",
      "B": "Create an AWS Lambda function triggered by Amazon CloudWatch Events to make regular backups of the DynamoDB table Set up S3 cross-region replication from us-east-1 to eu-west-1 Set up MFA delete on the S3 bucket in us-east-1.",
      "C": "Create a DynamoDB global table to replicate data between us-east-1 and eu-west-1. Enable versioning on the S3 bucket Implement strict ACLs on the S3 bucket",
      "D": "Create a DynamoDB global table to replicate data between us-east-1 and eu-west-1. Enable continuous backup on the DynamoDB table in us-east-1. Set up S3 cross-region replication from us-east-1 toeu-west-1. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "141.2",
    "question": "- (Exam Topic 2) A Solutions Architect is constructing a containerized.NET Core application for AWS Fargate. The application's backend needs a high-availability version of Microsoft SQL Server. All application levels must be extremely accessible. The credentials associated with the SQL Server connection string should not be saved to disk inside the.NET Core front-end containers. Which tactics should the Solutions Architect use to achieve these objectives? A. Set up SQL Server to run in Fargate with Service Auto Scalin B. Create an Amazon ECS task execution role that allows the Fargate task definition to get the secret value for the credentials to SQL Server running in Fargat C. Specify the ARN of the secret in AWS Secrets Manager in the secrets section of the Fargate task definition so the sensitive data can be injected into the containers as environment variables on startup for reading into the application to construct the connection strin D. Set up the .NET Core service using Service Auto Scaling behind an Application Load Balancer in multiple Availability Zones. E. Create a Multi-AZ deployment of SQL Server on Amazon RD F. Create a secret in AWS Secrets Manager for the credentials to the RDS databas G. Create an Amazon ECS task execution role that allows the Fargate task definition to get the secret value for the credentials to the RDS database in Secrets Manage H. Specify the ARN of the secret in Secrets Manager in the secrets section of the Fargate task definition so the sensitive data can be injected into the containers as environment variables on startup for reading into the application to construct the connection strin I. Set up the .NET Core service in Fargate using Service Auto Scaling behind an Application Load Balancer in multiple Availability Zones. J. Create an Auto Scaling group to run SQL Server on Amazon EC2. Create a secret in AWS Secrets Manager for the credentials to SQL Server running on EC2. Create an Amazon ECS task execution role that allows the Fargate task definition to get the secret value for the credentials to SQL Server on EC2. Specify the ARN of the secret in Secrets Manager in the secrets section of the Fargate task definition so the sensitive data can be injected into the containers as environment variables on startup for reading into the application to construct the connection strin K. Set up the .NET Core service using Service Auto Scaling behind an Application Load Balancer in multiple Availability Zones. L. Create a Multi-AZ deployment of SQL Server on Amazon RD M. Create a secret in AWS Secrets Manager for the credentials to the RDS databas N. Create non- persistent empty storage for the .NET Core containers in the Fargate task definition to store the sensitive informatio O. Create an Amazon ECS task execution role that allows the Fargate task definition to get the secret value for the credentials to the RDS database in Secrets Manage P. Specify the ARN of the secret in Secrets Manager in the secrets section of the Fargate task definition so the sensitive data can be written to the non-persistent empty storage on startup for reading into the application to construct the connection strin Q. Set up the .NET Core service using Service Auto Scaling behind an Application Load Balancer in multiple Availability Zones. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Set up SQL Server to run in Fargate with Service Auto Scalin",
      "B": "Create an Amazon ECS task execution role that allows the Fargate task definition to get the secret value for the credentials to SQL Server running in Fargat",
      "C": "Specify the ARN of the secret in AWS Secrets Manager in the secrets section of the Fargate task definition so the sensitive data can be injected into the containers as environment variables on startup for reading into the application to construct the connection strin",
      "D": "Set up the .NET Core service using Service Auto Scaling behind an Application Load Balancer in multiple Availability Zones.",
      "E": "Create a Multi-AZ deployment of SQL Server on Amazon RD",
      "F": "Create a secret in AWS Secrets Manager for the credentials to the RDS databas",
      "G": "Create an Amazon ECS task execution role that allows the Fargate task definition to get the secret value for the credentials to the RDS database in Secrets Manage",
      "H": "Specify the ARN of the secret in Secrets Manager in the secrets section of the Fargate task definition so the sensitive data can be injected into the containers as environment variables on startup for reading into the application to construct the connection strin",
      "I": "Set up the .NET Core service in Fargate using Service Auto Scaling behind an Application Load Balancer in multiple Availability Zones.",
      "J": "Create an Auto Scaling group to run SQL Server on Amazon EC2. Create a secret in AWS Secrets Manager for the credentials to SQL Server running on EC2. Create an Amazon ECS task execution role that allows the Fargate task definition to get the secret value for the credentials to SQL Server on EC2. Specify the ARN of the secret in Secrets Manager in the secrets section of the Fargate task definition so the sensitive data can be injected into the containers as environment variables on startup for reading into the application to construct the connection strin K. Set up the .NET Core service using Service Auto Scaling behind an Application Load Balancer in multiple Availability Zones. L. Create a Multi-AZ deployment of SQL Server on Amazon RD M. Create a secret in AWS Secrets Manager for the credentials to the RDS databas N. Create non- persistent empty storage for the .NET Core containers in the Fargate task definition to store the sensitive informatio O. Create an Amazon ECS task execution role that allows the Fargate task definition to get the secret value for the credentials to the RDS database in Secrets Manage P. Specify the ARN of the secret in Secrets Manager in the secrets section of the Fargate task definition so the sensitive data can be written to the non-persistent empty storage on startup for reading into the application to construct the connection strin Q. Set up the .NET Core service using Service Auto Scaling behind an Application Load Balancer in multiple Availability Zones. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "Secrets Manager natively supports SQL Server on RDS. No real need to create additional 'ephemeral storage' to fetch credentials, as these can be injected to\ncontainers as environment variables. https://aws.amazon.com/premiumsupport/knowledge-center/ecs-data-security-container-task/\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "143",
    "question": "- (Exam Topic 2) A company has an on-premises monitoring solution using a PostgreSQL database for persistence of events. The database is unable to scale due to heavy ingestion and it frequently runs out of storage. The company wants to create a hybrid solution and has already set up a VPN connection between its network and AWS. The solution should include the following attributes: • Managed AWS services to minimize operational complexity • A buffer that automatically scales to match the throughput of data and requires no on-going administration. • A visualization toot to create dashboards to observe events in near-real time. • Support for semi -structured JSON data and dynamic schemas. Which combination of components will enabled© company to create a monitoring solution that will satisfy these requirements'' (Select TWO.) A. Use Amazon Kinesis Data Firehose to buffer events Create an AWS Lambda function 10 process and transform events B. Create an Amazon Kinesis data stream to buffer events Create an AWS Lambda function to process and transform evens C. Configure an Amazon Aurora PostgreSQL DB cluster to receive events Use Amazon Quick Sight to read from the database and create near-real-time visualizations and dashboards D. Configure Amazon Elasticsearch Service (Amazon ES) to receive events Use the Kibana endpoint deployed with Amazon ES to create near-real-time visualizations and dashboards. E. Configure an Amazon Neptune 0 DB instance to receive events Use Amazon QuickSight to read from the database and create near-real-time visualizations and dashboards -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use Amazon Kinesis Data Firehose to buffer events Create an AWS Lambda function 10 process and transform events",
      "B": "Create an Amazon Kinesis data stream to buffer events Create an AWS Lambda function to process and transform evens",
      "C": "Configure an Amazon Aurora PostgreSQL DB cluster to receive events Use Amazon Quick Sight to read from the database and create near-real-time visualizations and dashboards",
      "D": "Configure Amazon Elasticsearch Service (Amazon ES) to receive events Use the Kibana endpoint deployed with Amazon ES to create near-real-time visualizations and dashboards.",
      "E": "Configure an Amazon Neptune 0 DB instance to receive events Use Amazon QuickSight to read from the database and create near-real-time visualizations and dashboards -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D",
      "E"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "146.2",
    "question": "- (Exam Topic 2) A solutions architect has been assigned to migrate a 50 TB Oracle data warehouse that contains sales data from on-premises to Amazon Redshift Major updates to the sales data occur on the final calendar day of the month For the remainder of the month, the data warehouse only receives minor daily updates and is primarily used for reading and reporting Because of this the migration process must start on the first day of the month and must be complete before the next set of updates occur. This provides approximately 30 days to complete the migration and ensure that the minor daily changes have been synchronized with the Amazon Redshift data warehouse Because the migration cannot impact normal business network operations, the bandwidth allocated to the migration for moving data over the internet is 50 Mbps The company wants to keep data migration costs low Which steps will allow the solutions architect to perform the migration within the specified timeline? A. Install Oracle database software on an Amazon EC2 instance Configure VPN connectivity between AWS and the company's data center Configure the Oracle database running on Amazon EC2 to join the Oracle Real Application Clusters (RAC) When the Oracle database on Amazon EC2 finishes synchronizing, create an AWS DMS ongoing replication task to migrate the data from the Oracle database on Amazon EC2 to Amazon Redshift Verify the data migration is complete and perform the cut over to Amazon Redshift. B. Create an AWS Snowball import job Export a backup of the Oracle data warehouse Copy the exported data to the Snowball device Return the Snowball device to AWS Create an Amazon RDS for Oracle database and restore the backup file to that RDS instance Create an AWS DMS task to migrate the data from the RDS for Oracle database to Amazon Redshift Copy daily incremental backups from Oracle in the data center to the RDS for Oracle database over the internet Verify the data migration is complete and perform the cut over to Amazon Redshift. C. Install Oracle database software on an Amazon EC2 instance To minimize the migration time configure VPN connectivity between AWS and the company's data center by provisioning a 1 Gbps AWS Direct Connect connection Configure the Oracle database running on Amazon EC2 to be a read replica of the data center Oracle database Start the synchronization process between the company's on-premises data center and the Oracle database on Amazon EC2 When the Oracle database on Amazon EC2 is synchronized with the on-premises database create an AWS DMS ongoing replication task from the Oracle database read replica that is running on Amazon EC2 to Amazon Redshift Verify the data migration is complete and perform the cut over to Amazon Redshift. D. Create an AWS Snowball import jo E. Configure a server in the company€TMs data center with an extraction agen F. Use AWS SCT to manage the extraction agent and convert the Oracle schema to an Amazon Redshift schem G. Create a new project in AWS SCT using the registered data extraction agen H. Create a local task and an AWS DMS task in AWS SCT with replication of ongoing change I. Copy data to the Snowball device and return the Snowball device to AW J. Allow AWS DMS to copy data from Amazon S3 to Amazon Redshif K. Verify that the data migration is complete and perform the cut over to Amazon Redshift. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Install Oracle database software on an Amazon EC2 instance Configure VPN connectivity between AWS and the company's data center Configure the Oracle database running on Amazon EC2 to join the Oracle Real Application Clusters (RAC) When the Oracle database on Amazon EC2 finishes synchronizing, create an AWS DMS ongoing replication task to migrate the data from the Oracle database on Amazon EC2 to Amazon Redshift Verify the data migration is complete and perform the cut over to Amazon Redshift.",
      "B": "Create an AWS Snowball import job Export a backup of the Oracle data warehouse Copy the exported data to the Snowball device Return the Snowball device to AWS Create an Amazon RDS for Oracle database and restore the backup file to that RDS instance Create an AWS DMS task to migrate the data from the RDS for Oracle database to Amazon Redshift Copy daily incremental backups from Oracle in the data center to the RDS for Oracle database over the internet Verify the data migration is complete and perform the cut over to Amazon Redshift.",
      "C": "Install Oracle database software on an Amazon EC2 instance To minimize the migration time configure VPN connectivity between AWS and the company's data center by provisioning a 1 Gbps AWS Direct Connect connection Configure the Oracle database running on Amazon EC2 to be a read replica of the data center Oracle database Start the synchronization process between the company's on-premises data center and the Oracle database on Amazon EC2 When the Oracle database on Amazon EC2 is synchronized with the on-premises database create an AWS DMS ongoing replication task from the Oracle database read replica that is running on Amazon EC2 to Amazon Redshift Verify the data migration is complete and perform the cut over to Amazon Redshift.",
      "D": "Create an AWS Snowball import jo",
      "E": "Configure a server in the company€TMs data center with an extraction agen",
      "F": "Use AWS SCT to manage the extraction agent and convert the Oracle schema to an Amazon Redshift schem",
      "G": "Create a new project in AWS SCT using the registered data extraction agen",
      "H": "Create a local task and an AWS DMS task in AWS SCT with replication of ongoing change",
      "I": "Copy data to the Snowball device and return the Snowball device to AW",
      "J": "Allow AWS DMS to copy data from Amazon S3 to Amazon Redshif K. Verify that the data migration is complete and perform the cut over to Amazon Redshift. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "Create an AWS Snowball import job. Configure a server in the company€TMs data center with an extraction agent. Use AWS SCT to manage the extraction agent\nand convert the Oracle schema to an Amazon Redshift schema. Create a new project in AWS SCT using the registered data extraction agent. Create a local task\nand an AWS DMS task in AWS SCT with replication of ongoing changes. Copy data to the Snowball device and return the Snowball device to AWS. Allow AWS\nDMS to copy data from Amazon S3 to Amazon Redshift. Verify that the data migration is complete and perform the cut over to Amazon Redshift.\nhttps://aws.amazon.com/getting-started/hands-on/migrate-oracle-to-amazon-redshift/\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "148",
    "question": "- (Exam Topic 2) A software development company has multiple engineers who are working remotely. The company is running Active Directory Domain Services (AD DS) on an Amazon EC2 instance. The company's security policy states that all internal, nonpublic services that are deployed in a VPC must be accessible through a VPN Multi-factor authentication (MFA) must be used for access to a VPN. Whet should a solution architect do to meet these requirements? A. Create an AWS Site-to-Site VPN connection Configure integration between a VPN and AD D B. Use an Amazon Workspaces client with MFA support enabled to establish a VPN connection. C. Create an AWS Client VPN endpoint Create an AD Connector directory for integration with AD DS Enable MFA for AD Connector Use AWS Client VPN to establish a VPN connection. D. Create multiple AWS Site-to-Site VPN connections by using AWS VPN CloudHub Configure integration between AWS VPN CloudHub and AD DS Use AWS Cop4ot to establish a VPN connection. E. Create an Amazon WorkLink endpoint Configure integration between Amazon WorkLink and AD D F. Enable MFA in Amazon WorkLink Use AWS Client VPN to establish a VPN connection. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an AWS Site-to-Site VPN connection Configure integration between a VPN and AD D",
      "B": "Use an Amazon Workspaces client with MFA support enabled to establish a VPN connection.",
      "C": "Create an AWS Client VPN endpoint Create an AD Connector directory for integration with AD DS Enable MFA for AD Connector Use AWS Client VPN to establish a VPN connection.",
      "D": "Create multiple AWS Site-to-Site VPN connections by using AWS VPN CloudHub Configure integration between AWS VPN CloudHub and AD DS Use AWS Cop4ot to establish a VPN connection.",
      "E": "Create an Amazon WorkLink endpoint Configure integration between Amazon WorkLink and AD D",
      "F": "Enable MFA in Amazon WorkLink Use AWS Client VPN to establish a VPN connection. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "165",
    "question": "- (Exam Topic 2) A company operates quick-service restaurants. The restaurants follow a predictable model with high sales traffic for -4 hours daily Sates traffic is lower outside of those peak hours. The point of sale and management platform is deployed in the AWS Cloud and has a backend that is based or Amazon DynamoDB The database table uses provisioned throughput mode with 100.000 RCUs and 80.000 WCUs to match Known peak resource consumption. The company wants to reduce its DynamoDB cost and minimize the operational overhead for the IT staff. Which solution meets these requirements MOST cost- effectively? A. Reduce the provisioned RCUs and WCUs B. Change the DynamoDB table to use on-demand capacity C. Enable Dynamo DB auto seating for the table. D. Purchase 1-year reserved capacity that is sufficient to cover the peak load for 4 hours each day. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Reduce the provisioned RCUs and WCUs",
      "B": "Change the DynamoDB table to use on-demand capacity",
      "C": "Enable Dynamo DB auto seating for the table.",
      "D": "Purchase 1-year reserved capacity that is sufficient to cover the peak load for 4 hours each day. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "170.2",
    "question": "- (Exam Topic 2) A company is running an application in the AWS Cloud. The company's security team must approve the creation of all new IAM users. When a new 1AM user is created, all access for the user must be removed automatically. The security team must then receive a notification to approve the user. The company has a multi- Region AWS CloudTrail trail In the AWS account. Which combination of steps will meet these requirements? (Select THREE.) A. Create an Amazon EventBridge (Amazon CloudWatch Events) rul B. Define a pattern with the detail-type value set to AWS API Call via CloudTrail and an eventName of CreateUser. C. Configure CloudTrail to send a notification for the CreateUser event to an Amazon Simple Notification Service (Amazon SNS) topic. D. Invoke a container that runs in Amazon Elastic Container Service (Amazon ECS) with AWS Fargatetechnology to remove access E. Invoke an AWS Step Functions state machine to remove access. F. Use Amazon Simple Notification Service (Amazon SNS) to notify the security team. G. Use Amazon Pinpoint to notify the security team. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an Amazon EventBridge (Amazon CloudWatch Events) rul",
      "B": "Define a pattern with the detail-type value set to AWS API Call via CloudTrail and an eventName of CreateUser.",
      "C": "Configure CloudTrail to send a notification for the CreateUser event to an Amazon Simple Notification Service (Amazon SNS) topic.",
      "D": "Invoke a container that runs in Amazon Elastic Container Service (Amazon ECS) with AWS Fargatetechnology to remove access",
      "E": "Invoke an AWS Step Functions state machine to remove access.",
      "F": "Use Amazon Simple Notification Service (Amazon SNS) to notify the security team.",
      "G": "Use Amazon Pinpoint to notify the security team. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "B",
      "E"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "175.3",
    "question": "- (Exam Topic 2) A financial services company loaded millions of historical stock trades into an Amazon DynamoDB table The table uses on-demand capacity mode Once each day at midnight, a few million new records are loaded into the table Application read activity against the table happens in bursts throughout the day, and a limited set of keys are repeatedly looked up. The company needs to reduce costs associated with DynamoDB. Which strategy should a solutions architect recommend to meet this requirement? A. Deploy an Amazon ElastiCache cluster in front of the DynamoDB table. B. Deploy DynamoDB Accelerator (DAX) Configure DynamoDB auto scaling Purchase Savings Plans in Cost Explorer C. Use provisioned capacity mode Purchase Savings Plans in Cost Explorer D. Deploy DynamoDB Accelerator (DAX) Use provisioned capacity mode Configure DynamoDB auto scaling -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy an Amazon ElastiCache cluster in front of the DynamoDB table.",
      "B": "Deploy DynamoDB Accelerator (DAX) Configure DynamoDB auto scaling Purchase Savings Plans in Cost Explorer",
      "C": "Use provisioned capacity mode Purchase Savings Plans in Cost Explorer",
      "D": "Deploy DynamoDB Accelerator (DAX) Use provisioned capacity mode Configure DynamoDB auto scaling -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "180.3",
    "question": "- (Exam Topic 2) A company is running a critical application that uses an Amazon RDS for MySQL database to store data. The RDS DB instance is deployed in Multi-AZ mode. A recent RDS database failover test caused a 40-second outage to the application A solutions architect needs to design a solution to reduce the outage time to less than 20 seconds. Which combination of steps should the solutions architect take to meet these requirements? (Select THREE.) A. Use Amazon ElastiCache for Memcached in front of the database B. Use Amazon ElastiCache for Redis in front of the database. C. Use RDS Proxy in front of the database D. Migrate the database to Amazon Aurora MySQL E. Create an Amazon Aurora Replica F. Create an RDS for MySQL read replica -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use Amazon ElastiCache for Memcached in front of the database",
      "B": "Use Amazon ElastiCache for Redis in front of the database.",
      "C": "Use RDS Proxy in front of the database",
      "D": "Migrate the database to Amazon Aurora MySQL",
      "E": "Create an Amazon Aurora Replica",
      "F": "Create an RDS for MySQL read replica -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "B",
      "F"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "182.2",
    "question": "- (Exam Topic 2) A company recently deployed a new application that runs on a group of Amazon EC2 Linux instances in a VPC In a peered VPC the company launched an EC2 Linux instance that serves as a bastion host The security group of the application instances allows access only on TCP port 22 from the private IP of the bastion host The security group of the bastion host allows access to TCP port 22 from 0 0 0.0/0 so that system administrators can use SSH to remotely log in to the application instances from several branch offices While looking through operating system logs on the bastion host, a cloud engineer notices thousands of failed SSH logins to the bastion host from locations around the world The cloud engineer wants to change how remote access is granted to the application instances and wants to meet the following requirements: • Eliminate brute-force SSH login attempts • Retain a log of commands run during an SSH session • Retain the ability to forward ports Which solution meets these requirements for remote access to the application instances? A. Configure the application instances to communicate with AWS Systems Manager Grant access to the system administrators to use Session Manager to establish a session with the application instances Terminate the bastion host B. Update the security group of the bastion host to allow traffic from only the public IP addresses of the branch offices C. Configure an AWS Client VPN endpoint and provision each system administrator with a certificate to establish a VPN connection to the application VPC Update the security group of the application instances to allow traffic from only the Client VPN IPv4 CID D. Terminate the bastion host. E. Configure the application instances to communicate with AWS Systems Manage F. Grant access to the system administrators to issue commands to the application instances by using Systems Manager Run Comman G. Terminate the bastion host. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure the application instances to communicate with AWS Systems Manager Grant access to the system administrators to use Session Manager to establish a session with the application instances Terminate the bastion host",
      "B": "Update the security group of the bastion host to allow traffic from only the public IP addresses of the branch offices",
      "C": "Configure an AWS Client VPN endpoint and provision each system administrator with a certificate to establish a VPN connection to the application VPC Update the security group of the application instances to allow traffic from only the Client VPN IPv4 CID",
      "D": "Terminate the bastion host.",
      "E": "Configure the application instances to communicate with AWS Systems Manage",
      "F": "Grant access to the system administrators to issue commands to the application instances by using Systems Manager Run Comman",
      "G": "Terminate the bastion host. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": "\"Session Manager removes the need to open inbound ports, manage SSH keys, or use bastion hosts\" Ref: https://docs.aws.amazon.com/systems-\nmanager/latest/userguide/session-manager.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "189",
    "question": "- (Exam Topic 2) A company is running its solution on AWS in a manually created VPC. The company is using AWS Cloud Formation to provision other parts of the infrastructure. According to a new requirement, the company must manage all infrastructure in an automatic way. What should the company do to meet this new requirement with the LEAST effort? A. Create a new AWS Cloud Development Kit (AWS CDK) stack that stnctly provisions the existing VPC resources and configuratio B. Use AWS CDK to import the VPC into the stack and to manage the VPC. C. Create a CloudFormation stack set that creates the VP D. Use the stack set to import the VPC into the stack. E. Create a new CloudFormation template that strictly provisions the existing VPC resources and configuratio F. From the CloudFormation console, create a new stack by importing the existing resources. G. Create a new CloudFormation template that creates the VP H. Use the AWS Serverless Application Model {AWS SAM) CLI to import the VPC. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a new AWS Cloud Development Kit (AWS CDK) stack that stnctly provisions the existing VPC resources and configuratio",
      "B": "Use AWS CDK to import the VPC into the stack and to manage the VPC.",
      "C": "Create a CloudFormation stack set that creates the VP",
      "D": "Use the stack set to import the VPC into the stack.",
      "E": "Create a new CloudFormation template that strictly provisions the existing VPC resources and configuratio",
      "F": "From the CloudFormation console, create a new stack by importing the existing resources.",
      "G": "Create a new CloudFormation template that creates the VP",
      "H": "Use the AWS Serverless Application Model {AWS SAM) CLI to import the VPC. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "196",
    "question": "- (Exam Topic 2) A car rental company has built a serverless REST API to provide data to its mobile app. The app consists of an Amazon API Gateway API with a Regional endpoint, AWS Lambda functions and an Amazon Aurora MySQL Serverless DB cluster The company recently opened the API to mobile apps of partners A significant increase in the number of requests resulted causing sporadic database memory errors Analysis of the API traffic indicates that clients are making multiple HTTP GET requests for the same queries in a short period of time Traffic is concentrated during business hours, with spikes around holidays and other events The company needs to improve its ability to support the additional usage while minimizing the increase in costs associated with the solution. Which strategy meets these requirements? A. Convert the API Gateway Regional endpoint to an edge-optimized endpoint Enable caching in the production stage. B. Implement an Amazon ElastiCache for Redis cache to store the results of the database calls Modify the Lambda functions to use the cache C. Modify the Aurora Serverless DB cluster configuration to increase the maximum amount of available memory D. Enable throttling in the API Gateway production stage Set the rate and burst values to limit the incoming calls -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Convert the API Gateway Regional endpoint to an edge-optimized endpoint Enable caching in the production stage.",
      "B": "Implement an Amazon ElastiCache for Redis cache to store the results of the database calls Modify the Lambda functions to use the cache",
      "C": "Modify the Aurora Serverless DB cluster configuration to increase the maximum amount of available memory",
      "D": "Enable throttling in the API Gateway production stage Set the rate and burst values to limit the incoming calls -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "197",
    "question": "- (Exam Topic 2) A company plans to refactor a monolithic application into a modern application designed deployed or AWS. The CLCD pipeline needs to be upgraded to support the modem design for the application with the following requirements • It should allow changes to be released several times every hour. * It should be able to roll back the changes as quickly as possible Which design will meet these requirements? A. Deploy a Cl-CD pipeline that incorporates AMIs to contain the application and their configurations Deploy the application by replacing Amazon EC2 instances B. Specify AWS Elastic Beanstak to sage in a secondary environment as the deployment target for the CI/CD pipeline of the applicatio C. To deploy swap the staging and production environment URLs. D. Use AWS Systems Manager to re-provision the infrastructure for each deployment Update the AmazonEC2 user data to pull the latest code art-fact from Amazon S3 and use Amazon Route 53 weighted routing to point to the new environment E. Roll out At application updates as pan of an Auto Scaling event using prebuilt AMI F. Use new versions of the AMIs to add instances, and phase out all instances that use the previous AMI version with the configured termination policy during a deployment event. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy a Cl-CD pipeline that incorporates AMIs to contain the application and their configurations Deploy the application by replacing Amazon EC2 instances",
      "B": "Specify AWS Elastic Beanstak to sage in a secondary environment as the deployment target for the CI/CD pipeline of the applicatio",
      "C": "To deploy swap the staging and production environment URLs.",
      "D": "Use AWS Systems Manager to re-provision the infrastructure for each deployment Update the AmazonEC2 user data to pull the latest code art-fact from Amazon S3 and use Amazon Route 53 weighted routing to point to the new environment",
      "E": "Roll out At application updates as pan of an Auto Scaling event using prebuilt AMI",
      "F": "Use new versions of the AMIs to add instances, and phase out all instances that use the previous AMI version with the configured termination policy during a deployment event. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "It is the fastest when it comes to rollback and deploying changes every hour\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "199",
    "question": "- (Exam Topic 2) A company runs many workloads on AWS and uses AWS Organizations to manage its accounts. The workloads are hosted on Amazon EC2, AWS Fargate, and AWS Lambda. Some of the workloads have unpredictable demand. Accounts record high usage in some months and low usage in other months. The company wants to optimize its compute costs over the next 3 years. A solutions architect obtains a 6-month average for each of the accounts across the organization to calculate usage. Which solution will provide the MOST cost savings for all the organization's compute usage? A. Purchase Reserved Instances for the organization to match the size and number of the most common EC2 instances from the member accounts. B. Purchase a Compute Savings Plan for the organization from the management account by using the recommendation at the management account level. C. Purchase Reserved Instances for each member account that had high EC2 usage according to the data from the last 6 months. D. Purchase an EC2 Instance Savings Plan for each member account from the management account based on EC2 usage data from the last 6 months. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Purchase Reserved Instances for the organization to match the size and number of the most common EC2 instances from the member accounts.",
      "B": "Purchase a Compute Savings Plan for the organization from the management account by using the recommendation at the management account level.",
      "C": "Purchase Reserved Instances for each member account that had high EC2 usage according to the data from the last 6 months.",
      "D": "Purchase an EC2 Instance Savings Plan for each member account from the management account based on EC2 usage data from the last 6 months. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "208",
    "question": "- (Exam Topic 2) A company wants to migrate its on-premises data center to the AWS Cloud. This includes thousands of virtualized Linux and Microsoft Windows servers SAN storage, Java and PHP applications with MySQL, and Oracle databases. There are many dependent services hosted either in the same data center or externally. The technical documentation is incomplete and outdated A solutions architect needs to understand the current environment and estimate the cloud resource costs after the migration Which tools or services should the solutions architect use to plan the cloud migration? (Select THREE.) A. AWS Application Discovery Service B. AWS SMS C. AWS X-Ray D. AWS Cloud Adoption Readiness Tool (CART) E. Amazon Inspector F. AWS Migration Hub -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "AWS Application Discovery Service",
      "B": "AWS SMS",
      "C": "AWS X-Ray",
      "D": "AWS Cloud Adoption Readiness Tool (CART)",
      "E": "Amazon Inspector",
      "F": "AWS Migration Hub -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "D",
      "F"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "210.2",
    "question": "- (Exam Topic 2) A company is using multiple AWS accounts The DNS records are stored in a private hosted zone for Amazon Route 53 in Account A The company's applications and databases are running in Account B. A solutions architect win deploy a two-net application In a new VPC To simplify the configuration, the db.example com CNAME record set tor the Amazon RDS endpoint was created in a private hosted zone for Amazon Route 53. During deployment, the application failed to start. Troubleshooting revealed that db.example com is not resolvable on the Amazon EC2 instance The solutions architect confirmed that the record set was created correctly in Route 53. Which combination of steps should the solutions architect take to resolve this issue? (Select TWO J A. Deploy the database on a separate EC2 instance in the new VPC Create a record set for the instance's private IP in the private hosted zone B. Use SSH to connect to the application tier EC2 instance Add an RDS endpoint IP address to the/eto/resolv.conf file C. Create an authorization lo associate the private hosted zone in Account A with the new VPC In Account B D. Create a private hosted zone for the example.com domain m Account B Configure Route 53 replicationbetween AWS accounts E. Associate a new VPC in Account B with a hosted zone in Account F. Delete the association authorization In Account A. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy the database on a separate EC2 instance in the new VPC Create a record set for the instance's private IP in the private hosted zone",
      "B": "Use SSH to connect to the application tier EC2 instance Add an RDS endpoint IP address to the/eto/resolv.conf file",
      "C": "Create an authorization lo associate the private hosted zone in Account A with the new VPC In Account B",
      "D": "Create a private hosted zone for the example.com domain m Account B Configure Route 53 replicationbetween AWS accounts",
      "E": "Associate a new VPC in Account B with a hosted zone in Account",
      "F": "Delete the association authorization In Account A. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C",
      "E"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "214",
    "question": "- (Exam Topic 2) A news company wants to implement an AWS Lambda function that calls an external API to receive new press releases every 10 minutes. The API provider Is planning to use an IP address allow list to protect the API. so the news company needs to provide any public IP addresses that access the API. The company's current architecture includes a VPC with an internet gateway and a NAT gateway. A solutions architect must implement a static IP address for the Lambda function. Which combination of steps should the solutions architect take to meet these requirements? (Select TWO.) A. Use the Elastic IP address that is associated with the NAT gateway for the IP address allow list. B. Assign an Elastic IP address to the Lambda functio C. Use the Lambda function's Elastic IP address for the IP address allow list. D. Configure the Lambda function to launch in the private subnet of the VPC. E. Configure the Lambda function to launch in the public subnet of the VPC. F. Create a transit gatewa G. Attach the VPC and the Lambda function to the transit gateway. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use the Elastic IP address that is associated with the NAT gateway for the IP address allow list.",
      "B": "Assign an Elastic IP address to the Lambda functio",
      "C": "Use the Lambda function's Elastic IP address for the IP address allow list.",
      "D": "Configure the Lambda function to launch in the private subnet of the VPC.",
      "E": "Configure the Lambda function to launch in the public subnet of the VPC.",
      "F": "Create a transit gatewa",
      "G": "Attach the VPC and the Lambda function to the transit gateway. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "109.3",
    "question": "- (Exam Topic 2) A company is running an application in the AWS Cloud. The application uses AWS Lambda functions and Amazon Elastic Container Service (Amazon ECS) containers that run with AWS Fargate technology as its primary compute. The load on the application is irregular. The application experiences long periods of no usage, followed by sudden and significant increases and decreases in traffic. The application is write-heavy and stores data in an Amazon Aurora MySQL database. The database runs on an Amazon RDS memory optimized D8 instance that is not able to handle the load. What is the MOST cost-effective way for the company to handle the sudden and significant changes in traffic? A. Add additional read replicas to the databas B. Purchase Instance Savings Plans and RDS Reserved Instances. C. Migrate the database to an Aurora multi-master DB cluste D. Purchase Instance Savings Plans. E. Migrate the database to an Aurora global database Purchase Compute Savings Plans and RDS Reserved Instances F. Migrate the database to Aurora Serverless v1. Purchase Compute Savings Plans -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Add additional read replicas to the databas",
      "B": "Purchase Instance Savings Plans and RDS Reserved Instances.",
      "C": "Migrate the database to an Aurora multi-master DB cluste",
      "D": "Purchase Instance Savings Plans.",
      "E": "Migrate the database to an Aurora global database Purchase Compute Savings Plans and RDS Reserved Instances",
      "F": "Migrate the database to Aurora Serverless v1. Purchase Compute Savings Plans -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "219",
    "question": "- (Exam Topic 2) A company has an organization in AWS Organizations. The organization consists of a large number of AWS accounts that belong to separate business units. The company requires all Amazon EC2 instances to be provisioned with custom, hardened AMIs. The company wants a solution that provides each AWS account access to the AMIs Which solution will meet these requirements with the MOST operational efficiency? A. Create the AMIs with EC2 Image Builder Create an AWS CodePipeline pipeline to share the AMIs across all AWS accounts. B. Deploy Jenkins on an EC2 instance Create jobs to create and share the AMIs across all AWS accounts. C. Create and share the AMIs with EC2 Image Builder Use AWS Service Catalog to configure a product that provides access to the AMIs across all AWS accounts. D. Create the AMIs with EC2 Image Builder Create an AWS Lambda function to share the AMIs across all AWS accounts. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create the AMIs with EC2 Image Builder Create an AWS CodePipeline pipeline to share the AMIs across all AWS accounts.",
      "B": "Deploy Jenkins on an EC2 instance Create jobs to create and share the AMIs across all AWS accounts.",
      "C": "Create and share the AMIs with EC2 Image Builder Use AWS Service Catalog to configure a product that provides access to the AMIs across all AWS accounts.",
      "D": "Create the AMIs with EC2 Image Builder Create an AWS Lambda function to share the AMIs across all AWS accounts. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "106.2",
    "question": "- (Exam Topic 2) A company runs its application in the eu-west-1 Region and has one account for each of its environments development, testing, and production All the environments are running 24 hours a day 7 days a week by using stateful Amazon EC2 instances and Amazon RDS for MySQL databases The databases are between 500 GB and 800 GB in size The development team and testing team work on business days during business hours, but the production environment operates 24 hours a day. 7 days a week. The company wants to reduce costs AH resources are tagged with an environment tag with either development, testing, or production as the key. What should a solutions architect do to reduce costs with the LEAST operational effort? A. Create an Amazon EventBridge (Amazon CloudWatch Events) rule that runs once every day Configure the rule to invoke one AWS Lambda function that starts or stops instances based on the tag day and time. B. Create an Amazon EventBridge (Amazon CloudWatch Events) rule that runs every business day in the evenin C. Configure the rule to invoke an AWS Lambda function that stops instances based on thetag-Create a second EventBridge (CloudWatch Events) rule that runs every business day in the morning Configure the second rule to invoke another Lambda function that starts instances based on the tag D. Create an Amazon EventBridge (Amazon CloudWatch Events) rule that runs every business day in the evening Configure the rule to invoke an AWS Lambda function that terminates instances based on the tag Create a second EventBridge (CloudWatch Events) rule that runs every business day in the morning Configure the second rule to invoke another Lambda function that restores the instances from their last backup based on the tag. E. Create an Amazon EventBridge (Amazon CloudWatch Events) rule that runs every hour Configure the rule to invoke one AWS Lambda function that terminates or restores instances from their ....based on the ta F. day, and time -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an Amazon EventBridge (Amazon CloudWatch Events) rule that runs once every day Configure the rule to invoke one AWS Lambda function that starts or stops instances based on the tag day and time.",
      "B": "Create an Amazon EventBridge (Amazon CloudWatch Events) rule that runs every business day in the evenin",
      "C": "Configure the rule to invoke an AWS Lambda function that stops instances based on thetag-Create a second EventBridge (CloudWatch Events) rule that runs every business day in the morning Configure the second rule to invoke another Lambda function that starts instances based on the tag",
      "D": "Create an Amazon EventBridge (Amazon CloudWatch Events) rule that runs every business day in the evening Configure the rule to invoke an AWS Lambda function that terminates instances based on the tag Create a second EventBridge (CloudWatch Events) rule that runs every business day in the morning Configure the second rule to invoke another Lambda function that restores the instances from their last backup based on the tag.",
      "E": "Create an Amazon EventBridge (Amazon CloudWatch Events) rule that runs every hour Configure the rule to invoke one AWS Lambda function that terminates or restores instances from their ....based on the ta",
      "F": "day, and time -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "104",
    "question": "- (Exam Topic 2) A financial services company in North America plans to release a new online web application to its customers on AWS . The company will launch the application in the us-east-1 Region on Amazon EC2 instances. The application must be highly available and must dynamically scale to meet user traffic. The company also wants to implement a disaster recovery environment for the application in the us-west-1 Region by using active-passive failover. Which solution will meet these requirements? A. Create a VPC in us-east-1 and a VPC in us-west-1 Configure VPC peering In the us-east-1 VP B. create an Application Load Balancer (ALB) that extends across multiple Availability Zones in both VPCs Create an Auto Scaling group that deploys the EC2 instances across the multiple Availability Zones in both VPCs Place the Auto Scaling group behind the ALB. C. Create a VPC in us-east-1 and a VPC in us-west-1. In the us-east-1 VP D. create an Application Load Balancer (ALB) that extends across multiple Availability Zones in that VP E. Create an Auto Scaling group that deploys the EC2 instances across the multiple Availability Zones in the us-east-1 VPC Place the Auto Scaling group behind the ALB Set up the same configuration in the us-west-1 VP F. Create an Amazon Route 53 hosted zone Create separate records for each ALB Enable health checks to ensure high availability between Regions. G. Create a VPC in us-east-1 and a VPC in us-west-1 In the us-east-1 VP H. create an Application Load Balancer (ALB) that extends across multiple Availability Zones in that VPC Create an Auto Scaling group that deploys the EC2 instances across the multiple Availability Zones in the us-east-1 VPC Place the Auto Scaling group behind the ALB Set up the same configuration in the us-west-1 VPC Create an Amazon Route 53 hosted zon I. Create separate records for each ALB Enable health checks and configure a failover routing policy for each record. J. Create a VPC in us-east-1 and a VPC in us-west-1 Configure VPC peering In the us-east-1 VP K. create an Application Load Balancer (ALB) that extends across multiple Availability Zones in Create an Auto Scaling group that deploys the EC2 instances across the multiple Availability Zones in both VPCs Place the Auto Scaling group behind the ALB Create an Amazon Route 53 host.. Create a record for the ALB. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a VPC in us-east-1 and a VPC in us-west-1 Configure VPC peering In the us-east-1 VP",
      "B": "create an Application Load Balancer (ALB) that extends across multiple Availability Zones in both VPCs Create an Auto Scaling group that deploys the EC2 instances across the multiple Availability Zones in both VPCs Place the Auto Scaling group behind the ALB.",
      "C": "Create a VPC in us-east-1 and a VPC in us-west-1. In the us-east-1 VP",
      "D": "create an Application Load Balancer (ALB) that extends across multiple Availability Zones in that VP",
      "E": "Create an Auto Scaling group that deploys the EC2 instances across the multiple Availability Zones in the us-east-1 VPC Place the Auto Scaling group behind the ALB Set up the same configuration in the us-west-1 VP",
      "F": "Create an Amazon Route 53 hosted zone Create separate records for each ALB Enable health checks to ensure high availability between Regions.",
      "G": "Create a VPC in us-east-1 and a VPC in us-west-1 In the us-east-1 VP",
      "H": "create an Application Load Balancer (ALB) that extends across multiple Availability Zones in that VPC Create an Auto Scaling group that deploys the EC2 instances across the multiple Availability Zones in the us-east-1 VPC Place the Auto Scaling group behind the ALB Set up the same configuration in the us-west-1 VPC Create an Amazon Route 53 hosted zon",
      "I": "Create separate records for each ALB Enable health checks and configure a failover routing policy for each record.",
      "J": "Create a VPC in us-east-1 and a VPC in us-west-1 Configure VPC peering In the us-east-1 VP K. create an Application Load Balancer (ALB) that extends across multiple Availability Zones in Create an Auto Scaling group that deploys the EC2 instances across the multiple Availability Zones in both VPCs Place the Auto Scaling group behind the ALB Create an Amazon Route 53 host.. Create a record for the ALB. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "220",
    "question": "- (Exam Topic 2) A flood monitoring agency has deployed more than 10.000 water-level monitoring sensors. Sensors send continuous data updates, and each update Is less than 1 MB in size. The agency has a fleet of on-premises application servers. These servers receive updates from the sensors, convert the raw data into a human readable format, and write the results to an on-premises relational database server Data analysts then use simple SQL queries to monitor the data. The agency wants to increase overall application availability and reduce the effort that is required to perform maintenance tasks. These maintenance tasks, which include updates and patches to the application servers, cause downtime. While an application server is down, data is lost from sensors because the remaining servers cannot handle the entire workload. The agency wants a solution that optimizes operational overhead and costs. A solutions architect recommends the use of AWS loT Core to collect the sensor data. What else should the solutions architect recommend to meet these requirements? A. Send the sensor data to Amazon Kinesis Data Firehos B. Use an AWS Lambda function to read the Kinesis Data Firehose data, convert it to .csv format, and insert it into an Amazon Aurora MySQL DB Instanc C. Instruct the data analysts to query the data directly from the DB Instance. D. Send the sensor data to Amazon Kinesis Data Firehos E. Use an AWS Lambda function to read the Kinesis Data Firehose data, convert it to Apache Parquet format, and save it to an Amazon S3 bucke F. Instruct the data analysts to query the data by using Amazon Athena. G. Send the sensor data to an Amazon Kinesis Data Analytics application to convert the data to csv format and store it in an Amazon S3 bucke H. Import the data Into an Amazon Aurora MySQL DB instanc I. Instruct the data analysts to query the data directly from the DB instance J. Send the sensor data to an Amazon Kinesis Data Analytics application to convert the data to Apache Parquet format and store it in an Amazon S3 bucke K. Instruct the data analysts to query the data by using Amazon Athena. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Send the sensor data to Amazon Kinesis Data Firehos",
      "B": "Use an AWS Lambda function to read the Kinesis Data Firehose data, convert it to .csv format, and insert it into an Amazon Aurora MySQL DB Instanc",
      "C": "Instruct the data analysts to query the data directly from the DB Instance.",
      "D": "Send the sensor data to Amazon Kinesis Data Firehos",
      "E": "Use an AWS Lambda function to read the Kinesis Data Firehose data, convert it to Apache Parquet format, and save it to an Amazon S3 bucke",
      "F": "Instruct the data analysts to query the data by using Amazon Athena.",
      "G": "Send the sensor data to an Amazon Kinesis Data Analytics application to convert the data to csv format and store it in an Amazon S3 bucke",
      "H": "Import the data Into an Amazon Aurora MySQL DB instanc",
      "I": "Instruct the data analysts to query the data directly from the DB instance",
      "J": "Send the sensor data to an Amazon Kinesis Data Analytics application to convert the data to Apache Parquet format and store it in an Amazon S3 bucke K. Instruct the data analysts to query the data by using Amazon Athena. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "17",
    "question": "- (Exam Topic 1) A company that tracks medical devices in hospitals wants to migrate its existing storage solution to the AWS Cloud. The company equips all of its devices with sensors that collect location and usage information. This sensor data is sent in unpredictable patterns with large spikes. The data is stored in a MySQL database running on premises at each hospital. The company wants the cloud storage solution to scale with usage. The company's analytics team uses the sensor data to calculate usage by device type and hospital. The team needs to keep analysis tools running locally while fetching data from the cloud. The team also needs to use existing Java application and SQL queries with as few changes as possible. How should a solutions architect meet these requirements while ensuring the sensor data is secure? A. Store the data in an Amazon Aurora Serverless databas B. Serve the data through a Network Load Balancer (NLB). Authenticate users using the NLB with credentials stored in AWS Secrets Manager. C. Store the data in an Amazon S3 bucke D. Serve the data through Amazon QuickSight using an IAM user authorized with AWS Identity and Access Management (IAM) with the S3 bucket as the data source. E. Store the data in an Amazon Aurora Serverless databas F. Serve the data through the Aurora Data API using an IAM user authorized with AWS Identity and Access Management (IAM) and the AWS Secrets Manager ARN. G. Store the data in an Amazon S3 bucke H. Serve the data through Amazon Athena using AWS PrivateLink to secure the data in transit. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Store the data in an Amazon Aurora Serverless databas",
      "B": "Serve the data through a Network Load Balancer (NLB). Authenticate users using the NLB with credentials stored in AWS Secrets Manager.",
      "C": "Store the data in an Amazon S3 bucke",
      "D": "Serve the data through Amazon QuickSight using an IAM user authorized with AWS Identity and Access Management (IAM) with the S3 bucket as the data source.",
      "E": "Store the data in an Amazon Aurora Serverless databas",
      "F": "Serve the data through the Aurora Data API using an IAM user authorized with AWS Identity and Access Management (IAM) and the AWS Secrets Manager ARN.",
      "G": "Store the data in an Amazon S3 bucke",
      "H": "Serve the data through Amazon Athena using AWS PrivateLink to secure the data in transit. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "https://aws.amazon.com/blogs/aws/new-data-api-for-amazon-aurora-serverless/ https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html\nhttps://aws.amazon.com/blogs/aws/aws-privatelink-for-amazon-s3-now-available/ https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-\napi.html#data-api.access\nThe data is currently stored in a MySQL database running on-prem. Storing MySQL data in S3 doesn't sound good so B & D are out. Aurora Data API \"enables the\nSQL HTTP endpoint, a connectionless Web Service API for running SQL queries against this database. When the SQL HTTP endpoint is enabled, you can also\nquery your database from inside the RDS console (these features are free to use).\"\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "3.3",
    "question": "- (Exam Topic 1) A company has a complex web application that leverages Amazon CloudFront for global scalability and performance. Over time, users report that the web application is slowing down. The company's operations team reports that the CloudFront cache hit ratio has been dropping steadily. The cache metrics report indicates that query strings on some URLs are inconsistently ordered and are specified sometimes in mixed-case letters and sometimes in lowercase letters. Which set of actions should the solutions architect take to increase the cache hit ratio as quickly as possible? A. Deploy a Lambda@Edge function to sort parameters by name and force them to be lowercas B. Select the CloudFront viewer request trigger to invoke the function. C. Update the CloudFront distribution to disable caching based on query string parameters. D. Deploy a reverse proxy after the load balancer to post-process the emitted URLs in the application to force the URL strings to be lowercase. E. Update the CloudFront distribution to specify casing-insensitive query string processing. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy a Lambda@Edge function to sort parameters by name and force them to be lowercas",
      "B": "Select the CloudFront viewer request trigger to invoke the function.",
      "C": "Update the CloudFront distribution to disable caching based on query string parameters.",
      "D": "Deploy a reverse proxy after the load balancer to post-process the emitted URLs in the application to force the URL strings to be lowercase.",
      "E": "Update the CloudFront distribution to specify casing-insensitive query string processing. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": "https://docs.amazonaws.cn/en_us/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-ex Before CloudFront serves content from the cache\nit will trigger any Lambda function associated with the Viewer Request, in which we can normalize parameters.\nhttps://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examp\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "4.3",
    "question": "- (Exam Topic 1) A fitness tracking company serves users around the world, with its primary markets in North America and Asia. The company needs to design an infrastructure for its read-heavy user authorization application with the following requirements: • Be resilient to problems with the application in any Region. • Write to a database in a single Region. • Read from multiple Regions. • Support resiliency across application tiers in each Region. • Support the relational database semantics reflected in the application. Which combination of steps should a solutions architect take? (Select TWO.) A. Use an Amazon Route 53 geoproximity routing policy combined with a multivalue answer routing policy. B. Deploy we C. application, and MySQL database servers to Amazon EC2 instances in each Regio D. Set up the application so that reads and writes are local to the Regio E. Create snapshots of the web, application, and database servers and store the snapshots in an Amazon S3 bucket in both Region F. Set upcross-Region replication for the database layer. G. Use an Amazon Route 53 geolocation routing policy combined with a failover routing policy. H. Set up web, application, and Amazon RDS for MySQL instances in each Regio I. Set up the application so that reads are local and writes are partitioned based on the use J. Set up a Multi-AZ failover for the web, application, and database server K. Set up cross-Region replication for the database layer. L. Set up active-active web and application servers in each Regio M. Deploy an Amazon Aurora global database with clusters in each Regio N. Set up the application to use the in-Region Aurora database endpoint O. Create snapshots of the web and application servers and store them in an Amazon S3 bucket in both Regions. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use an Amazon Route 53 geoproximity routing policy combined with a multivalue answer routing policy.",
      "B": "Deploy we",
      "C": "application, and MySQL database servers to Amazon EC2 instances in each Regio",
      "D": "Set up the application so that reads and writes are local to the Regio",
      "E": "Create snapshots of the web, application, and database servers and store the snapshots in an Amazon S3 bucket in both Region",
      "F": "Set upcross-Region replication for the database layer.",
      "G": "Use an Amazon Route 53 geolocation routing policy combined with a failover routing policy.",
      "H": "Set up web, application, and Amazon RDS for MySQL instances in each Regio",
      "I": "Set up the application so that reads are local and writes are partitioned based on the use",
      "J": "Set up a Multi-AZ failover for the web, application, and database server K. Set up cross-Region replication for the database layer. L. Set up active-active web and application servers in each Regio M. Deploy an Amazon Aurora global database with clusters in each Regio N. Set up the application to use the in-Region Aurora database endpoint O. Create snapshots of the web and application servers and store them in an Amazon S3 bucket in both Regions. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C",
      "E"
    ],
    "select_n": 2,
    "explanation": "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html\nGeoproximity routing policy is good to control the user traffic to specific regions. However, a multivalue answer routing policy may cause the users to be randomly\nsent to other healthy regions that may be far away from the user’s location. You can use geolocation routing policy to direct the North American users to your\nservers on the North America region and configure failover routing to the Asia region in case the North America region fails. You can configure the same for the\nAsian users pointed to the Asia region servers and have the North America region as its backup.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "7.2",
    "question": "- (Exam Topic 1) A company wants to change its internal cloud billing strategy for each of its business units. Currently, the cloud governance team shares reports for overall cloud spending with the head of each business unit. The company uses AWS Organizations lo manage the separate AWS accounts for each business unit. The existing tagging standard in Organizations includes the application, environment, and owner. The cloud governance team wants a centralized solution so each business unit receives monthly reports on its cloud spending. The solution should also send notifications for any cloud spending that exceeds a set threshold. Which solution is the MOST cost-effective way to meet these requirements? A. Configure AWS Budgets in each account and configure budget alerts that are grouped by application, environment, and owne B. Add each business unit to an Amazon SNS topic for each aler C. Use Cost Explorer in each account to create monthly reports for each business unit. D. Configure AWS Budgets in the organization's master account and configure budget alerts that are grouped by application, environment, and owne E. Add each business unit to an Amazon SNS topic for each aler F. Use Cost Explorer in the organization's master account to create monthly reports for each business unit. G. Configure AWS Budgets in each account and configure budget alerts lhat are grouped by application, environment, and owne H. Add each business unit to an Amazon SNS topic for each aler I. Use the AWS Billing and Cost Management dashboard in each account to create monthly reports for each business unit. J. Enable AWS Cost and Usage Reports in the organization's master account and configure reports grouped by application, environment, and owne K. Create an AWS Lambda function that processes AWS Cost and Usage Reports, sends budget alerts, and sends monthly reports to each business unit's email list. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure AWS Budgets in each account and configure budget alerts that are grouped by application, environment, and owne",
      "B": "Add each business unit to an Amazon SNS topic for each aler",
      "C": "Use Cost Explorer in each account to create monthly reports for each business unit.",
      "D": "Configure AWS Budgets in the organization's master account and configure budget alerts that are grouped by application, environment, and owne",
      "E": "Add each business unit to an Amazon SNS topic for each aler",
      "F": "Use Cost Explorer in the organization's master account to create monthly reports for each business unit.",
      "G": "Configure AWS Budgets in each account and configure budget alerts lhat are grouped by application, environment, and owne",
      "H": "Add each business unit to an Amazon SNS topic for each aler",
      "I": "Use the AWS Billing and Cost Management dashboard in each account to create monthly reports for each business unit.",
      "J": "Enable AWS Cost and Usage Reports in the organization's master account and configure reports grouped by application, environment, and owne K. Create an AWS Lambda function that processes AWS Cost and Usage Reports, sends budget alerts, and sends monthly reports to each business unit's email list. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "Configure AWS Budgets in the organization€TMs master account and configure budget alerts that are grouped by application, environment, and owner. Add each\nbusiness unit to an Amazon SNS topic for each alert. Use Cost Explorer in the organization€TMs master account to create monthly reports for each business unit.\nhttps://aws.amazon.com/about-aws/whats-new/2019/07/introducing-aws-budgets-reports/#:~:text=AWS%20Bud\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "8.3",
    "question": "- (Exam Topic 1) A solution architect is designing an AWS account structure for a company that consists of multiple terms. All the team will work in the same AWS Region. The company needs a VPC that is connected to the on-premises network. The company expects less than 50 Mbps of total to and from the on-premises network. Which combination of steps will meet these requirements MOST cost-effectively? (Select TWO) A. Create an AWS CloudFormation template that provisions a VPC and the required subnet B. Deploy the template to each AWS account C. Create an AWS CloudFormabon template that provisions a VPC and the required subnet D. Deploy the template to a shared services accoun E. Share the subnets by using AWS Resource Access Manager F. Use AWS Transit Gateway along with an AWS Site-to-Site VPN for connectivity to the on-premises networ G. Share the transit gateway by using AWS Resource Access Manager H. Use AWS Site-to-Site VPN for connectivity to the on-premises network I. Use AWS Direct Connect for connectivity to the on-premises network. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an AWS CloudFormation template that provisions a VPC and the required subnet",
      "B": "Deploy the template to each AWS account",
      "C": "Create an AWS CloudFormabon template that provisions a VPC and the required subnet",
      "D": "Deploy the template to a shared services accoun",
      "E": "Share the subnets by using AWS Resource Access Manager",
      "F": "Use AWS Transit Gateway along with an AWS Site-to-Site VPN for connectivity to the on-premises networ",
      "G": "Share the transit gateway by using AWS Resource Access Manager",
      "H": "Use AWS Site-to-Site VPN for connectivity to the on-premises network",
      "I": "Use AWS Direct Connect for connectivity to the on-premises network. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "D"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "10.3",
    "question": "- (Exam Topic 1) A company wants to host a new global website that consists of static content. A solutions architect is working on a solution that uses Amazon CloudFront with an origin access identity <OAI) to access website content that is stored in a private Amazon S3 bucket. During testing, the solutions architect receives 404 errors from the S3 bucket. Error messages appear only for attempts to access paths that end with a forward slash. such as example.com/path/. These requests should return the existing S3 object path/index.html. Any potential solution must not prevent CloudFront from caching the content. What should the solutions architect do to resolve this problem? A. Change the CloudFront origin to an Amazon API Gateway proxy endpoin B. Rewrite the S3 request URL by using an AWS Lambda function. C. Change the CloudFront origin to an Amazon API Gateway endpoin D. Rewrite the S3 request URL in an AWS service integration. E. Change the CloudFront configuration to use an AWS Lambda@Edge function that is invoked by a viewer request event to rewrite the S3 request URL. F. Change the CloudFront configuration to use an AWS Lambda@Edge function that is invoked by an origin request event to rewrite the S3 request URL. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Change the CloudFront origin to an Amazon API Gateway proxy endpoin",
      "B": "Rewrite the S3 request URL by using an AWS Lambda function.",
      "C": "Change the CloudFront origin to an Amazon API Gateway endpoin",
      "D": "Rewrite the S3 request URL in an AWS service integration.",
      "E": "Change the CloudFront configuration to use an AWS Lambda@Edge function that is invoked by a viewer request event to rewrite the S3 request URL.",
      "F": "Change the CloudFront configuration to use an AWS Lambda@Edge function that is invoked by an origin request event to rewrite the S3 request URL. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "10.4",
    "question": "- (Exam Topic 1) A company is storing data on premises on a Windows file server. The company produces 5 GB of new data daily. The company migrated part of its Windows-based workload to AWS and needs the data to be available on a file system in the cloud. The company already has established an AWS Direct Connect connection between the on-premises network and AWS. Which data migration strategy should the company use? A. Use the file gateway option in AWS Storage Gateway to replace the existing Windows file server, and point the existing file share to the new file gateway. B. Use AWS DataSync to schedule a daily task to replicate data between the on-premises Windows file server and Amazon FSx. C. Use AWS Data Pipeline to schedule a daily task to replicate data between the on-premises Windows file server and Amazon Elastic File System (Amazon EFS). D. Use AWS DataSync to schedule a daily task lo replicate data between the on-premises Windows file server and Amazon Elastic File System (Amazon EFS), -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use the file gateway option in AWS Storage Gateway to replace the existing Windows file server, and point the existing file share to the new file gateway.",
      "B": "Use AWS DataSync to schedule a daily task to replicate data between the on-premises Windows file server and Amazon FSx.",
      "C": "Use AWS Data Pipeline to schedule a daily task to replicate data between the on-premises Windows file server and Amazon Elastic File System (Amazon EFS).",
      "D": "Use AWS DataSync to schedule a daily task lo replicate data between the on-premises Windows file server and Amazon Elastic File System (Amazon EFS), -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "https://aws.amazon.com/storagegateway/file/ https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-files-to-fsx-datasync.html\nhttps://docs.aws.amazon.com/systems-manager/latest/userguide/prereqs-operating-systems.html#prereqs-os-win\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "12.2",
    "question": "- (Exam Topic 1) The company needs to determine which costs on the monthly AWS bill are attributable to each application or team. The company also must be able to create reports to compare costs from the last 12 months and to help forecast costs for the next 12 months. A solutions architect must recommend an AWS Billing and Cost Management solution that provides these cost reports. Which combination of actions will meet these requirements? (Select THREE.) A. Activate the user-defined cost allocation tags that represent the application and the team. B. Activate the AWS generated cost allocation tags that represent the application and the team. C. Create a cost category for each application in Billing and Cost Management. D. Activate IAM access to Billing and Cost Management. E. Create a cost budget. F. Enable Cost Explorer. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Activate the user-defined cost allocation tags that represent the application and the team.",
      "B": "Activate the AWS generated cost allocation tags that represent the application and the team.",
      "C": "Create a cost category for each application in Billing and Cost Management.",
      "D": "Activate IAM access to Billing and Cost Management.",
      "E": "Create a cost budget.",
      "F": "Enable Cost Explorer. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C",
      "F"
    ],
    "select_n": 3,
    "explanation": "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html https://aws.amazon.com/premiumsupport/knowledge-center/cost-\nexplorer-analyze-spending-and-usage/ https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html\nhttps://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "23.3",
    "question": "- (Exam Topic 1) A solutions architect needs to advise a company on how to migrate its on-premises data processing application to the AWS Cloud. Currently, users upload input files through a web portal. The web server then stores the uploaded files on NAS and messages the processing server over a message queue. Each media file can take up to 1 hour to process. The company has determined that the number of media files awaiting processing is significantly higher during business hours, with the number of files rapidly declining after business hours. What is the MOST cost-effective migration recommendation? A. Create a queue using Amazon SQ B. Configure the existing web server to publish to the new queue.When there are messages in the queue, invoke an AWS Lambda function to pull requests from the queue and process the file C. Store the processed files in an Amazon S3 bucket. D. Create a queue using Amazon M E. Configure the existing web server to publish to the new queue.When there are messages in the queue, create a new Amazon EC2 instance to pull requests from the queue and process the file F. Store the processed files in Amazon EF G. Shut down the EC2 instance after the task is complete. H. Create a queue using Amazon M I. Configure the existing web server to publish to the new queue.When there are messages in the queue, invoke an AWS Lambda function to pull requests from the queue and process the file J. Store the processed files in Amazon EFS. K. Create a queue using Amazon SO L. Configure the existing web server to publish to the new queu M. Use Amazon EC2 instances in an EC2 Auto Scaling group to pull requests from the queue and process the file N. Scale the EC2 instances based on the SOS queue lengt O. Store the processed files in an Amazon S3 bucket. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a queue using Amazon SQ",
      "B": "Configure the existing web server to publish to the new queue.When there are messages in the queue, invoke an AWS Lambda function to pull requests from the queue and process the file",
      "C": "Store the processed files in an Amazon S3 bucket.",
      "D": "Create a queue using Amazon M",
      "E": "Configure the existing web server to publish to the new queue.When there are messages in the queue, create a new Amazon EC2 instance to pull requests from the queue and process the file",
      "F": "Store the processed files in Amazon EF",
      "G": "Shut down the EC2 instance after the task is complete.",
      "H": "Create a queue using Amazon M",
      "I": "Configure the existing web server to publish to the new queue.When there are messages in the queue, invoke an AWS Lambda function to pull requests from the queue and process the file",
      "J": "Store the processed files in Amazon EFS. K. Create a queue using Amazon SO L. Configure the existing web server to publish to the new queu M. Use Amazon EC2 instances in an EC2 Auto Scaling group to pull requests from the queue and process the file N. Scale the EC2 instances based on the SOS queue lengt O. Store the processed files in an Amazon S3 bucket. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "26.2",
    "question": "- (Exam Topic 1) A company is running an Apache Hadoop cluster on Amazon EC2 instances. The Hadoop cluster stores approximately 100 TB of data for weekly operational reports and allows occasional access for data scientists to retrieve data. The company needs to reduce the cost and operational complexity for storing and serving this data. Which solution meets these requirements in the MOST cost-effective manner? A. Move the Hadoop cluster from EC2 instances to Amazon EM B. Allow data access patterns to remain the same. C. Write a script that resizes the EC2 instances to a smaller instance type during downtime and resizes the instances to a larger instance type before the reports are created. D. Move the data to Amazon S3 and use Amazon Athena to query the data for report E. Allow the data scientists to access the data directly in Amazon S3. F. Migrate the data to Amazon DynamoDB and modify the reports to fetch data from DynamoD G. Allow the data scientists to access the data directly in DynamoDB. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Move the Hadoop cluster from EC2 instances to Amazon EM",
      "B": "Allow data access patterns to remain the same.",
      "C": "Write a script that resizes the EC2 instances to a smaller instance type during downtime and resizes the instances to a larger instance type before the reports are created.",
      "D": "Move the data to Amazon S3 and use Amazon Athena to query the data for report",
      "E": "Allow the data scientists to access the data directly in Amazon S3.",
      "F": "Migrate the data to Amazon DynamoDB and modify the reports to fetch data from DynamoD",
      "G": "Allow the data scientists to access the data directly in DynamoDB. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "\"The company needs to reduce the cost and operational complexity for storing and serving this data. Which solution meets these requirements in the MOST cost-\neffective manner?\" EMR storage is ephemeral. The company has 100TB that need to persist, they would have to use EMRFS to backup to S3 anyway.\nhttps://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-storage.html\n100TB\nEBS - 8.109$ S3 - 2.355$\nYou have saved 5.752$\nThis amount can be used for Athen. BTW. we don't know indexes, amount of data that is scanned. What we know is that tit will be: \"occasional access for data\nscientists to retrieve data\"\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "27",
    "question": "- (Exam Topic 1) A company has many services running in its on-premises data center. The data center is connected to AWS using AWS Direct Connect (DX) and an IPSec VPN. The service data is sensitive and connectivity cannot traverse the internet. The company wants to expand into a new market segment and begin offering its services to other companies that are using AWS. Which solution will meet these requirements? A. Create a VPC Endpoint Service that accepts TCP traffic, host it behind a Network Load Balancer, and make the service available over DX. B. Create a VPC Endpoint Service that accepts HTTP or HTTPS traffic, host it behind an Application Load Balancer, and make the service available over DX. C. Attach an internet gateway to the VP D. and ensure that network access control and security group rules allow the relevant inbound and outbound traffic. E. Attach a NAT gateway to the VP F. and ensure that network access control and security group rules allow the relevant inbound and outbound traffic. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a VPC Endpoint Service that accepts TCP traffic, host it behind a Network Load Balancer, and make the service available over DX.",
      "B": "Create a VPC Endpoint Service that accepts HTTP or HTTPS traffic, host it behind an Application Load Balancer, and make the service available over DX.",
      "C": "Attach an internet gateway to the VP",
      "D": "and ensure that network access control and security group rules allow the relevant inbound and outbound traffic.",
      "E": "Attach a NAT gateway to the VP",
      "F": "and ensure that network access control and security group rules allow the relevant inbound and outbound traffic. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "30",
    "question": "- (Exam Topic 1) To abide by industry regulations, a solutions architect must design a solution that will store a company's critical data in multiple public AWS Regions, including in the United States, where the company's headquarters is located. The solutions architect is required to provide access to the data stored in AWS to the company's global WAN network. The security team mandates that no traffic accessing this data should traverse the public internet. How should the solutions architect design a highly available solution that meets the requirements and is cost-effective? A. Establish AWS Direct Connect connections from the company headquarters to all AWS Regions in use.Use the company WAN lo send traffic over to the headquarters and then to the respective DX connection to access the data. B. Establish two AWS Direct Connect connections from the company headquarters to an AWS Region.Use the company WAN to send traffic over a DX connectio C. Use inter-region VPC peering to access the data in other AWS Regions. D. Establish two AWS Direct Connect connections from the company headquarters to an AWS Region.Use the company WAN to send traffic over a DX connectio E. Use an AWS transit VPC solution to access data in other AWS Regions. F. Establish two AWS Direct Connect connections from the company headquarters to an AWS Region.Use the company WAN to send traffic over a DX connectio G. Use Direct Connect Gateway to access data in other AWS Regions. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Establish AWS Direct Connect connections from the company headquarters to all AWS Regions in use.Use the company WAN lo send traffic over to the headquarters and then to the respective DX connection to access the data.",
      "B": "Establish two AWS Direct Connect connections from the company headquarters to an AWS Region.Use the company WAN to send traffic over a DX connectio",
      "C": "Use inter-region VPC peering to access the data in other AWS Regions.",
      "D": "Establish two AWS Direct Connect connections from the company headquarters to an AWS Region.Use the company WAN to send traffic over a DX connectio",
      "E": "Use an AWS transit VPC solution to access data in other AWS Regions.",
      "F": "Establish two AWS Direct Connect connections from the company headquarters to an AWS Region.Use the company WAN to send traffic over a DX connectio",
      "G": "Use Direct Connect Gateway to access data in other AWS Regions. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "This feature also allows you to connect to any of the participating VPCs from any Direct Connect location, further reducing your costs for making using AWS\nservices on a cross-region basis. https://aws.amazon.com/blogs/aws/new-aws-direct-connect-gateway-inter-region-vpc-access/\nhttps://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-aws-transit-g\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "35.2",
    "question": "- (Exam Topic 1) A company is running a containerized application in the AWS Cloud. The application is running by using Amazon Elastic Container Service (Amazon ECS) on a set Amazon EC2 instances. The EC2 instances run in an Auto Scaling group. The company uses Amazon Elastic Container Registry (Amazon ECRJ to store its container images When a new image version is uploaded, the new image version receives a unique tag The company needs a solution that inspects new image versions for common vulnerabilities and exposures The solution must automatically delete new image tags that have Critical or High severity findings The solution also must notify the development team when such a deletion occurs Which solution meets these requirements? A. Configure scan on push on the repositor B. Use Amazon EventBridge (Amazon CloudWatch Events) to invoke an AWS Step Functions state machine when a scan is complete for images that have Critical or High severity findings Use the Step Functions state machine to delete the image tag for those images and to notify the development team through Amazon Simple Notification Service (Amazon SNS) C. Configure scan on push on the repository Configure scan results to be pushed to an Amazon SimpleQueue Service (Amazon SQS) queue Invoke an AWS Lambda function when a new message is added to the SOS queue Use the Lambda function to delete the image tag for images that have Critical or High seventy finding D. Notify the development team by using Amazon Simple Email Service (Amazon SES). E. Schedule an AWS Lambda function to start a manual image scan every hour Configure Amazon EventBridge (Amazon CloudWatch Events) to invoke another Lambda function when a scan is complet F. Use the second Lambda function to delete the image tag for images that have Cnocal or High severity finding G. Notify the development team by using Amazon Simple Notification Service (Amazon SNS) H. Configure periodic image scan on the repository Configure scan results to be added to an Amazon Simple Queue Service (Amazon SQS) queue Invoke an AWS Step Functions state machine when a new message is added to the SQS queue Use the Step Functions state machine to delete the image tag for images that have Critical or High severity finding I. Notify the development team by using Amazon Simple Email Service (Amazon SES). -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure scan on push on the repositor",
      "B": "Use Amazon EventBridge (Amazon CloudWatch Events) to invoke an AWS Step Functions state machine when a scan is complete for images that have Critical or High severity findings Use the Step Functions state machine to delete the image tag for those images and to notify the development team through Amazon Simple Notification Service (Amazon SNS)",
      "C": "Configure scan on push on the repository Configure scan results to be pushed to an Amazon SimpleQueue Service (Amazon SQS) queue Invoke an AWS Lambda function when a new message is added to the SOS queue Use the Lambda function to delete the image tag for images that have Critical or High seventy finding",
      "D": "Notify the development team by using Amazon Simple Email Service (Amazon SES).",
      "E": "Schedule an AWS Lambda function to start a manual image scan every hour Configure Amazon EventBridge (Amazon CloudWatch Events) to invoke another Lambda function when a scan is complet",
      "F": "Use the second Lambda function to delete the image tag for images that have Cnocal or High severity finding",
      "G": "Notify the development team by using Amazon Simple Notification Service (Amazon SNS)",
      "H": "Configure periodic image scan on the repository Configure scan results to be added to an Amazon Simple Queue Service (Amazon SQS) queue Invoke an AWS Step Functions state machine when a new message is added to the SQS queue Use the Step Functions state machine to delete the image tag for images that have Critical or High severity finding",
      "I": "Notify the development team by using Amazon Simple Email Service (Amazon SES). -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "39.2",
    "question": "- (Exam Topic 1) A company stores sales transaction data in Amazon DynamoDB tables. To detect anomalous behaviors and respond quickly, all changes lo the items stored in the DynamoDB tables must be logged within 30 minutes. Which solution meets the requirements? A. Copy the DynamoDB tables into Apache Hive tables on Amazon EMR every hour and analyze them (or anomalous behavior B. Send Amazon SNS notifications when anomalous behaviors are detected. C. Use AWS CloudTrail to capture all the APIs that change the DynamoDB table D. Send SNS notifications when anomalous behaviors are detected using CloudTrail event filtering. E. Use Amazon DynamoDB Streams to capture and send updates to AWS Lambd F. Create a Lambda function to output records lo Amazon Kinesis Data Stream G. Analyze any anomalies with Amazon Kinesis Data Analytic H. Send SNS notifications when anomalous behaviors are detected. I. Use event patterns in Amazon CloudWatch Events to capture DynamoDB API call events with an AWS Lambda (unction as a target to analyze behavio J. Send SNS notifications when anomalous behaviors are detected. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Copy the DynamoDB tables into Apache Hive tables on Amazon EMR every hour and analyze them (or anomalous behavior",
      "B": "Send Amazon SNS notifications when anomalous behaviors are detected.",
      "C": "Use AWS CloudTrail to capture all the APIs that change the DynamoDB table",
      "D": "Send SNS notifications when anomalous behaviors are detected using CloudTrail event filtering.",
      "E": "Use Amazon DynamoDB Streams to capture and send updates to AWS Lambd",
      "F": "Create a Lambda function to output records lo Amazon Kinesis Data Stream",
      "G": "Analyze any anomalies with Amazon Kinesis Data Analytic",
      "H": "Send SNS notifications when anomalous behaviors are detected.",
      "I": "Use event patterns in Amazon CloudWatch Events to capture DynamoDB API call events with an AWS Lambda (unction as a target to analyze behavio",
      "J": "Send SNS notifications when anomalous behaviors are detected. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "https://aws.amazon.com/blogs/database/dynamodb-streams-use-cases-and-design-patterns/#:~:text=DynamoDB DynamoDb Stream to capture DynamoDB\nupdate. And Kinesis Data Analytics for anomaly detection (it uses AWS proprietary Random Cut Forest Algorithm)\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "44",
    "question": "- (Exam Topic 1) A company plans to migrate to AWS. A solutions architect uses AWS Application Discovery Service over the fleet and discovers that there is an Oracle data warehouse and several PostgreSQL databases. Which combination of migration patterns will reduce licensing costs and operational overhead? (Select TWO.) A. Lift and shift the Oracle data warehouse to Amazon EC2 using AWS DMS. B. Migrate the Oracle data warehouse to Amazon Redshift using AWS SCT and AWS QMS. C. Lift and shift the PostgreSQL databases to Amazon EC2 using AWS DMS. D. Migrate the PostgreSQL databases to Amazon RDS for PostgreSQL using AWS DMS E. Migrate the Oracle data warehouse to an Amazon EMR managed cluster using AWS DMS. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Lift and shift the Oracle data warehouse to Amazon EC2 using AWS DMS.",
      "B": "Migrate the Oracle data warehouse to Amazon Redshift using AWS SCT and AWS QMS.",
      "C": "Lift and shift the PostgreSQL databases to Amazon EC2 using AWS DMS.",
      "D": "Migrate the PostgreSQL databases to Amazon RDS for PostgreSQL using AWS DMS",
      "E": "Migrate the Oracle data warehouse to an Amazon EMR managed cluster using AWS DMS. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "D"
    ],
    "select_n": 2,
    "explanation": "https://aws.amazon.com/getting-started/hands-on/migrate-oracle-to-amazon-redshift/ https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-\nan-on-premises-postgresql-database\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "52",
    "question": "- (Exam Topic 1) A financial company is building a system to generate monthly, immutable bank account statements for its users. Statements are stored in Amazon S3. Users should have immediate access to their monthly statements for up to 2 years. Some users access their statements frequently, whereas others rarely access their statements. The company's security and compliance policy requires that the statements be retained for at least 7 years. What is the MOST cost-effective solution to meet the company's needs? A. Create an S3 bucket with Object Lock disable B. Store statements in S3 Standar C. Define an S3 Lifecycle policy to transition the data to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 day D. Define another S3 Lifecycle policy to move the data to S3 Glacier Deep Archive after 2 year E. Attach an S3 Glacier Vault Lock policy with deny delete permissions for archives less than 7 years old. F. Create an S3 bucket with versioning enable G. Store statements in S3 Intelligent-Tierin H. Usesame-Region replication to replicate objects to a backup S3 bucke I. Define an S3 Lifecycle policy for the backup S3 bucket to move the data to S3 Glacie J. Attach an S3 Glacier Vault Lock policy with deny delete permissions for archives less than 7 years old. K. Create an S3 bucket with Object Lock enable L. Store statements in S3 Intelligent-Tierin M. Enable compliance mode with a default retention period of 2 year N. Define an S3 Lifecycle policy to move the data to S3 Glacier after 2 year O. Attach an S3 Glacier Vault Lock policy with deny delete permissionsfor archives less than 7 years old. P. Create an S3 bucket with versioning disable Q. Store statements in S3 One Zone-Infrequent Access (S3 One Zone-IA). Define an S3 Lifecyde policy to move the data to S3 Glacier Deep Archive after 2 year R. Attach an S3 Glader Vault Lock policy with deny delete permissions for archives less than 7 years old. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an S3 bucket with Object Lock disable",
      "B": "Store statements in S3 Standar",
      "C": "Define an S3 Lifecycle policy to transition the data to S3 Standard-Infrequent Access (S3 Standard-IA) after 30 day",
      "D": "Define another S3 Lifecycle policy to move the data to S3 Glacier Deep Archive after 2 year",
      "E": "Attach an S3 Glacier Vault Lock policy with deny delete permissions for archives less than 7 years old.",
      "F": "Create an S3 bucket with versioning enable",
      "G": "Store statements in S3 Intelligent-Tierin",
      "H": "Usesame-Region replication to replicate objects to a backup S3 bucke",
      "I": "Define an S3 Lifecycle policy for the backup S3 bucket to move the data to S3 Glacie",
      "J": "Attach an S3 Glacier Vault Lock policy with deny delete permissions for archives less than 7 years old. K. Create an S3 bucket with Object Lock enable L. Store statements in S3 Intelligent-Tierin M. Enable compliance mode with a default retention period of 2 year N. Define an S3 Lifecycle policy to move the data to S3 Glacier after 2 year O. Attach an S3 Glacier Vault Lock policy with deny delete permissionsfor archives less than 7 years old. P. Create an S3 bucket with versioning disable Q. Store statements in S3 One Zone-Infrequent Access (S3 One Zone-IA). Define an S3 Lifecyde policy to move the data to S3 Glacier Deep Archive after 2 year R. Attach an S3 Glader Vault Lock policy with deny delete permissions for archives less than 7 years old. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": "https://aws.amazon.com/about-aws/whats-new/2018/11/s3-object-lock/\nCreate an S3 bucket with Object Lock enabled. Store statements in S3 Intelligent-Tiering. Enable compliance mode with a default retention period of 2 years.\nDefine an S3 Lifecycle policy to move the data to S3 Glacier after 2 years. Attach an S3 Glacier Vault Lock policy with deny delete permissions for archives less\nthan 7 years old.\nhttps://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "56.2",
    "question": "- (Exam Topic 1) A company is creating a REST API to share information with six of its partners based in the United States. The company has created an Amazon API Gateway Regional endpoint. Each of the six partners will access the API once per day to post daily sales figures. After initial deployment, the company observes 1.000 requests per second originating from 500 different IP addresses around the world. The company believes this traffic is originating from a botnet and wants to secure its API while minimizing cost. Which approach should the company take to secure its API? A. Create an Amazon CloudFront distribution with the API as the origi B. Create an AWS WAF web ACL with a rule to block clients \"hat submit more than five requests per da C. Associate the web ACL with the CloudFront distributio D. Configure CloudFront with an origin access identity (OAI) and associate it with the distributio E. Configure API Gateway to ensure only the OAI can execute the POST method. F. Create an Amazon CloudFront distribution with the API as the origi G. Create an AWS WAF web ACL with a rule to block clients that submit more than five requests per da H. Associate the web ACL with the CloudFront distributio I. Add a custom header to the CloudFront distribution populated with an API ke J. Configure the API to require an API key on the POST method. K. Create an AWS WAF web ACL with a rule to allow access to the IP addresses used by the six partners.Associate the web ACL with the AP L. Create a resource policy with a request limit and associate it with the AP M. Configure the API to require an API key on the POST method. N. Associate the web ACL with the AP O. Create a usage plan with a request limit and associate it with the AP P. Create an API key and add it to the usage plan. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an Amazon CloudFront distribution with the API as the origi",
      "B": "Create an AWS WAF web ACL with a rule to block clients \"hat submit more than five requests per da",
      "C": "Associate the web ACL with the CloudFront distributio",
      "D": "Configure CloudFront with an origin access identity (OAI) and associate it with the distributio",
      "E": "Configure API Gateway to ensure only the OAI can execute the POST method.",
      "F": "Create an Amazon CloudFront distribution with the API as the origi",
      "G": "Create an AWS WAF web ACL with a rule to block clients that submit more than five requests per da",
      "H": "Associate the web ACL with the CloudFront distributio",
      "I": "Add a custom header to the CloudFront distribution populated with an API ke",
      "J": "Configure the API to require an API key on the POST method. K. Create an AWS WAF web ACL with a rule to allow access to the IP addresses used by the six partners.Associate the web ACL with the AP L. Create a resource policy with a request limit and associate it with the AP M. Configure the API to require an API key on the POST method. N. Associate the web ACL with the AP O. Create a usage plan with a request limit and associate it with the AP P. Create an API key and add it to the usage plan. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": "\"A usage plan specifies who can access one or more deployed API stages and methods—and also how much and how fast they can access them. The plan uses\nAPI keys to identify API clients and meters access to the associated API stages for each key. It also lets you configure throttling limits and quota limits that are\nenforced on individual client API keys.\"\nhttps://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "57.2",
    "question": "- (Exam Topic 1) A company is planning to set up a REST API application on AWS. The application team wants to set up a new identity store on AWS The IT team does not want to maintain any infrastructure or servers for this deployment. What is the MOST operationally efficient solution that meets these requirements? A. Deploy the application as AWS Lambda function B. Set up Amazon API Gateway REST API endpoints for the application Create a Lambda function, and configure a Lambda authorizer C. Deploy the application in AWS AppSync, and configure AWS Lambda resolvers Set up an Amazon Cognito user pool, and configure AWS AppSync to use the user pool for authorization D. Deploy the application as AWS Lambda function E. Set up Amazon API Gateway REST API endpoints for the application Set up an Amazon Cognito user pool, and configure an Amazon Cognito authorizer F. Deploy the application in Amazon Elastic Kubemetes Service (Amazon EKS) cluster G. Set up an Application Load Balancer for the EKS pods Set up an Amazon Cognito user pool and service pod for authentication. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy the application as AWS Lambda function",
      "B": "Set up Amazon API Gateway REST API endpoints for the application Create a Lambda function, and configure a Lambda authorizer",
      "C": "Deploy the application in AWS AppSync, and configure AWS Lambda resolvers Set up an Amazon Cognito user pool, and configure AWS AppSync to use the user pool for authorization",
      "D": "Deploy the application as AWS Lambda function",
      "E": "Set up Amazon API Gateway REST API endpoints for the application Set up an Amazon Cognito user pool, and configure an Amazon Cognito authorizer",
      "F": "Deploy the application in Amazon Elastic Kubemetes Service (Amazon EKS) cluster",
      "G": "Set up an Application Load Balancer for the EKS pods Set up an Amazon Cognito user pool and service pod for authentication. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "59",
    "question": "- (Exam Topic 1) A company wants to migrate an application to Amazon EC2 from VMware Infrastructure that runs in an on-premises data center. A solutions architect must preserve the software and configuration settings during the migration. What should the solutions architect do to meet these requirements? A. Configure the AWS DataSync agent to start replicating the data store to Amazon FSx for Windows File Server Use the SMB share to host the VMware data stor B. Use VM Import/Export to move the VMs to Amazon EC2. C. Use the VMware vSphere client to export the application as an image in Open Virealization Format (OVF) format Create an Amazon S3 bucket to store the image in the destination AWS Regio D. Create and apply an IAM role for VM Import Use the AWS CLI to run the EC2 import command. E. Configure AWS Storage Gateway for files service to export a Common Internet File System (CIFSJ shar F. Create a backup copy to the shared folde G. Sign in to the AWS Management Console and create an AMI from the backup copy Launch an EC2 instance that is based on the AMI. H. Create a managed-instance activation for a hybrid environment in AWS Systems Manage I. Download and install Systems Manager Agent on the on-premises VM Register the VM with Systems Manager to be a managed instance Use AWS Backup to create a snapshot of the VM and create an AM J. Launch an EC2 instance that is based on the AMI -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure the AWS DataSync agent to start replicating the data store to Amazon FSx for Windows File Server Use the SMB share to host the VMware data stor",
      "B": "Use VM Import/Export to move the VMs to Amazon EC2.",
      "C": "Use the VMware vSphere client to export the application as an image in Open Virealization Format (OVF) format Create an Amazon S3 bucket to store the image in the destination AWS Regio",
      "D": "Create and apply an IAM role for VM Import Use the AWS CLI to run the EC2 import command.",
      "E": "Configure AWS Storage Gateway for files service to export a Common Internet File System (CIFSJ shar",
      "F": "Create a backup copy to the shared folde",
      "G": "Sign in to the AWS Management Console and create an AMI from the backup copy Launch an EC2 instance that is based on the AMI.",
      "H": "Create a managed-instance activation for a hybrid environment in AWS Systems Manage",
      "I": "Download and install Systems Manager Agent on the on-premises VM Register the VM with Systems Manager to be a managed instance Use AWS Backup to create a snapshot of the VM and create an AM",
      "J": "Launch an EC2 instance that is based on the AMI -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html\n- Export an OVF Template\n- Create / use an Amazon S3 bucket for storing the exported images. The bucket must be in the Region where you want to import your VMs.\n- Create an IAM role named vmimport.\n- You'll use AWS CLI to run the import commands. https://aws.amazon.com/premiumsupport/knowledge-center/import-instances/\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "60",
    "question": "- (Exam Topic 1) A solutions architect is building a web application that uses an Amazon RDS for PostgreSQL DB instance The DB instance is expected to receive many more reads than writes The solutions architect needs to ensure that the large amount of read traffic can be accommodated and that the DB instance is highly available. Which steps should the solutions architect take to meet these requirements? (Select THREE.) A. Create multiple read replicas and put them into an Auto Scaling group B. Create multiple read replicas in different Availability Zones. C. Create an Amazon Route 53 hosted zone and a record set for each read replica with a TTL and a weighted routing policy D. Create an Application Load Balancer (ALBJ and put the read replicas behind the ALB. E. Configure an Amazon CloudWatch alarm to detect a failed read replica Set the alarm to directly invoke an AWS Lambda function to delete its Route 53 record set. F. Configure an Amazon Route 53 health check for each read replica using its endpoint -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create multiple read replicas and put them into an Auto Scaling group",
      "B": "Create multiple read replicas in different Availability Zones.",
      "C": "Create an Amazon Route 53 hosted zone and a record set for each read replica with a TTL and a weighted routing policy",
      "D": "Create an Application Load Balancer (ALBJ and put the read replicas behind the ALB.",
      "E": "Configure an Amazon CloudWatch alarm to detect a failed read replica Set the alarm to directly invoke an AWS Lambda function to delete its Route 53 record set.",
      "F": "Configure an Amazon Route 53 health check for each read replica using its endpoint -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "C",
      "F"
    ],
    "select_n": 3,
    "explanation": "https://aws.amazon.com/premiumsupport/knowledge-center/requests-rds-read-replicas/\nYou can use Amazon Route 53 weighted record sets to distribute requests across your read replicas. Within a Route 53 hosted zone, create individual record sets\nfor each DNS endpoint associated with your read replicas and give them the same weight. Then, direct requests to the endpoint of the record set. You can\nincorporate Route 53 health checks to be sure that Route 53 directs traffic away from unavailable read replicas\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "63",
    "question": "- (Exam Topic 1) A company is moving a business-critical multi-tier application to AWS. The architecture consists of a desktop client application and server infrastructure. The server infrastructure resides in an on-premises data center that frequently fails to maintain the application uptime SLA of 99.95%. A solutions architect must re-architect the application to ensure that it can meet or exceed the SLA. The application contains a PostgreSQL database running on a single virtual machine. The business logic and presentation layers are load balanced between multiple virtual machines. Remote users complain about slow load times while using this latency-sensitive application. Which of the following will meet the availability requirements with little change to the application while improving user experience and minimizing costs? A. Migrate the database to a PostgreSQL database in Amazon EC2. Host the application and presentation layers in automatically scaled Amazon ECS containers behind an Application Load Balance B. Allocate an Amazon Workspaces Workspace for each end user to improve the user experience. C. Migrate the database to an Amazon RDS Aurora PostgreSQL configuratio D. Host the application and presentation layers in an Auto Scaling configuration on Amazon EC2 instances behind an Application Load Balance E. Use Amazon AppStream 2.0 to improve the user experience. F. Migrate the database to an Amazon RDS PostgreSQL Mulli-AZ configuratio G. Host the application and presentation layers in automatically scaled AWS Fargate containers behind a Network Load Balance H. Use Amazon ElastiCache to improve the user experience. I. Migrate the database to an Amazon Redshift cluster with at least two node J. Combine and host the application and presentation layers in automatically scaled Amazon ECS containers behind an Application Load Balance K. Use Amazon CloudFront to improve the user experience. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Migrate the database to a PostgreSQL database in Amazon EC2. Host the application and presentation layers in automatically scaled Amazon ECS containers behind an Application Load Balance",
      "B": "Allocate an Amazon Workspaces Workspace for each end user to improve the user experience.",
      "C": "Migrate the database to an Amazon RDS Aurora PostgreSQL configuratio",
      "D": "Host the application and presentation layers in an Auto Scaling configuration on Amazon EC2 instances behind an Application Load Balance",
      "E": "Use Amazon AppStream 2.0 to improve the user experience.",
      "F": "Migrate the database to an Amazon RDS PostgreSQL Mulli-AZ configuratio",
      "G": "Host the application and presentation layers in automatically scaled AWS Fargate containers behind a Network Load Balance",
      "H": "Use Amazon ElastiCache to improve the user experience.",
      "I": "Migrate the database to an Amazon Redshift cluster with at least two node",
      "J": "Combine and host the application and presentation layers in automatically scaled Amazon ECS containers behind an Application Load Balance K. Use Amazon CloudFront to improve the user experience. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "Aurora would improve availability that can replicate to multiple AZ (6 copies). Auto scaling would improve the performance together with a ALB. AppStream is like\nCitrix that deliver hosted Apps to users.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "71.2",
    "question": "- (Exam Topic 1) A company has a data lake in Amazon S3 that needs to be accessed by hundreds of applications across many AWS accounts. The company's information security policy states that the S3 bucket must not be accessed over the public internet and that each application should have the minimum permissions necessary to function. To meet these requirements, a solutions architect plans to use an S3 access point that is restricted to specific VPCs tor each application. Which combination of steps should the solutions architect take to implement this solution? (Select TWO.) A. Create an S3 access point for each application in the AWS account that owns the S3 bucke B. Configure each access point to be accessible only from the application's VP C. Update the bucket policy to require access from an access point. D. Create an interface endpoint for Amazon S3 in each application's VP E. Configure the endpoint policy to allow access to an S3 access poin F. Create a VPC gateway attachment for the S3 endpoint. G. Create a gateway endpoint lor Amazon S3 in each application's VP H. Configure the endpoint policy to allow access to an S3 access poin I. Specify the route table that is used to access the access point. J. Create an S3 access point for each application in each AWS account and attach the access points to the S3 bucke K. Configure each access point to be accessible only from the application's VP L. Update the bucket policy to require access from an access point. M. Create a gateway endpoint for Amazon S3 in the data lake's VP N. Attach an endpoint policy to allow access to the S3 bucke O. Specify the route table that is used to access the bucket. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an S3 access point for each application in the AWS account that owns the S3 bucke",
      "B": "Configure each access point to be accessible only from the application's VP",
      "C": "Update the bucket policy to require access from an access point.",
      "D": "Create an interface endpoint for Amazon S3 in each application's VP",
      "E": "Configure the endpoint policy to allow access to an S3 access poin",
      "F": "Create a VPC gateway attachment for the S3 endpoint.",
      "G": "Create a gateway endpoint lor Amazon S3 in each application's VP",
      "H": "Configure the endpoint policy to allow access to an S3 access poin",
      "I": "Specify the route table that is used to access the access point.",
      "J": "Create an S3 access point for each application in each AWS account and attach the access points to the S3 bucke K. Configure each access point to be accessible only from the application's VP L. Update the bucket policy to require access from an access point. M. Create a gateway endpoint for Amazon S3 in the data lake's VP N. Attach an endpoint policy to allow access to the S3 bucke O. Specify the route table that is used to access the bucket. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C"
    ],
    "select_n": 2,
    "explanation": "https://joe.blog.freemansoft.com/2020/04/protect-data-in-cloud-with-s3-access.html https://aws.amazon.com/s3/features/access-points/\nhttps://aws.amazon.com/s3/features/access-points/\n&\nhttps://aws.amazon.com/blogs/storage/managing-amazon-s3-access-with-vpc-endpoints-and-s3-access-points/\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "72",
    "question": "- (Exam Topic 1) A company is using AWS CodePipeline for the CI/CO of an application to an Amazon EC2 Auto Scaling group. All AWS resources are defined in AWS CloudFormation templates. The application artifacts are stored in an Amazon S3 bucket and deployed to the Auto Scaling group using instance user data scripts. As the application has become more complex, recent resource changes in the Cloud Formation templates have caused unplanned downtime. How should a solutions architect improve the CI'CD pipeline to reduce the likelihood that changes in the templates will cause downtime? A. Adapt the deployment scripts to detect and report CloudFormation error conditions when performing deployment B. Write test plans for a testing team to execute in a non-production environment before approving the change for production. C. Implement automated testing using AWS CodeBuild in a test environmen D. Use CloudFormation changesets to evaluate changes before deploymen E. Use AWS CodeDeploy to leverage blue/green deployment patterns to allow evaluations and the ability to revert changes, if needed. F. Use plugins for the integrated development environment (IDE) to check the templates for errors, and use the AWS CLI to validate that the templates are correc G. Adapt the deployment code to check for error conditions and generate notifications on error H. Deploy to a test environment and execute a manual test plan before approving the change for production. I. Use AWS CodeDeploy and a blue/green deployment pattern with CloudFormation to replace the user data deployment script J. Have the operators log in to running instances and go through a manual test plan to verify the application is running as expected. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Adapt the deployment scripts to detect and report CloudFormation error conditions when performing deployment",
      "B": "Write test plans for a testing team to execute in a non-production environment before approving the change for production.",
      "C": "Implement automated testing using AWS CodeBuild in a test environmen",
      "D": "Use CloudFormation changesets to evaluate changes before deploymen",
      "E": "Use AWS CodeDeploy to leverage blue/green deployment patterns to allow evaluations and the ability to revert changes, if needed.",
      "F": "Use plugins for the integrated development environment (IDE) to check the templates for errors, and use the AWS CLI to validate that the templates are correc",
      "G": "Adapt the deployment code to check for error conditions and generate notifications on error",
      "H": "Deploy to a test environment and execute a manual test plan before approving the change for production.",
      "I": "Use AWS CodeDeploy and a blue/green deployment pattern with CloudFormation to replace the user data deployment script",
      "J": "Have the operators log in to running instances and go through a manual test plan to verify the application is running as expected. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": "https://aws.amazon.com/blogs/devops/performing-bluegreen-deployments-with-aws-codedeploy-and-auto-scalin When one adopts go infrastructure as code, we\nneed to test the infrastructure code as well via automated testing, and revert to original if things are not performing correctly.\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "77",
    "question": "- (Exam Topic 1) A company has implemented an ordering system using an event-dnven architecture. Dunng initial testing, the system stopped processing orders Further tog analysis revealed that one order message in an Amazon Simple Queue Service (Amazon SOS) standard queue was causing an error on the backend and blocking all subsequent order messages The visibility timeout of the queue is set to 30 seconds, and the backend processing timeout is set to 10 seconds. A solutions architect needs to analyze faulty order messages and ensure that the system continues to process subsequent messages Which step should the solutions architect take to meet these requirements? A. Increase the backend processing timeout to 30 seconds to match the visibility timeout B. Reduce the visibility timeout of the queue to automatically remove the faulty message C. Configure a new SOS FIFO queue as a dead-letter queue to isolate the faulty messages D. Configure a new SOS standard queue as a dead-letter queue to isolate the faulty messages. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Increase the backend processing timeout to 30 seconds to match the visibility timeout",
      "B": "Reduce the visibility timeout of the queue to automatically remove the faulty message",
      "C": "Configure a new SOS FIFO queue as a dead-letter queue to isolate the faulty messages",
      "D": "Configure a new SOS standard queue as a dead-letter queue to isolate the faulty messages. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "82.2",
    "question": "- (Exam Topic 1) A developer reports receiving an Error 403: Access Denied message when they try to download an object from an Amazon S3 bucket. The S3 bucket is accessed using an S3 endpoint inside a VPC. and is encrypted with an AWS KMS key. A solutions architect has verified that (he developer is assuming the correct IAM role in the account that allows the object to be downloaded. The S3 bucket policy and the NACL are also valid. Which additional step should the solutions architect take to troubleshoot this issue? A. Ensure that blocking all public access has not been enabled in the S3 bucket. B. Verify that the IAM rote has permission to decrypt the referenced KMS key. C. Verify that the IAM role has the correct trust relationship configured. D. Check that local firewall rules are not preventing access to the S3 endpoint. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Ensure that blocking all public access has not been enabled in the S3 bucket.",
      "B": "Verify that the IAM rote has permission to decrypt the referenced KMS key.",
      "C": "Verify that the IAM role has the correct trust relationship configured.",
      "D": "Check that local firewall rules are not preventing access to the S3 endpoint. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "83",
    "question": "- (Exam Topic 1) A public retail web application uses an Application Load Balancer (ALB) in front of Amazon EC2 instances running across multiple Availability Zones (AZs) in a Region backed by an Amazon RDS MySQL Multi-AZ deployment. Target group health checks are configured to use HTTP and pointed at the product catalogue page. Auto Scaling is configured to maintain the web fleet size based on the ALB health check. Recently, the application experienced an outage. Auto Scaling continuously replaced the instances during the outage. A subsequent investigation determined that the web server metrics were within the normal range, but the database tier was experiencing high load, resulting in severely elevated query response times. Which of the following changes together would remediate these issues while improving monitoring capabilities for the availability and functionality of the entire application stack for future growth? (Select TWO.) A. Configure read replicas for Amazon RDS MySQL and use the single reader endpoint in the web application to reduce the load on the backend database tier. B. Configure the target group health check to point at a simple HTML page instead of a product catalog page and the Amazon Route 53 health check against the product page to evaluate full application functionalit C. Configure Amazon CloudWatch alarms to notify administrators when the site fails. D. Configure the target group health check to use a TCP check of the Amazon EC2 web server and theAmazon Route 53 health check against the product page to evaluate full application functionalit E. Configure Amazon CloudWatch alarms to notify administrators when the site fails. F. Configure an Amazon CloudWatch alarm for Amazon RDS with an action to recover a high-load, impaired RDS instance in the database tier. G. Configure an Amazon ElastiCache cluster and place it between the web application and RDS MySQL instances to reduce the load on the backend database tier. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure read replicas for Amazon RDS MySQL and use the single reader endpoint in the web application to reduce the load on the backend database tier.",
      "B": "Configure the target group health check to point at a simple HTML page instead of a product catalog page and the Amazon Route 53 health check against the product page to evaluate full application functionalit",
      "C": "Configure Amazon CloudWatch alarms to notify administrators when the site fails.",
      "D": "Configure the target group health check to use a TCP check of the Amazon EC2 web server and theAmazon Route 53 health check against the product page to evaluate full application functionalit",
      "E": "Configure Amazon CloudWatch alarms to notify administrators when the site fails.",
      "F": "Configure an Amazon CloudWatch alarm for Amazon RDS with an action to recover a high-load, impaired RDS instance in the database tier.",
      "G": "Configure an Amazon ElastiCache cluster and place it between the web application and RDS MySQL instances to reduce the load on the backend database tier. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "E"
    ],
    "select_n": 2,
    "explanation": "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-types.html\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
  },
  {
    "id": "86",
    "question": "- (Exam Topic 1) A company is running an application on Amazon EC2 instances in three environments; development, testing, and production. The company uses AMIs to deploy the EC2 instances. The company builds the AMIs by using custom deployment scripts and infrastructure orchestration tools for each release in each environment. The company is receiving errors in its deployment process. Errors appear during operating system package downloads and during application code installation from a third-party Git hosting service. The company needs deployments to become more reliable across all environments. Which combination of steps will meet these requirements? (Select THREE). A. Mirror the application code to an AWS CodeCommit Git repositor B. Use the repository to build EC2 AMIs. C. Produce multiple EC2 AMI D. one for each environment, for each release. E. Produce one EC2 AMI for each release for use across all environments. F. Mirror the application code to a third-party Git repository that uses Amazon S3 storag G. Use therepository for deployment. H. Replace the custom scripts and tools with AWS CodeBuil I. Update the infrastructure deployment process to use EC2 Image Builder. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Mirror the application code to an AWS CodeCommit Git repositor",
      "B": "Use the repository to build EC2 AMIs.",
      "C": "Produce multiple EC2 AMI",
      "D": "one for each environment, for each release.",
      "E": "Produce one EC2 AMI for each release for use across all environments.",
      "F": "Mirror the application code to a third-party Git repository that uses Amazon S3 storag",
      "G": "Use therepository for deployment.",
      "H": "Replace the custom scripts and tools with AWS CodeBuil",
      "I": "Update the infrastructure deployment process to use EC2 Image Builder. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C",
      "E"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "91",
    "question": "- (Exam Topic 1) A company uses AWS Transit Gateway for a hub-and-spoke model to manage network traffic between many VPCs. The company is developing a new service that must be able to send data at 100 Gbps. The company needs a faster connection to other VPCs in the same AWS Region. Which solution will meet these requirements? A. Establish VPC peering between the necessary VPC B. Ensure that all route tables are updated as required. C. Attach an additional transit gateway to the VPC D. Update the route tables accordingly. E. Create AWS Site-to-Site VPN connections that use equal-cost multi-path (ECMP) routing between the necessary VPCs. F. Create an additional attachment from the necessary VPCs to the existing transit gateway. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Establish VPC peering between the necessary VPC",
      "B": "Ensure that all route tables are updated as required.",
      "C": "Attach an additional transit gateway to the VPC",
      "D": "Update the route tables accordingly.",
      "E": "Create AWS Site-to-Site VPN connections that use equal-cost multi-path (ECMP) routing between the necessary VPCs.",
      "F": "Create an additional attachment from the necessary VPCs to the existing transit gateway. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "114",
    "question": "- (Exam Topic 2) A company wants to migrate its workloads from on premises to AWS. The workloads run on Linux and Windows. The company has a large on-premises intra structure that consists of physical machines and VMs that host numerous applications. The company must capture details about the system configuration. system performance. running processure and network coi.net lions of its o. -premises ,on boards. The company also must divide the on-premises applications into groups for AWS migrations. The company needs recommendations for Amazon EC2 instance types so that the company can run its workloads on AWS in the most cost-effective manner. Which combination of steps should a solutions architect take to meet these requirements? (Select THREE.) A. Assess the existing applications by installing AWS Application Discovery Agent on the physical machines and VMs. B. Assess the existing applications by installing AWS Systems Manager Agent on the physical machines and VMs C. Group servers into applications for migration by using AWS Systems Manager Application Manager. D. Group servers into applications for migration by using AWS Migration Hub. E. Generate recommended instance types and associated costs by using AWS Migration Hub. F. Import data about server sizes into AWS Trusted Adviso G. Follow the recommendations for cost optimization. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Assess the existing applications by installing AWS Application Discovery Agent on the physical machines and VMs.",
      "B": "Assess the existing applications by installing AWS Systems Manager Agent on the physical machines and VMs",
      "C": "Group servers into applications for migration by using AWS Systems Manager Application Manager.",
      "D": "Group servers into applications for migration by using AWS Migration Hub.",
      "E": "Generate recommended instance types and associated costs by using AWS Migration Hub.",
      "F": "Import data about server sizes into AWS Trusted Adviso",
      "G": "Follow the recommendations for cost optimization. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "D",
      "F"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "118.2",
    "question": "- (Exam Topic 2) A fleet of Amazon ECS instances is used to poll an Amazon SQS queue and update items in an Amazon DynamoDB database Items in the table are not being updated, and the SQS queue Is filling up Amazon CloudWatch Logs are showing consistent 400 errors when attempting to update the table The provisioned write capacity units are appropriately configured, and no throttling is occurring What is the LIKELY cause of the failure*? A. The ECS service was deleted B. The ECS configuration does not contain an Auto Scaling group C. The ECS instance task execution IAM role was modified D. The ECS task role was modified -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "The ECS service was deleted",
      "B": "The ECS configuration does not contain an Auto Scaling group",
      "C": "The ECS instance task execution IAM role was modified",
      "D": "The ECS task role was modified -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "122.2",
    "question": "- (Exam Topic 2) A large company has many business units Each business unit has multiple AWS accounts for different purposes. The CIO of the company sees that each business unit has data that would be useful to share with other parts of the company in total there are about 10 PB of data that needs to be shared with users in 1.000 AWS accounts. The data is proprietary so some of it should only be available to users with specific job types Some of the data is used for throughput of intensive workloads such as simulations. The number of accounts changes frequently because of new initiatives acquisitions and divestitures A solutions architect has been asked to design a system that will allow for sharing data for use in AWS with all of the employees in the company Which approach will allow for secure data sharing in scalable way? A. Store the data in a single Amazon S3 bucket Create an IAM role for every combination of job type and business unit that allows for appropriate read/write access based on object prefixes in the S3 bucket The roles should have trust policies that allow the business unit's AWS accounts to assume their roles UseIAM in each business unit's AWS account to prevent them from assuming roles for a different job type Users get credentials to access the data by using AssumeRole from their business unit's AWS account Users can then use those credentials with an S3 client B. Store the data in a single Amazon S3 bucket Write a bucket policy that uses conditions to grant read and write access where appropriate based on each user's business unit and job typ C. Determine the business unit with the AWS account accessing the bucket and the job type with a prefix in the IAM user's name Users can access data by using IAM credentials from their business unit's AWS account with an S3 client D. Store the data in a series of Amazon S3 buckets Create an application running m Amazon EC2 that is integrated with the company's identity provider (IdP) thatauthenticates users and allows them to download or upload data through the application The application uses the business unit and job type information in the IdP to control what users can upload and download through the application The users can access the data through the application's API E. Store the data in a series of Amazon S3 buckets Create an AWS STS token vending machine that is integrated with the company's identity provider (IdP) When a user logs in: have the token vending machine attach an IAM policy that assumes the role that limits the user's access and/or upload only the data the user is authorized to access Users can get credentials by authenticating to the token vending machine's website or API and then use those credentials with an S3 client -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Store the data in a single Amazon S3 bucket Create an IAM role for every combination of job type and business unit that allows for appropriate read/write access based on object prefixes in the S3 bucket The roles should have trust policies that allow the business unit's AWS accounts to assume their roles UseIAM in each business unit's AWS account to prevent them from assuming roles for a different job type Users get credentials to access the data by using AssumeRole from their business unit's AWS account Users can then use those credentials with an S3 client",
      "B": "Store the data in a single Amazon S3 bucket Write a bucket policy that uses conditions to grant read and write access where appropriate based on each user's business unit and job typ",
      "C": "Determine the business unit with the AWS account accessing the bucket and the job type with a prefix in the IAM user's name Users can access data by using IAM credentials from their business unit's AWS account with an S3 client",
      "D": "Store the data in a series of Amazon S3 buckets Create an application running m Amazon EC2 that is integrated with the company's identity provider (IdP) thatauthenticates users and allows them to download or upload data through the application The application uses the business unit and job type information in the IdP to control what users can upload and download through the application The users can access the data through the application's API",
      "E": "Store the data in a series of Amazon S3 buckets Create an AWS STS token vending machine that is integrated with the company's identity provider (IdP) When a user logs in: have the token vending machine attach an IAM policy that assumes the role that limits the user's access and/or upload only the data the user is authorized to access Users can get credentials by authenticating to the token vending machine's website or API and then use those credentials with an S3 client -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "E"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "135.2",
    "question": "- (Exam Topic 2) A company is planning to migrate an application from on premises to the AWS Cloud. The company will begin the migration by moving the application's underlying data storage to AWS The application data is stored on a shared tie system on premises, and the application servers connect to the shared We system through SMB. A solutions architect must implement a solution that uses an Amazon S3 bucket tor shared storage Until the application Is fully migrated and code is rewritten to use native Amazon S3 APIs, the application must continue to have access to the data through SMB The solutions architect must migrate the application data to AWS to its new location while still allowing the on-premises application to access the data. Which solution will meet these requirements? A. Create a new Amazon FSx for Windows File Server fie system Configure AWS DataSync with one location tor the on-premises file share and one location for the new Amazon FSx file system Create a new DataSync task to copy the data from the on-premises file share location to the Amazon FSx file system B. Create an S3 bucket for the applicatio C. Copy the data from the on-premises storage to the S3 bucket D. Deploy an AWS Server Migration Service (AWS SMS) VM to the on-premises environmen E. Use AWS SMS to migrate the file storage server from on premises to an Amazon EC2 instance F. Create an S3 bucket for the applicatio G. Deploy a new AWS Storage Gateway Me gateway on anon-premises V H. Create a new file share that stores data in the S3 bucket and is associated with the tie gatewa I. Copy the data from the on-premises storage to the new file gateway endpoint. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a new Amazon FSx for Windows File Server fie system Configure AWS DataSync with one location tor the on-premises file share and one location for the new Amazon FSx file system Create a new DataSync task to copy the data from the on-premises file share location to the Amazon FSx file system",
      "B": "Create an S3 bucket for the applicatio",
      "C": "Copy the data from the on-premises storage to the S3 bucket",
      "D": "Deploy an AWS Server Migration Service (AWS SMS) VM to the on-premises environmen",
      "E": "Use AWS SMS to migrate the file storage server from on premises to an Amazon EC2 instance",
      "F": "Create an S3 bucket for the applicatio",
      "G": "Deploy a new AWS Storage Gateway Me gateway on anon-premises V",
      "H": "Create a new file share that stores data in the S3 bucket and is associated with the tie gatewa",
      "I": "Copy the data from the on-premises storage to the new file gateway endpoint. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "140",
    "question": "- (Exam Topic 2) A company has an organization in AWS Organizations that has a large number of AWS accounts. One of the AWS accounts is designated as a transit account and has a transit gateway that is shared with all of the other AWS accounts AWS Site-to-Site VPN connections are configured between ail of the company's global offices and the transit account The company has AWS Config enabled on all of its accounts. The company's networking team needs to centrally manage a list of internal IP address ranges that belong to the global offices Developers Will reference this list to gain access to applications securely. Which solution meets these requirements with the LEAST amount of operational overhead? A. Create a JSON file that is hosted in Amazon S3 and that lists all of the internal IP address ranges Configure an Amazon Simple Notification Service (Amazon SNS) topic in each of the accounts that can be involved when the JSON file is update B. Subscribe an AWS Lambda function to the SNS topic to update all relevant security group rules with Vie updated IP address ranges. C. Create a new AWS Config managed rule that contains all of the internal IP address ranges Use the rule to check the security groups in each of the accounts to ensure compliance with the list of IP address range D. Configure the rule to automatically remediate any noncompliant security group that is detected. E. In the transit account, create a VPC prefix list with all of the internal IP address range F. Use AWS Resource Access Manager to share the prefix list with all of the other account G. Use the shared prefix list to configure security group rules is the other accounts. H. In the transit account create a security group with all of the internal IP address range I. Configure the security groups in me other accounts to reference the transit account's securitygroup by using a nested security group reference of *<transit- account-id>./sg-1a2b3c4d\". -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create a JSON file that is hosted in Amazon S3 and that lists all of the internal IP address ranges Configure an Amazon Simple Notification Service (Amazon SNS) topic in each of the accounts that can be involved when the JSON file is update",
      "B": "Subscribe an AWS Lambda function to the SNS topic to update all relevant security group rules with Vie updated IP address ranges.",
      "C": "Create a new AWS Config managed rule that contains all of the internal IP address ranges Use the rule to check the security groups in each of the accounts to ensure compliance with the list of IP address range",
      "D": "Configure the rule to automatically remediate any noncompliant security group that is detected.",
      "E": "In the transit account, create a VPC prefix list with all of the internal IP address range",
      "F": "Use AWS Resource Access Manager to share the prefix list with all of the other account",
      "G": "Use the shared prefix list to configure security group rules is the other accounts.",
      "H": "In the transit account create a security group with all of the internal IP address range",
      "I": "Configure the security groups in me other accounts to reference the transit account's securitygroup by using a nested security group reference of *<transit- account-id>./sg-1a2b3c4d\". -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "68",
    "question": "- (Exam Topic 2) A solutions architect uses AWS Organizations to manage several AWS accounts for a company. The full Organizations feature set is activated for the organization. All production AWS accounts exist under an OU that is named \"production ‘’ Systems operators have full administrative privileges within these accounts by using IAM roles. The company wants to ensure that security groups in all production accounts do not allow inbound traffic for TCP port 22. All noncompliant security groups must be remediated immediately, and no new rules that allow port 22 can be created. Winch solution will meet these requirements? A. Write an SCP that denies the CreateSecurityGroup action with a condition o( ec2:tngress rule with value 22. Apply the SCP to the 'production' OU. B. Configure an AWS CloudTrail trail for all accounts Send CloudTrail logs to an Amazon S3 bucket In the Organizations management accoun C. Configure an AWS Lambda function on the management account with permissions to assume a role in all production accounts to describe and modify security group D. Configure Amazon S3 to invoke the Lambda function on every PutObject event on the S3 bucket Configure the Lambda function to analyze each CloudTrail event for noncompliant security group actions and to automatically remediate any issues. E. Create an Amazon EvertBridge (Amazon CloudWatch Events) event bus in the Organizations management accoun F. Create an AWS Cloud Formation template to deploy configurations that send CreateSecurityGroup events to the even! bus from an production accounts Configure an AWS Lambda function in the management account with permissions to assume a role «i all production accounts to describe and modify security group G. Configure the event bus to invoke the Lambda function Configure the Lambda function to analyse each event for noncompliant security group actions and to automatically remediate any issues. H. Create an AWS CloudFormation template to turn on AWS Config Activate the INCOMING_SSH_DISABLED AWS Config managed rule Deploy an AWS Lambda function that will run based on AWS Config findings and will remediate noncompliant resources Deploy the CloudFormation template by using a StackSet that is assigned to the \"production\" O I. Apply an SCP to the OU to deny modification of the resources that the CloudFormation template provisions. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Write an SCP that denies the CreateSecurityGroup action with a condition o( ec2:tngress rule with value 22. Apply the SCP to the 'production' OU.",
      "B": "Configure an AWS CloudTrail trail for all accounts Send CloudTrail logs to an Amazon S3 bucket In the Organizations management accoun",
      "C": "Configure an AWS Lambda function on the management account with permissions to assume a role in all production accounts to describe and modify security group",
      "D": "Configure Amazon S3 to invoke the Lambda function on every PutObject event on the S3 bucket Configure the Lambda function to analyze each CloudTrail event for noncompliant security group actions and to automatically remediate any issues.",
      "E": "Create an Amazon EvertBridge (Amazon CloudWatch Events) event bus in the Organizations management accoun",
      "F": "Create an AWS Cloud Formation template to deploy configurations that send CreateSecurityGroup events to the even! bus from an production accounts Configure an AWS Lambda function in the management account with permissions to assume a role «i all production accounts to describe and modify security group",
      "G": "Configure the event bus to invoke the Lambda function Configure the Lambda function to analyse each event for noncompliant security group actions and to automatically remediate any issues.",
      "H": "Create an AWS CloudFormation template to turn on AWS Config Activate the INCOMING_SSH_DISABLED AWS Config managed rule Deploy an AWS Lambda function that will run based on AWS Config findings and will remediate noncompliant resources Deploy the CloudFormation template by using a StackSet that is assigned to the \"production\" O",
      "I": "Apply an SCP to the OU to deny modification of the resources that the CloudFormation template provisions. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "153.2",
    "question": "- (Exam Topic 2) A company recently started hosting new application workloads in the AWS Cloud. The company is using Amazon EC2 instances. Amazon Elastic File System (Amazon EFS) file systems, and Amazon RDS DB instances. To meet regulatory and business requirements, the company must make the following changes for data backups: • Backups must be retained based on custom daily, weekly, and monthly requirements. • Backups must be replicated to at least one other AWS Region immediately after capture. • The backup solution must provide a single source of backup status across the AWS environment. • The backup solution must send immediate notifications upon failure of any resource backup. Which combination of steps will meet these requirements with the LEAST amount of operational overhead? (Select THREE.) A. Create an AWS Backup plan with a backup rule for each of the retention requirements. B. Configure an AWS Backup plan to copy backups to another Region. C. Create an AWS Lambda function to replicate backups to another Region and send notification if a failure occurs. D. Add an Amazon Simple Notification Service (Amazon SNS) topic to the backup plan to send a notification for finished jobs that have any status except BACKUP_JOB_COMPLETEO. E. Create an Amazon Data Lifecycle Manager (Amazon DLM) snapshot lifecycle policy for each of the retention requirements. F. Set up RDS snapshots on each database. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an AWS Backup plan with a backup rule for each of the retention requirements.",
      "B": "Configure an AWS Backup plan to copy backups to another Region.",
      "C": "Create an AWS Lambda function to replicate backups to another Region and send notification if a failure occurs.",
      "D": "Add an Amazon Simple Notification Service (Amazon SNS) topic to the backup plan to send a notification for finished jobs that have any status except BACKUP_JOB_COMPLETEO.",
      "E": "Create an Amazon Data Lifecycle Manager (Amazon DLM) snapshot lifecycle policy for each of the retention requirements.",
      "F": "Set up RDS snapshots on each database. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B",
      "D",
      "E"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "166.3",
    "question": "- (Exam Topic 2) A gaming company created a game leaderboard by using a Multi-AZ deployment of an Amazon RDS database. The number of users is growing, and the queries to get individual player rankings are getting slower over time. The company expects a surge in users for an upcoming version and wants to optimize the design for scalability and performance. Which solution will meet these requirements? A. Migrate the database to Amazon DynamoD B. Store the leader different table C. Use Apache HiveQL JOIN statements to build the leaderboard D. Keep the leaderboard data in the RDS DB instanc E. Provision a Multi-AZ deployment of an Amazon ElastiCache for Redis cluster. F. Stream the leaderboard data by using Amazon Kinesis Data Firehose with an Amazon S3 bucket as the destinatio G. Query the S3 bucket by using Amazon Athena for the leaderboard. H. Add a read-only replica to the RDS DB instanc I. Add an RDS Proxy database proxy. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Migrate the database to Amazon DynamoD",
      "B": "Store the leader different table",
      "C": "Use Apache HiveQL JOIN statements to build the leaderboard",
      "D": "Keep the leaderboard data in the RDS DB instanc",
      "E": "Provision a Multi-AZ deployment of an Amazon ElastiCache for Redis cluster.",
      "F": "Stream the leaderboard data by using Amazon Kinesis Data Firehose with an Amazon S3 bucket as the destinatio",
      "G": "Query the S3 bucket by using Amazon Athena for the leaderboard.",
      "H": "Add a read-only replica to the RDS DB instanc",
      "I": "Add an RDS Proxy database proxy. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "171",
    "question": "- (Exam Topic 2) A company is planning to migrate an application from on premises to AWS. The application currently uses an Oracle database and the company can tolerate a brief downtime of 1 hour when performing the switch to the new infrastructure As part of the migration. the database engine will be changed to MySQL. A solutions architect needs to determine which AWS services can be used to perform the migration while minimizing the amount of work and time required. Which of the following will meet the requirements? A. Use AWS SCT to generate the schema scripts and apply them on the target prior to migration Use AWS DMS to analyse the current schema and provide a recommendation for the optimal database engine Then, use AWS DMS to migrate to the recommended engine Use AWS SCT to identify what embedded SQL code in the application can be converted and what has to be done manually B. Use AWS SCT to generate the schema scripts and apply them on the target prior to migratio C. Use AWS DMS to begin moving data from the on-premises database to AW D. After the initial copy continue to use AWS DMS to keep the databases m sync until cutting over to the new database Use AWS SCT to identify what embedded SOL code in the application can be converted and what has to be done manually. E. Use AWS DMS lo help identify the best target deployment between installing the database engine on Amazon EC2 directly or moving to Amazon RD F. Then, use AWS DMS to migrate to the platfor G. Use AWS Application Discovery Service to identify what embedded SQL code in the application can be converted and what has to be done manually. H. Use AWS DMS to begin moving data from the on-premises database to AWS After the initial copy, continue to use AWS DMS to keep the databases in sync until cutting over to the new database use AWS Application Discovery Service to identify what embedded SQL code m the application can be convened and what has to be done manually -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS SCT to generate the schema scripts and apply them on the target prior to migration Use AWS DMS to analyse the current schema and provide a recommendation for the optimal database engine Then, use AWS DMS to migrate to the recommended engine Use AWS SCT to identify what embedded SQL code in the application can be converted and what has to be done manually",
      "B": "Use AWS SCT to generate the schema scripts and apply them on the target prior to migratio",
      "C": "Use AWS DMS to begin moving data from the on-premises database to AW",
      "D": "After the initial copy continue to use AWS DMS to keep the databases m sync until cutting over to the new database Use AWS SCT to identify what embedded SOL code in the application can be converted and what has to be done manually.",
      "E": "Use AWS DMS lo help identify the best target deployment between installing the database engine on Amazon EC2 directly or moving to Amazon RD",
      "F": "Then, use AWS DMS to migrate to the platfor",
      "G": "Use AWS Application Discovery Service to identify what embedded SQL code in the application can be converted and what has to be done manually.",
      "H": "Use AWS DMS to begin moving data from the on-premises database to AWS After the initial copy, continue to use AWS DMS to keep the databases in sync until cutting over to the new database use AWS Application Discovery Service to identify what embedded SQL code m the application can be convened and what has to be done manually -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "192.2",
    "question": "- (Exam Topic 2) A large education company recently introduced Amazon Workspaces to provide access to internal applications across multiple universities. The company is storing user proxies on an Amazon FSx for Windows File Server tile system. The Me system is configured with a DNS alias and is connected to a self-managed Active Directory As more users begin to use the Workspaces login time increases to unacceptable levels An investigation reveals a degradation in performance of the file system. The company created the file system on HDD storage with a throughput of 16 MBps A solutions architect must improve the performance of the file system during a defined maintenance window What should the solutions architect do to meet these requirements with the LEAST administrative effort? A. Use AWS Backup to create a point-in-time backup of the file system Restore the backup to a new FSx for Windows File Server file system Select SSD as the storage type Select 32 MBps as the throughput capacity When the backup and restore process is completed adjust the DNS alias accordingly Delete the original file system B. Disconnect users from the file system In the Amazon FSx console, update the throughput capacity to 32 MBps Update the storage type to SSD Reconnect users to the file system C. Deploy an AWS DataSync agent onto a new Amazon EC2 instanc D. Create a task Configure the existing file system as the source location Configure a new FSx forWindows File Server file system with SSD storage and 32 MBps of throughput as the target location Schedule the task When the task is completed adjust the DNS alias accordingly Delete the original file system. E. Enable shadow copies on the existing file system by using a Windows PowerShell command Schedule the shadow copy job to create a point-in-time backup of the file system Choose to restore previousversions Create a new FSx for Windows File Server file system with SSD storage and 32 MBps of throughput When the copy job is completed, adjust the DNS alias Delete the original file system -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Use AWS Backup to create a point-in-time backup of the file system Restore the backup to a new FSx for Windows File Server file system Select SSD as the storage type Select 32 MBps as the throughput capacity When the backup and restore process is completed adjust the DNS alias accordingly Delete the original file system",
      "B": "Disconnect users from the file system In the Amazon FSx console, update the throughput capacity to 32 MBps Update the storage type to SSD Reconnect users to the file system",
      "C": "Deploy an AWS DataSync agent onto a new Amazon EC2 instanc",
      "D": "Create a task Configure the existing file system as the source location Configure a new FSx forWindows File Server file system with SSD storage and 32 MBps of throughput as the target location Schedule the task When the task is completed adjust the DNS alias accordingly Delete the original file system.",
      "E": "Enable shadow copies on the existing file system by using a Windows PowerShell command Schedule the shadow copy job to create a point-in-time backup of the file system Choose to restore previousversions Create a new FSx for Windows File Server file system with SSD storage and 32 MBps of throughput When the copy job is completed, adjust the DNS alias Delete the original file system -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "194.2",
    "question": "- (Exam Topic 2) A company is deploying a third-party firewall appliance solution from AWS Marketplace to monitor and protect traffic that leaves the company's AWS environments. The company wants to deploy this appliance into a shared services VPC and route all outbound internet-bound traffic through the appliances. A solutions architect needs to recommend a deployment method that prioritizes reliability and minimizes failover time between firewall appliances within a single AWS Region. The company has set up routing from the shared services VPC to other VPCs. Which steps should the solutions architect recommend to meet these requirements? (Select THREE) A. Deploy two firewall appliances into the shared services VP B. each in a separate Availability Zone C. Create a new Network Load Balancer in the shared services VPC Create a new target group, and attach it to the new Network Load Balancer Add each of the firewall appliance instances to the target group. D. Create a new Gateway Load Balancer in the shared services VPC Create a new target group, and attach it to the new Gateway Load Balancer Add each of the firewall appliance instances to the target group E. Create a VPC interface endpoint Add a route to the route table in the shared services VP F. Designate the new endpoint as the next hop for traffic that enters the shared services VPC from other VPCs. G. Deploy two firewall appliances into the shared services VP H. each in the same Availability Zone -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Deploy two firewall appliances into the shared services VP",
      "B": "each in a separate Availability Zone",
      "C": "Create a new Network Load Balancer in the shared services VPC Create a new target group, and attach it to the new Network Load Balancer Add each of the firewall appliance instances to the target group.",
      "D": "Create a new Gateway Load Balancer in the shared services VPC Create a new target group, and attach it to the new Gateway Load Balancer Add each of the firewall appliance instances to the target group",
      "E": "Create a VPC interface endpoint Add a route to the route table in the shared services VP",
      "F": "Designate the new endpoint as the next hop for traffic that enters the shared services VPC from other VPCs.",
      "G": "Deploy two firewall appliances into the shared services VP",
      "H": "each in the same Availability Zone -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "C"
    ],
    "select_n": 3,
    "explanation": ""
  },
  {
    "id": "209",
    "question": "- (Exam Topic 2) An ecommerce company runs its infrastructure on AWS. The company exposes its APIs to its web and mobile clients through an Application Load Balancer (ALB) in front of an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. The EKS cluster runs thousands of pods that provide the APIs. After extending delivery to a new continent, the company adds an Amazon CloudFront distribution and sets the ALB as the origin. The company also adds AWS WAF to its architecture. After implementation of the new architecture, API calls are significantly. However, there is a sudden increase in HTTP status code 504 (Gateway Timeout) errors and HTTP status code 502 (Bad Gateway) errors. This increase in errors seems to be for a specific domain. Which factors could be a cause of these errors? (Select TWO.) A. AWS WAF is blocking suspicious requests. B. The origin is not properly configured in CloudFront. C. There is an SSL/TLS handshake issue between CloudFront and the origin. D. EKS Kubernetes pods are being cycled. E. Some pods are taking more than 30 seconds to answer API calls. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "AWS WAF is blocking suspicious requests.",
      "B": "The origin is not properly configured in CloudFront.",
      "C": "There is an SSL/TLS handshake issue between CloudFront and the origin.",
      "D": "EKS Kubernetes pods are being cycled.",
      "E": "Some pods are taking more than 30 seconds to answer API calls. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "E"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "112",
    "question": "- (Exam Topic 2) A software company has deployed an application that consumes a REST API by using Amazon API Gateway. AWS Lambda functions, and an Amazon DynamoDB table. The application is showing an increase in the number of errors during PUT requests. Most of the PUT calls come from a small number of clients that are authenticated with specific API keys. A solutions architect has identified that a large number of the PUT requests originate from one client. The API is noncritical, and clients can tolerate retries of unsuccessful calls. However, the errors are displayed to customers and are causing damage to the API's reputation. What should the solutions architect recommend to improve the customer experience? A. Implement retry logic with exponential backoff and irregular variation in the client applicatio B. Ensure that the errors are caught and handled with descriptive error messages. C. Implement API throttling through a usage plan at the API Gateway leve D. Ensure that the client application handles code 429 replies without error. E. Turn on API caching to enhance responsiveness for the production stag F. Run 10-minute load tests.Verify that the cache capacity is appropriate for the workload. G. Implement reserved concurrency at the Lambda function level to provide the resources that are needed during sudden increases in traffic. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Implement retry logic with exponential backoff and irregular variation in the client applicatio",
      "B": "Ensure that the errors are caught and handled with descriptive error messages.",
      "C": "Implement API throttling through a usage plan at the API Gateway leve",
      "D": "Ensure that the client application handles code 429 replies without error.",
      "E": "Turn on API caching to enhance responsiveness for the production stag",
      "F": "Run 10-minute load tests.Verify that the cache capacity is appropriate for the workload.",
      "G": "Implement reserved concurrency at the Lambda function level to provide the resources that are needed during sudden increases in traffic. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "115.2",
    "question": "- (Exam Topic 2) A company is running an application in the AWS Cloud. The application consists of microservices that run on a fleet of Amazon EC2 instances in multiple Availability Zones behind an Application Load Balancer. The company recently added a new REST API that was implemented in Amazon API Gateway. Some of the older microservices that run on EC2 instances need to call this new API The company does not want the API to be accessible from the public internet and does not want proprietary data to traverse the public internet What should a solutions architect do to meet these requirements? A. Create an AWS Site-to-Site VPN connection between the VPC and the API Gateway Use API Gateway to generate a unique API key for each microservic B. Configure the API methods to require the key. C. Create an interface VPC endpoint for API Gateway, and set an endpoint policy to only allow access to the specific API Add a resource policy to API Gateway to only allow access from the VPC endpoint Change the API Gateway endpoint type to private. D. Modify the API Gateway to use IAM authentication Update the IAM policy for the IAM role that isassigned to the EC2 instances to allow access to the API Gateway Move the API Gateway into a new VPC Deploy a transit gateway and connect the VPCs. E. Create an accelerator in AWS Global Accelerator and connect the accelerator to the API Gateway.Update the route table for all VPC subnets with a route to the created Global Accelerator endpoint IP addres F. Add an API key for each service to use for authentication. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an AWS Site-to-Site VPN connection between the VPC and the API Gateway Use API Gateway to generate a unique API key for each microservic",
      "B": "Configure the API methods to require the key.",
      "C": "Create an interface VPC endpoint for API Gateway, and set an endpoint policy to only allow access to the specific API Add a resource policy to API Gateway to only allow access from the VPC endpoint Change the API Gateway endpoint type to private.",
      "D": "Modify the API Gateway to use IAM authentication Update the IAM policy for the IAM role that isassigned to the EC2 instances to allow access to the API Gateway Move the API Gateway into a new VPC Deploy a transit gateway and connect the VPCs.",
      "E": "Create an accelerator in AWS Global Accelerator and connect the accelerator to the API Gateway.Update the route table for all VPC subnets with a route to the created Global Accelerator endpoint IP addres",
      "F": "Add an API key for each service to use for authentication. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "212",
    "question": "- (Exam Topic 2) A company plans to deploy a new private Intranet service on Amazon EC2 instances inside a VPC. An AWS Site-to-Site VPN connects the VPC to the company's ort-premises network. The new service must communicate with existing on-premises services. The on-premises services are accessible through the use of hostnames that reside in the company example DNS zone. This DNS zone is wholly hosted on premises and is available only on the company's private network. A solutions architect must ensure that the new service can resolve hostnames on the company.example domain to integrate with existing services. Which solution meets these requirements? A. Create an empty private zone in Amazon Route 53 for company.exampl B. Add an additional NS record to the company's on-premises company.example zone that points to the authoritative name servers for the new private zone in Route 53 C. Turn on DNS hostnames for the VP D. Configure a new outbound endpoint with Amazon Route 53 Resolve E. Create a Resolver rule to forward requests for company.example to the on-premises name servers. F. Turn on DNS hostnames for the VP G. Configure a new inbound resolver endpoint with Amazon Route 53 Resolve H. Configure the on-premises DNS server to forward requests for company.example to the new resolver. I. Use AWS Systems Manager to configure a run document that will install a hosts file that contains any required hostname J. Use an Amazon Event8ndge (Amazon CloudWatch Events) rule lo run the document when an instance is entering the running state. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Create an empty private zone in Amazon Route 53 for company.exampl",
      "B": "Add an additional NS record to the company's on-premises company.example zone that points to the authoritative name servers for the new private zone in Route 53",
      "C": "Turn on DNS hostnames for the VP",
      "D": "Configure a new outbound endpoint with Amazon Route 53 Resolve",
      "E": "Create a Resolver rule to forward requests for company.example to the on-premises name servers.",
      "F": "Turn on DNS hostnames for the VP",
      "G": "Configure a new inbound resolver endpoint with Amazon Route 53 Resolve",
      "H": "Configure the on-premises DNS server to forward requests for company.example to the new resolver.",
      "I": "Use AWS Systems Manager to configure a run document that will install a hosts file that contains any required hostname",
      "J": "Use an Amazon Event8ndge (Amazon CloudWatch Events) rule lo run the document when an instance is entering the running state. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "217",
    "question": "- (Exam Topic 2) A company has developed a new release of a popular video game and wants to make it available for public download. The new release package is approximately 5 GB in size. The company provides downloads for existing releases from a Linux-based, publicly facing FTP site hosted in an on-premises data center. The company expects the new release will be downloaded by users worldwide The company wants a solution that provides improved download performance and low transfer costs, regardless of a user's location. Which solutions will meet these requirements? A. Store the game files on Amazon EBS volumes mounted on Amazon EC2 instances within an Auto Scaling group Configure an FTP service on the EC2 instances Use an Application Load Balancer in front of the Auto Scaling grou B. Publish the game download URL for users to download the package. C. Store the game files on Amazon EFS volumes that are attached to Amazon EC2 instances within an Auto Scaling group Configure an FTP service on each of the EC2 instances Use an Application Load Balancer in front of the Auto Scaling group Publish the game download URL for users to download the package D. Configure Amazon Route 53 and an Amazon S3 bucket for website hosting Upload the game files to the S3 bucket Use Amazon CloudFront for the website Publish the game download URL for users to download the package. E. Configure Amazon Route 53 and an Amazon S3 bucket for website hosting Upload the game files to the S3 bucket Set Requester Pays for the S3 bucket Publish the game download URL for users to download the package -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Store the game files on Amazon EBS volumes mounted on Amazon EC2 instances within an Auto Scaling group Configure an FTP service on the EC2 instances Use an Application Load Balancer in front of the Auto Scaling grou",
      "B": "Publish the game download URL for users to download the package.",
      "C": "Store the game files on Amazon EFS volumes that are attached to Amazon EC2 instances within an Auto Scaling group Configure an FTP service on each of the EC2 instances Use an Application Load Balancer in front of the Auto Scaling group Publish the game download URL for users to download the package",
      "D": "Configure Amazon Route 53 and an Amazon S3 bucket for website hosting Upload the game files to the S3 bucket Use Amazon CloudFront for the website Publish the game download URL for users to download the package.",
      "E": "Configure Amazon Route 53 and an Amazon S3 bucket for website hosting Upload the game files to the S3 bucket Set Requester Pays for the S3 bucket Publish the game download URL for users to download the package -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "C"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "222",
    "question": "- (Exam Topic 2) A company is planning to migrate its on-premises data analysis application to AWS. The application is hosted across a fleet of servers and requires consistent system time. The company has established an AWS Direct Connect connection from its on-premises data center to AWS. The company has a high-precision stratum-0 atomic dock network appliance that acts as an NTP source for all on-premises servers. After the migration to AWS is complete, the clock on all Amazon EC2 instances that host the application must be synchronized with the on-premises atomic clock network appliance. Which solution will meet these requirements with the LEAST administrative overhead? A. Configure a DHCP options set with the on-premises NTP server address Assign the options set to the VP B. Ensure that NTP traffic is allowed between AWS and the on-premises networks. C. Create a custom AMI to use the Amazon Time Sync Service at 169.254.169.123 Use this AMI for the application Use AWS Config to audit the NTP configuration. D. Deploy a third-party time server from the AWS Marketplac E. Configure the time server to synchronize with the on-premises atomic clock network applianc F. Ensure that NTP traffic is allowed inbound in the network ACLs for the VPC that contains the third-party server. G. Create an IPsec VPN tunnel from the on-premises atomic clock network appliance to the VPC to encrypt the traffic over the Direct Connect connectio H. Configure the VPC route tables to direct NTP traffic over the tunnel. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Configure a DHCP options set with the on-premises NTP server address Assign the options set to the VP",
      "B": "Ensure that NTP traffic is allowed between AWS and the on-premises networks.",
      "C": "Create a custom AMI to use the Amazon Time Sync Service at 169.254.169.123 Use this AMI for the application Use AWS Config to audit the NTP configuration.",
      "D": "Deploy a third-party time server from the AWS Marketplac",
      "E": "Configure the time server to synchronize with the on-premises atomic clock network applianc",
      "F": "Ensure that NTP traffic is allowed inbound in the network ACLs for the VPC that contains the third-party server.",
      "G": "Create an IPsec VPN tunnel from the on-premises atomic clock network appliance to the VPC to encrypt the traffic over the Direct Connect connectio",
      "H": "Configure the VPC route tables to direct NTP traffic over the tunnel. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "225",
    "question": "- (Exam Topic 2) A video streaming company recently launched a mobile app for video sharing. The app uploads various files to an Amazon S3 bucket in the us-east-1 Region. The files range in size from 1 GB to 1 0 GB. Users who access the app from Australia have experienced uploads that take long periods of time Sometimes the files fail to completely upload for these users . A solutions architect must improve the app' performance for these uploads Which solutions will meet these requirements? (Select TWO.) A. Enable S3 Transfer Acceleration on the S3 bucket Configure the app to use the Transfer Acceleration endpoint for uploads B. Configure an S3 bucket in each Region to receive the upload C. Use S3 Cross-Region Replication to copy the files to the distribution S3 bucket. D. Set up Amazon Route 53 with latency-based routing to route the uploads to the nearest S3 bucket Region. E. Configure the app to break the video files into chunks Use a multipart upload to transfer files to Amazon S3. F. Modify the app to add random prefixes to the files before uploading -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Enable S3 Transfer Acceleration on the S3 bucket Configure the app to use the Transfer Acceleration endpoint for uploads",
      "B": "Configure an S3 bucket in each Region to receive the upload",
      "C": "Use S3 Cross-Region Replication to copy the files to the distribution S3 bucket.",
      "D": "Set up Amazon Route 53 with latency-based routing to route the uploads to the nearest S3 bucket Region.",
      "E": "Configure the app to break the video files into chunks Use a multipart upload to transfer files to Amazon S3.",
      "F": "Modify the app to add random prefixes to the files before uploading -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "A",
      "E"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "231",
    "question": "- (Exam Topic 2) A solutions architect has deployed a web application that serves users across two AWS Regions under a custom domain The application uses Amazon Route 53 latency-based routing The solutions architect has associated weighted record sets with a pair of web servers in separate Availability Zones for each Region The solutions architect runs a disaster recovery scenario When all the web servers in one Region are stopped Route 53 does not automatically redirect users to the other Region Which of the following are possible root causes of this issue? (Select TWO.) A. The weight for the Region where the web servers were stopped is higher than the weight for the other Region B. One of the web servers in the secondary Region did not pass its HTTP health check C. Latency resource record sets cannot be used in combination with weighted resource record sets D. The setting to evaluate target health is not turned on for the latency alias resource record set that is associated with the domain in the Region where the web servers were stopped E. An HTTP health check has not been set up for one or more of the weighted resource record sets associated with the stopped web servers -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "The weight for the Region where the web servers were stopped is higher than the weight for the other Region",
      "B": "One of the web servers in the secondary Region did not pass its HTTP health check",
      "C": "Latency resource record sets cannot be used in combination with weighted resource record sets",
      "D": "The setting to evaluate target health is not turned on for the latency alias resource record set that is associated with the domain in the Region where the web servers were stopped",
      "E": "An HTTP health check has not been set up for one or more of the weighted resource record sets associated with the stopped web servers -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D",
      "E"
    ],
    "select_n": 2,
    "explanation": ""
  },
  {
    "id": "232",
    "question": "- (Exam Topic 2) A company has a web application that securely uploads pictures and videos to an Amazon S3 bucket The company requires that only authenticated users are allowed to post content T.he application generates a presigned URL that is used to upload objects through a browser interface. Most users are reporting slow upload times for objects larger than 100 MB What can a solutions architect do to improve the performance of these uploads while ensuring only authenticated users are allowed to post content? A. Set up an Amazon API Gateway with an edge-optimized API endpoint that has a resource as an S3 service proxy Configure the PUT method for this resource to expose the S3 Putobject operation Secure the API Gateway using a cognito_user_pools authonzer Have the browser interface use API Gateway instead of the presigned URL to upload objects B. Set up an Amazon API Gateway with a regional API endpoint that has a resource as an S3 service proxyConfigure the PUT method for this resource to expose the S3 Putobject operation Secure the API Gateway using an AWS Lambda authonzer Have the browser interface use API Gateway instead of the presigned URL to upload objects C. Enable an S3 Transfer Acceleration endpoint on the S3 bucket Use the endpoint when generating the presigned URL Have the browser interface upload the objects to this URL using the S3 multipart upload API D. Configure an Amazon CloudFront distribution for the destination S3 bucket Enable PUT and POST methods for the CloudFront cache behavior Update the CloudFront origin to use an origin access identity (OAI) Give the OAl user s 3: Putobject permissions in the bucket policy Have the browser interface upload objects using the CloudFront distribution -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Set up an Amazon API Gateway with an edge-optimized API endpoint that has a resource as an S3 service proxy Configure the PUT method for this resource to expose the S3 Putobject operation Secure the API Gateway using a cognito_user_pools authonzer Have the browser interface use API Gateway instead of the presigned URL to upload objects",
      "B": "Set up an Amazon API Gateway with a regional API endpoint that has a resource as an S3 service proxyConfigure the PUT method for this resource to expose the S3 Putobject operation Secure the API Gateway using an AWS Lambda authonzer Have the browser interface use API Gateway instead of the presigned URL to upload objects",
      "C": "Enable an S3 Transfer Acceleration endpoint on the S3 bucket Use the endpoint when generating the presigned URL Have the browser interface upload the objects to this URL using the S3 multipart upload API",
      "D": "Configure an Amazon CloudFront distribution for the destination S3 bucket Enable PUT and POST methods for the CloudFront cache behavior Update the CloudFront origin to use an origin access identity (OAI) Give the OAl user s 3: Putobject permissions in the bucket policy Have the browser interface upload objects using the CloudFront distribution -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "D"
    ],
    "select_n": 1,
    "explanation": ""
  },
  {
    "id": "234",
    "question": "- (Exam Topic 2) A company is deploying a distributed in-memory database on a fleet of Amazon EC2 instances. The fleet consists of a primary node and eight worker nodes. The primary node is responsible for monitoring cluster health, accepting user requests, distributing user requests to worker nodes and sending an aggregate response back to a client. Worker nodes communicate with each other to replicate data partitions. The company requires the lowest possible networking latency to achieve maximum performance. Which solution will meet these requirements? A. Launch memory optimized EC2 instances in a partition placement group B. Launch compute optimized EC2 instances in a partition placement group C. Launch memory optimized EC2 instances in a cluster placement group D. Launch compute optimized EC2 instances in a spread placement group. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------",
    "options": {
      "A": "Launch memory optimized EC2 instances in a partition placement group",
      "B": "Launch compute optimized EC2 instances in a partition placement group",
      "C": "Launch memory optimized EC2 instances in a cluster placement group",
      "D": "Launch compute optimized EC2 instances in a spread placement group. -----------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    },
    "correct": [
      "B"
    ],
    "select_n": 1,
    "explanation": ""
  }
]

st.set_page_config(page_title="SAP-C02 Practice Quiz", layout="wide")

def init_state():
    if "order" not in st.session_state:
        st.session_state.order = list(range(len(QUESTIONS)))
    if "idx" not in st.session_state:
        st.session_state.idx = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "attempted" not in st.session_state:
        st.session_state.attempted = 0
    if "answered" not in st.session_state:
        st.session_state.answered = {}  # q_index -> set of chosen letters
    if "revealed" not in st.session_state:
        st.session_state.revealed = {}  # q_index -> bool

init_state()

st.title("SAP-C02 Practice Quiz")
st.caption("Offline practice with immediate feedback.")

# Sidebar controls
with st.sidebar:
    st.header("Controls")
    shuffle = st.checkbox("Shuffle questions", value=True)
    if st.button("Start/Reset"):
        st.session_state.order = list(range(len(QUESTIONS)))
        if shuffle:
            random.shuffle(st.session_state.order)
        st.session_state.idx = 0
        st.session_state.score = 0
        st.session_state.attempted = 0
        st.session_state.answered = {}
        st.session_state.revealed = {}
        st.success("Quiz reset!")

    st.markdown("---")
    st.metric("Score", f"{st.session_state.score} / {st.session_state.attempted}")

def current_q():
    if not QUESTIONS:
        return None, None
    if st.session_state.idx < 0:
        st.session_state.idx = 0
    if st.session_state.idx >= len(st.session_state.order):
        st.session_state.idx = len(st.session_state.order)-1
    qi = st.session_state.order[st.session_state.idx]
    return qi, QUESTIONS[qi]

qi, q = current_q()
if q is None:
    st.error("No questions available in dataset.")
    st.stop()

st.subheader(f"Question {st.session_state.idx+1} / {len(QUESTIONS)}  (ID {q['id']})")

wrap_width = 110
st.write("\n".join(textwrap.wrap(q['question'], width=wrap_width)))

# Options
letters = sorted(q['options'].keys())

# Capture user choices
user_key = f"choice_{qi}"
if q['select_n'] == 1:
    sel = st.radio("Select one:", options=letters, format_func=lambda k: f"{k}. {q['options'][k]}", key=user_key, index=None)
    user_sel = [sel] if sel else []
else:
    sel = st.pills("Select exactly {q['select_n']}:", options=letters, selection_mode="multi", key=user_key) if hasattr(st, "pills") else st.multiselect("Select exactly {q['select_n']}:", options=letters, format_func=lambda k: f"{k}. {q['options'][k]}")
    user_sel = list(sel)

cols = st.columns(4)
with cols[0]:
    if st.button("Check"):
        # Validate
        if len(user_sel) != q['select_n']:
            st.warning(f"This question expects {q['select_n']} selection(s); you chose {len(user_sel)}.")
        else:
            correct = sorted(q['correct'])
            st.session_state.attempted += 1
            if sorted(user_sel) == correct:
                st.session_state.score += 1
                st.session_state.revealed[qi] = True
                st.success("✅ Correct!")
            else:
                st.session_state.revealed[qi] = True
                st.error("❌ Incorrect.")
            st.session_state.answered[qi] = set(user_sel)

with cols[1]:
    if st.button("Reveal Answer"):
        st.session_state.revealed[qi] = True

with cols[2]:
    if st.button("Previous"):
        st.session_state.idx = max(0, st.session_state.idx - 1)

with cols[3]:
    if st.button("Next"):
        st.session_state.idx = min(len(st.session_state.order)-1, st.session_state.idx + 1)

# Feedback/Explanation
if st.session_state.revealed.get(qi):
    correct = " ".join(q['correct'])
    st.info(f"**Correct answer:** {correct}")
    if q.get('explanation'):
        with st.expander("Explanation"):
            st.write(q['explanation'])

# Footer progress
st.progress(0 if st.session_state.attempted==0 else min(1.0, st.session_state.score/max(1, st.session_state.attempted)))
st.caption("Tip: Use the sidebar to shuffle and reset.")