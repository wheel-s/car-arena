
from fastapi import APIRouter, Depends
from sqlalchemy.orm import  Session
from typing import List
from app import crud, schema, database
from fastapi import FastAPI, HTTPException, Depends

router = APIRouter()



@router.get("/", response_model=List[schema.ModelBase])
def get_models(db:Session= Depends(database.get_db)):
    return crud.get_models(db)


@router.get("/{model_name}", response_model=List[schema.ModelBase])
def get_model(model_name =str, db:Session= Depends(database.get_db)):
    model = crud.get_model_by_name(db, model_name)
    if not model:
        raise HTTPException(status_code= 404, detail = "Spec not found")
    return model



@router.post("/", response_model= schema.ModelBase)
def create_model(model:schema.ModelCreate, db:Session=Depends(database.get_db)):
    return crud.create_models(db, model)




