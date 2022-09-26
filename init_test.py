from web3 import Web3, EthereumTesterProvider
w3 = Web3(EthereumTesterProvider())
print(w3.isConnected())
print(w3)

from web3 import Web3

web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:9933'))

print(web3)