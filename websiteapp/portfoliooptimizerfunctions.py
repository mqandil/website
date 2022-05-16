from lib2to3.pgen2.grammar import opmap_raw
from flask import request
from pynance import portfolio_optimizer as po

ticker_list = ['MSFT', 'PG', 'HLI']

class OptimizationMethods():

    def __init__(self, ticker_list):
        self.portfolio = po.PortfolioCalculations(ticker_list)

    def max_sharpe_return_rr(self):
        risk_return = self.portfolio.max_sharpe_portfolio('rr')
        print(risk_return)
    
    def max_sharpe_return_df(self):
        risk_return = self.portfolio.max_sharpe_portfolio('df')
        print(risk_return)
    
    def max_sharpe_return_pie(self):
        risk_return = self.portfolio.max_sharpe_portfolio('pie')
        print(risk_return)

if __name__ == '__main__':
    print(OptimizationMethods(ticker_list).max_sharpe_return_pie())