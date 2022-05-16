from lib2to3.pgen2.grammar import opmap_raw
from flask import request
from pynance import portfolio_optimizer as po
import plotly.graph_objs as go
import plotly
import json


ticker_list = ['MSFT', 'PG', 'HLI']

class OptimizationMethods():

    def __init__(self, ticker_list):
        self.portfolio = po.PortfolioCalculations(ticker_list)

    def max_sharpe_return_rr(self):
        risk_return = self.portfolio.max_sharpe_portfolio('rr')
        return risk_return
    
    def max_sharpe_return_df(self):
        risk_return = self.portfolio.max_sharpe_portfolio('df')
        return risk_return
    
    def max_sharpe_return_pie(self):
        risk_return = self.portfolio.max_sharpe_portfolio('pie')
        graphJSON = json.dumps(risk_return, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

if __name__ == '__main__':
    print(OptimizationMethods(ticker_list).max_sharpe_return_df())