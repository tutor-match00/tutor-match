from flask import Blueprint,request
from Problem.ProblemModel import Problem
from Tutor.TutorModel import Tutor

from flask_cors import CORS
problem_routes = Blueprint('problem_routes', __name__)
CORS(problem_routes)


@problem_routes.route('/problems/', methods=['GET'])
def get_all_problems():
    from app import session
    try:
        problems = session.query(Problem).all()
        print(problems)
    except:
        pass
        
    return {
        'problems': "Hello World"
    }

@problem_routes.route('/problem/<tagId>', methods=['GET'])
def tutorMatch(tagId):
    from app import session
    try:
        problem_match = session.query(Problem).filter(Problem.status==1 and Problem.tag_id == tagId).first()
        tutor = session.query(Tutor).filter(Tutor.tag_id == tagId and Tutor.status == 1).first()
        if(tutor):
            return ({
            "status": True,
            "msg": {
                "id_problem": problem_match.id,
                "title": problem_match.title,
                "description": problem_match.description,
                "tutor_name": tutor.first_name + tutor.last_name,
                "tutor_whatsapp": tutor.whatsapp_number
            }            
            }),200
        else:
            return ({
            "status": False,
            "msg": "No tutor available"      
            }),200
        
    except Exception as e:
        return  ({
                 'status': False,
                 'msg':{
                        "dev_message" : (f"{e}"),
                        "message":"Error"
                        }
                }),400
        


@problem_routes.route('/problem/<tuteeId>', methods=['GET'])
def tuteeProblems(tuteeId):
    from app import session
    try:
        problems = session.query(Problem).filter(Problem.tutee_id == tuteeId ).all()
        print(problems)
        return {
            'status': True,
            "msg" : [{
                "id_problem": problem.id,
                "title": problem.title,
                "description": problem.description,
            } for problem in problems
            ]}
    except Exception as e:
                session.rollback()  
                return  ( {
                'msg': {
                    "message": "Connection Error: Unable to register hospital",
                    "dev_message": (f"{e}"),
                    
                },
                "status": False
            }),400

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
            try: 
                session.add(newHospital)
                session.commit()
            except Exception as e:
                session.rollback()  
                return  ( {
                'msg': {
                    "message": "Connection Error: Unable to register hospital",
                    "dev_message": (f"{e}"),
                    
                },
                "status": False
            }),400
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
