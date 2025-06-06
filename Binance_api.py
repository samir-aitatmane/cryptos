import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    price = data['p']
    volume = data['q']
    print(f"Prix : {price} | Volume : {volume}")

def on_error(ws, error):
    print("Erreur :", error)

def on_close(ws):
    print("Connexion fermée")

def on_open(ws):
    print("Connexion établie")

# BTC/USDT trade stream
socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"

ws = websocket.WebSocketApp(socket,
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()
