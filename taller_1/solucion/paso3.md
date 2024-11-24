## Creación de lambda
Creamos nuesta función lambda

```bash
aws lambda create-function \
  --function-name taller1-lambda \
  --runtime python3.8 \
  --role arn:aws:iam::575108931787:role/taller1-bucket-access-rol \
  --handler script.lambda_handler \
  --zip-file fileb://script.zip
```

## Resultado

```json
{
  "statusCode": 200,
  "body": "File test-file.txt uploaded to taller1-bucket"
}
```



