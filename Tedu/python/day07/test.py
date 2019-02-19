import hashlib

m = hashlib.md5(b'12346')
print(m.hexdigest())

with open('/etc/passwd','rb') as f:
    data = f.read()
    m = hashlib.md5(data)
    print(m.hexdigest())