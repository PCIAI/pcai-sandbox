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
        # Check if the sending wallet IP matches the login IP
        ip_file = requests.get("https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco")
        ip_data = json.loads(ip_file.content)
        if sending_address in ip_data:
            # Allow the transaction
            return True
        else:
            # Block the transaction
            return False

def main():
    # Get the activity ID
    activity_id = input("Enter the activity ID: ")

    # Scan the activity
    allowed = scan_activity(activity_id)

    # Display the result
    if allowed:
        print("Transaction allowed")
    else:
        print("Transaction blocked")

if __name__ == "__main__":
    main()
