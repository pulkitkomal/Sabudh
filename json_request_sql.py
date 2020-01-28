from flask import Flask, request, jsonify
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database='sabudh'
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO json_api (id, value, desc) VALUES ('1','pulkit','student')")

mydb.commit()

#
# print(mydb)
# app = Flask(__name__)
#
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port= 5000, debug=True)