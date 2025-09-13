import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

BITGO_ACCESS_TOKEN = os.getenv("BITGO_ACCESS_TOKEN")
BITGO_ENTERPRISE_ID = os.getenv("BITGO_ENTERPRISE_ID")
BITGO_WALLET_PASSPHRASE = os.getenv("BITGO_WALLET_PASSPHRASE")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WALLET_ID = os.getenv("WALLET_ID")
COIN = "hteth"

# BitGo Express base URL (adjust if running on a different port/host)
BASE_URL = "http://localhost:3080/api/v2"

# API endpoint
url = f"{BASE_URL}/{COIN}/wallet/{WALLET_ID}/webhooks"

# Request payload
payload = {
    "type": "transfer",
    "url": WEBHOOK_URL,
    "allToken": True,
    "numConfirmations": 0,  # Trigger immediately when transfer is seen
    "label": "Deposit Webhook"
}

# Headers
headers = {
    "Authorization": f"Bearer {BITGO_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Send POST request
try:
    webhook_response = requests.post(url, headers=headers, data=json.dumps(payload))
    if webhook_response.status_code == 200:
        webhook_data = webhook_response.json()
        print("\n✅ Webhook created successfully:")
        print(json.dumps(webhook_data, indent=2))

        # Save webhook data to JSON file
        with open("hteth_webhook.json", "w") as f:
            json.dump(webhook_data, f, indent=2)
        print("\n📂 Webhook data saved to hteth_webhook.json")
    else:
        print(f"\n❌ Webhook creation failed with status {webhook_response.status_code}: {webhook_response.text}")
except requests.exceptions.HTTPError as e:
    print(f"\n❌ HTTP Error: {e}")
except Exception as e:
    print(f"\n❌ Unexpected error: {str(e)}")