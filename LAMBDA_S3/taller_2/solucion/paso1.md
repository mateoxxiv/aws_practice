## Creamos nuestra función lambda

```bash
aws lambda create-function \
  --function-name taller2-lambda \
  --runtime python3.8 \
  --role arn:aws:iam::575108931787:role/lambda-general-politics \
  --handler script.lambda_handler \
  --zip-file fileb://script.zip
```

## Le indicamos a nuestra función que la pueden llamar evetos de s3
```bash
aws lambda add-permission \
  --function-name taller2-lambda \
  --principal s3.amazonaws.com \
  --statement-id 65d26125-99ed-4ae9-b0bd-15e24b5e96bb \
  --action "lambda:InvokeFunction" \
  --source-arn arn:aws:s3:::taller1-bucket

```