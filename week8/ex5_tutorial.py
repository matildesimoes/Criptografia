from ecdsa import VerifyingKey, SigningKey, NIST192p
import hashlib

# Alínea a
def generate_keys():
    private_key = SigningKey.generate(curve=NIST192p)
    public_key = private_key.verifying_key
    
    # Hexadecimal format
    private_key_hex = private_key.to_string().hex()
    public_key_hex = public_key.to_string().hex()
    
    return private_key_hex, public_key_hex

private_key, public_key = generate_keys()
print("Private Key:", private_key)
print("Public Key:", public_key)

# Alínea b
def sign_message(private_key_hex, message):
    # Hex to SigningKey
    private_key = SigningKey.from_string(bytes.fromhex(private_key_hex), curve=NIST192p)
    hashed_message = hashlib.sha256(message.encode()).digest()
    signature = private_key.sign(hashed_message)

    return signature.hex()

message = "This is a test message."
signature = sign_message(private_key, message)
print("--------------------")
print("Message:", message)
print("Signature:", signature)

# Alínea c
def verify_signature(public_key_hex, message, signature_hex):
    # Hex to VerifyingKey
    public_key = VerifyingKey.from_string(bytes.fromhex(public_key_hex), curve=NIST192p)
    hashed_message = hashlib.sha256(message.encode()).digest()
    signature = bytes.fromhex(signature_hex)

    is_valid = public_key.verify(signature, hashed_message)
    return is_valid

is_valid = verify_signature(public_key, message, signature)
print("--------------------")
print("Signature is valid:", is_valid)