import hashlib

data = b"Authenticate me"
digest = hashlib.sha256(data).hexdigest()