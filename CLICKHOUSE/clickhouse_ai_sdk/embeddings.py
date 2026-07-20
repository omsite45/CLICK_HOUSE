class EmbeddingMixin:

    def embed(self, text):

        return self.provider.embed(text)
    

    def embed_batch(self, texts):
        return self.provider.embed_batch(texts)
