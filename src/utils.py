```python
import requests
from flask import jsonify

def embed_deck(deck_url):
    try:
        response = requests.get(deck_url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as err:
        return jsonify({"message": "HTTP error occurred", "error": str(err)}), 400
    except requests.exceptions.RequestException as err:
        return jsonify({"message": "Error occurred", "error": str(err)}), 400

def interact_with_ai(gpt3, message):
    try:
        response = gpt3.complete_prompt(message, max_tokens=60)
        return response.choices[0].text.strip()
    except Exception as err:
        return jsonify({"message": "AI interaction error occurred", "error": str(err)}), 400

def mint_nft(nft, ai_character):
    try:
        token_id = nft.mint(ai_character)
        return token_id
    except Exception as err:
        return jsonify({"message": "NFT minting error occurred", "error": str(err)}), 400

def personalize_ai(nlp, preferences, ai_character):
    try:
        personalized_character = nlp.personalize(ai_character, preferences)
        return personalized_character
    except Exception as err:
        return jsonify({"message": "AI personalization error occurred", "error": str(err)}), 400

def live_mint(nft, ai_character):
    try:
        token_id = nft.mint(ai_character)
        return token_id
    except Exception as err:
        return jsonify({"message": "Live minting error occurred", "error": str(err)}), 400

def visualize_data(db):
    try:
        data = db.get_all_data()
        return data
    except Exception as err:
        return jsonify({"message": "Data visualization error occurred", "error": str(err)}), 400
```