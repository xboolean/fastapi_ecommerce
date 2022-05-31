from base64 import decode
import os
import time
import jwt

JWT_SECRET = os.environ.get("secret")
JWT_ALGORITHM = "HS256"

def token_response(token: str):
    return {
        "access token": token
    }

def sign_JWT(userID: str):
    payload = {
        "userID": userID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}