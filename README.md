# pcai-API-sandbox
PC.AI API sandbox testcode that will allow MetaMask API to sign transactions that include hashes and sign files sending wallet. The scan_activity function will scan the activity data and determine if the transaction is allowed. If the transaction is allowed, the sign_transaction function will sign the transaction using the MetaMask provider. The sign_file function will sign a file using the MetaMask provider. The main function will prompt the user for the activity ID and then scan the activity. If the transaction is allowed, the signature will be printed. If the transaction is blocked, nothing will happen.


****Updated 6/6/2023
allowSameNetworkTransactions option is set to True before the transaction is signed. This allows the transaction to be sent to an address on the same network as the sending wallet, even if the sending and receiving wallets are not connected to the same RPC provider.
