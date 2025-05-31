from flask import Flask, render_template, request, session
from datafile import filename
from classes.customer import Customer
from classes.orderproduct import OrderProduct
from classes.category import Category
from classes.product import Product
from classes.customerorder import CustomerOrder
from classes.userlogin import Userlogin
from subs.apps_gform import apps_gform
from subs.apps_subform import apps_subform
from subs.apps_plot import apps_plot
from subs.apps_plotly import apps_plotly
from subs.apps_userlogin import apps_userlogin

app = Flask(__name__)

Category.read(filename + 'trabalho.db')
OrderProduct.read(filename + 'trabalho.db')
Customer.read(filename + 'trabalho.db')
Product.read(filename + 'trabalho.db')
CustomerOrder.read(filename + 'trabalho.db')
Userlogin.read(filename + 'trabalho.db')
app.secret_key = 'BAD_SECRET_KEY'
@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")
@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))
@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname):
    return apps_gform(cname)
@app.route("/subform/<cname>", methods=["post","get"])
def subform(cname):
    return apps_subform(cname)
@app.route("/plot", methods=["post","get"])
def plot():
    return apps_plot()
@app.route("/plotly", methods=["post","get"])
def plotly():
    return apps_plotly()
@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    return apps_userlogin()
if __name__ == '__main__':
    app.run()

