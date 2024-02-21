from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
import json

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    with db.session.begin():
        result = db.session.execute(db.select(Cafe))
        all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    with db.session.begin():
        result = db.session.execute(db.select(Cafe))
        all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def get_locations():
    loc = request.args.get('loc')
    with db.session.begin():
        result = db.session.execute(db.select(Cafe))
        all_cafes = result.scalars().all()
    cafes = [cafe.to_dict() for cafe in all_cafes if cafe.location == loc]
    error = {"Not Found": "Sorry, we don't have a cafe at that location"}
    db.session.close()
    if not cafes:
        return jsonify(error)
    else:
        return jsonify(cafes)



@app.route("/new", methods=['POST'])
def create_new_cafe():
    # Assuming you expect 'name', 'location', and 'rating' keys in the form data
    form_data = request.form.to_dict()

    # Perform any validation or processing logic here
    boolean_fields = ['has_toilet', 'has_wifi', 'has_sockets', 'can_take_calls']
    for field in boolean_fields:
        form_data[field] = form_data[field].lower() == 'true'
    # Assuming you have a Cafe model or data structure
    new_cafe = Cafe(
        name=form_data['name'],
        map_url=form_data['map_url'],
        img_url=form_data['img_url'],
        location=form_data['location'],
        has_sockets=form_data['has_sockets'],
        has_toilet=form_data['has_toilet'],
        has_wifi=form_data ['has_wifi'],
        can_take_calls=form_data['can_take_calls'],
        seats=form_data['seats'],
        coffee_price=form_data['coffee_price']
    )
    try:
        with db.session.begin():
            db.session.add(new_cafe)
        return jsonify(response={"success": "Successfully added the new cafe."})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        db.session.close()


@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_coffee_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if not cafe:
        return jsonify({'error': 'Cafe not found'}), 404
    new_price = request.args.get('new_price')

    if new_price is not None:
        # Update the coffee price and commit changes to the database
        cafe.coffee_price = new_price
        db.session.commit()

        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 400

@app.route("/delete-cafe/<int:cafe_id>", methods=['DELETE'])
def delete_location(cafe_id):
    try:
        Cafe.query.filter_by(id=cafe_id).delete()
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the location."}), 200
    except:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 400

if __name__ == '__main__':
    app.run(debug=True)
