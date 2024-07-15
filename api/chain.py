from flask import Blueprint, current_app, jsonify

chain_bp = Blueprint('chain', __name__)

@chain_bp.route('/chain')
def chain_tree():
    blockchain = current_app.config['BLOCKCHAIN']
    response = {
        'chain': [block.to_dict() for block in blockchain.chain],
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200
