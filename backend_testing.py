import requests
#
USER_ID = 666666
NAME = 'Daniel'


def post_user(user_id,user_name):
    res = requests.post(f"http://127.0.0.1:5000/users/{user_id}", json={"user_name":user_name})
    if res.status_code==200:
        print(res.json())
    elif res.status_code==500:
        print(res.json())

def get_user_api(user_id):
    res = requests.get(f"http://127.0.0.1:5000/users/{user_id}")
    if res.ok:
        print(res.text)
    else:
        print(res.text)


post_user(USER_ID,NAME)
get_user_api(88888)

# {'status': 'ok','user_id':user_id, 'user_name': user_name , 'code': 200}