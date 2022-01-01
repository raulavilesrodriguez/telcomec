import os

from sqlalchemy import create_engine, Table, MetaData
from flask import Flask, flash, redirect, render_template, request, session, Markup, url_for
from flask_session import Session
from tempfile import mkdtemp
from login import login_required
from werkzeug.security import check_password_hash, generate_password_hash
import numpy as np


# Configure application
app = Flask(__name__)
app.secret_key = 'es_una_clave_secreta'
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure to use SQLite database
db = create_engine("sqlite:///telecoec.db")
metadata = MetaData(bind=db)
users = Table('users', metadata, autoload=True)
services = Table('services', metadata, autoload=True)


@app.route("/")
@login_required
def index():

    # Get logged in username
    user_id = session["user_id"]

    name_user = db.execute("SELECT username FROM users WHERE id = ?", user_id)
    name_user = name_user.fetchall()
    usuario = name_user[0]["username"]

    # Get data from services table
    data = db.execute("SELECT * FROM services")
    data = data.fetchall()

    # Get the different data series
    x = []
    sma = []
    fixed_phone = []
    fixed_internet = []
    mobile_internet = []
    portador_enlaces = []
    audio_video = []

    for i in range(len(data)):
        x.append(data[i]["Fecha"])
        sma.append(data[i]["SMA"])
        fixed_phone.append(data[i]["telefonia_fija"])
        fixed_internet.append(data[i]["Internet_Fijo"])
        mobile_internet.append(data[i]["Internet_Movil"])
        portador_enlaces.append(data[i]["Portadores_Enlaces"])
        audio_video.append(data[i]["AVS"])

    # Send updated information on services to index.html
    return render_template('index.html', x=x, sma=sma, fixed_phone=fixed_phone,
                           fixed_internet=fixed_internet, mobile_internet=mobile_internet,
                           portador_enlaces=portador_enlaces, audio_video=audio_video, usuario=usuario)


@app.route("/update", methods=["GET", "POST"])
@login_required
def update():

    # Get logged in username
    user_id = session["user_id"]

    name_user = db.execute("SELECT username FROM users WHERE id = ?", user_id)
    name_user = name_user.fetchall()
    usuario = name_user[0]["username"]

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if not request.form.get("service1"):
            flash("You must select the two services to compare!")
            return render_template("update.html")

        if not request.form.get("service2"):
            flash("You must select the two services to compare!")
            return render_template("update.html")

        service1 = request.form.get("service1")
        service2 = request.form.get("service2")

        # Obtain information service1
        data1 = db.execute("SELECT * FROM services")
        data1 = data1.fetchall()

        x = []
        datos1 = []

        for i in range(len(data1)):
            x.append(data1[i]["Fecha"])
            datos1.append(data1[i][service1])

        # Obtain information service2
        data2 = db.execute("SELECT * FROM services")
        data2 = data2.fetchall()

        datos2 = []

        for i in range(len(data2)):
            datos2.append(data2[i][service2])

        versus = "versus"
        densidad = "Density"

        # Obtain the correlation of two series
        r = np.corrcoef(datos1[15:20], datos2[15:20])
        correlacion = r[0, 1]

        # Get tacc compound annual growth rate
        tacc_datos1 = (((datos1[19]/datos1[14])**0.2) - 1) * 100
        tacc_datos2 = (((datos2[19]/datos2[14])**0.2) - 1) * 100

        # Get the values of the last year
        datos1_last = datos1[19]
        datos2_last = datos2[19]

        # Get the density of the service
        density1 = (datos1[19]/data1[19]["POBLACION"]) * 100
        density2 = (datos2[19]/data2[19]["POBLACION"]) * 100

        # Get the history of the density
        historic_density1 = []
        historic_density2 = []

        for i in range(len(data1)):
            density = round((data1[i][service1]/data1[i]["POBLACION"]) * 100)
            historic_density1.append(density)

        for i in range(len(data2)):
            density = round((data2[i][service2]/data1[i]["POBLACION"]) * 100)
            historic_density2.append(density)

        # Redirect user to home page
        return render_template("update.html",
                               x=x, datos1=datos1, datos2=datos2, label1=service1, label2=service2,
                               versus=versus, correlacion=correlacion, tacc_datos1=tacc_datos1,
                               tacc_datos2=tacc_datos2, datos1_last=datos1_last, datos2_last=datos2_last,
                               density1=density1, density2=density2, historic_density1=historic_density1,
                               historic_density2=historic_density2, densidad=densidad, usuario=usuario)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("update.html", usuario=usuario)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Must provide username!")
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password!")
            return render_template("login.html")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        rows = rows.fetchall()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("invalid username and/or password")
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username is sent
        if not request.form.get("username"):
            flash("Must provide username!")
            return render_template("register.html")

        # Ensure password is sent
        elif not request.form.get("password"):
            flash("Must provide username!")
            return render_template("register.html")

        # Ensure confirmation is sent
        elif not request.form.get("confirmation"):
            flash("It is necessary to confirm your password")
            return render_template("register.html")

        # Show message if password and confirmation are not the same
        elif not request.form.get("password") == request.form.get("confirmation"):
            flash("PASSWORDS DO NOT MATCH")
            return render_template("register.html")

        # Get username, password and confirmation values
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check if user exists,
        row = db.execute("SELECT * FROM users WHERE username = ?", username)
        row = row.fetchall()
        if len(row) == 1:
            flash("User already exists")
            return render_template("register.html")

        # To check password conditions
        validation = True

        # Require users’ passwords to have some number of letters
        if len(password) < 5:
            flash("Length should be at least 4!")
            return render_template("register.html")
            validation = False

        # The user'passwords have at least one number
        if not any(char.isdigit() for char in password):
            flash("Password should have al least one numeral")
            return render_template("register.html")
            validation = False

        # Requires that the user'passwords have at least one uppercase letter
        if not any(char.isupper() for char in password):
            flash("Password should have at least one uppercase letter")
            return render_template("register.html")
            validation = False

        # If validation is TRUE continue with the registration
        elif validation:

            # Insert the value of the new registered user and his password
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username,
                       generate_password_hash(password, 'pbkdf2:sha256', salt_length=8))

            # Remember which user has logged in
            new_user = db.execute("SELECT * FROM users WHERE username = ?", username)
            new_user = new_user.fetchall()
            session["user_id"] = new_user[0]["id"]

            # Redirect user to home page
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


if __name__ == '__main__':
    app.run_server(debug=True)

