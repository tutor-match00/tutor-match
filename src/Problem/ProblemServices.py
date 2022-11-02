from flask import Blueprint, request
from flask_cors import CORS
problem_routes = Blueprint('problem_routes', __name__)
CORS(problem_routes)


@problem_routes.route('/problems/', methods=['POST'])
def enterProblem():
    content_type = request.headers.get("Content-Type")
    # making sure that the content type is json
    if content_type == "application/json":
        try:
            request_data = request.json
        except Exception as e:
            return ({
                "status": False,
                "message": f"Error: {e}",
            }, 400)

        try:
            course = request_data["course"]
            topic = request_data["topic"]
            problem_description = request_data["problem_description"]
        except Exception as e:
            return ({
                "status": False,
                "message": f"Error: {e}",
            }, 400)

        problem_info = {
            "course": course,
            "topic": topic,
            "problem_description": problem_description
        }

        print(problem_info)

        return ({
            "status": True,
            "message": "Problem successfully entered",
        }, 200)
