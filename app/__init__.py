from flask import Flask, request, redirect, render_template, session
import db

app = Flask(__name__)
app.secret_key = "foo"

@app.route("/")
def index():
    """
    Displays the default page of the website
    """
    return render_template("index.html")

@app.route("/signup", methods=['POST'])
def signup():
    """
    Retrieves user inputs from signup page.
    Checks it against the database to make sure the information is unique.
    Adds information to the "users" database table.
    """
    user = request.form["newusername"]
    pwd = request.form["newpassword"]
    if user.strip() == "" or pwd.strip == "":
        return render_template("index.html", explain="Username or Password cannot be blank")
    # Add user information if passwords match
    if (request.form["newpassword"] != request.form["newpassword1"]):
        return render_template("index.html", explain="The passwords do not match")

    register_success = db.register_user(user, pwd) #returns whether or not user was registered
    if not register_success:
        return render_template("index.html", explain="Username already exists")
    else:
        return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    """
    Retrieves user login inputs and checks it against the "users" database table.
    Brings user to home page after successful login.
    """
    user = request.form["username"]
    pwd = request.form["password"]

    if user.strip() == "" or pwd.strip() == "":
        return render_template("index.html", explain1 = "Username or Password cannot be blank")

    user_id = db.fetch_user_id(user, pwd) # None when no user_id exists for that user and pwd
    if user_id is None:
        return render_template("index.html", explain1 = "Username or Password is incorrect")
    # Adds user and user id to session if all is well
    session["user"] = db.fetch_username(user_id)
    session["user_id"] = user_id
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
	app.debug = True
	app.run()