import os
import json
from web3 import Web3

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Load contract ABI and address
contract_path = os.path.join(os.path.dirname(__file__), '../build/contracts/BQPD.json')
with open(contract_path) as f:
    contract_json = json.load(f)
    abi = contract_json['abi']
    address = list(contract_json['networks'].values())[0]['address']

contract = web3.eth.contract(address=address, abi=abi)

# Use first account for sending transactions
account = web3.eth.accounts[9]

# 0-TA
# 1-PS
# 2-PS
# 3-PS
# 4-PS
# 5-ECC
# 6-ECC
# 7-ECC
# 8-ECC
# 9-ECC
