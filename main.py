from Block import Block
from Transaction import Transaction


def printBlock(block):
    for b in block:
        print(b)


if __name__ == "__main__":
    transaction = []
    transaction.append(Transaction("Alice", "Bob", 100))
    transaction.append(Transaction("Bob", "Alice", 50))
    block = [Block.genisisBlock()]
    block.append(Block("0",  transaction, block[-1].nonce + 1))
    block.append(Block("0", transaction, block[-1].nonce))
    block.append(Block("0", transaction, block[-1].nonce))
    block.append(Block("0", transaction, block[-1].nonce))
    printBlock(block)
