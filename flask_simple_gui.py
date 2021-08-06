"""
Prototype web gui find the nearest airport from a given location.
The gui provides a form to input a location, then displays the nearest airport.
The gui can also display a list of all possible airport locations.
The about page provides additional information on the application.

The web gui is currently only a prototype and runs using  the python development server
on http://127.0.0.1:5001/
"""

from flask import Flask, render_template, request, redirect
simple_app = Flask(__name__)


@simple_app.route('/')
def index():
    return redirect(f"/home/")


@simple_app.route('/home/')
def home():
    return render_template('simple/get_location_simple.html')


@simple_app.route('/about/')
def about():
    return render_template('about.html.jinja', documentation=simple_app.config['documentation'])


@simple_app.route('/locations/')
def locations():
    return render_template('simple/list_locations_simple.html.jinja', airports=simple_app.config['airports'])


@simple_app.route('/result', methods = ['POST', 'GET'])
def find_nearest():
    if request.method == 'POST':
        result = request.form
        return render_template(
             "simple/distance_result_simple.html.jinja",
             result=result,
             nearest=simple_app.config['airports'].shortest_distance(
                (float(result['latitude']),
                 float(result['longitude']))))


if __name__ == '__main__':
    simple_app.run(debug=False)
