from blockchain import Blockchain, Transaction


'''
This is an example on how the simplified blockchain code can be used.
To see it in action simply run the entire notebook.
'''

# Setup blockchain
blockchain = Blockchain()

transaction_1 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 1.00)
transaction_2 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 2.50)
transaction_3 = Transaction("Wiktor Domaradzki", "Aleksander Sadowski", 3.50)
blockchain.add_transactions([transaction_1, transaction_2, transaction_3])

transaction_1 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 1.00)
transaction_2 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 2.50)
transaction_3 = Transaction("Wiktor Domaradzki", "Aleksander Sadowski", 3.50)
blockchain.add_transactions([transaction_1, transaction_2, transaction_3])

transaction_4 = Transaction("Wiktor Domaradzki", "Aleksander Sadowski", 12.00)
transaction_5 = Transaction("Aleksander Sadowski", "Wiktor Domaradzki", 5.50)
blockchain.add_transactions([transaction_4, transaction_5])

# Print blockchain to the console
blockchain.display()