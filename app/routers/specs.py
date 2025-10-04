
from fastapi import APIRouter, Depends
from sqlalchemy.orm import  Session
from typing import List
from app import crud, schema, database

from fastapi import FastAPI, HTTPException, Depends

router = APIRouter()



@router.get("/", response_model=List[schema.Spec])
def get_specs(db: Session =Depends(database.get_db)):
    return crud.get_specs(db)


@router.get("spec/{spe_name}", response_model=schema.Spec)
def read_spec(spec_name:str, db:Session =Depends(database.get_db)):
    spec = crud.get_spec_by_name(db, spec_name)
    if not spec:
        raise HTTPException(status_code= 404, detail = "Spec not found")
    return spec

@router.post("/{model_id}", response_model=schema.SpecCreate)
def create_spec(model_id:int, spec:schema.SpecCreate, db: Session = Depends(database.get_db),):
    return crud.create_spec(db, spec, model_id)




