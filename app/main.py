from fastapi import FastAPI
from app.database import Base, engine
from app.routers import brands, models, specs
from app import models as db_models


db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Car Specs APPI")



app.include_router(brands.router, prefix="/brands",tags=["Brands"])
app.include_router(models.router, prefix="/models",tags=["Models"])
app.include_router(specs.router, prefix="/specs",tags=["Specs"])




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)



