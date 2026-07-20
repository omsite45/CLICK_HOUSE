SYSTEM_PROMPT = """
You previously generated SQL that failed.

Your task is to repair it.

Rules:

- Use ONLY the schema provided.
- Never invent tables.
- Never invent columns.
- Fix ONLY the SQL.
- Return ONLY SQL.
"""

def build_prompt(schema, question):
    return f"""

            {SYSTEM_PROMPT}

            Database Schema:

            {schema}

            Question:

            {question}
            """