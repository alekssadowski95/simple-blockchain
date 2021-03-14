# -*- coding: utf-8 -*-

from .context import sample
from sample.blockchain import Transaction, Block, Blockchain

import unittest


class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 1.00)

    def test_init(self):
        self.assertEqual(self.transaction.sender, 'Aleksander Sadowski')
        self.assertEqual(self.transaction.receiver, 'Wiktor Domaradzki')
        self.assertEqual(self.transaction.amount, 1.00)

class TestBlock(unittest.TestCase):

    def setUp(self):
        transaction_1 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 1.00)
        transaction_2 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 2.50)
        transaction_3 = Transaction("Wiktor Domaradzki", "Aleksander Sadowski", 3.50)      
        self.block = Block('7575bc27e0468cc35aa4eeefb97bc7e69ac20b61ce9d5053d80bb561bb6460cf', [transaction_1, transaction_2, transaction_3])

    def test_init(self):
        self.assertEqual(self.block.hash.hexdigest(), 'dca49128531b2575e431be3ab883342b5b0adf8b3d57592c17b3ffebd01ed28b')
        self.assertEqual(self.block.transactions[0].sender, 'Aleksander Sadowski')
        self.assertEqual(self.block.transactions[0].receiver, 'Wiktor Domaradzki')
        self.assertEqual(self.block.transactions[0].amount, 1.00)
        self.assertEqual(self.block.transactions[2].sender, 'Wiktor Domaradzki')
        self.assertEqual(self.block.transactions[2].receiver, 'Aleksander Sadowski')
        self.assertEqual(self.block.transactions[2].amount, 3.50)

    def test_transactions_hash(self):
        self.assertEqual(self.block.transactions_hash(), 'Aleksander SadowskiWiktor Domaradzki1.0Aleksander SadowskiWiktor Domaradzki2.5Wiktor DomaradzkiAleksander Sadowski3.5')

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.blockchain = Blockchain()
        transaction_1 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 1.00)
        transaction_2 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 2.50)
        transaction_3 = Transaction("Wiktor Domaradzki", "Aleksander Sadowski", 3.50)
        self.blockchain.add_transactions([transaction_1, transaction_2, transaction_3])
        transaction_4 = Transaction("Wiktor Domaradzki", "Aleksander Sadowski", 12.00)
        transaction_5 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 5.50)
        block = Block(self.blockchain.blocks[0].hash.hexdigest(), [transaction_4, transaction_5])
        self.blockchain.add(block)

    def test_init(self):
        self.assertEqual(self.blockchain.blocks[0].transactions[0].sender, 'Aleksander Sadowski')
        self.assertEqual(self.blockchain.blocks[0].transactions[0].receiver, 'Aleksander Sadowski')
        self.assertEqual(self.blockchain.blocks[0].transactions[0].amount, 1000.0)
               
    def test_add_transactions(self):     
        self.assertEqual(self.blockchain.blocks[0].transactions[0].sender, 'Aleksander Sadowski')
        self.assertEqual(self.blockchain.blocks[0].transactions[0].receiver, 'Aleksander Sadowski')
        self.assertEqual(self.blockchain.blocks[0].transactions[0].amount, 1000.0)
        self.assertEqual(self.blockchain.blocks[1].transactions[2].sender, 'Wiktor Domaradzki')
        self.assertEqual(self.blockchain.blocks[1].transactions[2].receiver, 'Aleksander Sadowski')
        self.assertEqual(self.blockchain.blocks[1].transactions[2].amount, 3.50)
 
    def test_add(self):  
        self.assertEqual(self.blockchain.blocks[2].transactions[0].sender, 'Wiktor Domaradzki')
        self.assertEqual(self.blockchain.blocks[2].transactions[0].receiver, 'Aleksander Sadowski')
        self.assertEqual(self.blockchain.blocks[2].transactions[0].amount, 12.00)

