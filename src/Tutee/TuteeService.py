from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from Tutee.TuteeModel import Tutee
from flask_cors import CORS
tutee_routes= Blueprint("tutee_routes", __name__)
CORS(tutee_routes)

@tutee_routes.route('/tutee/', methods=['POST'])
def signup():
    from app import session
    content_type = request.headers.get("Content-Type")
    # making sure that the content type is json
    print(content_type)
    print(request.json)
    return {
        "g":"gg"
    }

    # if content_type == "application/json":
    #     print("here")
    #     print(request.__dict__)
    #     if request.method == "POST":
    #         print(request.get_json())
    #     print(request.json)
    #     try:
    #         request_data = request.get_json()
    #         print(request)
    #         first_name = request_data["first_name"]
    #         last_name = request_data["last_name"]
    #         user_email = request_data["user_email"]
    #         user_password = request_data["user_password"]
    #         whatsapp_number = request_data["whatsapp_number"]
    #         passwordHash = generate_password_hash(user_password)
    #     except Exception as e:
    #         return ({
    #             "status": False,
    #             "message": f"Error: {e}",
    #         }, 400)

        
    #     newTutee = Tutee(first_name=first_name, last_name=last_name, user_email=user_email, user_password=passwordHash,
    #                                     whatsapp_number=whatsapp_number)
    #     print(newTutee)
    #     try:
    #         session.add(newTutee)
    #         session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         return ({
    #             'status': False,
    #             'msg': {
    #                 "dev_message": (f"{e}"),
    #                 "message": "Connection Error: User not recorded"
    #             }
    #     }), 400