import os
import logging
from databricks import sql
import data_types

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
    
    # Use Databricks API to write metadata
    with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       = os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:
        cursor = connection.cursor()
        try:
            # Write table description
            cursor.execute(f"COMMENT ON TABLE {table_fqdn} IS '{metadata.description}'")
            
            # Write column descriptions
            for column in metadata.columns:
                cursor.execute(f"ALTER TABLE {table_fqdn} ALTER COLUMN {column.name} COMMENT '{column.description}'")
        except Exception as e:
            logging.error(f"Failed to write metadata for {table_fqdn}: {e}")
    logging.info(f"Metadata for {table_fqdn} written successfully.")