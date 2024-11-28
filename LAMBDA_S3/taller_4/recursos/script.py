import boto3
import io

# Cliente S3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Obtener el nombre del bucket y la clave del archivo desde el evento
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    print(f"Recibido evento para el archivo: {file_key} en el bucket: {bucket_name}")

    try:
        # Obtén el archivo en forma de stream
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        file_stream = response['Body']
        
        print(f"Archivo obtenido correctamente, comenzando a procesar en bloques.")

        # Procesa el archivo en bloques (por ejemplo, 1 KB a la vez)
        chunk_size = 1024  # 1 KB por fragmento
        while True:
            chunk = file_stream.read(chunk_size)
            if not chunk:
                break
            # Procesa cada fragmento aquí
            print(chunk.decode('utf-8'))  # Ejemplo de procesamiento: imprimir el contenido del archivo

        print("Procesamiento del archivo completado.")

    except Exception as e:
        # Si hay algún error, imprime el mensaje y vuelve a lanzarlo para asegurar que Lambda lo registre
        print(f"Error procesando el archivo: {e}")
        raise e
