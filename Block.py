from hashlib import sha256
import time
from Transaction import Transaction
from Util import Util

class Block():
    def __init__(self, transaction, previous_hash = "Genesis Block", nonce = 0, difficulty = 4):
        self.index = self.getIndex()
        self.previous_hash = previous_hash
        self.timestamp = self.setTimestamp()
        self.nonce = nonce
        self.difficulty = difficulty
        self.Transaction = transaction
        self.hash = self.calculateHash()
        self.merkle_root = self.calculateMerkleRoot()

    def __str__(self):
        return str(f"Previous Hash: {self.previous_hash}\tTimestamp: {self.getTimestamp()}\tHash: {self.hash}\t{self.nonce}\t{self.Transaction} \t{self.merkle_root}")

    def printTransaction(self):
        for transaction in self.Transaction:
            print(transaction)

    def getIndex(self):
        try:
            return self[-1].index + 1
        except:
            return 0

    def getTimestamp(self):
        s = time.gmtime(self.timestamp)
        return time.strftime("%Y-%m-%d", s)

    def setHash(self):
        self.hash = self.calculateHash()
             
    def setTimestamp(self):
        return time.time()

    # TODO: Implement nonce and difficulty on the block to be hashed
    def calculateHash(self):
        return sha256(str(self.previous_hash + str(self.nonce) + str(self.timestamp) + str(self.Transaction)).encode()).hexdigest()
   
    def mineBlock(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculateHash()
            self.difficulty = difficulty
        print (f"Block Mined: {self.hash}")
            
    def calculateMerkleRoot(self):
            newTransaction = []
            for i in range(0, len(self.Transaction), 2):
                if i + 1 < len(self.Transaction):
                    newTransaction.append(Util.calculateBothHash(self.Transaction[i], self.Transaction[i + 1]))
                else:
                    newTransaction.append(Util.calculateBothHash(self.Transaction[i], self.Transaction[i]))

            while len(newTransaction) > 1:
                temp = []
                for i in range(0, len(newTransaction), 2):
                    if i + 1 < len(newTransaction):
                        temp.append(Util.calculateBothHash(newTransaction[i], newTransaction[i + 1]))
                    else:
                        temp.append(newTransaction[i])
                newTransaction = temp
            return newTransaction[0]
