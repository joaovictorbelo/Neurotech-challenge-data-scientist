from typing import Literal
from pydantic import BaseModel

class Path(BaseModel):
    path: str