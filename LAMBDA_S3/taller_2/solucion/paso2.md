## Agregarle oilitica al bucket
Esto em permitira enviarle eventos a mi función lambda
```bash
aws s3api put-bucket-notification-configuration --bucket taller1-bucket --notification-configuration file://notification.json
```