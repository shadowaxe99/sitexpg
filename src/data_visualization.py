```python
import matplotlib.pyplot as plt
from database import db

def visualize_data():
    # Fetch data from the database
    ai_creation_data = db.session.query(AICharacter).all()
    transaction_data = db.session.query(NFT).all()

    # Prepare data for visualization
    ai_creation_count = len(ai_creation_data)
    transaction_count = len(transaction_data)

    # Create a bar chart for AI agent creation
    plt.figure(figsize=(10, 5))
    plt.bar(['AI Agent Creation'], [ai_creation_count], color='b')
    plt.title('AI Agent Creation')
    plt.xlabel('Activity')
    plt.ylabel('Count')
    plt.show()

    # Create a bar chart for transaction volume
    plt.figure(figsize=(10, 5))
    plt.bar(['Transaction Volume'], [transaction_count], color='r')
    plt.title('Transaction Volume')
    plt.xlabel('Activity')
    plt.ylabel('Count')
    plt.show()

    # Create a pie chart for token exchanges
    token_exchanges = [transaction.token_amount for transaction in transaction_data]
    plt.figure(figsize=(10, 5))
    plt.pie(token_exchanges, labels=[transaction.token_name for transaction in transaction_data])
    plt.title('Token Exchanges')
    plt.show()

    return 'data_visualized'
```