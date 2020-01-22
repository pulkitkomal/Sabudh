from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {
        'id' : '1',
        'value' : 'Samiksha',
        'desc' : 'Student'
    },
    {
        'id' : '2',
        'value' : 'Komal',
        'desc' : 'Student'
    }
]

@app.route('/task', methods=['POST'])
def apnd():
    id = str(int(tasks[-1]['id']) + 1)
    desc = request.json['desc']
    value = request.json['value']
    post_dict = {
        'id': id,
        'desc': desc,
        'value': value
    }
    tasks.append(post_dict)
    print(tasks)
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000, debug=True)