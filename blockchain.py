# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:33:10 2021

@author: masou
"""


class Blockchain(object):
    ''' define a block chain on one machine '''
    def __init__(self):
        self.chain = []
        self.current_trxs = []
        
    def new_block(self):
        ''' creat a new block '''
        block = {'index': len(self.chain) + 1, }
    
    def new_trx(self, sender, recipient, amount):
        ''' add a new trxs to the mempool '''
        self.current_trxs.append({'sender': sender, 'recipient': recipient, 'amount': amount})
    
    @staticmethod
    def hash(block):
        ''' hash a block '''
        pass
    
    @property
    def last_block(self):
        ''' return last block '''
        pass




