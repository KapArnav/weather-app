from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    api_key = "your_api_key"
    city = "Chandigarh"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]
        }
    else:
        weather = None 
        
    return render_template('index.html', weather=weather)

if __name__ == "__main__":
    app.run(debug=True)