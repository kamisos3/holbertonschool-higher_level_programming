#!/usr/bin/python3
"""
Script that prints the state object with the name passed as argument
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <username> <password> "
              "<database_name> <state_name>")
        sys.exit(1)

    user, password, db_name, search_name = sys.argv[1:]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == search_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
