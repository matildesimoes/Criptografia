import os

MOD = 256

def KSA(key):
    ''' Key Scheduling Algorithm (from wikipedia):
        for i from 0 to 255
            S[i] := i
        endfor
        j := 0
        for i from 0 to 255
            j := (j + S[i] + key[i mod keylength]) mod 256
            swap values of S[i] and S[j]
        endfor
    '''
    key_length = len(key)
    S = list(range(MOD))
    j = 0
    for i in range(MOD):
        j = (j + S[i] + key[i % key_length]) % MOD
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S):
    ''' Psudo Random Generation Algorithm (from wikipedia):
        i := 0
        j := 0
        while GeneratingOutput:
            i := (i + 1) mod 256
            j := (j + S[i]) mod 256
            swap values of S[i] and S[j]
            K := S[(S[i] + S[j]) mod 256]
            output K
        endwhile
    '''
    i = 0
    j = 0
    while True:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % MOD]
        yield K

def get_keystream(key):
    ''' Takes the encryption key to get the keystream using PRGA
        return object is a generator
    '''
    S = KSA(key)
    return PRGA(S)

def encrypt_logic(key, text):
    ''' :key -> encryption key used for encrypting, as hex string
        :text -> array of unicode values/ byte string to encrpyt/decrypt
    '''
    key = [ord(c) for c in key]
    keystream = get_keystream(key)

    res = []
    for c in text:
        val = c ^ next(keystream)
        res.append(val)
    return bytes(res)

def encrypt_file(key, input_file):
    with open(input_file, 'rb') as f:
        file_data = f.read()

    encrypted_data = encrypt_logic(key, file_data)

    encrypted_hex = encrypted_data.hex().upper()
    with open('ciphertext.txt', 'w') as f:
        f.write(encrypted_hex)
    
    print(f"O texto cifrado encontra-se em ciphertext.txt.")

    return encrypted_data

def decrypt_file(key, encrypted_data):
    decrypted_data = encrypt_logic(key, encrypted_data)

    try:
        original_text = decrypted_data.decode('utf-8')
        print(f"Texto decifrado: {original_text}")
    except UnicodeDecodeError:
        print("Erro ao decifrar o texto.")
    
    return decrypted_data

def main():

    if os.path.exists('ciphertext.txt'):
        os.remove('ciphertext.txt')
        print("O ficheiro ciphertext.txt criado na execução anterior foi removido.")

    key = 'not-so-random-key'

    input_file = 'plaintext.txt'
    encrypt_file(key, input_file)

    with open('ciphertext.txt', 'r') as f:
        encrypted_hex = f.read()
    
    encrypted_data_from_file = bytes.fromhex(encrypted_hex)
    decrypt_file(key, encrypted_data_from_file)

if __name__ == '__main__':
    main()
