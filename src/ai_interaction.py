```python
from openai import OpenAI
from config import OPENAI_API_KEY

class AIInteraction:
    def __init__(self):
        self.gpt3 = OpenAI(api_key=OPENAI_API_KEY)

    def interact_with_ai(self, message):
        response = self.gpt3.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
        )
        return response.choices[0].message['content']

ai_interaction = AIInteraction()
```