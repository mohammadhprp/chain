from api.model.serializable import Serializable

class Transaction(Serializable):
    """A class used to represent a Transaction in a blockchain.

    Attributes:
        sender (str): The address of sender
        recipient (str): The address of recipient
        amount (float): A amount of transaction
    """
    def __init__(self,
                 sender: str,
                 recipient: str,
                 amount: float) -> None:
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        """
        Convert the Transaction object to a dictionary representation.

        Returns:
            dict: A dictionary containing the sender, recipient, and amount of the transaction.
        """
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
        }
