from typing import List, Dict
from pydantic import BaseModel

class DataInput(BaseModel):
    data: List[Dict[str, object]]