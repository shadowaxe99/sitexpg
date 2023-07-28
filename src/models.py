```python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()

class Investor(db.Model):
    __tablename__ = 'investors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    preferences = db.Column(JSON)

    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences

    def __repr__(self):
        return '<id {}>'.format(self.id)


class AICharacter(db.Model):
    __tablename__ = 'ai_characters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    personality = db.Column(JSON)

    def __init__(self, name, personality):
        self.name = name
        self.personality = personality

    def __repr__(self):
        return '<id {}>'.format(self.id)


class NFT(db.Model):
    __tablename__ = 'nfts'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('investors.id'))
    ai_character_id = db.Column(db.Integer, db.ForeignKey('ai_characters.id'))
    metadata = db.Column(JSON)

    def __init__(self, owner_id, ai_character_id, metadata):
        self.owner_id = owner_id
        self.ai_character_id = ai_character_id
        self.metadata = metadata

    def __repr__(self):
        return '<id {}>'.format(self.id)
```