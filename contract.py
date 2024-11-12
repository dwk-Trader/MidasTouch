# This file has custom functions for creating different types of contracts.
# At this time it has only the function for creating a stock contract.

from ibapi.contract import Contract

def stock(symbol, exchange, currency):
    contract = Contract()
    contract.symbol = symbol
    contract.exchange = exchange
    contract.currency = currency
    contract.secType = "STK"
    return contract

