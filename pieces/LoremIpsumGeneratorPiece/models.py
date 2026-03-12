from pydantic import BaseModel, Field
from enum import Enum


class ItemsType(str, Enum):
    words = 'words'
    sentences = 'sentences'
    paragraphs = 'paragraphs'


class InputModel(BaseModel):
    """
    LoremIpsumGeneratorPiece Input Model
    """
    items: ItemsType = Field(
        default=ItemsType.words,
        description="要生成的项类型",
        json_schema_extra={
            "title": "项类型"
        }
    )
    number_of_items: int = Field(
        default=1,
        description="要生成的项数量",
        json_schema_extra={
            "title": "项数量"
        }
    )


class OutputModel(BaseModel):
    """
    LoremIpsumGeneratorPiece Output Model
    """
    output_text: str = Field(
        description="生成的文本"
    )
