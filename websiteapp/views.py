from datetime import datetime
from flask import Flask, render_template, request
from . import app
from . import auto_remote
from IPython.display import display
from . import portfoliooptimizerfunctions

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

###################AUTO REMOTE###########################
@app.route("/auto-remote/")
def auto_remote_viewer():
    return render_template(
        'auto_remote.html'
    )

@app.route("/auto-remote/live-situation/", methods=['GET', 'POST'])
def auto_remote_live_sit_viewer():
    live_situation_info = auto_remote.GetPyRemote().get_live_situation()

    return render_template(
        'auto_remote_live.html', data = live_situation_info.to_html(index=False)
    )

@app.route("/auto-remote/interest-index/", methods=['GET', 'POST'])
def auto_remote_interest_index_viewer():
    interest_index_info = auto_remote.GetPyRemote().get_interest_index()

    return render_template(
        'auto_remote_live.html', data = interest_index_info.to_html(index=False)
    )

@app.route("/auto-remote/ii-calculations/", methods=['GET', 'POST'])
def auto_remote_ii_calculations_viewer():
    ii_calculations_info = auto_remote.GetPyRemote().get_ii_calculations()

    return render_template(
        'auto_remote_live.html', data = ii_calculations_info.to_html(index=False)
    )

###################PORTFOLIO OPTIMIZER###########################

@app.route("/portfolio_optimizer/", methods=["GET", "POST"])
def portfolio_optimizer_home():
    if request.method == 'POST':
        tickers = request.form['ticker_list'].upper()
        ticker_list = tickers.split(', ')
        # data = portfoliooptimizerfunctions.OptimizationMethods(ticker_list).max_sharpe_return_df().to_html()
        data = portfoliooptimizerfunctions.OptimizationMethods(ticker_list).max_sharpe_return_pie()
        return render_template('portfolio_optimizer_home.html', data=data)

    return render_template(
        'portfolio_optimizer_home.html'
    )

@app.route('/portfolio_optimizer/max_sharpe_portfolio/', methods=["GET", "POST"])
def portfolio_opt_home():
    ticker_list = []
    if request.method == 'POST':
           ticker_list = request.form['ticker_list']

    return render_template(
        'portfolio_optimizer_max_sharpe.html',
        data = ticker_list
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

