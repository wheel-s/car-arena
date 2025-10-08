
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base




class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), unique=True, index=True)
    models = relationship("Model", back_populates='brand', uselist=True)


class Model(Base):
    __tablename__ = "car_models"

    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey("brands.id"), nullable=False)
    name = Column(String(20), nullable=False, index=True)
    year = Column(Integer)
    image_url = Column(String(100))
    brand = relationship("Brand", back_populates='models')
    spec = relationship("Spec", back_populates='model', uselist=False)


class Spec(Base):
    __tablename__ = "car_specs"

    id = Column(Integer, primary_key=True, index=True)

    model_id = Column(Integer, ForeignKey("car_models.id"), nullable=False)
    year=Column(Integer)
    image_url = Column(String(100))
    engine=Column(String(30))
    power=Column(String(50))
    torque=Column(String(50))
    fuel_type = Column(String(50))
    transmmission = Column(String(50))
    weight = Column(String(50))
    horsepower = Column(Integer)
    wheelbase=Column(String(50))
    fuel_consumption =Column(String(50))
    top_speed =Column(String(50))
    acceleration = Column(String(50))
    tires = Column(String(50))
    suspension = Column(String(50))
    seats = Column(String(50))
    dimensions= Column(String(50))
    drivetrain = Column(String(50))
    cargo_capacity = Column(String(50))

    model = relationship("Model", back_populates="spec")

