import os
import logging
from utils import yaml_parser, metadata_writer, data_types

def process_metadata(path:str, catalog:str, schema:str):
    """
    Process all yml metadata files in the given path with format:
    ```tables:
        - name: foo
            description: Description of the table
            columns:
            - name: column1
                description: Description of column1
            - name: column2
                description: Description of column2
        - name: bar
            description: Description of another table
            columns:
            - name: columnA
                description: Description of columnA
        ```
    And write the metadata to the Databricks catalog.
    """

    if not os.path.exists(path):
        logging.error(f"Path {path} does not exist.")
        return
    
    tables = []

    for filename in os.listdir(path):
        if filename.endswith('.yml') or filename.endswith('.yaml'):
            logging.debug(f"Processing file: {filename}")
            file_path = os.path.join(path, filename)
            with open(file_path, 'r') as file:
                yaml_content = file.read()
                t = yaml_parser.parse_yaml_to_tables(yaml_content)
                if tables is None:
                    logging.error(f"Failed to parse YAML content from {file_path}.")
                    continue
                logging.debug(f"Parsed {len(tables)} tables from {file_path}.")
                tables = tables + t

    if not tables:
        logging.warning("No tables found in the provided YAML files.")
        return
    
    logging.info("tables: {}".format(tables))

    for table in tables:
        logging.debug(f"Processing table: {table}")
        if not isinstance(table, data_types.Table):
            logging.error("Parsed object is not an instance of Table.")
            continue
        
        try:
            metadata_writer.write_table_metadata(catalog, schema, table.name, table)
        except Exception as e:
            logging.error(f"Failed to write metadata for table {table.name}: {e}")
        else:
            logging.info(f"Metadata for table {table.name} written successfully.")
    logging.info("Metadata processing completed.")
