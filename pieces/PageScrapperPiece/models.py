from pydantic import BaseModel, Field
from typing import List


class ItemType(BaseModel):
    tag: str = Field(
        default="p",
        description='HTML标签名称',
    )
    class_name: str = Field(
        default="",
        description='HTML标签类名',
    )


class InputModel(BaseModel):
    """
    PageScrapperPiece Input Model
    """
    url: str = Field(
        default="",
        description='要检索内容的URL',
        json_schema_extra={
            "title": "URL"
        }
    )
    search_items: List[ItemType] = Field(
        default=[ItemType()],
        description='要搜索的HTML标签和类名列表',
        json_schema_extra={
            "title": "搜索项"
        }
    )


class OutputModel(BaseModel):
    """
    PageScrapperPiece Output Model
    """
    scrapped_text: str = Field(
        description='从URL抓取的文本'
    )
