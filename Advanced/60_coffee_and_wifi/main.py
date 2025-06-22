from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('cafes location on google map URL', validators=[DataRequired(), URL()])
    open_time = StringField('Opening time e.g. 6AM', validators=[DataRequired()])
    close_time = StringField('Closing time e.g. 4:30PM', validators=[DataRequired()])

    coffee_rating = SelectField(label='Coffee Rating',
                                choices=[(1, '✘'), (1, '☕️'), (2, '☕️' * 2), (3, '☕️' * 3), (4, '☕️' * 4), (5, '☕️' * 5)],
                                coerce=int,  # Coerce the submitted value to an integer
                                validators=[DataRequired()])
    wifi_rating = SelectField(label='WiFi Rating',
                              choices=[(1, '✘'), (1, '💪'), (2, '💪' * 2), (3, '💪' * 3), (4, '💪' * 4), (5, '💪' * 5)],
                              coerce=int,  # Coerce the submitted value to an integer
                              validators=[DataRequired()])
    power_rating = SelectField(label='Power Outlet',
                               choices=[(1, '✘'), (1, '🔌'), (2, '🔌' * 2), (3, '🔌' * 3), (4, '🔌' * 4), (5, '🔌' * 5)],
                               coerce=int,  # Coerce the submitted value to an integer
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location = form.location.data
        otime = form.open_time.data
        ctime = form.close_time.data
        coffee_rate = "☕️"*form.coffee_rating.data if form.coffee_rating.data != 0 else "✘"
        wifi_rate = "💪" * form.coffee_rating.data if form.wifi_rating.data != 0 else "✘"
        power_rate = "🔌️" * form.coffee_rating.data if form.power_rating.data != 0 else "✘"
        data = [cafe, location, otime, ctime, coffee_rate, wifi_rate, power_rate]

        with open('cafe-data.csv', 'a', newline='\n', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(data)
        return render_template("success.html")

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='\n', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
