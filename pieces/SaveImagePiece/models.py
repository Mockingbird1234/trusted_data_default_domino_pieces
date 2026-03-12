from pydantic import BaseModel, Field


class InputModel(BaseModel):
    base64_data: str = Field(
        description='要保存为图像的输入数据',
        json_schema_extra={
            "title": "Base64数据"
        }
    )


class OutputModel(BaseModel):
    output_image_path: str = Field(
        description='保存图像的输出文件路径'
    )
