## Taller 1: Crear una función Lambda para cargar un archivo a S3
Vamos a usar solo cli en todo el proceso
### Paso 1
Configurar un bucket de S3
Abre la consola de S3 y crea un nuevo bucket con un nombre único, por ejemplo, my-lambda-bucket-123.
Asegúrate de configurar las políticas adecuadas para que Lambda pueda escribir en este bucket.
### Paso 2
Crear un rol de IAM para Lambda
Abre la consola de IAM y crea un rol de IAM.
Selecciona el tipo de rol: "Lambda".
Agrega las políticas necesarias para que Lambda tenga acceso a S3. Puedes usar la política AmazonS3FullAccess para facilitar las pruebas, pero en un entorno real sería mejor usar una política más restrictiva.
Dale un nombre descriptivo al rol, como lambda-s3-access-role.
### Paso 3
Crear una función Lambda
Abre la consola de Lambda y crea una nueva función.
Elige "Autor desde cero" y configura el rol de ejecución usando el rol que creaste anteriormente (lambda-s3-access-role).
El código de la función Lambda será el siguiente:
``` python
import boto3

def lambda_handler(event, context):
    # Nombre del bucket de S3 y el nombre del archivo
    bucket_name = 'my-lambda-bucket-123'
    file_name = 'test-file.txt'
    file_content = 'This is a test file uploaded by Lambda.'

    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)

    return {
        'statusCode': 200,
        'body': f'File {file_name} uploaded to {bucket_name}'
    }
```
Este código carga un archivo de texto con contenido predefinido al bucket de S3.
4. Probar la función Lambda
En la consola de Lambda, selecciona "Test" y crea un evento de prueba (puedes dejarlo vacío para este ejercicio).
Ejecuta la función Lambda y verifica si el archivo test-file.txt aparece en el bucket de S3.
5. Verificar los permisos
Si Lambda no tiene permisos para acceder a S3, asegúrate de que el rol de IAM tiene la política correcta.
Cuando termines este ejercicio, me avisas y pasamos al siguiente.