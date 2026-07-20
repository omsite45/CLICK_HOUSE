import pandas as pd


class MetadataMixin:

    def get_schema(self):
        result = self.client.query("""
            SELECT
                table,
                name,
                type
            FROM system.columns
            WHERE database = currentDatabase()
            ORDER BY table, position
        """)

        return pd.DataFrame(
            result.result_rows,
            columns=result.column_names
        )

    def get_table_schema(self, table_name: str):
        result = self.client.query(f"""
            SELECT
                name,
                type
            FROM system.columns
            WHERE database = currentDatabase()
              AND table = '{table_name}'
            ORDER BY position
        """)

        return pd.DataFrame(
            result.result_rows,
            columns=result.column_names
        )
    
    def get_schema_for_llm(self):
        
        schema = {}

        tables = self.show_tables()

        for table in tables:

            columns = self.describe_table(table)

            schema[table] = {
                "columns": columns
            }

        return json.dumps(schema, indent=2)