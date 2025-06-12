from flask import Flask, jsonify, make_response
from models import *
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin123@127.0.0.1:5432/hospital"

db.init_app(app)

migrations = Migrate(app,db)

@app.route("/")
def index():
    return "<h1>Welcome to our Hospital.</h1>"

@app.route("/doctors")
def doctors():
    doctors = Doctor.query.all()
    res = {}
    if doctors:
        stat = 200
        for doctor in doctors:
            res[doctor.id] = doctor.to_dict()
    else:
        res = {
            "Message": "Doctors not found"
        }
        stat = 404
    # print([doctor for doctor in Doctor.query.all()])
    return make_response(res, stat)


if __name__ == '__main__':
    app.run(port=5555, debug=True)