```python
from flask import Flask
from src.database import db
from src.routes import setup_routes
from src.ai_interaction import gpt3
from src.nft_minting import nft

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')

    db.init_app(app)
    gpt3.init_app(app)
    nft.init_app(app)

    with app.app_context():
        db.create_all()
        setup_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
```