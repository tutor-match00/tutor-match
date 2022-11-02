from flask import render_template, Blueprint

tutee_auth_routes = Blueprint(
    "tutee_login", __name__, template_folder="./src/templates")


@tutee_auth_routes.route('/tutee_login/')
def tutee_login():
    return render_template('tutee_login.html')
