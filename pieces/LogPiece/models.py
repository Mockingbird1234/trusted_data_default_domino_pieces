from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional
from datetime import datetime, time, date


class InputEnum(str, Enum):
    option1 = "option1"
    option2 = "option2"
    option3 = "option3"


class InputModel(BaseModel):
    """
    LogPiece Input Model
    """
    input_str: str = Field(
        default="default value",
        description='要记录的输入字符串',
        json_schema_extra={
            "title": "输入字符串"
        }
    )
    input_int: int = Field(
        default=10,
        description='要记录的输入整数',
        json_schema_extra={
            "title": "输入整数"
        }
    )
    input_float: float = Field(
        default=10.5,
        description='要记录的输入浮点数',
        json_schema_extra={
            "title": "输入浮点数"
        }
    )
    input_bool: bool = Field(
        default=False,
        description='要记录的输入布尔值',
        json_schema_extra={
            "title": "输入布尔值"
        }
    )
    input_enum: InputEnum = Field(
        default=InputEnum.option1,
        description='要记录的输入枚举值',
        json_schema_extra={
            "title": "输入枚举值"
        }
    )
    input_date: date = Field(
        default="2023-01-01",
        description='要记录的输入日期',
        json_schema_extra={
            "title": "输入日期"
        }
    )
    input_time: time = Field(
        default="16:20:00",
        description='要记录的输入时间',
        json_schema_extra={
            "title": "输入时间"
        }
    )
    input_datetime: datetime = Field(
        default="2023-01-01T16:20:00",
        description='要记录的输入日期时间',
        json_schema_extra={
            "title": "输入日期时间"
        }
    )
    input_array: List[str] = Field(
        default=["default_1", "default_2", "default_3"],
        description='要记录的输入数组',
        json_schema_extra={
            "title": "输入数组"
        }
    )
    input_code: str = Field(
        default="print('Hello world!')",
        description='要记录的输入代码',
        json_schema_extra={
            'widget': "codeeditor",
            "title": "输入代码"
        }
    )


class OutputModel(BaseModel):
    """
    LogPiece Output Model
    """
    output_log: str = Field(
        description='所有记录的值'
    )
    output_str: Optional[str] = Field(
        description='记录的输出字符串'
    )
    output_int: Optional[int] = Field(
        description='记录的输出整数'
    )
    output_float: Optional[float] = Field(
        description='记录的输出浮点数'
    )
    output_bool: Optional[bool] = Field(
        description='记录的输出布尔值'
    )
    output_enum: Optional[str] = Field(
        description='记录的输出枚举值'
    )
    output_date: date = Field(
        description='记录的输出日期'
    )
    output_time: time = Field(
        description='记录的输出时间',
    )
    output_datetime: datetime = Field(
        description='记录的输出日期时间'
    )
    output_array: List[str] = Field(
        description='记录的输出数组'
    )
    output_code: str = Field(
        description='记录的输出代码',
        json_schema_extra={
            'widget': "codeeditor",
        }
    )
