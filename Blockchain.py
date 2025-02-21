from Block import Block
from Transaction import Transaction



class Blockchain():
    def __init__(self):
        self.block = []

    def addBlock(self, block):
        self.block.append(block)

    def addTransaction(self, transaction, index):
        self.block[index].transaction.append(transaction)
        return self.transaction

    def printBlock(self):
        for b in self.block:
            print(f"{b}\n\n")
