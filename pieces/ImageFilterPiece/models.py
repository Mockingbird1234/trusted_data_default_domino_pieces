from pydantic import BaseModel, Field
from enum import Enum


class OutputTypeType(str, Enum):
    """
    Output type for the result text
    """
    file = "file"
    base64_string = "base64_string"
    both = "both"


class InputModel(BaseModel):
    input_image: str = Field(
        description='输入图像。应该是文件路径或base64编码字符串',
        json_schema_extra={
            "from_upstream": "always",
            "title": "输入图像"
        }
    )
    sepia: bool = Field(
        default=False,
        description='应用棕褐色效果',
        json_schema_extra={
            "title": "棕褐色效果"
        }
    )
    black_and_white: bool = Field(
        default=False,
        description='应用黑白效果',
        json_schema_extra={
            "title": "黑白效果"
        }
    )
    brightness: bool = Field(
        default=False,
        description='应用亮度效果',
        json_schema_extra={
            "title": "亮度效果"
        }
    )
    darkness: bool = Field(
        default=False,
        description='应用暗度效果',
        json_schema_extra={
            "title": "暗度效果"
        }
    )
    contrast: bool = Field(
        default=False,
        description='应用对比度效果',
        json_schema_extra={
            "title": "对比度效果"
        }
    )
    red: bool = Field(
        default=False,
        description='应用红色效果',
        json_schema_extra={
            "title": "红色效果"
        }
    )
    green: bool = Field(
        default=False,
        description='应用绿色效果',
        json_schema_extra={
            "title": "绿色效果"
        }
    )
    blue: bool = Field(
        default=False,
        description='应用蓝色效果',
        json_schema_extra={
            "title": "蓝色效果"
        }
    )
    cool: bool = Field(
        default=False,
        description='应用冷色效果',
        json_schema_extra={
            "title": "冷色效果"
        }
    )
    warm: bool = Field(
        default=False,
        description='应用暖色效果',
        json_schema_extra={
            "title": "暖色效果"
        }
    )
    output_type: OutputTypeType = Field(
        default=OutputTypeType.both,
        description='输出图像的格式。选项有：`file`（文件）、`base64_string`（base64字符串）、`both`（两者）',
        json_schema_extra={
            "title": "输出类型"
        }
    )


class OutputModel(BaseModel):
    image_base64_string: str = Field(
        default='',
        description='输出图像的base64编码字符串',
    )
    image_file_path: str = Field(
        default='',
        description='输出图像文件的路径',
    )
