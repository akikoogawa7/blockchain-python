import hashlib

message = "Python is great."

h1 = hashlib.sha256(message.encode())

print(h1)
print(h1.hexdigest())