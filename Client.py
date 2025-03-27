import socket

class Client():

    def client():
        # Create a socket object
        s = socket.socket()

        # Get local machine name
        host = socket.gethostname()
        port = 12345

        # Connect to the server
        s.connect((host, port))

        msg = s.recv(1024)

        while True:
            send = input("Send a message: ")
            s.send(send.encode())
            

        s.close()

    if __name__ == '__main__':
        client()
