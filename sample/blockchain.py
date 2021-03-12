import hashlib


'''
Simplified model of a blockchain

This simplified model of a blockchain was created to help students understand 
the blockchain technology, which is also the technology behind the well known 
crypto-currency Bitcoin.
'''

class Transaction():
  """This is a conceptual class representation of a blockchain transaction

    :param sender: The sender of this transaction
    :type sender: str
    :param receiver: The receiver of this transaction
    :type receiver: str
    :param amount: The amount to be sent in this transaction
    :type amount: float
    """
  def __init__(self, sender, receiver, amount):
    """Constructor method
    """
    self.sender = sender
    self.receiver = receiver
    self.amount = amount

  def __str__(self):
    ''' Implementation of string representation of this object 
    '''
    return f'{self.sender}{self.receiver}{self.amount}'
  
  def display(self):
    ''' Prints this transaction to the console 
    '''
    print(f'Sender:{self.sender}, Receiver:{self.receiver}, Amount:{self.amount}')


class Block():
  """This is a conceptual class representation of a blockchain block
 
  :param transactions: List of transactions in this block
  :type transactions: :class:`Transaction`[]
  """
  def __init__(self, previous_hash, transactions):
    """Constructor method
    """
    self.transactions = []
    for transaction in transactions:
      self.transactions.append(transaction)
    self.hash = hashlib.sha256(self.transactions_hash().encode('utf-8') + previous_hash.encode('utf-8'))

  def transactions_hash(self):
    ''' Converts a list of transactions to string. This method should only be called by the constructor method
    :param transactions: List of transactions to be converted to string
    :type transactions: :class:`Transaction`[]
    :return: String from a list of Transaction objects
    :rtype: str
    '''
    hash_str = ''
    for transaction in self.transactions:
      hash_str += str(transaction)
    return hash_str
 
  def display(self):
    ''' Prints this block to the console 
    '''
    print('--- Block ---')
    print(f'Hash: {self.hash.hexdigest()}')
    for transaction in self.transactions:
      transaction.display()
 
  def display_with_index(self, block_index):
    ''' Prints this block including its index in the blockchain to the console. 
    This method should only be called by the parent blockchain of this block
    '''
    if (block_index == 0):
      print(f'--- Genesis block ---')
    else:
      print(f'--- Block {block_index} ---')
    print(f'Hash: {self.hash.hexdigest()}')
    for transaction in self.transactions:
      transaction.display()


class Blockchain():
  """This is a conceptual class representation of a blockchain block
 
  :param init_block: the initial block of this blockchain
  :type init_block: :class:`Block`
  """
  def __init__(self, transactions = [Transaction('Aleksander Sadowski', 'Aleksander Sadowski', 1000.0)]):
    """Constructor method
    """
    self.blocks = []
    self.blocks.append(Block('', transactions))
  
  def add_transactions(self, transactions):
    ''' Creates and adds a block from given transactions to this blockchain
 
    :param transactions: The transactions to be added as a block to this blockchain
    :type transactions: :class:`Transaction`[]
    '''
    self.blocks.append(Block(self.blocks[-1].hash.hexdigest(),transactions))
 
  def add(self, block):
    ''' Adds an exisiting block to this blockchain
 
    :param block: The block to be added to this blockchain
    :type block: :class:`Block`
    '''
    self.blocks.append(block)
 
  def display(self):
    ''' Prints this blockchain to the console 
    '''
    print('###### Blockchain ######')
    for block in self.blocks:
      block.display_with_index(self.blocks.index(block))