import jwt
#screet_key = "hello"
private_key = b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS..."
public_key = b"-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEAC..."
payload = {
   'user_id' : 123456,
   'username' : 'topu'
   
}
encode_token= jwt.encode(payload,private_key,algorithm='HS256')
print(encode_token)
decode_token = jwt.decode(encode_token,public_key,algorithms='HS256')
print(decode_token)


