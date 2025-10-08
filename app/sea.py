import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from models import Brand, Model
from database import Base, engine, SessionLocal


import httpx


Base.metadata.create_all(bind=engine)
db:Session = SessionLocal()



api_brand ="https://www.carqueryapi.com/api/0.3/?cmd=getMakes"
api_models = "https://www.carqueryapi.com/api/0.3/?cmd=getModels&make={brand}&year={year}"



bran_list = [
    "Toyota", "Honda","Ford","Mercedes","Tesla","Benz","Chevrolet","Nissan", "Volkswagen","BMW"
    ,"Hyundai", "Kai","Mazda","Audi","Lexus","Subaru","Volvo"
]

years = range(2018, 2026)



for brand in bran_list:
   
    db_brand =db.query(Brand).filter_by(name = brand).first()
    if not db_brand:
        db_brand = Brand(name= brand)
        db.add(db_brand)
        db.commit()
        db.refresh(db_brand)

    inserted_models = set()

    for year in years:
        url= f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/{brand}/modelyear/{year}?format=json"
        resp = requests.get(url)
        print(resp.text)
        data = resp.json().get("Results",[])
        

        for item in data:
            model_name = item["Model_Name"]

            if model_name in inserted_models:
                continue
            if len(inserted_models) >= 25:
                break
            inserted_models.add(model_name)

            db_model = db.query(Model).filter_by( name = model_name, year = year, brand_id = db_brand.id).first()
            if not db_model: 
                db_model = Model(name= model_name, year = year, brand_id = db_brand.id)
                db.add(db_model)
                db.commit()
                db.refresh(db_model)
                print(f"added {brand} {model_name}{year} to db")
print("complete")
db.close()
            
















def fetch_models_for_brand(brand):

    url= f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{brand}?format=json'
    try:
        response = requests.get(url)
        data = response.json()  
        models = [m['Model_Name'] for m in data['Results']]
        print(models)
        return models[:20]
    except:
        print("no result found")



