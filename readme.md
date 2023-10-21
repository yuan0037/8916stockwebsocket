#GraphQL Stock Service

This project is based on flask and SocketIO. 

## Installation

1. Clone/Download repo
2. Open the project in VS Code. 
3. In VS Code, open the Command Palette (View > Command Palette or (⇧⌘P)). Then select the Python: Create Environment command to create a virtual environment in your workspace. Select venv and then the Python environment (Python V3.x) you want to use to create it.
4. Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
| |────models/
| | |────__init__.py
| | |────stock.py
|──────app.py
|──────available_stock.py

```
5. Run the app
python app.py

6. Use the app 

Once it is launched, the GUI client can be accessied by http://127.0.0.1:5999/

Enter "AAPL" as the symbol to get real-time apple's stock price on the webpage. 

Alternatively, PostMan can be used to access the SocketIO service. 
Create a SocketIO request, and use ws://127.0.0.1:5999/ as the address. Connect first, then send a message called "get_stock_info" with the content of {"symbol":"AAPL"} as message body. A list of messages will be received with the Apple stock's real-time price/volume/min/max price. 