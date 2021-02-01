# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:33:10 2021

@author: masou
"""

import json
import hashlib
from time import time


import json
import hashlib
from time import time


class Blockchain(object):
    ''' define a block chain on one machine '''

    def __init__(self):
        self.chain = []
        self.current_trxs = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        ''' creat a new block '''
        block = {'index': len(self.chain) + 1, 'timestamp': time(), 'trxs': self.current_trxs,
                 'proof': proof, 'previous_hash': previous_hash or self.hash(self.chain[-1]), }
        self.current_trxs = []
        self.chain.append(block)
        return block

    def new_trx(self, sender, recipient, amount):
        ''' add a new trxs to the mempool '''
        self.current_trxs.append(
            {'sender': sender, 'recipient': recipient, 'amount': amount})

    @staticmethod
    def hash(block):
        ''' hash a block '''
        block_string = json.dump(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        ''' return last block '''
        pass
