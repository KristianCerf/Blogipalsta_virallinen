from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cerfkris"
db = SQLAlchemy(app)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/register")
def register():
    hash_value = generate_password_hash(password)
    sql = "INSERT INTO users (username, password, admon) VALUES (:username, :password, 0)"
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()



