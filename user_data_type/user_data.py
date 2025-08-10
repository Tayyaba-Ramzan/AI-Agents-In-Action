from dataclasses import dataclass
from pydantic import BaseModel

@dataclass
class UserDataType:
    name:str
    age:int
    role:str

class HotelDataType(BaseModel):
    is_query_about_mehran_hotel:bool
    reason:str
    is_hotel_mehran_account_or_tax_query:bool

