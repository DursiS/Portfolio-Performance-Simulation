""" Outside Modules """
import yfinance as yf
import numpy as np
import pandas as pd


""" Only returns the price today """
def current_price(ticker):
    ticker = yf.Ticker(f"{ticker}")
    latest = ticker.history(period="1d")["Close"].iloc[-1]
    return latest


""" Only returns the portfolio value for today """
def portfolio_total(portfolio):
    total = 0
    for stock in portfolio:
        total += current_price(stock) * portfolio[stock]
    total = round(total, 2)
    print(f"Current Value: {total} $")
    return total
    
    
""" Dictionnary of stocks and their total value """
def stock_to_total(portfolio):
    stock_to_total = {}
    for stock in portfolio:
        
        total = current_price(stock) * portfolio[stock] 
        total = round(total, 2)
        
        stock_to_total[stock] = total # Adds corresponding total
    return stock_to_total


""" Makes the labels for the pie chart """
def price_label(stock_to_total):
    pricing_label = []
    for stock in stock_to_total:
        price = stock_to_total[stock]
        label = f"{stock} {price}$"
        pricing_label.append(label)
    return pricing_label 
   

    
    