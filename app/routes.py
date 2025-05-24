from flask import Blueprint, render_template, request
from .api import get_weather_data

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    error = None
    if request.method == 'POST':
        city = request.form.get('city')
        try:
            weather = get_weather_data(city)
        except Exception as e:
            error = str(e)
    return render_template('index.html', weather=weather, error=error)
