from datetime import datetime
from flask import Flask, render_template, request
from . import app
from . import auto_remote
from IPython.display import display

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route('/hello/')
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/auto-remote/")
def auto_remote_viewer():
    return render_template(
        'auto_remote.html'
    )

@app.route("/auto-remote/live-situation/", methods=['GET', 'POST'])
def auto_remote_live_sit_viewer():
    live_situation_info = auto_remote.GetPyRemote().get_live_situation()

    return render_template(
        'auto_remote_live.html', live_situation = live_situation_info.to_html(index=False)
    )

@app.route("/portfolio_optimizer/")
def portfolio_optimizer_home():
    return render_template(
        'portfolio_optimizer_home.html'
    )

@app.route('/portfolio_optimizer/max_sharpe_portfolio/', methods=["GET", "POST"])
def portfolio_opt_home():
    return render_template(
        'portfolio_optimizer_max_sharpe.html'
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

