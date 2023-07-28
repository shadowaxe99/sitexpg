```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Application
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenAI GPT-3
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # Ethereum
    ETHEREUM_PRIVATE_KEY = os.getenv('ETHEREUM_PRIVATE_KEY')
    ETHEREUM_NETWORK = os.getenv('ETHEREUM_NETWORK')

    # AWS
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION')

    # Google Cloud
    GOOGLE_CLOUD_PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
    GOOGLE_CLOUD_KEYFILE_JSON = os.getenv('GOOGLE_CLOUD_KEYFILE_JSON')
```
