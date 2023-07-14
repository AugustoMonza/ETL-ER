# README: Modelado de Datos y Proceso de Carga

Este README proporciona una descripción detallada del modelado de datos y el proceso de carga de datos en las tablas utilizando Python, Docker, DBeaver, Pandas, SQLAlchemy y un entorno virtual.

## Requisitos Previos

Asegúrate de tener instalado lo siguiente:

- Entorno Virtual: Ejecuta `pip install virtualenv`

## Configuración del Entorno Virtual

1. Crea un nuevo directorio para tu proyecto y navega hasta él.
2. Crea un entorno virtual ejecutando el siguiente comando:
3. Activa el entorno virtual:
- En Windows:
  ```
  venv\Scripts\activate
  ```
- En macOS y Linux:
  ```
  source venv/bin/activate
  ```

## Instalación de Dependencias

Instala las dependencias necesarias ejecutando el siguiente comando:
3. Activa el entorno virtual:
- En Windows:
  ```
  venv\Scripts\activate
  ```
- En macOS y Linux:
  ```
  source venv/bin/activate
  ```

## Instalación de Dependencias

Instala las dependencias necesarias ejecutando el siguiente comando: `pip install -r requirements.txt`

El archivo `requirements.txt` contiene una lista de las dependencias y sus versiones específicas necesarias para el proyecto.

## Modelado de Datos

| Tabla               | Columnas                                                                       |
|---------------------|--------------------------------------------------------------------------------|
| dim_tienda          | id_tienda (integer, primary key)                                               |
|                     | tipo_tienda (string, not nullable)                                             |
| dim_barrio          | id_barrio (integer, primary key)                                               |
|                     | nombre_barrio (string, not nullable)                                           |
| dim_codigo_tienda   | id_codigo_tienda (integer, primary key)                                        |
|                     | codigo_tienda (integer, not nullable)                                           |
|                     | id_barrio (integer, foreign key to dim_barrio.id_barrio, not nullable)         |
|                     | id_tienda (integer, foreign key to dim_tienda.id_tienda)                       |
| dim_coordenada      | id (integer, primary key)                                                      |
|                     | latitud_tienda (float, not nullable)                                           |
|                     | longitud_tienda (float, not nullable)                                          |
|                     | id_codigo_tienda (integer, foreign key to dim_codigo_tienda.id_codigo_tienda)   |
| dim_documentos      | id_documento (integer, primary key)                                            |
|                     | num_documento_cliente (big integer, not nullable)                              |
| dim_tipo_documento  | tipo_documento_cliente (integer, primary key)                                  |
|                     | descripcion (string, not nullable)                                              |
| fact_table          | id_table (integer, primary key)                                                 |
|                     | fecha_compra (date, not nullable)                                               |
|                     | id_codigo_tienda (integer, foreign key to dim_codigo_tienda.id_codigo_tienda)   |
|                     | id_documento (integer, foreign key to dim_documentos.id_documento)             |
|                     | tipo_documento_cliente (integer, foreign key to dim_tipo_documento.tipo_documento_cliente) |


Diagrama Entidad Relación:

![App Screenshot](https://github.com/AugustoMonza/ETL-ER/blob/master/img/Diagrama%20ER.jpeg?raw=true)

El porqué de este modelo:

Se decidió utilizar la metodología Snowflake debido a que nos permite mayor consistencia y precisión en la normalización de los datos y un ahorro de mantenimientos a futuro lo que evita la duplicación de datos mejorando la eficiencia del almacenamiento. 
