import common
import socket

AGENT = "Alice"

keys = common.read_keys(AGENT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((common.HOST, common.PORT))
    s.listen()
    connection, address = s.accept()
    with connection:
        print("\nAlice connected with Bob\n")
        
        sequence_number = 1

        common.send(AGENT, connection, keys, b"Hello Bob", sequence_number)

        sequence_number = common.receive(AGENT, connection, keys, sequence_number) + 1

        common.send(AGENT, connection, keys, b"I would like to have dinner", sequence_number)

        sequence_number = common.receive(AGENT, connection, keys, sequence_number) + 1

        common.send(AGENT, connection, keys, b"Sure!", sequence_number)

print("Alice disconnected from Bob")
