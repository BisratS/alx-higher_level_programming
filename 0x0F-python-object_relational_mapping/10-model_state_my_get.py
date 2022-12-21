#!/usr/bin/python3
"""
Define function main
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import State


def main():
    """
    Print the State object with the name passed as argument
    from the database hbtn_0e_6_usa
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)
    sName = argv[4]

    for state in states:
        if state.name == sName:
            print(state.id)
            return
    print("Not found")


if __name__ == "__main__":
    main()
