from pydantic import BaseModel, Field
from typing import Optional


class InputModel(BaseModel):
    data_path: str = Field(
        description='要分析的CSV文件路径',
        json_schema_extra={
            "from_upstream": "always",
            "title": "CSV文件路径"
        }
    )
    report_tile: Optional[str] = Field(
        description='报告的标题', 
        default='分析报告',
        json_schema_extra={
            "title": "报告标题"
        }
    )

class OutputModel(BaseModel):
    profile_file_path: str = Field(title='输出文件路径', description='输出文件的路径')
