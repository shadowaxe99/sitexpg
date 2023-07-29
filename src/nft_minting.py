```python
from web3 import Web3
from solcx import compile_standard
from src.models import NFT, db

class NFTMinting:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545')) # Connect to local Ethereum node

    def compile_contract(self, contract_path):
        with open(contract_path, 'r') as file:
            contract_source_code = file.read()

        compiled_sol = compile_standard({
            "language": "Solidity",
            "sources": {
                "NFTContract.sol": {
                    "content": contract_source_code
                }
            },
            "settings":
                {
                    "outputSelection": {
                        "*": {
                            "*": [
                                "metadata", "evm.bytecode"
                                , "evm.bytecode.sourceMap"
                            ]
                        }
                    }
                }
        })

        bytecode = compiled_sol['contracts']['NFTContract.sol']['NFTContract']['evm']['bytecode']['object']
        abi = json.loads(compiled_sol['contracts']['NFTContract.sol']['NFTContract']['metadata'])['output']['abi']

        return bytecode, abi

    def deploy_contract(self, bytecode, abi):
        contract = self.web3.eth.contract(abi=abi, bytecode=bytecode)
        tx_hash = contract.constructor().transact()
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt['contractAddress']

    def mint_nft(self, contract_address, abi, owner_address, token_uri):
        contract = self.web3.eth.contract(address=contract_address, abi=abi)
        tx_hash = contract.functions.mint(owner_address, token_uri).transact()
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def save_nft_to_db(self, investor_id, token_uri, contract_address):
        new_nft = NFT(investor_id=investor_id, token_uri=token_uri, contract_address=contract_address)
        db.session.add(new_nft)
        db.session.commit()

nft = NFTMinting()
```