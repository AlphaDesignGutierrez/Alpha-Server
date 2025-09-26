import asyncio
import websockets

connected_clients = set()

# Define the connection handler function
async def handler(websocket):
    connected_clients.add(websocket)
    async for message in websocket:
        #print(f"Received message from client: {message}")
        websockets.broadcast(connected_clients, message)

# Set up and run the server
async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("WebSocket server started on ws://0.0.0.0:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())