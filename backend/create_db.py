############################################
#
# Program: Create DB Tables in MySQL
# Method: Connect to Cloud Proxy SQL
# Project: DB MGMT Final Project
# Author: Jacob Janzen
# Last Updated: 11/22/23
#
#####################################


import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

Base = declarative_base()

class TestTable(Base):
    __tablename__ = 'test_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
    db_host = os.environ["DB_HOST"] = "round-gasket-405922:us-west1:music-streaming-app"
    db_user = os.environ["DB_USER"] = "root"  
    db_pass = os.environ["DB_PASS"] = "Jifgev-dufmu8-tuzzug"
    db_port = os.environ["DB_PORT"] = "3306"
    db_name = os.environ["DB_NAME"] = "music_db"

    engine = create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername="mysql+pymysql",
            username=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
            database=db_name,
        ),
        echo=False  # for debugging purposes
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        try:
            new_data = TestTable(name='Example Data')
            session.add(new_data)
            session.commit()
            print("\nData Inserted Successfully\n")

            query_result = session.query(TestTable).all()
            for row in query_result:
                print(f"ID: {row.id}, Name: {row.name}")

        except sqlalchemy.exc.SQLAlchemyError as err:
            print(f"Error: {err}")
            session.rollback()

    return engine

connect_tcp_socket()
