```python
from flask import render_template
from src.controllers import interact_with_ai, mint_nft, personalize_ai, live_mint, visualize_data

def setup_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/interactive-deck')
    def interactive_deck():
        return render_template('interactive_deck.html')

    @app.route('/ai-character-demo', methods=['GET', 'POST'])
    def ai_character_demo():
        message = interact_with_ai()
        return render_template('ai_character_demo.html', message=message)

    @app.route('/nft-wallet-showcase', methods=['GET', 'POST'])
    def nft_wallet_showcase():
        message = mint_nft()
        return render_template('nft_wallet_showcase.html', message=message)

    @app.route('/personalized-ai-experience', methods=['GET', 'POST'])
    def personalized_ai_experience():
        message = personalize_ai()
        return render_template('personalized_ai_experience.html', message=message)

    @app.route('/live-minting', methods=['GET', 'POST'])
    def live_minting():
        message = live_mint()
        return render_template('live_minting.html', message=message)

    @app.route('/data-visualization', methods=['GET', 'POST'])
    def data_visualization():
        message = visualize_data()
        return render_template('data_visualization.html', message=message)
```