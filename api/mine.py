from flask import Blueprint, current_app, jsonify
from uuid import uuid4

import json
from chain.transaction import Transaction

mine_bp = Blueprint('mine', __name__)

@mine_bp.route('/mine')
def mining():
    blockchain = current_app.config['BLOCKCHAIN']
    node_identifier = current_app.config['NODE_IDETIFIER']

    last_block = blockchain.last_block
    last_proof = last_block.proof

    proof = blockchain.proof_of_work(last_proof)

    # receive a reward for finding the proof.
    transaction = Transaction(
        sender="0x",
        recipient=node_identifier,
        amount=1,
    )
    blockchain.new_transaction(transaction)

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'data': block.to_dict(),
    }
    return jsonify(response), 200
