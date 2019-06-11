from uclcoin import Block
import requests
import json
from collections import namedtuple

r = requests.get('http://127.0.0.1:5000/block/minable/036b86d828203c1d2f30d689b45fcae5bc700358afafd18012f15121220de17662')
last_block = json.loads(r.text)
block = Block.from_dict(last_block["block"])
difficulty = last_block["difficulty"]

while block.current_hash[:difficulty].count('0') < difficulty:
    block.nonce += 1
    block.recalculate_hash()

data = json.dumps(block, default=lambda x: x.__dict__)

r = requests.post('http://127.0.0.1:5000/block',data,json=True)
print(r.text)