class ClickHouseAIError(Exception):
    pass


class TableNotFoundError(ClickHouseAIError):
    pass


class ConnectionError(ClickHouseAIError):
    pass