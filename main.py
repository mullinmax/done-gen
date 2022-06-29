#!/home/maxwell/miniconda3/envs/done-gen/bin/python
import json
from flask import Flask, request, jsonify

from names import names
app = Flask(__name__)
@app.route('/full-name')
def index():
    popularity = int(request.args.get('popularity', '1'))
    gender = request.args.get('gender', None)
    return jsonify(names.get_name(gender=gender, popularity=popularity))

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="192.168.0.4", port=5000)