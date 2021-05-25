from flask import Flask ,render_template

app = Flask(__name__)

# home page
@app.route("/")
def homepage():
    return render_template("index.html",pagetitle = "ANPRecognition")

# about us page
@app.route("/about")
def about():
    return render_template("about.html",pagetitle = "About Us Page",custom_css = 'about')

# login page
@app.route("/login")
def login():
    return render_template("login.html",pagetitle = "Logging In Page",custom_css = "signup")

# signup page
@app.route("/signup")
def signup():
    return render_template("signup.html",pagetitle = "Registration Page",custom_css = "signup")

# contact page
@app.route("/contact")
def contact():
    return render_template("contact.html",pagetitle = "Contact Us Page",custom_css = "contact",custom_js = 'contact')

# run
if __name__ == "__main__":
    app.run(debug=True)