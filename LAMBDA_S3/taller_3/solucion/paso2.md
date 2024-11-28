## creamos función lambda
´´´bash
aws lambda create-function \
  --function-name taller3-lambda \
  --runtime python3.8 \
  --role arn:aws:iam::575108931787:role/lambda-general-politics \
  --handler script.lambda_handler \
  --zip-file fileb://script.zip
```
