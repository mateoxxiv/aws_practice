## Taller 3: Procesar archivos cargados en S3 con Lambda
**Objetivo**
Crear una función Lambda que procese un archivo cargado en un bucket de S3. Por ejemplo, la función puede leer un archivo de texto, contar las líneas o palabras, y luego almacenar el resultado en otro archivo dentro del mismo bucket.
### Paso 1: Configurar un bucket
Si ya tienes un bucket desde los ejercicios anteriores, puedes usarlo. Si no, crea uno nuevo y asegúrate de tener configurada la política de eventos para activar la función Lambda cuando un archivo sea subido al bucket.

Abre la consola de S3 y crea un bucket (si no tienes uno).
Habilita el evento para la carga de archivos (evento PUT) y selecciona como destino la función Lambda que vamos a crear.
### Paso 2: Creación de lambda:
1. Abre la consola de Lambda y crea una nueva función.
2. Elige "Autor desde cero", asigna el rol lambda-s3-access-role (si aún no lo has hecho) para que Lambda pueda acceder a S3.
3. Usa el siguiente código para la función Lambda:
```python
import json
import boto3

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    
    # Extraer detalles del archivo subido desde el evento
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # Descargar el archivo desde S3
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read().decode('utf-8')

    # Contar las palabras del archivo
    word_count = len(file_content.split())
    line_count = len(file_content.splitlines())

    # Crear un nuevo archivo con el resultado
    result_key = f"processed/{file_key.replace('.txt', '-result.txt')}"
    result_content = f"Word count: {word_count}\nLine count: {line_count}"

    # Subir el archivo procesado al bucket
    s3_client.put_object(Body=result_content, Bucket=bucket_name, Key=result_key)

    return {
        'statusCode': 200,
        'body': json.dumps(f"File processed. Results saved to {result_key}")
    }
```
### Paso 3
En la consola de S3, crea un evento para que la función Lambda se active cuando se cargue un archivo en el bucket.
Asegúrate de que el evento dispare la función Lambda que acabas de crear.

### Paso 4
Sube un archivo de texto al bucket. Por ejemplo, crea un archivo test.txt con algunas líneas y palabras.
Ve a la consola de S3 y verifica que un nuevo archivo con el sufijo -result.txt se haya generado en la carpeta processed/.
Abre el archivo generado y verifica que contenga el número de palabras y líneas procesado por la función Lambda.

### Paso 5
Si no se ejecuta correctamente, asegúrate de que el rol de IAM tenga permisos suficientes para que Lambda pueda leer y escribir archivos en S3.