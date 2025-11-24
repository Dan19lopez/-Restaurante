from flask import Flask, render_template, request, redirect, url_for
from .database import SessionLocal
from .crud import DishService

app = Flask(__name__)

@app.route("/")
def index():
    db = SessionLocal()
    try:
        service = DishService(db)
        dishes = service.list_dishes()
    finally:
        db.close()

    return render_template("index.html", dishes=dishes)


@app.route("/dish/<int:dish_id>")
def dish_detail(dish_id):
    db = SessionLocal()
    try:
        service = DishService(db)
        dish = service.get_dish(dish_id)
    finally:
        db.close()

    return render_template("dish_detail.html", dish=dish)


@app.route("/upload-csv", methods=["GET", "POST"])
def upload_csv():
    if request.method == "POST":
        file = request.files["csvfile"]
        if file:
            path = f"./data/{file.filename}"
            file.save(path)

            from .services import import_csv_to_db
            import_csv_to_db(path)

            return redirect(url_for("index"))

    return render_template("upload_csv.html")


if __name__ == "__main__":
    app.run(debug=True)