#!/usr/bin/python3
"""
Take in arguments and display all values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time, write one that is safe from
MySQL injections!
"""
import MySQLdb
from sys import argv


def main():
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
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    states = cur.fetchall()
    for s in states:
        if s[1] == _sName:
            print(s)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
