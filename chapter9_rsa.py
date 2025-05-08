from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate keys
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Encrypt with recipient’s public key
rsa_pub = RSA.import_key(public_key)
cipher = PKCS1_OAEP.new(rsa_pub)
ciphertext = cipher.encrypt(b"Top secret")

# Decrypt with private key
rsa_priv = RSA.import_key(private_key)
decipher = PKCS1_OAEP.new(rsa_priv)
plaintext = decipher.decrypt(ciphertext)