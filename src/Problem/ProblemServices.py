from flask import Blueprint,request
import Problem
from flask_cors import CORS
problem_routes = Blueprint('problem_routes', __name__)
CORS(problem_routes)


@problem_routes.route('/problems/', methods=['GET'])
def get_all_problems():
    from app import session
    try:
        problems = session.query(Problem).all()
    except:
        pass
        
    return {
        'problems': "Hello World"
    }
