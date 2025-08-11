from data_types import Table
from typing import List
import logging
import yaml

def parse_yaml_to_tables(yaml_content: str) -> List[Table]:
    """
    Parses a YAML string and converts it into a list of Table objecta.
    
    Args:
        yaml_content (str): The YAML content as a string. Formatted as:
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
    Returns:
        Table: An instance of Table containing the parsed columns.
    """
    data = yaml.safe_load(yaml_content)
    if not isinstance(data, dict) or 'tables' not in data:
        logging.error("Invalid YAML format: 'tables' key not found.")
        return None
    
    tables = data['tables']
    if not isinstance(tables, list):
        logging.error("Invalid YAML format: 'tables' should be a list.")
        return None
    
    out = []
    for table_data in tables:
        try:
            table = process_table(table_data)
        except Exception as e:
            logging.error(f"Error processing table: {e}")
            continue
        out.append(table)
    
    return out
    
def process_table(table_dict: dict) -> Table:
    """
    Processes a single table dictionary and converts it into a Table object.
    Args:
        table_dict (dict): A dictionary representing a table with 'name', 'description', and 'columns'.
    Returns:
        Table: An instance of Table containing the parsed columns.
    """
    if not isinstance(table_dict, dict):
        raise ValueError("Table data must be a dictionary.")
    name = table_dict.get('name')
    if not name:
        raise ValueError("Table must have a 'name' field.")
    description = table_dict.get('description', "")
    columns_data = table_dict.get('columns', [])
    if not isinstance(columns_data, list):
        raise ValueError("Columns must be a list.")
    table = Table(name=name, description=description)
    for column_data in columns_data:
        if not isinstance(column_data, dict):
            raise ValueError("Each column must be a dictionary.")
        column_name = column_data.get('name')
        if not column_name:
            raise ValueError("Column must have a 'name' field.")
        column_description = column_data.get('description', "")
        table.add_column(name=column_name, description=column_description)
    logging.info(f"Processed table: {table.name}")
    
    return table
