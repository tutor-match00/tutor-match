from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from Tutor.TutorModel import Tutor
from flask_cors import CORS
tutor_routes = Blueprint("tutor_routes", __name__)
CORS(tutor_routes)


@tutor_routes.route('/tutor/signup/', methods=['POST'])
def signup():
    content_type = request.headers.get("Content-Type")
    # making sure that the content type is json
    if content_type == "application/json":
        from app import session
        try:
            request_data = request.json
        except Exception as e:
            return ({
                "status": False,
                "msg": f"Error: {e}",
            }, 400)

        try:

            first_name = request_data["first_name"]
            last_name = request_data["last_name"]
            password = request_data["password"]
            email = request_data["email"]
            course_tag = request_data["course_tag"]
            whatsapp_number = request_data["whatsapp_number"]
        except Exception as e:
            return ({
                "status": False,
                "msg": f"Error: {e}",
            }, 400)

        try:
            passwordHash = generate_password_hash(password)
            newTutee = Tutor(first_name=first_name, last_name=last_name, user_email=email,
                             user_password=passwordHash, whatsapp_number=whatsapp_number)
            session.add(newTutee)
            session.commit()

            if (check_password_hash(passwordHash, password)):
                the_tutee = session.query(Tutor).filter(
                    Tutor.user_email == email).first()

                return ({
                    "status": True,
                    "msg": {
                        "id": the_tutee.id,
                    },
                }, 200)
            else:
                return ({
                    "status": False,
                    "msg": "Error: Passwords do not match",
                }, 400)

        except Exception as e:
            session.rollback()
            return ({
                "status": False,
                "msg": f"Error: {e}",
            }, 400)


@tutor_routes.route('/tutor/login/', methods=['POST'])
def login():
    content_type = request.headers.get("Content-Type")
    # making sure that the content type is json
    if content_type == "application/json":
        from app import session
        try:
            request_data = request.json
        except Exception as e:
            return ({
                "status": False,
                "msg": f"Error: {e}",
            }, 400)

        try:
            password = request_data["password"]
            email = request_data["email"]
        except Exception as e:
            return ({
                "status": False,
                "msg": f"Error: {e}",
            }, 400)

        try:
            passwordHash = generate_password_hash(password)
            tutor_id = session.query(Tutor.id).filter(
                Tutor.user_email == email, Tutor.user_password == check_password_hash(passwordHash, password)).first()
            tutorIn = session.query(Tutor).get(tutor_id)
        except Exception as e:
            session.rollback()
            return ({
                "status": False,
                "msg": f"Error: {e}",
            }, 400)

        return ({
            "status": True,
            "msg": {
                "id": tutorIn.id,
            },
        }, 200)
