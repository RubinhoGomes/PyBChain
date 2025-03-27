import socket
from dataclasses import dataclass



class NetState:
    PING = 'PING' #TODO: [] Implement this ping to check if the server is up
    PONG = 'PONG' #TODO: [] Implement this pong to check if the client is up
    CONNECT = 'CONNECT' #TODO: [] Implement this to Create an user and his hash and send Blockchain Ping
    DISONNECT = 'DISCONNECT' #TODO: [] Implement this to disconnect the user
    MINE = 'MINE' #TODO: [] Implement this to mine the block
    BLOCKCHAIN = 'BLOCKCHAIN' #TODO: [] Send the blockchain through the network
    TRANSACTION = 'TRANSACTION' #TODO: [] Send the transaction through the network
    TRANSACTION_ADD = 'TRANSACTION_ADD' #TODO: [] Begin the add an transaction process, The user will choose from a list the user ID after will choose the amount and FINISH
    TRANSACTION_VIEW = 'TRANSACTION_VIEW' #TODO: [] Will show all the user pending transactions, or don't know how to show all the transactions, but probably "locally"

class Network:

