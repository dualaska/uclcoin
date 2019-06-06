from uclcoin import Block
import requests
import json
from collections import namedtuple

r = requests.get('https://blockchainpiv.azurewebsites.net/block/minable/02f6a1813ae470f9c3c71eda29bbc711de17822946e87d84936eb3990ec4c74350')
last_block = json.loads(r.text)
block = Block.from_dict(last_block["block"])
difficulty = last_block["difficulty"]

while block.current_hash[:difficulty].count('0') < difficulty:
    block.nonce += 1
    block.recalculate_hash()

data = json.dumps(block, default=lambda x: x.__dict__)

requests.post('https://blockchainpiv.azurewebsites.net/block',data,json=True)
