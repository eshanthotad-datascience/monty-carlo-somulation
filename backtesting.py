import yfinance as yf3

stocks = [
    "RELIANCE.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "INFY.NS",
    "CIPLA.NS",
    
]

data = yf.download(stocks, period="1y")
close_data = data["Close"]
close_data.to_excel("data.xlsx")

