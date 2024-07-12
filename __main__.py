from flask import Flask, render_template

app=Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/user_dashboard", methods=["GET"])
def user_dashboard(): 
    return "<h1>This is the user dashboard</h1>"

@app.route("/admin_login", methods = ["GET", "POST"])
def admin_login(): 

    return render_template("admin/admin_login.html")


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=8085)