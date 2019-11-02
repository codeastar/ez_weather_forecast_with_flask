# ez_weather_forecast_with_flask
Easy Weather Forecast Single-Page Web App with Flask

Full document: 
http://www.codeastar.com/flask-easy-web-app-python/

## Quick start
$cd ezw

$export DARK_SKY_KEY={your Dark Sky API Key}

$python ezw_app.py  

## Docker deployment
$docker build -t ezw .

$docker run -d --name ezcon -p 8081:5000 -e DARK_SKY_KEY={your Dark Sky API Key} ezw

