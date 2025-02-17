from hashlib import sha256
import time


class Block():

    def __init__(self, previous_hash, transaction, nonce=0):
        self.previous_hash = previous_hash
        self.timestamp = self.setTimestamp()
        self.nonce = self.CalculateNonce(nonce)
        self.Transaction = transaction
        self.hash = self.calculateHash()

    def __str__(self):
        return str(f"Previous Hash: {self.previous_hash}\tTimestamp: {self.getTimestamp()}\tHash: {self.hash}\t{self.nonce}\t{self.printTransaction()}")

    def genisisBlock():
        return Block("Genesis Block", [])

    def printTransaction(self):
        for transaction in self.Transaction:
            print(transaction)

    def addTransationToBlock(self, block):
        block.Transaction.append(self)
        return block

    def getTimestamp(self):
        s = time.gmtime(self.timestamp)
        return time.strftime("%Y-%m-%d", s)

    def setHash(self):
        self.hash = self.calculateHash()
             
    def setTimestamp(self):
        return time.time()

    # TODO: Implement nonce and difficulty on the block to be hashed
    def calculateHash(self):
        return sha256(str(self.previous_hash + str(self.timestamp) + str(self.Transaction)).encode()).hexdigest()
    
    def calculateSomeHash(self, nonce):
        return sha256(str(nonce).encode()).hexdigest()
 
    def CalculateNonce(self, nonce=0):
        if(nonce == 0):
            return 0
        nonce += 1
        while self.calculateSomeHash(nonce)[:1] != "f":
            nonce += 1

        return nonce
 
    def mineBlock(self):
        









