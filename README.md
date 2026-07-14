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
                 User
                  |
                  v
              Memory
                  |
                  v
             AI Planner
                  |
                  |
        +---------+---------+
        |                   |
        v                   v
    Employee Tool          RAG Tool
        |                   |
        +---------+---------+
                    |
                    v
                Summarizer
                    |
                    v
                Memory Update
                    |
                    v
                Final Response
