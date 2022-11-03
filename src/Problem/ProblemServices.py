from flask import Blueprint, request
from Problem.ProblemModel import Problem
from Tutor.TutorModel import Tutor
from Tutee.TuteeModel import Tutee

from flask_cors import CORS
problem_routes = Blueprint('problem_routes', __name__)
CORS(problem_routes)


@problem_routes.route('/problems/', methods=['GET'])
def getProblems():
    from app import session

    if request.args.get("tutor_id"):
        try:
            tutor_id = int(request.args.get("tutor_id"))
            tutor = session.query(Tutor).filter_by(id=tutor_id).first()
            problems = session.query(Problem).filter(
                (Problem.course_tag == tutor.course_tag), (Problem.status == False)).all()
            print(tutor.course_tag)
            return {
                "status": True,
                "msg": [{
                    "id": problem.id,
                    "title": problem.title,
                    "description": problem.description,
                    "course_tag": problem.course_tag,
                    "status": problem.status,
                    "tutee": {
                        "id": problem.tutee.id,
                        "name": f"{problem.tutee.first_name} {problem.tutee.last_name}",
                        "whatsapp_number": problem.tutee.whatsapp_number,
                    } if problem.tutee else None,
                    "tutor": {
                        "id": problem.tutor.id,
                        "name": f"{problem.tutor.first_name} {problem.tutor.last_name}",
                        "whatsapp_number": problem.tutor.whatsapp_number,
                    } if problem.tutor else None,
                } for problem in problems]
            }
        except Exception as e:
            return {
                "status": False,
                "msg": f"Error getting problems - {e}"
            }
    elif request.args.get("tutee_id"):
        try:
            tutee_id = int(request.args.get("tutee_id"))
            problems = session.query(Problem).filter(
                Problem.tutee_id == tutee_id).all()
            print(problems)
            return {
                "status": True,
                "msg": [{
                    "id": problem.id,
                    "title": problem.title,
                    "description": problem.description,
                    "course_tag": problem.course_tag,
                    "status": problem.status,
                    "tutee": {
                        "id": problem.tutee.id,
                        "name": f"{problem.tutee.first_name} {problem.tutee.last_name}",
                        "whatsapp_number": problem.tutee.whatsapp_number,
                    } if problem.tutee else None,
                    "tutor": {
                        "id": problem.tutor.id,
                        "name": f"{problem.tutor.first_name} {problem.tutor.last_name}",
                        "whatsapp_number": problem.tutor.whatsapp_number,
                    } if problem.tutor else None
                } for problem in problems]
            }
        except Exception as e:
            return {
                "status": False,
                "msg": f"Error getting problems - {e}"
            }
    else:
        try:
            problems = session.query(Problem).all()
        except Exception as e:
            return {
                "status": False,
                "msg": f"Error getting problems - {e}"
            }
        return {
            "status": True,
            "msg": [{
                "id_problem": problem.id,
                "title": problem.title,
                "description": problem.description,
                "course_tag": problem.course_tag,
                "status": problem.status,
                "tutee_id": problem.tutee_id,
                "tag_id": problem.tag_id,
                "tutor_id_tutor": problem.tutor_id_tutor

            } for problem in problems]
        }


@problem_routes.route('/problems/', methods=['POST'])
def enterProblem():
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
            course_tag = request_data["course_tag"]
            title = request_data["title"]
            description = request_data["description"]
            tutee_id = request_data["tutee_id"]
        except Exception as e:
            return ({
                "status": False,
                "msg": f"Error: {e}",
            }, 400)

        try:
            new_problem = Problem(course_tag=course_tag, title=title,
                                  description=description, tutee_id=tutee_id, status=False)
            session.add(new_problem)
            session.commit()
        except Exception as e:
            session.rollback()
            return ({
                "status": False,
                "msg": f"Error: {e}",
            }, 400)

        return ({
            "status": True,
            "msg": "Problem successfully entered",
        }, 200)


@problem_routes.route('/problems/', methods=['PUT'])
def updateProblem():
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
            id_problem = request_data["problem_id"]
            tutor_id = request_data["tutor_id"]
            status = request_data["status"]
        except Exception as e:
            return ({
                "status": False,
                "msg": f"Error: {e}",
            }, 400)

        try:
            problem = session.query(Problem).get(id_problem)
            problem.status = status
            problem.tutor_id = tutor_id
            session.commit()
        except Exception as e:
            session.rollback()
            return ({
                "status": False,
                "msg": f"Error: {e}",
            }, 400)

        return ({
            "status": True,
            "msg": "Problem successfully updated",
        }, 200)
