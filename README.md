# API Gateway Workshop / Simple Web App with GET and POST

## Workshop Links:

* Hands-On AWS Lab Environment: https://dashboard.eventengine.run/login

* Event Hash: ``

* Tutorial / Documentation: https://aws.amazon.com/getting-started/hands-on/build-web-app-s3-lambda-api-gateway-dynamodb/

* My Custom Code Samples: https://github.com/msiposm/api-gateway-workshop


## Overview:

* Module 1: Create and host simple website frontend (AWS Amplify)  -  5 min

    1. Create and host website
    2. Test website URL

* Module 2: Build backend logic with serverless function (AWS Lambda)  -  10 min

    1. Create Lambda function
    2. Test Lambda function

* Module 3: Build API Gateway as an interface for the backend (Amazon API Gateway)  - 10 min

    1. Create new REST API
    2. Create new resource ("/") and POST method, add Lambda integration
    3. Enable CORS and deploy stage
    4. Test/Validate API

* Module 4: Persist data with a database (Amazon DynamoDB)  -  15 min

    1. Create DynamoDB table
    2. Give Lambda permission to DynamoDB (AWS IAM)
    3. Modify Lambda function
    4. Test Lambda function (check DynamoDB to see the new record)

* Module 5: Enhance website with dynamic POST & GET via API Gateway calls -  15 min

    1. Create a new Lambda function that gets table items
    2. Create and deploy a 'GET' API Gateway method that integrates with the new Lambda
        - You will use the API Gateway URL in the next step, copy it down
    3. Update website code (get new index.html, replace API endpoint with your API URL, compress to .zip)
    4. Use Amplify to deploy new website version
    5. Test Website!
   
**Architecture Diagram:**

![Workshop Architecture Diagram](https://d1.awsstatic.com/webteam/getting_started/GSRC%202020%20updates/full-stack%20amplify%20console%20arch%20diagram%20module%205.8d82fc2a7b47b307dfcefb6fa5f364e8c24426bc.png "Workshop Architecture Diagram")
