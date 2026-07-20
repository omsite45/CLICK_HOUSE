from .prompts import SYSTEM_PROMPT


class LLMMixin:

    # -----------------------------
    # Generic LLM Generation
    # -----------------------------
    def generate(self, prompt: str):
        """
        Send any prompt to the configured LLM provider.
        """
        return self.provider.generate(prompt)

    # -----------------------------
    # Natural Language -> SQL
    # -----------------------------
    def ask(self, question: str):

        schema = self.get_schema()

        sql = self.generate_sql(question, schema)

        print("\nGenerated SQL:\n")
        print(sql)

        return self.query_df(sql)

    def generate_sql(self, question, schema):

        prompt = self.build_sql_prompt(
            question=question,
            schema=schema
        )

        return self.generate(prompt)

    # -----------------------------
    # SQL Prompt Builder
    # -----------------------------
    def build_sql_prompt(self, question, schema):

        return f"""
You are an expert ClickHouse SQL generator.

Rules:

- Use ONLY the tables and columns in the schema.
- Never invent tables.
- Never invent columns.
- Generate valid ClickHouse SQL.
- Return ONLY SQL.

Schema:

{schema}

Question:

{question}
"""


    def repair_sql(
        self,
        question,
        schema,
        previous_sql,
        error,
    ):

        prompt = f"""
{SYSTEM_PROMPT}

Schema

{schema}

Question

{question}

Previous SQL

{previous_sql}

Database Error

{error}
"""

        return self.generate(prompt)