from typing import List
from pydantic import BaseModel
from datetime import datetime

class CallBase(BaseModel):
    extension : str(4)
    nu_ddd : str(2)
    nu_phone : str(9)
    dt_start : datetime
    dt_answer : datetime
    dt_finish : datetime    

class CallCreate(CallBase):
    pass

class Call(CallBase):
    id_call: int
    owner_id: int

    class Config:
        orm_mode = True


class ExtentEventBase(BaseModel):
    extension : str(4)
    status : str(9)
    dt_event : datetime

class ExtentEventCreate(ExtentEventBase):
    pass

class ExtentEvent(ExtentEventBase):
    id_extent_event: int
    owner_id: int

    class Config:
        orm_mode = True 


class ExtensionBase(BaseModel):
    extension : str(4)
    nm_extension : str(9)
    is_active : bool
    must_record : bool
    nm_transfer : str(9)
    was_exported : bool

class ExtensionCreate(ExtensionBase):
    pass

class Extension(ExtensionBase):
    id_extension: int

    class Config:
        orm_mode = True 