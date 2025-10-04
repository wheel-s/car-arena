from sqlalchemy.orm import Session
from app import models, schema




def get_brands(db:Session):
    print("get all brands")
    return db.query(models.Brand).all()

def create_brand(db: Session, brand:schema.BrandCreate):
    print("create brand")
    brands = models.Brand(name = brand.name)
    db.add(brands)
    db.commit()
    db.refresh(brands)
    return brands

def get_models(db:Session):
    print("get all brands")
    return db.query(models.Model).all()

def create_models(db:Session, model:schema.ModelCreate):
    db_model = models.Model(
        name = model.name, 
        year = model.year, 
         image_url = model.image_url,
        brand_id = model.brand_id
       )
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

def get_model_by_name(db:Session, model_name:str):
    return db.query(models.Model).filter(models.Model.name == model_name).first()

def get_specs(db:Session):
    return db.query(models.Spec).all()

def get_spec_by_name(db:Session, spec_name:str):
    return db.query(models.Spec).filter(models.Spec.model == spec_name).first()

def create_spec(db: Session, spec:schema.SpecCreate, model_id:int):
    db_spec =models.Spec(**spec.dict(exclude_unset=True),
                          model_id=model_id)
    db.add(db_spec)
    db.commit()
    db.refresh(db_spec)
    return db_spec
    
