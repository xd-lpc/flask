from flask import Flask, request
import utils

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    r = request.args.get('info', 'hi')
    return utils.get_dp()


@app.route('/add', methods=['POST'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = request.json['a'] + request.json['b']
    return str(result)




#fffff

if __name__ == '__main__':
    app.run(debug=True)