from base import Base
import os
from flask import Flask
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from Problem.ProblemServices import problem_routes
from Tutee.TuteeService import tutee_routes
from Tutor.TutorService import tutor_routes

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

engine = create_engine("mysql+pymysql://sql8538126:INUluUg1VU@sql8.freesqldatabase.com:3306/sql8538126",
                       pool_pre_ping=True, pool_size=20, max_overflow=10)  # establish a connection with the database
Session = sessionmaker(bind=engine)
session = Session()
meta = MetaData()


# App Blueprint


# Database Connection
try:
    engine.connect()
    Base.metadata.create_all(engine)
    session.commit()
    print("Database Successfully Connected")
except Exception as e:
    print('Database connection failed: %s' % (e))
    session.rollback()
finally:
    session.close()


@app.route('/', methods=["GET"])
def hello():
    return 'Hello, World!'


app.register_blueprint(problem_routes)
app.register_blueprint(tutee_routes)
app.register_blueprint(tutor_routes)


if __name__ == '__main__':
    app.run(debug=True)
