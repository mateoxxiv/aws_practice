## Ejercicio 4: Procesamiento de archivos grandes en S3 con Lambda

**Objetivo:**  
Aprender a manejar archivos grandes almacenados en S3, asegurando que la función Lambda no se quede sin memoria o falle por exceder el límite de tamaño.

**Descripción:**  
Cuando trabajas con archivos grandes, puedes encontrar problemas relacionados con los límites de memoria y tiempo de ejecución en Lambda. Por eso, es importante procesar esos archivos de manera eficiente.

Para manejar archivos grandes en S3 con Lambda, puedes hacer lo siguiente:

1. Utilizar Streams en lugar de cargar el archivo completo en memoria.
Al usar streams, puedes leer el archivo de S3 de manera incremental, procesarlo en fragmentos pequeños y evitar consumir toda la memoria de Lambda.

2. Dividir el archivo en bloques pequeños.
Si el archivo es muy grande (por ejemplo, más de 6 MB), puedes dividirlo en partes más pequeñas y procesarlas por separado. Esto es especialmente útil cuando trabajas con archivos como CSV o JSON.

## Paso 1 -> Crear la función lambda:
```python
import boto3
import io

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    try:
        # Obtén el archivo en forma de stream
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        file_stream = response['Body']

        # Procesa el archivo en bloques (por ejemplo, 1 KB a la vez)
        chunk_size = 1024  # 1 KB por fragmento
        while True:
            chunk = file_stream.read(chunk_size)
            if not chunk:
                break
            # Procesa cada fragmento aquí
            print(chunk.decode('utf-8'))  # Ejemplo de procesamiento

    except Exception as e:
        print(f"Error procesando el archivo: {e}")
        raise e

```
## Paso 2 -> Configura un bucket S3:
- Asegúrate de que tienes un bucket S3 con archivos grandes (por ejemplo, CSV o JSON) cargados en él.
- Asegúrate de que tu función Lambda esté configurada para ser invocada por un evento de S3, de modo que cada vez que subas un archivo al bucket, se active Lambda.
## Paso 3 -> Probar función lambda:
- Sube un archivo grande al bucket S3 y observa cómo la función Lambda lee el archivo en bloques pequeños y lo procesa sin sobrecargar la memoria de la función.
## Monitoremosm el rendimiento de lambda
- Si deseas mejorar aún más el rendimiento, puedes considerar aumentar la memoria de la función Lambda para asegurar que pueda manejar grandes volúmenes de datos.