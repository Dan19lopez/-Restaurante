import pandas as pd
from .models import Category, Dish
from .database import SessionLocal

def import_csv_to_db(csv_path: str, sep=','):
    df = pd.read_csv(csv_path, sep=sep)
    db = SessionLocal()

    try:
        for _, row in df.iterrows():

            category_name = row.get("category") or "Sin categoria"
            category = db.query(Category).filter_by(name=category_name).first()

            if not category:
                category = Category(name=category_name)
                db.add(category)
                db.flush()

            dish = Dish(
                name=row["name"],
                description=row.get("description", ""),
                price=float(row.get("price") or 0),
                ingredients=row.get("ingredients", ""),
                vegetarian=bool(row.get("vegetarian", False)),
                category=category
            )

            db.add(dish)

        db.commit()

    finally:
        db.close()