#!/usr/bin/python3
"""script that lists all State objects, and corresponding City
 objects, contained in the database hbtn_0e_101_usa"""
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Connecting"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)
    for st in result:
        print("{}: {}".format(st.id, st.name))
        for ct in st.cities:
            print("\t{}: {}".format(ct.id, ct.name))
    session.close()
