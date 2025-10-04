
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base




class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    models = relationship("Model", back_populates='brand', uselist=True)


class Model(Base):
    __tablename__ = "car_models"

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey("brands.id"), nullable=False)
    name = Column(String, nullable=False, index=True)
    year = Column(Integer)
    image_url = Column(String)
    brand = relationship("Brand", back_populates='models')
   


class Spec(Base):
    __tablename__ = "car_specs"

    id = Column(Integer, primary_key=True, index=True)

    model_id = Column(Integer, ForeignKey("car_models.id"), nullable=False)
    year=Column(Integer)
    image_url = Column(String)
    engine=Column(String)
    power=Column(String)
    torque=Column(String)
    fuel_type = Column(String)
    transmmission = Column(String)
    weight = Column(String)
    horsepower = Column(Integer)
    body_type =Column(String)
    wheelbase=Column(String)
    fuel_consumption =Column(String)
    top_speed =Column(String)
    acceleration = Column(String)
    tires = Column(String)
    suspension = Column(String)
    seats = Column(String)
    dimensions= Column(String)
    drivetrain = Column(String)
    cargo_capacity = Column(String)

    model = relationship("Model", back_populates=" spec")

