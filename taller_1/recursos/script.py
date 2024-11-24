import boto3

def lambda_handler(event, context):
    # Nombre del bucket de S3 y el nombre del archivo
    bucket_name = 'taller1-bucket'
    file_name = 'test-file.txt'
    file_content = 'This is a test file uploaded by Lambda.'

    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)

    return {
        'statusCode': 200,
        'body': f'File {file_name} uploaded to {bucket_name}'
    }