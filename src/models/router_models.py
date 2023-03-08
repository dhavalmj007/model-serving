from datetime import datetime
from typing import List

from pydantic import BaseModel


class InputFeatures(BaseModel):
    ip: int
    app: int
    device: int
    os: int
    channel: int
    click_time: datetime


class Request(BaseModel):
    input_data: List[InputFeatures]


class Return(BaseModel):
    is_attributed: bool


class ReturnModel(BaseModel):
    response: List[Return]

