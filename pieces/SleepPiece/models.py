from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Sleep Piece Input Model
    """

    sleep_time: float = Field(
        default=1,
        description="休眠的秒数",
        json_schema_extra={
            "title": "休眠时间"
        }
    )


class OutputModel(BaseModel):
    """
    Sleep Piece Output Model
    """
    message: str = Field(
        description="休眠组件已执行"
    )
