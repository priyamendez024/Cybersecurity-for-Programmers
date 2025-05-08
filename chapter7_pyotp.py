import pyotp
secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)
code = totp.now()         # user enters this
assert totp.verify(code)  # verify in backend