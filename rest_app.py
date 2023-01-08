import requests

def post_user(user_id,user_name):
    res = requests.post(f"http://127.0.0.1:5000/users/{user_id}", json={"user_name":user_name})
    if res.status_code==200:
        return res.json()
    elif res.status_code==500:
        return res.json()

def get_user_api(user_id,user_name):
    res = requests.get(f"http://127.0.0.1:5000/users/{user_id}")
    if res.ok:
        return {'status': 'ok','user_id':user_id, 'user_name': user_name , 'code': 200}
    else:
        print(f"User Not Found code:{res.status_code}")

def delete_user(user_id):
    res = requests.delete('http://127.0.0.1:5000/users/5', json={"user_name":"lalal"})
    if res.ok:
        print(f"Success : code {res.status_code}")
    else:
        print(res.text)

# res = requests.get('http://127.0.0.1:5000/users/3')
# if res.ok:
#     print(res.text)
# else:
#     print(f"User Not Found code:{res.status_code}")
#
# res = requests.delete('http://127.0.0.1:5000/users/20', json={"user_name": "lalal"})
# if res.ok:
#     print(f"Success : code {res.status_code}")
# else:
#     print(res.text)
