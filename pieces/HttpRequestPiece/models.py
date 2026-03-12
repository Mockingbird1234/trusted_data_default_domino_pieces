from pydantic import BaseModel, Field
from enum import Enum


class MethodTypes(str, Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class InputModel(BaseModel):
    url: str = Field(
        description="要请求的URL",
        json_schema_extra={
            "title": "URL"
        }
    )
    method: MethodTypes = Field(
        default=MethodTypes.GET,
        description="使用的HTTP方法",
        json_schema_extra={
            "title": "HTTP方法"
        }
    )
    bearer_token: str = Field(
        default=None,
        description="用于认证的Bearer令牌",
        json_schema_extra={
            "title": "Bearer令牌"
        }
    )
    body_json_data: str = Field(
        default="""{
    "key_1": "value_1",
    "key_2": "value_2"
}
""",
        description="在请求正文中发送的JSON数据",
        json_schema_extra={
            'widget': "codeeditor-json",
            "title": "JSON数据"
        }
    )


class OutputModel(BaseModel):
    base64_bytes_data: str = Field(
        description='base64编码的输出数据字符串'
    )
