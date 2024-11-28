## Deifnimos una politica para acceder al bucket
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::taller1-bucket/*"
        }
    ]
}
```
**Creamos la politica:** arn:aws:iam::575108931787:policy/taller1-bucket-access-policy
```bash
aws iam create-policy --policy-name taller1-bucket-access-policy --policy-document file://taller1-bucket-access-policy.json

```
**Creamos un rol:**
```bash
aws iam create-role --role-name taller1-bucket-access-rol --assume-role-policy-document file://trust-policy.json
```
**Asignamos politica de servicio**
```bash
aws iam attach-role-policy --role-name taller1-bucket-access-rol --policy-arn arn:aws:iam::575108931787:policy/taller1-bucket-access-policy
```