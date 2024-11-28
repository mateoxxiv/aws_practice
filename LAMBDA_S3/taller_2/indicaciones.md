## Taller 2: Activar una función Lambda con un evento de S3
**Objetivo**
Configurar un bucket de S3 para que active una función Lambda automáticamente cada vez que se suba un archivo. La función Lambda procesará los metadatos del archivo cargado.

### Paso 1
Configurar un bucket de S3
Ve a la consola de S3 y selecciona el bucket que creaste en el ejercicio anterior (por ejemplo, my-lambda-bucket-123).
En las configuraciones del bucket, ve a la sección "Propiedades" y habilita el registro de eventos.
Configura un evento que se active cuando se suba un archivo (PUT) en el bucket. Selecciona como destino una función Lambda (crearemos esta función en el siguiente paso).
### Paso 2
Crear una función Lambda
Abre la consola de Lambda y crea una nueva función.

Selecciona "Autor desde cero" y usa el rol que creaste en el ejercicio anterior (lambda-s3-access-role).

Usa el siguiente código para la función Lambda:

```python
import json

def lambda_handler(event, context):
    # Extracción de detalles del evento
    records = event.get('Records', [])
    for record in records:
        bucket_name = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']
        print(f'Archivo subido: {file_key} en el bucket: {bucket_name}')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Evento procesado correctamente.')
    }
```
### Paso 3
Asociar el evento de S3 con Lambda
Vuelve a la consola de S3 y termina de configurar el evento creado en el paso 1.
Selecciona la función Lambda creada como el destino del evento.
### Paso 4
Probar el flujo
Sube un archivo al bucket de S3, por ejemplo, un archivo de texto llamado example.txt.
Ve a los logs de CloudWatch para verificar que la función Lambda se activó y procesó el evento.
Asegúrate de que la función imprimió correctamente el nombre del archivo y el bucket.