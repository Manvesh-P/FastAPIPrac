from mysql.connector import connect as _connect
import csv


my_db = _connect(user='nikhil', 
                 password='Nikhil123@', 
                 host='localhost', 
                 database='peopleDB'
                 )


_cursor = my_db.cursor()
# _query = """CREATE TABLE IF NOT EXISTS people_table (
#             playerID VARCHAR(200), birthYear INT, birthMonth VARCHAR(200), birthDay VARCHAR(200), birthCountry VARCHAR(200),	birthState VARCHAR(200),	birthCity VARCHAR(200),	deathYear INT,	deathMonth VARCHAR(200),	deathDay VARCHAR(200),	deathCountry VARCHAR(200),	deathState VARCHAR(200),	deathCity VARCHAR(200),	nameFirst VARCHAR(200),	nameLast VARCHAR(200),	nameGiven VARCHAR(200),	weight FLOAT,	height VARCHAR(200),	bats VARCHAR(200),	throws VARCHAR(200),	debut VARCHAR(200),	finalGame VARCHAR(200),	retroID	VARCHAR(200), bbrefID VARCHAR(200)
# );"""

_query = """CREATE TABLE IF NOT EXISTS people_table (
            playerID VARCHAR(200), birthYear VARCHAR(200), birthMonth VARCHAR(200), birthDay VARCHAR(200), birthCountry VARCHAR(200),	birthState VARCHAR(200),	birthCity VARCHAR(200),	deathYear VARCHAR(200),	deathMonth VARCHAR(200),	deathDay VARCHAR(200),	deathCountry VARCHAR(200),	deathState VARCHAR(200),	deathCity VARCHAR(200),	nameFirst VARCHAR(200),	nameLast VARCHAR(200),	nameGiven VARCHAR(200),	weight VARCHAR(200),	height VARCHAR(200),	bats VARCHAR(200),	throws VARCHAR(200),	debut VARCHAR(200),	finalGame VARCHAR(200),	retroID	VARCHAR(200), bbrefID VARCHAR(200)
);"""
# _query_one = ''

with open('/home/nikhilmanvesh/Downloads/Banksy/People.csv', mode='r') as f:
    _data = list(csv.reader(f))

# print(_data)

_cursor.execute(_query)
for _record in _data[1: ]:
    print(_record)
    # _cursor.execute('INSERT INTO people_table (playerID,	birthYear,	birthMonth,	birthDay,	birthCountry,	birthState,	birthCity,	deathYear,	deathMonth,	deathDay,	deathCountry,	deathState,	deathCity,	nameFirst,	nameLast,	nameGiven,	weight,	height,	bats,	throws,	debut,	finalGame,	retroID	bbrefID) ' + \
    #                 'VALUES %s;' % tuple(_record))
    _cursor.execute('INSERT INTO people_table (playerID,	birthYear,	birthMonth,	birthDay,	birthCountry,	birthState,	birthCity,	deathYear,	deathMonth,	deathDay,	deathCountry,	deathState,	deathCity,	nameFirst,	nameLast,	nameGiven,	weight,	height,	bats,	throws,	debut,	finalGame,	retroID,	bbrefID) ' + \
                    'VALUES %s;' % str(tuple(_record)))

# _cursor.commit()
my_db.commit()
my_db.close()
