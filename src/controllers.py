```python
from flask import request, jsonify
from src import app, db, gpt3, nft
from src.models import Investor, AICharacter, NFT
from src.ai_interaction import interact_with_ai
from src.nft_minting import mint_nft
from src.personalization_system import personalize_ai
from src.data_visualization import visualize_data

@app.route('/embed_deck', methods=['POST'])
def embed_deck():
    url = request.json.get('url')
    # Embed the deck here
    # Send a message when the deck is embedded
    return jsonify({'message': 'deck_embedded'}), 200

@app.route('/ai_interaction', methods=['POST'])
def ai_interaction():
    investor_id = request.json.get('investor_id')
    message = request.json.get('message')
    investor = Investor.query.get(investor_id)
    if not investor:
        return jsonify({'message': 'Investor not found'}), 404
    response = interact_with_ai(investor, message)
    return jsonify({'message': 'ai_interaction', 'response': response}), 200

@app.route('/mint_nft', methods=['POST'])
def mint_nft_route():
    investor_id = request.json.get('investor_id')
    ai_character_id = request.json.get('ai_character_id')
    investor = Investor.query.get(investor_id)
    ai_character = AICharacter.query.get(ai_character_id)
    if not investor or not ai_character:
        return jsonify({'message': 'Investor or AI Character not found'}), 404
    nft_token = mint_nft(investor, ai_character)
    return jsonify({'message': 'nft_minted', 'nft_token': nft_token}), 200

@app.route('/personalize_ai', methods=['POST'])
def personalize_ai_route():
    investor_id = request.json.get('investor_id')
    preferences = request.json.get('preferences')
    investor = Investor.query.get(investor_id)
    if not investor:
        return jsonify({'message': 'Investor not found'}), 404
    personalize_ai(investor, preferences)
    return jsonify({'message': 'ai_personalized'}), 200

@app.route('/live_mint', methods=['POST'])
def live_mint():
    investor_id = request.json.get('investor_id')
    investor = Investor.query.get(investor_id)
    if not investor:
        return jsonify({'message': 'Investor not found'}), 404
    # Live minting process here
    return jsonify({'message': 'live_minting'}), 200

@app.route('/visualize_data', methods=['GET'])
def visualize_data_route():
    data = visualize_data()
    return jsonify({'message': 'data_visualized', 'data': data}), 200
```