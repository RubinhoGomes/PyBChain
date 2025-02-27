from hashlib import sha256

class Util:
    
    @staticmethod
    def checkTransactionPair(Transaction):
        calculate = len(Transaction) % 2
        if calculate == 0:
            return True
        else:
            return False

    @staticmethod
    def calculateBothHash(transactionA, transactionB):
        transactionA = Util.calculaTransactionHash(transactionA)
        transactionB = Util.calculaTransactionHash(transactionB)
        return sha256(str(transactionA + transactionB).encode()).hexdigest()
        
    @staticmethod
    def calculaTransactionHash(transaction):
        return sha256(str(transaction).encode()).hexdigest()






