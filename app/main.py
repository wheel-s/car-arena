from fastapi import FastAPI
from database import Base, engine
from routers import brands, models, specs
import models as db_models


db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Car Specs APPI")



app.include_router(brands.router, prefix="/brands",tags=["Brands"])
app.include_router(models.router, prefix="/models",tags=["Models"])
app.include_router(specs.router, prefix="/specs",tags=["Specs"])



