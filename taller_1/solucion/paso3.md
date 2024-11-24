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
## Les quitamos los bloqueos de acceso pulico al bucket
```bash
aws s3api delete-bucket-policy --bucket taller1-bucket
```
## Le otorgamos una politica para acceso pulico a los objetos de nuestro bucket
```bash
aws s3api put-bucket-policy --bucket taller1-bucket --policy file://bucket-public-policy.json
```
https://taller1-bucket.s3.us-east-2.amazonaws.com/test-file.txt
```json
{
  "statusCode": 200,
  "body": "File test-file.txt uploaded to taller1-bucket"
}
```



