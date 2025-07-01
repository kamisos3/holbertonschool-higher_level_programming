#!/usr/bin/python3
"""Prints all city objects grouped by state"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
