class Commands:
 
    def showBlockchain(blockchain):
        for block in blockchain.block:
            print(block)

    def addTransaction(blockchain, transaction):
        sender = self.inputs("Enter sender: ")
        receiver = self.inputs("Enter receiver: ")
        amount = self.inputs("Enter amount: ")
        transaction.append(Transaction(sender, receiver, amount))
        blockchain.addTransaction(transaction, len(blockchain.block) - 1)

    def getData(typeOfData, message = "Enter option: "):
        option = None
        while typeOfData != type(option):
            try:
                option = int(input(message))
            except ValueError:
                print(f"Invalid input, insert a type: {typeOfData.__name__}")
        return option
    
    # TODO: Implement the necessary logic to select the correct option
    def selectOption(option, typeOfOption):
        if(option == 1):
            print("Showing Blockchain")
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            print("Exiting")

    #TODO: Implement the lines to make it prettier
    # Implement the logic to receive the necessary data to show the blockchain
    def startMenu():
        print("1. Show Blockchain")
        print("2. Mine Block")
        print("3. Add Transaction")
        print("4. Exit")
        data = Commands.getData(type(1))
        Commands.selectOption(data, type(1))


