import requests, datetime
from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def run_app():

    if request.method == 'POST':  #this block is only entered when the form is submitted

        city = request.form.get('city')
        country = request.form.get('country')
        url ='http://api.openweathermap.org/data/2.5/forecast?q={},{}&units=Metric&appid=bipbop_api_id'
        response =requests.get(url.format(city,country)).json()
        date=datetime.datetime.now()
        hour=date.hour
        weather = {
            'tempNow': response['list'][1]['main']['temp'],
            'temp3': response['list'][2]['main']['temp'],
            'temp6': response['list'][3]['main']['temp'],
            'temp9': response['list'][4]['main']['temp'],
            'temp24': response['list'][9]['main']['temp'],

            'humidityNow': response['list'][1]['main']['humidity'],
            'humidity3': response['list'][2]['main']['humidity'],
            'humidity6': response['list'][3]['main']['humidity'],
            'humidity9': response['list'][4]['main']['humidity'],
            'humidity24': response['list'][9]['main']['humidity'],

            'descriptionNow': response['list'][1]['weather'][0]['description'],
            'description3': response['list'][2]['weather'][0]['description'],
            'description6': response['list'][3]['weather'][0]['description'],
            'description9': response['list'][4]['weather'][0]['description'],
            'description24': response['list'][9]['weather'][0]['description']
        }

        return render_template('weather.html',weather=weather,hour=hour)

    return render_template('form.html')
