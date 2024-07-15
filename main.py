from flask import Flask

from blockchain import Blockchain
from api.home import home_bp
from api.transaction import transaction_bp
from api.chain import chain_bp

app = Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(transaction_bp)
app.register_blueprint(chain_bp)

blockchain = Blockchain()

app.config['BLOCKCHAIN'] = blockchain

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
