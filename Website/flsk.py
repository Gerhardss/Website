from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
         # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
            
        # Here you can process the message, send emails, save to database, etc.
        # For this example, let's just print the data to the console
        print(f"Name: {name}, Email: {email}, Message: {message}")

        # Optionally, you can redirect the user to a thank you page
        return render_template("thank_you.html", name=name)

    return render_template("contact.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Get form data
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Here you would typically validate the user's credentials
        # For this example, let's assume the user is valid
        
        # Redirect the user to their account page
        return redirect(url_for('account', name=username))
        
    return render_template("login.html")

@app.route("/account/<name>")
def account(name):
    # Render the account page with the user's name
    return render_template("account.html", name=name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
