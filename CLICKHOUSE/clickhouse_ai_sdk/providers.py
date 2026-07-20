from urllib import response

from openai import OpenAI
import os

class BaseProvider:

    def generate(self, prompt: str):
        raise NotImplementedError

    def embed(self, text: str):
        raise NotImplementedError


class OpenAIProvider(BaseProvider):

    def __init__(
        self,
        model="gpt-4.1-mini",
        embedding_model="text-embedding-3-small",
    ):

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set.")

        self.client = OpenAI(api_key=api_key)

        self.model = model
        self.embedding_model = embedding_model   # <-- THIS LINE IS REQUIRED

    def generate(self, prompt: str):

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        sql = response.output_text.strip()
        sql = sql.replace("```sql", "").replace("```", "")
        return sql

    def embed(self, text: str):

        response = self.client.embeddings.create(
            model=self.embedding_model,
            input=text,
        )

        return response.data[0].embedding
    
    def embed_batch(self, texts):
        
        response = self.client.embeddings.create(
            model=self.embedding_model,
            input=texts
        )

        return [item.embedding for item in response.data]