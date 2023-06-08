function scanActivity(activityId) {
  const response = await fetch(`https://api.metamask.io/activities/${activityId}`);
  const data = await response.json();

  const receivingAddresses = [];
  for (const transaction of data.transactions) {
    receivingAddresses.push(transaction.to);
  }

  const sendingAddress = data.from;

  return sendingAddress in receivingAddresses ? true : false;
}

function signTransaction(data, provider) {
  const provider = detectEthereumProvider();

  const signature = provider.personalSign(data);

  return signature;
}

function signFile(filePath, provider) {
  const data = await fs.readFileSync(filePath, "rb");

  const signature = signTransaction(data, provider);

  await fs.writeFileSync(filePath + ".sig", signature);
}

function uploadSignature(signature, decentralizedStorageNetwork) {
  const ipfsClient = decentralizedStorageNetwork.getIpfsClient();

  const ipfsHash = await ipfsClient.add(signature);

  return ipfsHash;
}

async function main() {
  const activityId = await prompt("Enter the activity ID: ");

  const allowed = await scanActivity(activityId);

  if (allowed) {
    const provider = web3.eth.get_default_provider();

    provider.allowSameNetworkTransactions = true;

    const networkId = await provider.getNetworkId();

    const signature = await signTransaction(data, provider);

    await fs.writeFileSync("signature.sig", signature);

    const ipfsHash = await uploadSignature(signature, IPFS);

    await fs.appendFileSync("whitelist.txt", sendingWalletAddress + "\n");
  } else {
    const sendingWalletAddress = await prompt("Enter the sending wallet address to whitelist: ");

    await fs.appendFileSync("whitelist.txt", sendingWalletAddress + "\n");
  }
}

if (__name__ == "__main__") {
  main();
}
