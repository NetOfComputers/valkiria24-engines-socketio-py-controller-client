import socketio

# Create a new Socket.IO client instance
sio = socketio.Client()

# Event handler for server connection
@sio.event
def connect():
    print('Connected to server')
    sio.emit('register_controller')

# Event handler to receive commands from server
@sio.event
def command(data):
    print(f'Received command: {data}')

# Connect to the server
sio.connect('http://95.217.178.151:5000')

# Example of sending a command
while True:
    command = input('Enter command to send: ')
    sio.emit('send_command', command)
