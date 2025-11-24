from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    dishes = relationship("Dish", back_populates="category")


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True, nullable=False)
    description = Column(Text)
    price = Column(Float)
    ingredients = Column(Text)
    vegetarian = Column(Boolean, default=False)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="dishes")