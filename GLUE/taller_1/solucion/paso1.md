## Creamos una base de datos
### ¿Que es una base de datos en AWS GLUE?
Es una representación de una base de datos, pero prodriamos decir que en si no es una.  
Actúa como un contenedor lógico para organizar las tablas que contienen metadatos
```bash
aws_practice % aws glue create-database --database-input '{"Name": "taller1GlueDB", "Description": "Esta es la base de datos del taller 1 glue"}'
```
Revisemos si está creada la bd
```bash
aws glue get-databases
```
