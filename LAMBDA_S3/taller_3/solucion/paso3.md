## Indicamos que lambda va a ser llamado por nuestro bucket

```bash
aws lambda add-permission \
  --function-name taller3-lambda \
  --principal s3.amazonaws.com \
  --statement-id b1e82a4c-5ae6-4dfc-9265-78b4d96c3c90 \
  --action "lambda:InvokeFunction" \
  --source-arn arn:aws:s3:::taller3-bucket
```

## Le agreamos el evento al bucket
```bash
aws s3api put-bucket-notification-configuration --bucket taller3-bucket --notification-configuration file://pilitica-s3lambda.json
```