import pymysql


user_list = []
def add_user(user_id, username):
    schema_name = "freedb_sql_freedb_tec"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_read_only', passwd='PdX4Dn?2%VTZ7Cx',
                           db=schema_name)
    # Getting a cursor from Database
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()
    # Inserting data into table
    cursor.execute(f"INSERT into {schema_name}.users (user_id,user_name,create_date) "
                   f"VALUES ('{user_id}','{username}',sysdate())")

    cursor.close()
    conn.close()


def delete_user(user_id):
    schema_name = "freedb_sql_freedb_tec"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_read_only', passwd='PdX4Dn?2%VTZ7Cx',
                           db=schema_name)
    # Getting a cursor from Database
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Deleting data from table
    cursor.execute(f"DELETE  FROM {schema_name}.users WHERE user_id = {user_id}")
    return cursor.rowcount


def get_user(user_id):
    result = {}
    schema_name = "freedb_sql_freedb_tec"
    # Establishing a connection to DB
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_read_only', passwd='PdX4Dn?2%VTZ7Cx',
                           db=schema_name)
    cursor = conn.cursor()
    cursor.execute(f"SELECT user_id,user_name FROM {schema_name}.users where user_id = {user_id}")
    result = cursor.fetchone()
    return result[1]
    cursor.close()
    conn.close()

