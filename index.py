import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BITGO_ACCESS_TOKEN = os.getenv("BITGO_ACCESS_TOKEN")
BITGO_ENTERPRISE_ID = os.getenv("BITGO_ENTERPRISE_ID")
BITGO_WALLET_PASSPHRASE = os.getenv("BITGO_WALLET_PASSPHRASE")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# BitGo Express base URL (adjust if running on a different port/host)
BASE_URL = "http://localhost:3080/api/v2"

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BITGO_ACCESS_TOKEN}"
}

# Step 1: Create HTETH Wallet
wallet_url = f"{BASE_URL}/hteth/wallet/generate"

wallet_payload = {
    "label": "My HTETH Wallet",
    "passphrase": BITGO_WALLET_PASSPHRASE,  # Loaded from .env
    "enterprise": BITGO_ENTERPRISE_ID,
    "type": "hot",  # Hot wallet (self-managed)
    "multisigType": "tss",
    "walletVersion": 3
}

# POST request to create the wallet
wallet_response = requests.post(wallet_url, headers=headers, json=wallet_payload)

if wallet_response.status_code == 200:
    wallet_data = wallet_response.json()
    print("✅ Wallet created successfully:")
    print(f"Wallet ID: {wallet_data['wallet']['id']}")
    print(f"Receiving Address: {wallet_data['wallet']['receiveAddress']['address']}")

    # Save wallet data to JSON file
    with open("hteth_wallet.json", "w") as f:
        json.dump(wallet_data, f, indent=2)
    print("\n📂 Wallet data saved to hteth_wallet.json")

