import threading
import time
from wrapper import IBWrapper
from client import IBClient
from contract import stock
from order import limit, BUY

class IBApp(IBWrapper, IBClient):
    def __init__(self, ip, port, client_id):
        IBWrapper.__init__(self)
        IBClient.__init__(self, wrapper=self)
        self.connect(ip, port,client_id)
        thread = threading.Thread(target=self.run, daemon=True)
        thread.start()
        setattr(self, "thread", thread)
        
if __name__ == "__main__":
    app = IBApp("127.0.0.1", 7497, client_id=10)
    aapl = stock("AAPL", "SMART", "USD")
    limit_order = limit(BUY, 100, 190.00)
    time.sleep(30)
    app.disconnect()

