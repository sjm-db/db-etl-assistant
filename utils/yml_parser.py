from utils.data_types import Table, TableColumn
import yaml

def parse_yaml_to_table(yaml_content: str) -> Table:
    """
    Parses a YAML string and converts it into a Table object.
    
    Args:
        yaml_content (str): The YAML content as a string.
        
    Returns:
        Table: An instance of Table containing the parsed columns.
    """
    data = yaml.safe_load(yaml_content)
    table = Table()

    for col in data.get('columns', []):
        name = col.get('name')
        description = col.get('description', '')
        if name:
            table.add_column(name, description)

    return table