import pandas as pd


class QueryMixin:

    def show_tables(self):
        result = self.client.query("SHOW TABLES")
        return [row[0] for row in result.result_rows]

    def describe_table(self, table_name: str):
        result = self.client.query(f"DESCRIBE TABLE {table_name}")

        return pd.DataFrame(
            result.result_rows,
            columns=result.column_names
        )
    
    def describe_table(self, table):

        result = self.client.query(f"DESCRIBE TABLE {table}")

        columns = []

        for row in result.result_rows:

            columns.append({
                "name": row[0],
                "type": row[1]
            })

        return columns




    def table_exists(self, table_name: str):
        result = self.client.query(
            f"""
            SELECT count()
            FROM system.tables
            WHERE database = currentDatabase()
              AND name = '{table_name}'
            """
        )

        return result.result_rows[0][0] > 0

    def drop_table(self, table_name: str):
        self.client.command(f"DROP TABLE IF EXISTS {table_name}")
        return {"status": "success"}

    def query_df(self, sql: str):
        result = self.client.query(sql)

        return pd.DataFrame(
            result.result_rows,
            columns=result.column_names
        )
    def head(self, table_name: str, limit: int = 5):
            
        return self.query_df(
            f"SELECT * FROM {table_name} LIMIT {limit}"
        )
    def count(self, table_name: str):
        result = self.client.query(
            f"SELECT count() FROM {table_name}"
        )
        return result.result_rows[0][0]
    
    def execute(self, sql: str):
        return self.query(sql)
    
    def list_databases(self):
            
        result = self.client.query("SHOW DATABASES")
        return [row[0] for row in result.result_rows]
    
    def create_database(self, database_name: str):
            
        self.client.command(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        return {"status": "success"}

    def use_database(self, database_name: str):
            
        self.client.command(f"USE DATABASE {database_name}")
        return {"status": "success"}