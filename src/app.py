from flask import Flask
from views.auth.tutee_auth import tutee_auth_routes

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


app.register_blueprint(tutee_auth_routes)

if __name__ == '__main__':
    app.run()
