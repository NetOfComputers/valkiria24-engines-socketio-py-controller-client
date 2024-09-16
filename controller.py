import socketio
import os

# Secret key to sign JWT tokens (must be kept secret)
TOKEN = os.getenv('CONTROLLER_TOKEN')
if not TOKEN:
    raise ValueError("No TOKEN set for CONTROLLER")
# Create a new Socket.IO client instance
sio = socketio.Client()

# Event handler for server connection
@sio.event
def connect():
    print('Connected to server')
    # Send the TOKEN when registering the controller
    sio.emit('register_controller', TOKEN)

# Event handler for server disconnection
@sio.event
def disconnect():
    print('Disconnected from server')

# Event handler to receive commands from server
@sio.event
def command(data):
    print(f'Received command: {data}')

# Connect to the server
try:
    sio.connect('http://95.217.178.151:5000')
except Exception as e:
    print(f"Connection failed: {e}")

# Example of sending a command
try:
    while True:
        command = input('Enter command to send: ')
        if command.strip().lower() == 'exit':
            break
        # Send the command to the server
        sio.emit('send_command', command)
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    sio.disconnect()
