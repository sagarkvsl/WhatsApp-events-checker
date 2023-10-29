from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_api_response', methods=['POST'])
def get_api_response():
    api_key = request.form['api_key']
    limit = request.form['limit']

    url = f'https://api.brevo.com/v3/whatsapp/statistics/events?limit={limit}&offset=0&sort=desc'

    headers = {
        'api-key': api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return render_template('response.html', data=data)
    else:
        return 'Error: Unable to fetch data from the API'

if __name__ == '__main__':
    app.run(debug=True)
