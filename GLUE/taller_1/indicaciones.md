¡Perfecto! Vamos a empezar desde el ejercicio 1 y lo haremos todo utilizando la **AWS CLI**.

### **Ejercicio 1: Introducción a AWS Glue con CLI**

**Objetivo:** Familiarizarte con la consola de AWS Glue a través de la CLI.

#### Paso 1: Configurar tu entorno de AWS CLI

1. **Instalar AWS CLI (si no lo tienes instalado):**

   Si aún no has instalado la CLI, puedes hacerlo ejecutando el siguiente comando:

   ```bash
   pip install awscli
   ```

2. **Configurar las credenciales de AWS:**

   Usa el siguiente comando para configurar tus credenciales de AWS:

   ```bash
   aws configure
   ```

   Aquí tendrás que ingresar tu **Access Key ID**, **Secret Access Key**, **region** y **output format**. Si no tienes las claves, puedes crearlas en la consola de AWS IAM.

#### Paso 2: Crear una base de datos en AWS Glue

Usaremos el siguiente comando para crear una base de datos en Glue:

```bash
aws glue create-database --database-input '{"Name": "mi_base_de_datos"}'
```

Este comando crea una base de datos llamada `mi_base_de_datos`. Puedes cambiar el nombre por el que prefieras.

#### Paso 3: Verificar la base de datos creada

Para verificar que la base de datos se creó correctamente, puedes usar este comando:

```bash
aws glue get-databases
```

Esto debería devolver una lista de todas las bases de datos en Glue, y deberías ver la que acabas de crear.

#### Paso 4: Crear una tabla en el Glue Data Catalog

Ahora vamos a crear una tabla en el Glue Data Catalog para almacenar información de un archivo CSV en S3. Primero, debes cargar un archivo CSV en un bucket de S3. Aquí un ejemplo de cómo cargar un archivo:

```bash
aws s3 cp mi_archivo.csv s3://mi-bucket/mi_archivo.csv
```

Luego, puedes crear la tabla en Glue con el siguiente comando (modifica las rutas y tipos según tu archivo):

```bash
aws glue create-table --database-name mi_base_de_datos --table-input '{
  "Name": "mi_tabla",
  "StorageDescriptor": {
    "Columns": [
      {"Name": "columna1", "Type": "string"},
      {"Name": "columna2", "Type": "int"}
    ],
    "Location": "s3://mi-bucket/mi_archivo.csv",
    "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
    "OutputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
    "SerdeInfo": {
      "Name": "csv_serde",
      "SerializationLibrary": "org.apache.hadoop.hive.serde2.OpenCSVSerde"
    }
  }
}'
```

Este comando crea una tabla llamada `mi_tabla` en el catálogo de Glue que hace referencia a un archivo CSV almacenado en S3.

#### Paso 5: Verificar la tabla creada

Para asegurarte de que la tabla fue creada correctamente, puedes listar las tablas de la base de datos con el siguiente comando:

```bash
aws glue get-tables --database-name mi_base_de_datos
```

Esto debería devolver la lista de tablas en la base de datos, y deberías ver `mi_tabla`.

---

### Resumen de lo que hicimos:
1. Creamos una base de datos en AWS Glue.
2. Verificamos que la base de datos se haya creado correctamente.
3. Creamos una tabla en el Glue Data Catalog que hace referencia a un archivo CSV en S3.
4. Verificamos la creación de la tabla.

Este ejercicio te ayuda a familiarizarte con las operaciones básicas de Glue usando la CLI. Cuando termines, podemos pasar al siguiente ejercicio. ¿Listo para continuar?¡Perfecto! Vamos a empezar desde el ejercicio 1 y lo haremos todo utilizando la **AWS CLI**.

### **Ejercicio 1: Introducción a AWS Glue con CLI**

**Objetivo:** Familiarizarte con la consola de AWS Glue a través de la CLI.

#### Paso 1: Configurar tu entorno de AWS CLI

1. **Instalar AWS CLI (si no lo tienes instalado):**

   Si aún no has instalado la CLI, puedes hacerlo ejecutando el siguiente comando:

   ```bash
   pip install awscli
   ```

2. **Configurar las credenciales de AWS:**

   Usa el siguiente comando para configurar tus credenciales de AWS:

   ```bash
   aws configure
   ```

   Aquí tendrás que ingresar tu **Access Key ID**, **Secret Access Key**, **region** y **output format**. Si no tienes las claves, puedes crearlas en la consola de AWS IAM.

#### Paso 2: Crear una base de datos en AWS Glue

Usaremos el siguiente comando para crear una base de datos en Glue:

```bash
aws glue create-database --database-input '{"Name": "mi_base_de_datos"}'
```

Este comando crea una base de datos llamada `mi_base_de_datos`. Puedes cambiar el nombre por el que prefieras.

#### Paso 3: Verificar la base de datos creada

Para verificar que la base de datos se creó correctamente, puedes usar este comando:

```bash
aws glue get-databases
```

Esto debería devolver una lista de todas las bases de datos en Glue, y deberías ver la que acabas de crear.

#### Paso 4: Crear una tabla en el Glue Data Catalog

Ahora vamos a crear una tabla en el Glue Data Catalog para almacenar información de un archivo CSV en S3. Primero, debes cargar un archivo CSV en un bucket de S3. Aquí un ejemplo de cómo cargar un archivo:

```bash
aws s3 cp mi_archivo.csv s3://mi-bucket/mi_archivo.csv
```

Luego, puedes crear la tabla en Glue con el siguiente comando (modifica las rutas y tipos según tu archivo):

```bash
aws glue create-table --database-name mi_base_de_datos --table-input '{
  "Name": "mi_tabla",
  "StorageDescriptor": {
    "Columns": [
      {"Name": "columna1", "Type": "string"},
      {"Name": "columna2", "Type": "int"}
    ],
    "Location": "s3://mi-bucket/mi_archivo.csv",
    "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
    "OutputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
    "SerdeInfo": {
      "Name": "csv_serde",
      "SerializationLibrary": "org.apache.hadoop.hive.serde2.OpenCSVSerde"
    }
  }
}'
```

Este comando crea una tabla llamada `mi_tabla` en el catálogo de Glue que hace referencia a un archivo CSV almacenado en S3.

#### Paso 5: Verificar la tabla creada

Para asegurarte de que la tabla fue creada correctamente, puedes listar las tablas de la base de datos con el siguiente comando:

```bash
aws glue get-tables --database-name mi_base_de_datos
```

Esto debería devolver la lista de tablas en la base de datos, y deberías ver `mi_tabla`.

---

### Resumen de lo que hicimos:
1. Creamos una base de datos en AWS Glue.
2. Verificamos que la base de datos se haya creado correctamente.
3. Creamos una tabla en el Glue Data Catalog que hace referencia a un archivo CSV en S3.
4. Verificamos la creación de la tabla.

Este ejercicio te ayuda a familiarizarte con las operaciones básicas de Glue usando la CLI. Cuando termines, podemos pasar al siguiente ejercicio. ¿Listo para continuar?