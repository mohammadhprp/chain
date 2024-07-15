from typing import List, Optional

from .transaction import Transaction
from api.model.serializable import Serializable

class Block(Serializable):
    """A class used to represent a Block in a blockchain.

    Attributes:
        index (int): The index of the block in the blockchain.
        timestamp (float): The time when the block was created.
        transactions (List[object]): A list of transactions included in the block.
        proof (int): The proof of work for the block.
        previous_hash (Optional[str]): The hash of the previous block in the blockchain.
    """
    def __init__(self,
                 index: int,
                 timestamp: float,
                 transactions: List[Transaction],
                 proof: int,
                 previous_hash: Optional[str]) -> None:
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash

    def to_dict(self):
        """
        Convert the Block object to a dictionary representation.

        Returns:
            dict: A dictionary containing the index, previous hash, timestamp,
                transactions (converted to dictionaries), proof, and timestamp of the block.
        """
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'transactions': [transaction.to_dict() for transaction in self.transactions],
            'proof': self.proof,
            'timestamp': self.timestamp,
        }
