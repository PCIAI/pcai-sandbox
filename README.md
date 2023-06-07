# pcai-API-sandbox
PC.AI API sandbox testcode that will allow MetaMask API to sign transactions that include hashes and sign files sending wallet. The scan_activity function will scan the activity data and determine if the transaction is allowed. If the transaction is allowed, the sign_transaction function will sign the transaction using the MetaMask provider. The sign_file function will sign a file using the MetaMask provider. The main function will prompt the user for the activity ID and then scan the activity. If the transaction is allowed, the signature will be printed. If the transaction is blocked, nothing will happen.


****Updated 6/6/2023
allowSameNetworkTransactions option is set to True before the transaction is signed. This allows the transaction to be sent to an address on the same network as the sending wallet, even if the sending and receiving wallets are not connected to the same RPC provider.

****Updated 6/7/2023
PC.AI exchange will first check if the sending wallet address is in the list of receiving wallets. If it is, then the transaction will be allowed. If it is not, then the code will check if the sending wallet IP matches the login IP. If it does, then the transaction will be allowed. If it does not, then the transaction will be blocked.

**Note: Code must not be changed to malaciously change rules and functions as all ip address and metadata is logged. The Code is Open Sourced to everyone



============================================================================================

HOW TO UPDATE CODE ON REPOSITORY BELOW

Fork the repository. This creates a copy of the repository on your own account. Make changes to the code. You can do this by editing the files in the repository. Commit the changes. This saves the changes to your local copy of the repository. Push the changes to your remote repository. This makes the changes available to other users. To update code on a GitHub repository, you can follow these steps:

Go to the GitHub repository that you want to update. 

Click on the "Code" button. Click on the "Pull requests" tab. 
Click on the "New pull request" button. 
In the "Pull request" dialog, select the branch that you want to update and the branch that you want to merge the changes into. 
Add a comment that describes the changes that you are making. 
Click on the "Create pull request" button. 

Once you have created a pull request, other users can review your changes and approve them. 
Once your pull request is approved, the changes will be merged into the main branch of the repository.

Here are some additional tips for updating code on a GitHub repository:

Use descriptive commit messages. This will help other users understand what changes you have made. Use a consistent coding style. This will make your code easier to read and maintain. Test your changes before you push them to the remote repository. This will help to avoid errors. Document your changes. This will help other users understand how to use your code.
