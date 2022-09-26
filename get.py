from compile import abi, bytecode
from web3 import Web3

provider_rpc = {
    'development': 'http://localhost:9933',
    'alphanet': 'https://rpc.api.moonbase.moonbeam.network',
}
web3 = Web3(Web3.HTTPProvider(provider_rpc["development"]))  # Change to correct network

contract_address = '0x970951a12F975E6762482ACA81E57D5A2A4e73F4'

print(f'Making a call to contract at address: { contract_address }')

Incrementer = web3.eth.contract(address=contract_address, abi=abi)
number = Incrementer.functions.number().call()

print(f'The current number stored is: { number } ')