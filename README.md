Built an autonomous enterprise AI agent with planning, tool execution, retrieval augmentation, memory, evaluation, and self-correction capabilities.
# Architecure
                    User
                      │
                      ▼
                Agent Orchestrator
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
    Planner        Tool Executor     Memory
    │               │                │
    └───────────────┼────────────────┘
                    ▼
        MCP Enterprise Gateway
        ┌────────────┼──────────────┐
        ▼            ▼              ▼
        RAG API     Employee API   Ticket API
                     │
                     ▼
                Gather Results
                     │
                     ▼
                 Response Evaluator
                     │
                     ▼
                Final Response

# Real Agent Pattern
autonomous-enterprise-agent

                 User Request
                      |
                      v
                  Agent
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
     Memory       Planner       Executor
                                  |
                    +-------------+-------------+
                    |                           |
                    v                           v
             Employee Tool                 RAG Tool
                    |                           |
                    +-------------+-------------+
                                  |
                                  v
                              Summary
                                  |
                                  v
                             Evaluator
                                  |
                         +--------+--------+
                         |                 |
                       PASS              FAIL


# Enterprise Multi-Agent System

    Supervisor Agent
    |
    +---- HR Agent
    |
    +---- Knowledge Agent
    |
    +---- Report Agent

# Technologies Used
langchain, langgraph, ollama, python, pydantic, fastapi, uvicorn, pytest, pytest-asyncio, pytest-mock

