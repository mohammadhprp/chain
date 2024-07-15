from flask import Blueprint, jsonify, request, current_app
from marshmallow import validates, ValidationError

from chain import Transaction
from .schemas import TransactionSchema

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/transactions', methods=['POST'])
def new_transaction():
    values = request.get_json()


    # Check that the required fields are in the POST'ed data
    transaction_schema = TransactionSchema()
    try:
        validated_data = transaction_schema.load(values)
    except ValidationError as err:
        return jsonify({"message": "Invalid data", "errors": err.messages}), 400

    blockchain = current_app.config['BLOCKCHAIN']

    # Create a new Transaction
    transaction = Transaction(
        sender=values['sender'],
        recipient= values['recipient'],
        amount=values['amount']
    )
    index = blockchain.new_transaction(transaction)

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201
