from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = AESGCM.generate_key(bit_length=128)
aesgcm = AESGCM(key)
nonce = os.urandom(12)
plaintext = b"Secret message"
aad = b"header-data"

ciphertext = aesgcm.encrypt(nonce, plaintext, aad)
# decrypt with same key, nonce and aad:
decrypted = aesgcm.decrypt(nonce, ciphertext, aad)