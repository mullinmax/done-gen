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
    diveristy = int(request.args.get('diveristy', '1'))
    gender = request.args.get('gender', None)
    return jsonify(names.get_name(gender=gender, diveristy=diveristy))

@app.route('/npc', methods=["POST", "GET"])
def npc():
    title ='npc'
    diveristy = float(request.form.get('diversity', '1'))
    gender = request.form.get('gender', None)
    print(diveristy, gender)
    first, last = names.get_name(gender=gender, diveristy=diveristy)
    return render_template('npc.html', first_name = first, last_name = last)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="192.168.0.4", port=5000)