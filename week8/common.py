from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

FILE = "pw"
HOST = "127.0.0.1"
PORT = 2000

def check_sequence_number(agent, received, sent):
    if received > sent:
        print(f"{agent} validated sequence number {received} because it is greater than {sent}")
    else:
        print(f"ERROR: {agent} tried to validate sequence number {received} but it less than or equal to {sent}")

def encrypt(agent, key, plaintext, nonce):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    print(f"{agent} encrypted {plaintext} to {ciphertext}")
    return ciphertext

def decrypt(agent, key, ciphertext, nonce):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    print(f"{agent} decrypted {ciphertext} to {plaintext}")
    return plaintext

def read_keys(agent):
    with open(FILE, "rb") as f:
        keys = f.read()
    encryption_key = keys[:16]
    authentication_key = keys[16:]
    print(f"{agent} read encryption key of {len(encryption_key)} bytes: {encryption_key}")
    print(f"{agent} read authentication key of {len(authentication_key)} bytes: {authentication_key}")
    return (encryption_key, authentication_key)

def receive(agent, connection, keys, last_sequence_number_sent = 0):
    message = connection.recv(1024)
    signature = message[-32:]                                                               # HMAC-SHA256 - 32 bytes
    nonce = message[-48:-32]                                                                # AES-128-CTR - 16 bytes
    ciphertext = message[1:-48]
    sequence_number = message[0]
    print(f"{agent} received {message} with sequence number {sequence_number}")
    check_sequence_number(agent, sequence_number, last_sequence_number_sent)
    verify(agent, keys[1], sequence_number.to_bytes(1, "big") + ciphertext, signature)      # 1. MAC
    plaintext = decrypt(agent, keys[0], ciphertext, nonce)                                  # 2. Decrypt
    print(f"{agent} read {plaintext}\n")
    return sequence_number

def send(agent, connection, keys, plaintext, sequence_number):
    print(f"{agent} wants to send {plaintext} with sequence number {sequence_number}")
    nonce = os.urandom(16)                                                                  # AES-128-CTR - 16 bytes
    ciphertext = encrypt(agent, keys[0], plaintext, nonce)                                  # 1. Encrypt
    signature = sign(agent, keys[1], sequence_number.to_bytes(1, "big") + ciphertext)       # 2. MAC
    message = sequence_number.to_bytes(1, "big") + ciphertext + nonce + signature
    connection.sendall(message)
    print(f"{agent} sent {message}\n")

def sign(agent, key, message):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(message)
    signature = h.finalize()
    print(f"{agent} signed message {message} with signature {signature}")
    return signature

def verify(agent, key, message, signature):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(message)
    try:
        h.verify(signature)
        print(agent, "verified signature", signature, "for message", message)
    except InvalidSignature:
        print(f"ERROR: {agent} tried to verify signature", signature, "for message", message, "but signature does not match digest")
