from flask import Flask, render_template, request, jsonify, abort
from datetime import datetime

app = Flask(__name__)

data = {
    'hello': 'Hello World!',
    'name': 'My name is Flask Server',
}

@app.route('/')
def render_index():
    return render_template('index.html')

@app.route('/dictionary', methods=['POST'])
def post_func():
    if 'key' in request.json and 'value' in request.json:
        key = request.json['key']
        value = request.json['value']
        if key in data:
            return abort(409)
        node = {key: value}
        data.update(node)
        return jsonify(success=True, result=data)
    else:
        return abort(400)

@app.route('/dictionary', methods=['PUT'])
def put_func():
    if 'key' in request.json and 'value' in request.json:
        key = request.json['key']
        value = request.json['value']
        if not (key in data):
            return abort(404)
        if data[key] == value:
            return abort(409)
        node = {key: value}
        data.update(node)
        return jsonify(success=True, result=data)
    else:
        return abort(404)

@app.route('/dictionary/<key>', methods=['DELETE'])
def delete_func(key):
    if key in data:
        if data.pop(key):
            time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M")
            return jsonify(success=True, result="{\"%s\": \"null\", \"time\": \"%s\"}" % (key, time))
        else:
            return jsonify(success=True, result='200')
    else:
        return jsonify(success=True, result='200')

@app.route('/dictionary/<key>',methods=['GET'])
def get_func(key):
    if key in data:
        return jsonify(success=True, result=data[key])
    else:
        return abort(404)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
