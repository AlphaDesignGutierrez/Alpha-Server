import asyncio
import websockets
import os

PORT = int(os.environ.get("PORT", 8765))
HOST = "0.0.0.0"
connected_clients = set()

# Define the connection handler function
async def handler(websocket):
    #uri = "wss://alpha-server.koyeb.app/"
    connected_clients.add(websocket)
    #try:
    #async with websockets.connect(uri) as websocket:
    try:
        async for message in websocket:
            print(f"client: {message}")
            lists = connected_clients
            lists.remove(websocket)
            websockets.broadcast(lists, message)

    except Exception as e:
        print(e)
    #finally:
        #connected_clients.remove(websocket)

# Set up and run the server
async def main():
    async with websockets.serve(handler, HOST, PORT):
        print(f"WebSocket server started on {PORT}")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":

    asyncio.run(main())





