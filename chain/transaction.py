class Transaction:
    """A class used to represent a Transaction in a blockchain.

    Attributes:
        sender (str): The address of sender
        recpient (str): The address of recpient
        amount (float): A amount of transaction
    """
    def __init__(self,
                 sender: str,
                 recipent: str,
                 amount: float) -> None:
        self.sender = sender
        self.recipent = recipent
        self.amount = amount
