
from pydantic import BaseModel
from typing import List, Optional



class SpecBase(BaseModel):
    engine:Optional[str]
    fuel_type:Optional[str]
    body_type:Optional[str]
    engine:Optional[str]
    power:Optional[str]
    torque:Optional[str]
    fuel_type: Optional[str]
    transmmission:Optional[str]
    weight: Optional[str]
    horsepower:Optional[int]
    body_type: Optional[str]
    wheelbase:Optional[str]
    fuel_consumption: Optional[str]
    top_speed:Optional[str]
    acceleration:Optional[str]
    tires: Optional[str]
    suspension:Optional[str]
    seats:Optional[str]
    dimensions: Optional[str]
    drivetrain: Optional[str]
    cargo_capacity:Optional[str]



class SpecCreate(SpecBase):
    pass

class Spec(SpecBase):
    id:int
    class Config:
        orm_mode =True  



class ModelBase(BaseModel):
    name:str
    year:int
    image_url: Optional[str] = None

class ModelCreate(ModelBase):
    brand_id:int
    

class Model(ModelBase):
    id:int
    specs:List[Spec] = []
    class Config:
        orm_mode = True


class BrandBase(BaseModel):
    name:str


class BrandCreate(BrandBase):
    pass
    

class Brand(BrandBase):
    id:int
    models: List[Model] = []
    class Config:
        orm_mode = True

