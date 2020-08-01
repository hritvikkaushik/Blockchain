class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        #Create and add new block to chain
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount: <int> Amount
        :return: <int> Index of block that will hold this transaction. 
        """
        
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1


    @staticmethod
    def hash(block):
        #Hash a block
        pass

    @property
    def last_block(self):
        #Return last block in the chain
        pass
