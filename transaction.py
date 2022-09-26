from web3 import Web3

provider_rpc = {
    "development": "http://localhost:9933",
    "alphanet": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["development"]))  # Change to correct network

account_from = {
    "private_key": "4d0a6c94f6d4a068ae03ec6a27a7afab8eb7bf99b2899f6f48fffdc65fe79596",
    "address": "0x795a21680660A13ABDCf713626cFE687E11f8957",
}
account_from={
	"private_key":"0x5fb92d6e98884f76de468fa3f6278f8807c48bebc13595d45af5bdc4da702133",
	"address":"0xf24FF3a9CF04c71Dbc94D0b566f7A27B94566cac"
}
address_to = "0x9808aC26DF5162FE61c775A8D872B77512C4F92C"
address_to="0x3Cd0A705a2DC65e5b1E1205896BaA2be8A07c6e0"
print(
    f'Attempting to send transaction from { account_from["address"] } to { address_to }'
)
from web3.gas_strategies.rpc import rpc_gas_price_strategy
web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)
tx_create = web3.eth.account.signTransaction(
    {
        "nonce": web3.eth.getTransactionCount(account_from["address"]),
        "gasPrice":  web3.eth.generate_gas_price(),
        "gas": 21000,
        "to": address_to,
        "value": web3.toWei("1", "ether"),
    },
    account_from["private_key"],
)

tx_hash = web3.eth.sendRawTransaction(tx_create.rawTransaction)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print(f"Transaction successful with hash: { tx_receipt.transactionHash.hex() }")