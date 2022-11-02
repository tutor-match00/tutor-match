from flask import Blueprint
from flask_cors import CORS
# from Problem.Problem import Problem

problem_routes = Blueprint('problem_routes', __name__)
CORS(problem_routes)


@problem_routes.route('/problems/', methods=['POST'])
def get_all_problems():
    return {
        'problems': "Hello World"
    }
