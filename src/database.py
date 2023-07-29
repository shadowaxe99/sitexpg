```python
from flask_sqlalchemy import SQLAlchemy
from src.config import Config

# Initialize database instance
db = SQLAlchemy()

def init_app(app):
    # Set the app's configuration
    app.config.from_object(Config)
    
    # Bind the app to the database
    db.init_app(app)

    # Create all tables
    with app.app_context():
        db.create_all()
```