from typing import List, Optional


class Block:
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
                 transactions: List[object],
                 proof: int,
                 previous_hash: Optional[str]) -> None:
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.prood = proof
        self.previous_hash = previous_hash
