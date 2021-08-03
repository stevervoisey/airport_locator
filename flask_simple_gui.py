"""
Prototype web gui find the nearest airport from a given location.
The gui provides a form to input a location, then displays the nearest airport.
The gui can also display a list of all possible airport locations.
The about page provides additional information on the application.

The web gui is currently only a prototype and runs using  the python development server
on http://127.0.0.1:5001/
"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(f"/home/")


@app.route('/home/')
def home():
    return render_template('get_location_form.html')


@app.route('/about/')
def about():
    return render_template('about.html.jinja', documentation=app.config['documentation'])


@app.route('/locations/')
def locations():
    return render_template('locations.html.jinja', airports=app.config['airports'])


@app.route('/result', methods = ['POST', 'GET'])
def find_nearest():
    if request.method == 'POST':
        result = request.form
        return render_template(
             "distance_result.html.jinja",
             result=result,
             nearest=app.config['airports'].shortest_distance(
                (float(result['latitude']),
                 float(result['longitude']))))


if __name__ == '__main__':
    app.run(debug=False)
