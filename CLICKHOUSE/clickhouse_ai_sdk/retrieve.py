class RetrievalMixin:
    """
    Retrieval-Augmented Generation (RAG) utilities.
    """

    def retrieve(
        self,
        table,
        query,
        top_k=5,
        filters=None,
    ):
        """
        Retrieve the most relevant documents using semantic search.
        """
        return self.semantic_search(
            table=table,
            query=query,
            top_k=top_k,
            filters=filters,
        )

    def retrieve_context(
        self,
        table,
        query,
        text_column="description",
        top_k=5,
        filters=None,
    ):
        """
        Retrieve documents and concatenate them into a single context string.
        """
        docs = self.retrieve(
            table=table,
            query=query,
            top_k=top_k,
            filters=filters,
        )

        if docs.empty:
            return ""

        if text_column not in docs.columns:
            raise ValueError(
                f"Column '{text_column}' not found in retrieved documents."
            )

        return "\n\n".join(
            docs[text_column].fillna("").astype(str)
        )

    def build_rag_prompt(
        self,
        table,
        question,
        text_column="description",
        top_k=5,
        filters=None,
    ):
        """
        Build a prompt for Retrieval-Augmented Generation.
        """

        context = self.retrieve_context(
            table=table,
            query=question,
            text_column=text_column,
            top_k=top_k,
            filters=filters,
        )

        return f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the retrieved context below.

If the answer is not present in the context, reply:

"I don't know based on the available data."

==========================
Context
==========================

{context}

==========================
Question
==========================

{question}

==========================
Answer
==========================
"""

    def chat(
    self,
    table,
    question,
    text_column="description",
    top_k=5,
    filters=None,
    system_prompt=None,
):
            

        prompt = self.build_rag_prompt(
            table=table,
            question=question,
            text_column=text_column,
            top_k=top_k,
            filters=filters,
        )

        if system_prompt:
            prompt = system_prompt + "\n\n" + prompt

        return self.generate(prompt)