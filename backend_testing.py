from rest_app import post_user, get_user_api
import requests
#
USER_ID = input("Add User ID: ")
NAME = input("Add User Name: ")



def check_user(USER_ID,NAME):
    data_from_db = get_user_api(USER_ID,NAME)
    if data_from_db['code'] == 200 and NAME ==data_from_db['user_name']:
        if USER_ID==data_from_db['user_id'] and NAME == data_from_db['user_name']:
            print(f"The user name is : {data_from_db['user_name']} and user ID {data_from_db['user_id']} are stored inside DB")
    else:
        print(f"{data_from_db['user_name']} Not Found")

result = post_user(USER_ID,NAME)
if result['status']=='saved':
    check_user(USER_ID,NAME)
else:
    print("User Already Exists")
