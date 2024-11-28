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
        'body': json.dumps(f"File processed. Results saved to {result_key}"),
        'data': event
    }