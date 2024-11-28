## Le damos permisos a nuestros servicios

### Le decimos a nuestra lambda que acepte eventos de nuestro bucket
```bash
aws lambda add-permission \
  --function-name taller4-lambda \
  --principal s3.amazonaws.com \
  --statement-id c1a9811b-bcc8-4d56-a0de-977887ccd923 \
  --action "lambda:InvokeFunction" \
  --source-arn arn:aws:s3:::taller4-bucket
```

### Le definimos el evento a nuestro bucket
```bash
aws s3api put-bucket-notification-configuration --bucket taller4-bucket --notification-configuration file://notification-config.json
```