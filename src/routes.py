```python
from flask import render_template, request, jsonify
from src import app
from src.controllers import interact_with_ai, mint_nft, personalize_ai, live_mint, visualize_data, embed_deck

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/interactive-deck', methods=['GET', 'POST'])
def interactive_deck():
    if request.method == 'POST':
        url = request.form.get('url')
        embed_deck(url)
        return jsonify({'message': 'deck_embedded'}), 200
    return render_template('interactive_deck.html')

@app.route('/ai-character-demo', methods=['GET', 'POST'])
def ai_character_demo():
    if request.method == 'POST':
        message = request.form.get('message')
        response = interact_with_ai(message)
        return jsonify({'message': 'ai_interaction', 'response': response}), 200
    return render_template('ai_character_demo.html')

@app.route('/nft-wallet-showcase', methods=['GET', 'POST'])
def nft_wallet_showcase():
    if request.method == 'POST':
        mint_nft()
        return jsonify({'message': 'nft_minted'}), 200
    return render_template('nft_wallet_showcase.html')

@app.route('/personalized-ai-experience', methods=['GET', 'POST'])
def personalized_ai_experience():
    if request.method == 'POST':
        preferences = request.form.get('preferences')
        personalize_ai(preferences)
        return jsonify({'message': 'ai_personalized'}), 200
    return render_template('personalized_ai_experience.html')

@app.route('/live-minting', methods=['GET', 'POST'])
def live_minting():
    if request.method == 'POST':
        live_mint()
        return jsonify({'message': 'live_minting'}), 200
    return render_template('live_minting.html')

@app.route('/data-visualization', methods=['GET'])
def data_visualization():
    data = visualize_data()
    return render_template('data_visualization.html', data=data)
```