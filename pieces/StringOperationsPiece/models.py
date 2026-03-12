from pydantic import BaseModel, Field
from enum import Enum
from typing import List


class OperationsTypes(str, Enum):
    concatenate = 'concatenate'
    lower_case = 'lower_case'
    upper_case = 'upper_case'
    split_by = 'split_by'
    replace_by = 'replace_by'
    strip_spaces = 'strip_spaces'


class OperationItem(BaseModel):
    operation: OperationsTypes = Field(
        description='要执行的操作。选项：`concatenate`（连接）、`lower_case`（小写）、`upper_case`（大写）、`split_by`（分割）、`replace_by`（替换）',
        json_schema_extra={
            "from_upstream": "never"
        }
    )
    second_argument: str = Field(
        default='',
        description='第二个参数的值',
    )
    auxiliary_argument: str = Field(
        default='',
        description="""用于 `split_by` 和 `replace_by` 操作的辅助参数。
如果选择 `split_by`，此参数将用作分割数组的索引。
如果选择 `replace_by`，此参数将用作要替换的字符串。
""",
    )


class InputModel(BaseModel):
    first_argument: str = Field(
        description='第一个参数的值',
        json_schema_extra={
            "title": "第一个参数"
        }
    )
    operations: List[OperationItem] = Field(
        description='要执行的操作序列',
        json_schema_extra={
            "title": "操作序列"
        }
    )


class OutputModel(BaseModel):
    output_string: str = Field(
        description='输出字符串',
    )
