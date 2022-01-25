from flask import Flask,render_template, request
from weather import Weather
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/weather', methods=['POST'])
def weather():
        city = request.form.get('city')
        weather = Weather(api_key, city)
        data = weather.get_weather()
        return render_template('weather.html', data=data)
    
