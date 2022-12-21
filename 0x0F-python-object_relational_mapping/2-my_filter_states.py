#!/usr/bin/python3
"""
Display all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    _user = argv[1]
    _pw = argv[2]
    _dbname = argv[3]
    _sName = argv[4]

    conn = MySQLdb.connect(
         host="localhost",
         port=3306,
         user=_user,
         passwd=_pw,
         db=_dbname,
         charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states \
                WHERE BINARY `name` = '{}' \
                ORDER BY id ASC".format(_sName)
    cur.execute(query)
    states = cur.fetchall()
    for s in states:
        print(s)
    cur.close()
    conn.close()
