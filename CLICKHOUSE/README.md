# ClickHouse AI SDK

## Overview

A lightweight Python SDK for AI-powered interaction with ClickHouse.

## Features

-   Data ingestion
-   SQL queries
-   Metadata discovery
-   Embeddings
-   Semantic search
-   Hybrid search
-   Retrieval-Augmented Generation (RAG)
-   Natural Language to SQL

## Installation

``` bash
pip install -r requirements.txt
```

## Quick Start

``` python
from clickhouse_ai_sdk import ClickHouseAI

sdk = ClickHouseAI(...)

sdk.create_embeddings("products")

answer = sdk.chat(
    table="products",
    question="Which brands sell headphones?"
)
print(answer)
```

## Architecture

User Question → Embedding → ClickHouse Vector Search → Retrieved Context
→ Prompt → LLM → Answer

## Project Structure

``` text
clickhouse_ai_sdk/
├── client.py
├── ingest.py
├── query.py
├── metadata.py
├── embeddings.py
├── providers.py
├── llm.py
├── search.py
├── retrieve.py
└── prompts.py
```

## Future Improvements

-   Streaming
-   Conversation memory
-   Source attribution
-   Document loaders
-   Evaluation
