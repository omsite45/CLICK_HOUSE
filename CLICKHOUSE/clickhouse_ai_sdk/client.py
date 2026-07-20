import clickhouse_connect
from .ingest import IngestionMixin
from .query import QueryMixin
from .metadata import MetadataMixin
from .llm import LLMMixin
from .embeddings import EmbeddingMixin
from .search import SearchMixin
from .retrieve import RetrievalMixin


class ClickHouseAI(IngestionMixin, QueryMixin, MetadataMixin,LLMMixin, EmbeddingMixin,SearchMixin, RetrievalMixin):

    def __init__(
        self,
        host="localhost",
        port=8123,
        database="default",
        user="default",
        password="admin123",
        provider=None,

    ):
        self.provider = provider
        self.client = clickhouse_connect.get_client(
            host=host,
            port=port,
            username=user,
            password=password,
            database=database,
        )

    def query(self, sql: str):
        result = self.client.query(sql)

        return {
            "columns": result.column_names,
            "rows": result.result_rows,
            "row_count": len(result.result_rows),
        }