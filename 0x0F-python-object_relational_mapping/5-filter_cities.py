#!/usr/bin/python3
"""
Lists all cities of that state, using the database hbtn_0e_4_usa.
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
    cur.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    cities = cur.fetchall()

    tCities = ''

    for city in cities:
        if city[2] == _sName:
            tCities += city[1] + ', '

    print(tCities[:-2])
    cur.close()
    conn.close()
