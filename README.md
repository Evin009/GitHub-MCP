# GitHub MCP Server - Architecture Flowchart

## Data Flow

```
User Request
    │
    ▼
┌─────────────────────────────────────┐
│   github_mcp_server.py              │
│   (Receives JSON-RPC Request)       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   github_api.py                     │
│   (Processes GitHub API Call)       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   GitHub Servers                    │
│   (Returns Data)                    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   github_api.py                     │
│   (Parses Response)                 │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   github_mcp_server.py              │
│   (Formats as JSON-RPC)             │
└──────────────┬──────────────────────┘
               │
               ▼
         Claude Response
         "You have 5 repos"
```

## Simple Linear Flow

```
User → MCP Server → GitHub API Handler → GitHub → Handler → MCP Server → Claude
```

## Component Responsibilities

| Component                | Does What                         |
| ------------------------ | --------------------------------- |
| **User/Claude**          | Sends natural language request    |
| **github_mcp_server.py** | Converts request to function call |
| **github_api.py**        | Calls GitHub API                  |
| **GitHub Servers**       | Returns actual data               |
| **Claude**               | Returns human-readable response   |
