import pandas as pd


class SchemaInferer:

    TYPE_MAPPING = {
        "int64": "Int64",
        "int32": "Int32",
        "float64": "Float64",
        "float32": "Float32",
        "bool": "Bool",
        "object": "String",
        "string": "String",
        "datetime64[ns]": "DateTime",
    }

    @classmethod
    def infer(cls, dataframe: pd.DataFrame):

        columns = []

        for column, dtype in dataframe.dtypes.items():

            clickhouse_type = cls.TYPE_MAPPING.get(
                str(dtype).lower(),
                "String"
            )

            columns.append(f"{column} {clickhouse_type}")

        return columns