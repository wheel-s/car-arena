
from fastapi import APIRouter, Depends
from sqlalchemy.orm import  Session
from typing import List
import crud, schema, database



router = APIRouter()


@router.get("/", response_model=List[schema.Brand])
def get_brands(db: Session=Depends(database.get_db)):
    return crud.get_brands(db)

@router.post("/", response_model=schema.Brand)
def create_brand(brand:schema.BrandCreate, db:Session = Depends(database.get_db)):
    return crud.create_brand(db, brand)
