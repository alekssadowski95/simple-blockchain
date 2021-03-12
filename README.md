# Simplified Blockchain

This simplified model of a blockchain was created to help students understand the blockchain technology, which is also the technology behind the well known crypto-currency Bitcoin.
Download with:
```
pip install simple-blockchain
```

## How to use
Create your own blockchain in 3 easy steps.

### 1. Create blockchain
```python
blockchain = Blockchain()
```
### 2. Add transactions
```python
transaction_1 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 1.00)
transaction_2 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 2.50)
transaction_3 = Transaction("Wiktor Domaradzki", "Aleksander Sadowski", 3.50)
blockchain.add_transactions([transaction_1, transaction_2, transaction_3])
```
### 3. Display blockchain
```python
blockchain.display()
```
