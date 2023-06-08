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
        # Block the transaction and prompt the user to whitelist the sending wallet
        print("The transaction has been blocked. Please enter the sending wallet address to whitelist it: ")
        sending_wallet_address = input()
        web3.eth.defaultAccount = sending_wallet_address
        return False

def main():
    # Get the activity ID
    activity_id = input("Enter the activity ID: ")

    # Scan the activity
    allowed = scan_activity(activity_id)

    # If the transaction is allowed, do nothing
    if allowed:
        pass

    # If the transaction is blocked, print a message and exit
    else:
        print("The transaction has been blocked.")
        exit()

if __name__ == "__main__":
    main()
