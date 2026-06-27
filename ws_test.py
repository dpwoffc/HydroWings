from websocket import create_connection

ws = create_connection("ws://127.0.0.1:8081/console/testbot")

while True:
    print(ws.recv())
