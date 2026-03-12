from pydantic import BaseModel, Field
from typing import Union
from datetime import date as dt_date, datetime as dt_datetime, time as dt_time
from enum import Enum


class IndexType(str, Enum):
    first = 'first'
    last = 'last'
    random = 'random'
    another = 'another'


class InputModel(BaseModel):
    """
    GetItemFromArrayPiece Input Model
    """
    input_array: list = Field(
        description='要获取项的输入数组',
        json_schema_extra={
            "from_upstream": "always",
            "title": "输入数组"
        }
    )
    index: IndexType = Field(
        default=IndexType.first,
        description='从输入数组获取项的索引',
        json_schema_extra={
            "title": "索引类型"
        }
    )
    another_index: int = Field(
        default=1,
        ge=1,
        description='从输入数组获取项的索引编号',
        json_schema_extra={
            "title": "索引编号"
        }
    )


class OutputModel(BaseModel):
    """
    GetItemFromArrayPiece Output Model
    """
    output_value: Union[str, list, int, float, bool, dict, dt_date, dt_time, dt_datetime] = Field(
        description='指定索引处输入数组的项'
    )
