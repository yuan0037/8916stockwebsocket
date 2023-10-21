# https://www.educba.com/flask-websocket/
# https://flask-socketio.readthedocs.io/en/latest/getting_started.html

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import random
from available_stock import stocks
import json
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)

socketio = SocketIO(logger=True, engineio_logger=True)
socketio.init_app(app)

class DynamicJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__dict__'):
            # If the object has a '__dict__' attribute, assume it's a custom class.
            return obj.__dict__
        return super().default(obj)

def update_stock_data(stock):
    stock.current_price = round(random.uniform(10, 500.0), 2)
    stock.volume = random.randint(1, 5000)
    stock.update_min_price(stock.current_price)
    stock.update_max_price(stock.current_price)
    return stock

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('get_stock_info')
def handle_update_request(data):    
    stock_matching = [s for s in stocks if s.symbol.lower() ==  data['symbol'].lower()]
    stock_found = None
    if len(stock_matching) > 0:
        stock_found = stock_matching[0]
        for i in range(0, 10):
            stock_found = update_stock_data(stock_found)
            emit('get_stock_info', json.dumps(stock_found, cls=DynamicJSONEncoder))
            socketio.sleep(1)
    else:
        emit('get_stock_info', {'error': 'Stock not found'})

@socketio.on('connect')
def test_connect():
    socketio.emit('after connect', {'data':'Let us learn Web Socket in Flask'})
    
if __name__ == "__main__":
    pywsgi.WSGIServer(("", 5999), app, handler_class=WebSocketHandler).serve_forever()