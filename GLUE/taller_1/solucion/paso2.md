## Creamos una tabla en nuestra base de datos
### ¿Que es una tabla en una base de datos en AWS GLUE?
Una tabla en Glue describe los datos de una fuente específica, como un archivo o un conjunto de archivos en S3.  
Podriamos decir que es una representación de una tabla en una tabla relacional, en donde vamos a definir nuestro esquema.

### Creación de bucket de S3
```bash
aws s3 mb s3://glue-taller1
```
### Cargar datos a nuestro bucket de S3
```bash
aws s3 cp mock-data.csv s3://glue-taller1/dummie_data.csv
```
### Nuestros datos tienen una estructura con las siguientes tablas
1. id : string
2. first_name : string
3. last_name : string
4. email : string
5. gender : string
6. ip_address : string
### Creamos nuestra tabla en nuestra base de datos
```bash
aws glue create-table --database-name taller1GlueDB --table-input '{
  "Name": "my-first-table",
  "StorageDescriptor": {
    "Columns": [
      {"Name": "id", "Type": "string"},
      {"Name": "first_name", "Type": "string"},
      {"Name": "last_name", "Type": "string"},
      {"Name": "email", "Type": "string"},
      {"Name": "gender", "Type": "string"},
      {"Name": "ip_address", "Type": "string"},
    ],
    "Location": "s3://glue-taller1/dummie_data.csv",
    "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
    "OutputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
    "SerdeInfo": {
      "Name": "csv_serde",
      "SerializationLibrary": "org.apache.hadoop.hive.serde2.OpenCSVSerde"
    }
  }
}'
```
### Revisamos si efectivamente se creo nuestra tabla
