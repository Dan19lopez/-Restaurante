from sqlalchemy.orm import Session
from . import models

class DishService:
    def __init__(self, db: Session):
        self.db = db

    def create_dish(self, name, description, price, ingredients, category=None, vegetarian=False):
        dish = models.Dish(
            name=name,
            description=description,
            price=price,
            ingredients=ingredients,
            vegetarian=vegetarian,
            category=category
        )
        self.db.add(dish)
        self.db.commit()
        self.db.refresh(dish)
        return dish

    def get_dish(self, dish_id):
        return self.db.query(models.Dish).filter(models.Dish.id == dish_id).first()

    def list_dishes(self, skip=0, limit=100):
        return self.db.query(models.Dish).offset(skip).limit(limit).all()

    def find_by_name(self, name):
        return self.db.query(models.Dish).filter(models.Dish.name.ilike(f"%{name}%")).all()