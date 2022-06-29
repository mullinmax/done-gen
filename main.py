#!/home/maxwell/miniconda3/envs/done-gen/bin/python
import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home_route():
    return render_template('index.html')

from lists.names import names
@app.route('/full-name')
def names_rounte():
    popularity = int(request.args.get('popularity', '1'))
    gender = request.args.get('gender', None)
    return jsonify(names.get_name(gender=gender, popularity=popularity))

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="192.168.0.4", port=5000)