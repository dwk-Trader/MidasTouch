""" This user created class inherits the Order class from the 
    Interactive Brokers Python API.
"""
# This file implements custom functions to create and return Order objects using the IB API:

from ibapi.order import Order

BUY = "BUY"
SELL = "SELL"

# Function to create and return a "market" order.
def market(action, quantity):
    order = Order()
    order.action = action
    order.orderType = "MKT"
    order.totalQuantity = quantity
    return order

# Function to create and return a "limit" order.
def limit(action, quantity, limit_price):
    order = Order()
    order.action = action
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limit_price
    return order

# Function to create and return a "stop" order.
def stop(action, quantity, stop_price):
    order = Order()
    order.action = action
    order.orderType = "STP"
    order.auxPrice = stop_price
    order.totalQuantity = quantity
    return order


    