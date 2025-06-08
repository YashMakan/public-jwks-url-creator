from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from jwcrypto import jwk
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load public key once at startup
with open("public.pem", "rb") as f:
    key = jwk.JWK.from_pem(f.read())

# Export public key in JWKS format
jwks = {
    "keys": [json.loads(key.export(private_key=False))]
}

@app.get("/.well-known/jwks.json")
async def get_jwks():
    return jwks

