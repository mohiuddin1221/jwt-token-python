import jwt
import datetime
import time

encoded_token = jwt.encode({"exp": 1371720939}, "secret")
expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=20)
encoded_token2 = jwt.encode({"exp": expiration_time}, "secret")

print(encoded_token)
time.sleep(25)
try: 
  print(encoded_token2)
except Exception as e:
   print("Error", e)
   print("Time out")