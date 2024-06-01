import base64, pickle

# 反序列化
data = "gASVDwAAAAAAAACMC3RvcCAtYiAtbiAxlC4="
print(pickle.loads(base64.b64decode(data)))


# 序列化
print(base64.b64encode(pickle.dumps("echo 'python pickle serialize'")))