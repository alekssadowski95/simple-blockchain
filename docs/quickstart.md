# Quickstart

This simplified model of a blockchain was created to help students understand the blockchain technology, which is also the technology behind the well known crypto-currency Bitcoin.

To run this code you need to have a python interpreter installed: <https://www.python.org/downloads/>

```text
pip install simple-blockchain
```

## 1. Create blockchain
```python
from sample.blockchain import Blockchain
blockchain = Blockchain()
```
## 2. Add transactions
```python
transaction_1 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 1.00)
transaction_2 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 2.50)
transaction_3 = Transaction("Wiktor Domaradzki", "Aleksander Sadowski", 3.50)
blockchain.add_transactions([transaction_1, transaction_2, transaction_3])
```
## 3. Display blockchain
```python
blockchain.display()
```
