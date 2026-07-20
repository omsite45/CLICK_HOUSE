import pandas as pd
from .schema import SchemaInferer
class IngestionMixin:

    def ingest(
        self,
        table_name: str,
        records,
        create_table=True,
    ):
        if isinstance(records, pd.DataFrame):
            df = records.copy()

        elif isinstance(records, list):
            df = pd.DataFrame(records)

        else:
            raise TypeError(
                "records must be a pandas DataFrame or list of dictionaries"
            )

        return self.ingest_dataframe(
            table_name=table_name,
            dataframe=df,
            create_table=create_table,
        )

    def ingest_dataframe(
        self,
        table_name: str,
        dataframe: pd.DataFrame,
        create_table=False,
    ):
        if create_table:
            
            cols = SchemaInferer.infer(dataframe)

            sql = f"""
            CREATE TABLE IF NOT EXISTS {table_name}
            (
                {",".join(cols)}
            )
            ENGINE = MergeTree()
            ORDER BY tuple()
            """

            self.client.command(sql)

        self.client.insert_df(table_name, dataframe)

        return {
            "status": "success",
            "rows": len(dataframe),
        }