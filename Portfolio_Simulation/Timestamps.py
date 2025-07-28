""" Outside Modules """
import pandas as pd
import yfinance as yf


""" Returns a list of times from the past year  """
def times():
    
    now = pd.Timestamp.now().normalize()
    start = (now - pd.Timedelta(days=365)).normalize()

    times = pd.date_range(start=start, end=now, freq='D')
    return times 
    
    
""" Goes through every plotpoint and calculates the value for that day """
def portfolio_values(portfolio, times):
    values = []
    times = times.normalize()
    
    
    """ Gets yahoo pricing data for the year """
    start = (times.min()).normalize()
    end = (pd.Timestamp.now()).normalize()
    pricing_data = {}
    
    for stock in portfolio:
        data = yf.download(
        stock, 
        start=start, 
        end=end, 
        interval='1d', 
        progress=False,
        auto_adjust=False
        )
        data.index = data.index.normalize()
        full_index = pd.date_range(start=start, end=end, freq='D')
        data = data.reindex(full_index).ffill().bfill()

        pricing_data[stock] = data['Close']
    
    
    """ Pulls price portfolio every valid day from yahoo data """
    for date in times:
        date = pd.to_datetime(date).normalize()
        total = 0
        for stock, shares in portfolio.items():
            price = pricing_data.get(stock)   
            price.index.normalize()
            if price is not None and date in price.index:
                price_at = price.loc[price.index.asof(date)]
                if isinstance(price_at, pd.Series):
                    price_at = price_at.iloc[0]
                    total += price_at * shares
            else:
                total += 0
        values.append(round(total, 2))
        
    return values

    
