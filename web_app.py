from flask import Flask, request
import pymysql

from db_connector import add_user,get_user,delete_user

app = Flask(__name__)
users = {}
data_list = []# supported methods
@app.route('/users/<user_id>', methods=['POST', 'GET','DELETE'])
def users(user_id):
    if request.method == 'GET':
        user_name = str(get_user(user_id))
        if user_name == None:
            return f"<H1 id='error'>" 'no such user:' + user_id + "</H1>" + 500
        else:
            return f"<H1 id={user_id}>"+ user_name +"</H1>"# status code

    if request.method == 'POST':
        try:
            # getting the json data payload from request
            request_data = request.json
            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            add_user(user_id, user_name)
            return {'user_id': user_id, 'username': user_name, 'status': 'saved'}, 200  # status code
        except pymysql.err.IntegrityError:
            return {'user_id': user_id, 'username': user_name, 'status': '500'}, 500  # status code

    elif request.method == 'DELETE':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        is_delete = delete_user(user_id)
        if is_delete == 0:
            return {'status': 'error','reason': 'no such id'} ,500  # status code`
        else:
            return {'user id': user_id,'user_name': user_name,'status': 'deleted'}, 200  # status code`

#
# # todo elif for put and delete


app.run(host='127.0.0.1', debug=True, port=5000)
