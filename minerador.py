from uclcoin import Block
import requests
import json
from collections import namedtuple

r = requests.get('http://127.0.0.1:5000/block/minable/0304cd2edaa5e6571b752dc90038486f66ad60b2886252a319ae50942a737304c4')
last_block = json.loads(r.text)
block = Block.from_dict(last_block["block"])
difficulty = last_block["difficulty"]

while block.current_hash[:difficulty].count('0') < difficulty:
    block.nonce += 1
    block.recalculate_hash()

data = json.dumps(block, default=lambda x: x.__dict__)

r = requests.post('http://127.0.0.1:5000/block',data,json=True)
print(r.text)
