import common
import socket

AGENT = "Bob"

keys = common.read_keys(AGENT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
    connection.connect((common.HOST, common.PORT))
    print("\nBob connected with Alice\n")

    sequence_number = common.receive(AGENT, connection, keys) + 1
    
    common.send(AGENT, connection, keys, b"Hello Alice", sequence_number)

    sequence_number = common.receive(AGENT, connection, keys, sequence_number) + 1
    
    common.send(AGENT, connection, keys, b"Me too. Same time, same place?", sequence_number)

    sequence_number = common.receive(AGENT, connection, keys, sequence_number) + 1

print("Bob disconnected from Alice")
