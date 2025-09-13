import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

BITGO_ACCESS_TOKEN = os.getenv("BITGO_ACCESS_TOKEN")
BITGO_ENTERPRISE_ID = os.getenv("BITGO_ENTERPRISE_ID")

# BitGo Express base URL (adjust if running on a different port/host)
BASE_URL = "http://localhost:3080/api/v2"

# Wallet creation endpoint
url = f"{BASE_URL}/hteth/wallet/generate"

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BITGO_ACCESS_TOKEN}"
}

# Request body
payload = {
    "label": "My HTETH Wallet",
    "passphrase": "StrongPassphrase123!",  # replace with your secure passphrase
    "enterprise": BITGO_ENTERPRISE_ID,
    "type": "hot",   # hot wallet (self-managed)
    "multisigType": "tss",
    "walletVersion": 3
}

# POST request to create the wallet
response = requests.post(url, headers=headers, json=payload)

# Print result
if response.status_code == 200:
    print("✅ Wallet created successfully:")
    print(response.json())
else:
    print(f"❌ Error {response.status_code}: {response.text}")
