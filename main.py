import hashlib

s = "Python Bootcamp"

# full version

hash = hashlib.sha1(s.encode())
hex_dig = hash.hexdigest()
print(hex_dig)
#
print()
# a shorter version
print(hashlib.sha256(s.encode()))