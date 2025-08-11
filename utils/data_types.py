from dataclasses import dataclass, field
from typing import List

@dataclass
class TableColumn:
    name: str
    description: str

@dataclass
class Table:
    name: str
    description: str = ""
    columns: List[TableColumn] = field(default_factory=list)

    def add_column(self, name: str, description: str):
        self.columns.append(TableColumn(name=name, description=description))

    def __str__(self):
        column_strs = [f"{col.name}: {col.description}" for col in self.columns]
        return f"Table: {self.name}\nDescription: {self.description}\nColumns:\n" + "\n".join(column_strs)