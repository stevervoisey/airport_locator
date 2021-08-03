"""
Prototype web gui find the nearest airport from a given location.
The gui provides a form to input a location, then displays the nearest airport.
The gui can also display a list of all possible airport locations.
The about page provides additional information on the application.

The web gui is currently only a prototype and runs using  the python development server
on http://127.0.0.1:5001/
"""
import os

from flask import Flask, render_template, redirect, flash
from forms import CoordinateForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)  # Return a string of 32 random bytes suitable for cryptographic use.


@app.route('/')
def index():
    return redirect(f"/home/")


@app.route('/home/', methods=['get', 'post'])
def home():
    form = CoordinateForm()
    if form.validate_on_submit():
        print("\nData received. Now redirecting ...")
        flash("Message Received", "success")
        return find_nearest(form)
    return render_template('get_location_flask_form.html', form=form)


@app.route('/about/')
def about():
    return render_template('about.html.jinja', documentation=app.config['documentation'])


@app.route('/locations/')
def locations():
    return render_template('locations.html.jinja', airports=app.config['airports'])


def find_nearest(form: CoordinateForm):
    nearest = app.config['airports'].shortest_distance(
        (float(form.data['latitude']),
         float(form.data['longitude']))
    )
    return render_template(
         "distance_result_from_form.html.jinja",
         form=form,
         nearest=nearest)


if __name__ == '__main__':
    app.run(debug=False)