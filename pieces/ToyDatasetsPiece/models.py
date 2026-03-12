from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional

class DatasetName(str, Enum):
    iris = "iris"
    diabetes = "diabetes"
    digits = "digits"
    wine = "wine"
    breast_cancer = "breast_cancer"
    linnerrud = "linnerrud"

class InputModel(BaseModel):
    dataset: DatasetName = Field(
        default='iris', 
        description='数据集名称',
        json_schema_extra={
            "title": "数据集名称"
        }
    )

class OutputModel(BaseModel):
    file_path: Optional[str] = Field(default=None, title='文件路径')
