from pydantic import BaseModel, Field
from enum import Enum
from typing import List


class ChecksTypes(str, Enum):
    contains_case_sensitive = 'contains_case_sensitive'
    contains_case_insensitive = 'contains_case_insensitive'
    length_greater_than = 'length_greater_than'
    length_greater_than_or_equal_to = 'length_greater_than_or_equal_to'
    length_less_than = 'length_less_than'
    length_less_than_or_equal_to = 'length_less_than_or_equal_to'
    length_equal_to = 'length_equal_to'
    regex_match = 'regex_match'


class LogicalOperators(str, Enum):
    and_operator = 'and'
    or_operator = 'or'


class OperationItem(BaseModel):
    operation: ChecksTypes = Field(
        description="""要执行的操作。
选项：`contains_case_sensitive`（区分大小写包含）、`contains_case_insensitive`（不区分大小写包含）、`length_greater_than`（长度大于）、`length_greater_than_or_equal_to`（长度大于等于）、`length_less_than`（长度小于）、`length_less_than_or_equal_to`（长度小于等于）、`length_equal_to`（长度等于）、`regex_match`（正则匹配）。
""",
        json_schema_extra={
            "from_upstream": "never"
        }
    )
    second_argument: str = Field(
        default='',
        description="""第二个参数的值。
如果选择 `contains_case_sensitive` 或 `contains_case_insensitive`，此参数将用作要搜索的字符串。
如果选择 `length_greater_than`、`length_greater_than_or_equal_to`、`length_less_than`、`length_less_than_or_equal_to` 或 `length_equal_to`，此参数将用作要比较的整数值。
如果选择 `regex_match`，此参数将用作与正则表达式模式匹配的字符串。
""",
    )
    next_logical_operator: LogicalOperators = Field(
        default=LogicalOperators.and_operator,
        description="与下一个操作结果一起使用的逻辑运算符",
    )


class InputModel(BaseModel):
    input_string: str = Field(
        description='输入字符串',
        json_schema_extra={
            "title": "输入字符串"
        }
    )
    operations: List[OperationItem] = Field(
        description='要执行的操作序列',
        json_schema_extra={
            "title": "操作序列"
        }
    )


class OutputModel(BaseModel):
    check_result: bool = Field(
        description='检查结果',
    )
