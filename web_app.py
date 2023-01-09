from flask import Flask, request
import pymysql

from db_connector import add_user,get_user,delete_user

app = Flask(__name__)
users = {}

@app.route('/get_user_data/<user_id>',methods=['GET'])
def get_user_name(user_id):
    if request.method == 'GET':
        user_name = str(get_user(user_id))
        if user_name == None:
            return f"<H1 id='error'>" 'no such user:' + user_id + "</H1>" + 500
        else:
            return f"<H1 id={user_id}>"+ user_name +"</H1>"# status code



app.run(host='127.0.0.1', debug=True, port=5000)

