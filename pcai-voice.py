###### EXPERIMENTAL ######

import requests
import json
import web3

def scan_activity(activity_id):
    # Get the activity data
    response = requests.get(f"https://api.metamask.io/activities/{activity_id}")
    data = json.loads(response.content)

    # Get the receiving wallet addresses
    receiving_addresses = []
    for transaction in data["transactions"]:
        receiving_addresses.append(transaction["to"])

    # Get the sending wallet address
    sending_address = data["from"]

    # Check if the receiving wallet has the sending wallet address
    if sending_address in receiving_addresses:
        # Allow the transaction
        return True
    else:
        # Block the transaction
        return False

def sign_transaction(data, provider):
    # Sign the transaction
    signature = provider.personal_sign(data)

    # Return the signature
    return signature

def sign_file(file_path, provider):
    # Read the file contents
    with open(file_path, "rb") as f:
        data = f.read()

    # Sign the data
    signature = sign_transaction(data, provider)

    # Save the signature to the file
    with open(file_path + ".sig", "wb") as f:
        f.write(signature)

def upload_signature(signature, decentralized_storage_network):
    # Upload the signature to the decentralized storage network
    ipfs_client = decentralized_storage_network.get_ipfs_client()

    # Add the signature to IPFS
    ipfs_hash = ipfs_client.add(signature)

    # Return the IPFS hash
    return ipfs_hash

def main():
    # Get the activity ID
    activity_id = input("Enter the activity ID: ")

    # Scan the activity
    allowed = scan_activity(activity_id)

    # If the transaction is allowed, sign it and save the signature to the .sig file
    if allowed:
        # Get the MetaMask provider
        provider = web3.eth.get_default_provider()

        # Set the `allowSameNetworkTransactions` option to True
        provider.allowSameNetworkTransactions = True

        # Sign the transaction using Google API voice commands
        if allowed:
            print("Allowed transaction. Signing transaction using Google API voice commands...")
            signature = google_api_voice_commands.sign_transaction(data, provider)
        else:
            print("Blocked transaction.")

        # Save the signature to the file
        with open("signature.sig", "wb") as f:
            f.write(signature)

        # Upload the signature to IPFS
        ipfs_hash = upload_signature(signature, IPFS)

    # If the transaction is blocked, prompt the user to enter the sending wallet address to whitelist
    else:
        sending_wallet_address = input("Enter the sending wallet address to whitelist: ")

        # Add the sending wallet address to the whitelist
        with open("whitelist.txt", "a") as f:
            f.write(sending_wallet_address + "\n")

if __name__ == "__main__":
    main()
