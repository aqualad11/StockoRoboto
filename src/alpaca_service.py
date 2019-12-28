from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import os

load_dotenv()

# Global
api = tradeapi.REST()


# Gets data for stock using it's symbol, the time of the data, and the count(how much of it)
def get_stock_data(symbol, time, count):
    barset = api.get_barset(symbol, time, limit=count)
    return barset[symbol]

# Get current value of stock
def get_value(symbol):
    data = api.get_barset(symbol, 'minute', limit=1)
    return data[symbol][0].c

# Returns account entity
def get_account():
    return api.get_account()

# Returns clock entity which contains
# if market open
# when it closes next
# current time
def get_clock():
    return api.get_clock()

# Cancels all orders
def cancel_all_orders():
    api.cancel_all_orders()

def list_positions():
    return api.list_positions()
