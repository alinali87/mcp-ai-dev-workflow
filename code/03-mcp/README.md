# Homework 3: MCP (Model Context Protocol)

AI Dev Tools Zoomcamp 2025 - Module 3

## Answers

### Question 1: FastMCP Hash
**Answer:** `sha256:aee50872923a9cba731861fc0120e7dbe4642a2685ba251b2b202b82fb6c25a9`

The first hash found in the wheels section of fastmcp in the `uv.lock` file.

### Question 2: FastMCP Transport
**Answer:** `STDIO`

When running a FastMCP server with `mcp.run()` or `mcp.run(transport="stdio")`, the default transport protocol is STDIO (Standard Input/Output).

### Question 3: Minsearch characters
**Answer:** `29184`

Character count when scraping https://github.com/alexeygrigorev/minsearch using Jina Reader (`r.jina.ai/` prefix).

### Question 4: Data in DataTalks.Club
**Answer:** `61`

Number of times the word "data" (case-insensitive, substring match) appears on https://datatalks.club/ when scraped using Jina Reader.

### Question 5: Search
**Answer:** `examples/testing_demo/README.md`

After indexing 259 markdown files from the FastMCP repository using minsearch and searching for the query "demo", the first returned result is `examples/testing_demo/README.md`.

## Repository Structure

```
code/03-mcp/
├── README.md (this file)
└── (homework solutions)
```

## Submission

Repository: https://github.com/alinali87/mcp-ai-dev-workflow
Folder: code/03-mcp
