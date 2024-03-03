import jwt
screet_key = "hello"
payload = {
   'user_id' : 123456,
   'username' : 'topu'
   
}
encode_token= jwt.encode(payload,screet_key,algorithm='HS256')
print(encode_token)
decode_token = jwt.decode(encode_token,screet_key,algorithms='HS256')
print(decode_token)


