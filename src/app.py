from flask import Flask
from Problem.ProblemServices import problem_routes
from flask_cors import CORS

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


app.register_blueprint(problem_routes)

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)
