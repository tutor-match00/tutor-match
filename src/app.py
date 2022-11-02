from flask import Flask
from Problem.ProblemServices import problem_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["POST"])
def hello():
    return 'Hello, World!'


app.register_blueprint(problem_routes)

if __name__ == '__main__':
    app.run(debug=True)
