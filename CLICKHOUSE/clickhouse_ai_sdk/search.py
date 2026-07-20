import numpy as np
import pandas as pd


class SearchMixin:

    def create_embeddings(
        self,
        table,
        id_column,
        text_column,
        batch_size=250,
    ):
        

        # Read ALL columns from source table
        df = self.query_df(f"""
            SELECT *
            FROM {table}
        """)

        embedding_table = f"{table}_embeddings"

        # Drop and recreate embedding table
        self.execute(f"DROP TABLE IF EXISTS {embedding_table}")

        # Get schema from source table
        schema = self.query_df(f"""
            DESCRIBE TABLE {table}
        """)

        columns = []

        for _, row in schema.iterrows():
            columns.append(f"{row['name']} {row['type']}")

        columns.append("embedding Array(Float32)")

        create_sql = f"""
        CREATE TABLE {embedding_table}
        (
            {', '.join(columns)}
        )
        ENGINE = MergeTree()
        ORDER BY {id_column}
        """

        self.execute(create_sql)

        total_rows = len(df)

        print(f"Creating embeddings for {total_rows} rows...")

        for start in range(0, total_rows, batch_size):

            batch = df.iloc[start:start + batch_size]

            texts = batch[text_column].tolist()

            vectors = self.embed_batch(texts)

            batch_rows = []

            for (_, row), vector in zip(batch.iterrows(), vectors):

                record = row.to_dict()

                record["embedding"] = vector

                batch_rows.append(record)

            batch_df = pd.DataFrame(batch_rows)

            self.ingest(
                table_name=embedding_table,
                records=batch_df,
            )

            print(
                f"Processed {min(start + batch_size, total_rows)}/{total_rows}"
            )

        print("Embedding generation completed.")

        return self.query_df(
            f"SELECT * FROM {embedding_table}"
        )


    def semantic_search(
    self,
    table,
    query,
    filters=None,
    top_k=5,
):
            

        embedding_table = f"{table}_embeddings"

        query_vector = self.embed(query)

        vector_sql = "[" + ",".join(
            str(float(x))
            for x in query_vector
        ) + "]"

        where_clause = ""

        if filters:

            conditions = []

            for column, value in filters.items():

                conditions.append(
                    f"{column} = '{value}'"
                )

            where_clause = "WHERE " + " AND ".join(conditions)

        sql = f"""
        SELECT
            *,
            cosineDistance(
                embedding,
                {vector_sql}
            ) AS distance
        FROM {embedding_table}
        {where_clause}
        ORDER BY distance ASC
        LIMIT {top_k}
        """

        return self.query_df(sql)