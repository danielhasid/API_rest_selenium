
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
        print(user_name)
        if user_name == None:
            return f"<H1 id='error'>" 'no such user:' + user_id + "</H1>" + 500
        else:
            return user_name

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

app.run(host='127.0.0.1', debug=True, port=5000)

#
# def post_user(user_id,user_name):
#     res = requests.post(f"http://127.0.0.1:5000/users/{user_id}", json={"user_name":user_name})
#     if res.status_code==200:
#         return res.json()
#     elif res.status_code==500:
#         return res.json()
#
# def get_user_api(user_id,user_name):
#     res = requests.get(f"http://127.0.0.1:5000/users/{user_id}")
#     if res.ok:
#         return {'status': 'ok','user_id':user_id, 'user_name': user_name , 'code': 200}
#     else:
#         return(f"User Not Found code:{res.status_code}")
#
# def delete_user(user_id):
#     res = requests.delete(f'http://127.0.0.1:5000/users/{user_id}', json={"user_name":"lalal"})
#     if res.ok:
#         print(f"Success : code {res.status_code}")
#     else:
#         print(res.text)
