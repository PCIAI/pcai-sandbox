# pcai-API-sandbox
PC.AI API sandbox testcode that will allow MetaMask API to sign transactions that include hashes and sign files sending wallet. The scan_activity function will scan the activity data and determine if the transaction is allowed. If the transaction is allowed, the sign_transaction function will sign the transaction using the MetaMask provider. The sign_file function will sign a file using the MetaMask provider. The main function will prompt the user for the activity ID and then scan the activity. If the transaction is allowed, the signature will be printed. If the transaction is blocked, nothing will happen.


****Updated 6/6/2023
allowSameNetworkTransactions option is set to True before the transaction is signed. This allows the transaction to be sent to an address on the same network as the sending wallet, even if the sending and receiving wallets are not connected to the same RPC provider.

****Updated 6/7/2023
PC.AI exchange will first check if the sending wallet address is in the list of receiving wallets. If it is, then the transaction will be allowed. If it is not, then the code will check if the sending wallet IP matches the login IP. If it does, then the transaction will be allowed. If it does not, then the transaction will be blocked.

**Note: Code must not be changed to malaciously change rules and functions as all ip address and metadata is logged. The Code is Open Sourced to everyone
