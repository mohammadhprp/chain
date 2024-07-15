from marshmallow import Schema, fields

class TransactionSchema(Schema):
    sender = fields.Str(required=True)
    recipient = fields.Str(required=True)
    amount = fields.Float(required=True)
