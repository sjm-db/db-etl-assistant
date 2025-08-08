from dataclasses import dataclass, field
from typing import List

@dataclass
class TableColumn:
    name: str
    description: str

@dataclass
class Table:
    columns: List[TableColumn] = field(default_factory=list)

    def add_column(self, name: str, description: str):
        self.columns.append(TableColumn(name=name, description=description))

    def __str__(self):
        return "\n".join(f"{col.name}: {col.description}" for col in self.columns)
    