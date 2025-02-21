from Block import Block
from Transaction import Transaction
from Blockchain import Blockchain
from Commands import Commands

def printBlock(block):
    for b in block:
        print(b)


if __name__ == "__main__":
    Commands.startMenu()
    transaction = []
    transaction.append(Transaction("Alice", "Bob", 100))
    transaction.append(Transaction("Bob", "Alice", 50))
    transaction.append(Transaction("Alice", "Bob", 100))
    transactionSecond = []
    transactionSecond.append(Transaction("Alice", "Bob", 100))

    blockchain = Blockchain()
    blockchain.addBlock(Block(transactionSecond))
    blockchain.addBlock(Block(transaction, blockchain.block[-1].hash, blockchain.block[-1].nonce + 1 ))
    blockchain.addBlock(Block(transaction, blockchain.block[-1].hash, blockchain.block[-1].nonce + 1 ))
    blockchain.printBlock()
