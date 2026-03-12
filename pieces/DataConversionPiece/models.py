from pydantic import BaseModel, Field
from enum import Enum


class DataFormatOption(str, Enum):
    csv = 'csv'
    json = 'json'


class InputModel(BaseModel):
    input_data: str = Field(
        description='要转换的输入数据。可以是文件路径或字符串数据',
        json_schema_extra={
            "title": "输入数据"
        }
    )
    input_data_format: DataFormatOption = Field(
        default=DataFormatOption.csv,
        description='要转换的输入数据格式',
        json_schema_extra={
            "title": "输入数据格式"
        }
    )
    output_data_format: DataFormatOption = Field(
        default=DataFormatOption.json,
        description='输出数据格式',
        json_schema_extra={
            "title": "输出数据格式"
        }
    )


class OutputModel(BaseModel):
    output_file_path: str = Field(
        description='转换后的文件路径'
    )
