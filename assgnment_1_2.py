from flask import Flask, request, abort, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:XzXy#897@cluster0-s6ir1.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/signup", methods=["POST"])
def signup():

    user = {
        'name': request.json['name'],
        'desc': request.json['desc'],
        'cost': request.json['cost'],
        'supplier': request.json['supplier']

    }

    users = mongo.db.users

    users.insert(user)

    return jsonify({'status': 200, "response_message": "name " + request.json['name'] + ""})

@app.route("/items",methods=["GET"])
def login():
    items = mongo.db.items

    res = items.find()
    # res = res.toString()
    item_details = []

    for item in res:
        name = item['name']
        desc = item['desc']
        cost = item['cost']
        supplier = item['supplier']
        item_details.append({'name': name, 'desc': desc, 'cost': cost, 'supplier': supplier})


    return jsonify({'status': 200})




if __name__ == '__main__':
    app.run(port=4000,debug=True)