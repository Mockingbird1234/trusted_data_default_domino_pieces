from pydantic import BaseModel, Field
from typing import Union
from datetime import date as dt_date, datetime as dt_datetime, time as dt_time


class InputModel(BaseModel):
    """
    ToStringPiece Input Model
    """
    input_value: Union[str, list, int, float, bool, dict, dt_date, dt_time, dt_datetime] = Field(
        description='要转换为字符串的输入值',
        json_schema_extra={
            "from_upstream": "always",
            "title": "输入值"
        }
    )


class OutputModel(BaseModel):
    """
    ToStringPiece Output Model
    """
    output_value: str = Field(
        description='转换为字符串的输入值'
    )
