from cryptography.hazmat.primitives.asymmetric import ed25519

private = ed25519.Ed25519PrivateKey.generate()
public = private.public_key()

message = b"Important data"
signature = private.sign(message)
public.verify(signature, message)  # throws if invalid