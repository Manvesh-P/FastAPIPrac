from fastapi import FastAPI
from mysql.connector import connect as _connect
# import csv


def connect_to_db():
    my_db = _connect(user='nikhil', 
                    password='Nikhil123@', 
                    host='localhost', 
                    database='peopleDB'
                    )

    # _cursor = my_db.cursor()
    return my_db


app = FastAPI()

# @app.route('/get_data/<_id:int>')
# @app.route('/get_data/{_id}')
@app.get('/get_data/{_id}')
def get_data_by_id(_id):
    print('_id, ', _id)
    _my_db = connect_to_db()
    print('_my_db ', _my_db)
    _cursor = _my_db.cursor()
    req_data = _cursor.execute('SELECT * FROM people_table WHERE playerID = "%s"' % _id)
    # req_data = _cursor.execute('SELECT * FROM people_table LIMIT 10;')
    # _cursor.execute('SELECT * FROM people_table LIMIT 10;')
    # print('req_data, ', req_data)
    # print(list(_cursor))
    req_data = list(_cursor)
    _my_db.close()

    return req_data
    


@app.get('/get_all_data/{limit}/{offset}')
def get_all_data(limit: int = 10, offset: int = 0):
    print('limit, ', limit)
    print('offset, ', offset)
    print('get_all_data called')
    # _id = 1
    _my_db = connect_to_db()
    print('_my_db ', _my_db)
    _cursor = _my_db.cursor()
    # req_data = _cursor.execute('SELECT * FROM people_table WHERE playerID = "%s"' % _id)
    # req_data = _cursor.execute('SELECT * FROM people_table LIMIT 10;')
    # _cursor.execute('SELECT * FROM people_table LIMIT 10;')
    _cursor.execute(f'SELECT * FROM people_table limit {limit} offset {offset};')
    # print('req_data, ', req_data)
    # print(list(_cursor))
    req_data = list(_cursor)
    _my_db.close()

    return req_data


if __name__ == '__main__':
    app.run()
