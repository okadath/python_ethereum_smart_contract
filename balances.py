from web3 import Web3

provider_rpc = {
    "development": "http://localhost:9933",
    "alphanet": "https://rpc.api.moonbase.moonbeam.network",
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["development"]))  # Change to correct network

 
address_from="0x795a21680660A13ABDCf713626cFE687E11f8957"#alpha
address_from= "0xf24FF3a9CF04c71Dbc94D0b566f7A27B94566cac"

 
address_to="0x9808aC26DF5162FE61c775A8D872B77512C4F92C"#alpha
address_to="0x3Cd0A705a2DC65e5b1E1205896BaA2be8A07c6e0"

balance_from = web3.fromWei(web3.eth.getBalance(address_from), "ether")
balance_to = web3.fromWei(web3.eth.getBalance(address_to), "ether")

print(f"The balance of { address_from } is: { balance_from } ETH")
print(f"The balance of { address_to } is: { balance_to } ETH")