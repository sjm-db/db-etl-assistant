import logging
from pyspark.sql import SparkSession	
from utils import data_types

def write_table_metadata(catalog: str, schema: str, table: str, metadata: data_types.Table):
    """
    Write metadata for a table to the Databricks catalog.

    :param catalog: The name of the catalog.
    :param schema: The name of the schema.
    :param table: The name of the table.
    :param metadata: An instance of data_types.Table containing the metadata.
    """
    # Construct the full table path
    table_fqdn = f"{catalog}.{schema}.{table}"
    
    try:
        spark = SparkSession.builder.getOrCreate()
        # Write table description
        spark.sql(f"COMMENT ON TABLE {table_fqdn} IS '{metadata.description}'")
        
        # Write column descriptions
        for column in metadata.columns:
            spark.sql(f"ALTER TABLE {table_fqdn} ALTER COLUMN {column.name} COMMENT '{column.description}'")
    except Exception as e:
        logging.error(f"Failed to write metadata for {table_fqdn}: {e}")
    else:
        logging.info(f"Metadata for {table_fqdn} written successfully.")