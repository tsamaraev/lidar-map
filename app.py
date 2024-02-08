from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/get_data/')
def get_data():
    with open('lidar/lidar01.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)