import json
import hashlib

from time import time
from typing import Optional

from chain import Block, Transaction

class Blockchain(object):
    def __init__(self):
          """
          Initialize a new Blockchain instance.

          Attributes:
              chain (List[Block]): The list of blocks in the blockchain.
              current_transactions (List[Transaction]): The list of transactions to be added to the next block.
          """
          self.chain = []
          self.current_transactions = []

    def new_block(self, proof: int, previous_hash: Optional[str] = None) -> Block:
        """
        Creates a new Block and adds it to the chain.

        Args:
            proof (int): The proof given by the Proof of Work algorithm.
            previous_hash (Optional[str]): Hash of previous Block. If None, will use the hash of the last block in the chain.

        Returns:
            Block: The newly created block.
        """
        block = Block(
            index=len(self.chain) + 1,
            timestamp=time(),
            transactions=self.current_transactions,
            proof=proof,
            previous_hash=previous_hash or self.hash(self.chain[-1]),
        )

        # Reset the current list of transactions
        self.current_transactions.clear()

        # Append the block to the chain
        self.chain.append(block)

        return block

    def new_transaction(self, transaction: Transaction) -> int:
        """
        Adds a new transaction to the list of transactions.

        Args:
            transaction (Transaction): The transaction to be added.

        Returns:
            int: The index of the block that will hold this transaction.
        """
        self.current_transactions.append(transaction)
        return self.last_block.index + 1

    def prof_of_work(self, last_proof: int) -> int:
        """
        Simple Proof of Work Algorithm

        Args:
            last_proof (int): the value of last proof

        Returns:
            proof (int)
        """

        proof = 0

        while self.valid_proof(last_proof=last_proof, current_proof=proof) is False:
            proof += 1

        return proof

    @staticmethod
    def hash(block: Block) -> str:
        """
        Creates a SHA-256 hash of a Block.

        Args:
            block (Block): The block to hash.

        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps(block.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def valid_proof(last_proof :int, current_proof: int) -> bool:
        """ Validates the Proof

        Args:
            last_proof (int): Previous Proof
            current_proof (int): Current Proof

        Returns:
            bool: the rusult of validation
        """

        guess = f'{last_proof}{current_proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def last_block(self) -> Block:
        """
        Returns the last Block in the chain.

        Returns:
            Block: The last block in the chain.
        """
        return self.chain[-1]
