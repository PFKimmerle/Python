from flask import Flask, jsonify, request, render_template_string
import random

app = Flask(__name__)

weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Windy', 'Snowy']

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weather API for Postman Testing</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }
            h1 { color: #333; }
            code { background-color: #f4f4f4; padding: 2px 5px; border-radius: 3px; }
        </style>
    </head>
    <body>
        <h1>Weather API for Postman Testing</h1>
        <p>This API is designed for testing with Postman. Please use Postman to interact with the following endpoint:</p>
        <code>GET /weather?city=&lt;city_name&gt;</code>
        <p>Example: <code>/weather?city=NewYork</code></p>
        <p>For more information on API testing and development, check out articles at: 
        <a href="https://pfkimmerle.substack.com/" target="_blank">Pixels to Code</a>
    </body>
    </html>
    ''')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Unknown')
    temperature = random.randint(-10, 40)
    condition = random.choice(weather_conditions)
    return jsonify({
        'city': city,
        'temperature': temperature,
        'condition': condition
    })

if __name__ == '__main__':
    app.run(debug=True)