from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, URL
import csv
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_APP_SECRET_KEY')
Bootstrap(app)


class CafeForm(FlaskForm):
    coffee_opts = ['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
    wifi_opts = ['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
    power_opts = ['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[URL()])
    open_time = StringField('Opening Time e.g. 8AM')
    close_time = StringField('Closing Time e.g. 5:30PM')
    coffee = SelectField('Coffee Rating', choices=coffee_opts)
    wifi = SelectField('WIFI Rating', choices=wifi_opts)
    power = SelectField('Power Socket Availability', choices=power_opts)
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', encoding='utf-8') as fd:
            fd.write(f"{form.cafe.data},{form.location.data},{form.open_time.data},{form.close_time.data},{form.coffee.data},{form.wifi.data},{form.power.data}\n")

        return render_template("index.html")
    else:
        return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
