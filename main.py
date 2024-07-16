from flask import Flask
from uuid import uuid4

from blockchain import Blockchain
from api.home import home_bp
from api.transaction import transaction_bp
from api.chain import chain_bp
from api.mine import mine_bp

app = Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(transaction_bp)
app.register_blueprint(chain_bp)
app.register_blueprint(mine_bp)

blockchain = Blockchain()

# Generate a globally unique address for this node
uuid = str(uuid4()).replace('-', '')
node_identifier = f"0x{uuid}"


app.config['BLOCKCHAIN'] = blockchain
app.config['NODE_IDETIFIER'] = node_identifier

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
