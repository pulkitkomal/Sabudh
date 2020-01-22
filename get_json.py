from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    lst =[
         {'Samiksha': ['Jain','Here Glamour'],
         'Jigarjeet':['Kaur','Jigar'],
         'Sourav':['Arora','Goda'],
         'Sudhakar':['Kashyap','Sudha']}
    ]
    return jsonify(lst)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)