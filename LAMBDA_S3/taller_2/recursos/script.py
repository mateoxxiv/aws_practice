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