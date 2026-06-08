# 🚀 AI PR Reviewer

An intelligent multi-agent Pull Request Review System that automatically analyzes code changes, generates structured feedback, prioritizes issues by severity, and posts review comments directly on GitHub Pull Requests.

Built using **FastAPI**, **Celery**, **Redis**, **LangGraph**, **LangFuse**, and **LLMs** to create a scalable and production-oriented AI code review pipeline.

---

## 🎯 Problem Statement

Code reviews are one of the most important parts of the software development lifecycle, but manual reviews are:

* Time-consuming
* Inconsistent
* Difficult to scale
* Dependent on reviewer expertise

AI PR Reviewer automates the review process using specialized AI agents that evaluate Pull Requests from multiple perspectives and provide actionable feedback directly within GitHub.

---

# 🎥 Demo Video

> **Demo Video:** Add your demo recording link here

```markdown
[Watch Demo](https://drive.google.com/file/d/1Z5bafOMbkvK_UWV8UMLvC8rS4RcN7xKZ/view?usp=sharing)
```

---

# 🏗️ Architecture

![AI PR Reviewer Architecture](./PR-Reviewer%20Architecture.png)

---

# ✨ Features

### 🤖 Multi-Agent AI Review System

Specialized agents analyze Pull Requests independently:

* Security Agent
* Performance Agent
* Code Quality Agent
* Architecture Agent

### ⚡ Asynchronous Processing

* Celery Workers
* Redis Message Broker
* Non-blocking PR analysis

### 🔄 LangGraph Orchestration

* Dynamic workflow execution
* Multi-agent coordination
* Centralized review pipeline

### 📊 Structured Review Generation

* Issue aggregation
* Deduplication
* Severity classification
* Summarization
* Formatting

### 🔗 GitHub Integration

* Webhook-based triggering
* Automatic PR commenting
* Pull Request metadata extraction

### 📈 Observability

* LangFuse tracing
* Request tracking
* Agent execution monitoring

---

# 🏛️ System Architecture

```text
GitHub Pull Request
        │
        ▼
 GitHub Webhook
        │
        ▼
 FastAPI Backend
        │
        ▼
 Redis Broker
        │
        ▼
 Celery Queue
        │
        ▼
 Celery Worker
        │
        ▼
 LangGraph Orchestrator
        │
 ┌──────┼────────┬────────┬────────┐
 ▼      ▼        ▼        ▼
Security Performance Quality Architecture
 Agent     Agent    Agent      Agent
 └────────┴────────┴──────────┘
                │
                ▼
         Aggregator Agent
                │
                ▼
        Review Formatter
                │
                ▼
      GitHub Comment API
                │
                ▼
     Pull Request Comment
```

---

# ⚙️ How It Works

## Step 1: Pull Request Event

A developer opens or updates a Pull Request.

GitHub sends a webhook event to the FastAPI backend.

---

## Step 2: Metadata Extraction

The backend extracts:

* Repository information
* Pull Request number
* Changed files
* Author information
* Code diff

---

## Step 3: Task Queueing

The review request is sent to Celery.

Redis acts as the message broker between the API layer and worker layer.

This prevents long-running AI reviews from blocking API requests.

---

## Step 4: Worker Execution

A Celery worker picks up the review task and starts the LangGraph workflow.

---

## Step 5: Multi-Agent Review

The LangGraph orchestrator coordinates multiple specialized review agents.

### 🔒 Security Agent

Reviews code for:

* Hardcoded secrets
* Authentication flaws
* SQL injection risks
* Security vulnerabilities

---

### ⚡ Performance Agent

Reviews code for:

* Expensive computations
* Memory inefficiencies
* Slow database access
* Optimization opportunities

---

### ✅ Quality Agent

Reviews code for:

* Readability issues
* Code smells
* Maintainability concerns
* Best-practice violations

---

### 🏛️ Architecture Agent

Reviews code for:

* Design issues
* Scalability concerns
* Modularity
* Architectural anti-patterns

---

## Step 6: Aggregation

All agent outputs are merged by the Aggregator Agent.

---

## Step 7: Review Formatting

The final review is:

* Summarized
* Deduplicated
* Severity-ranked
* Organized into a structured format

---

## Step 8: GitHub Commenting

The generated review is automatically posted as a Pull Request comment using the GitHub API.

---

# 🤖 AI Review Workflow

```text
PR Diff
   │
   ▼
LangGraph Orchestrator
   │
   ├── Security Agent
   ├── Performance Agent
   ├── Quality Agent
   └── Architecture Agent
   │
   ▼
Aggregator Agent
   │
   ▼
Formatter
   │
   ▼
GitHub Comment
```

---

# 📁 Project Structure

```text
AI-PR-REVIEWER/
│
├── app/
│   │
│   ├── agents/
│   │   ├── aggregate_agent.py
│   │   ├── architecture_agent.py
│   │   ├── performance_agent.py
│   │   ├── quality_agent.py
│   │   └── security_agent.py
│   │
│   ├── api/
│   │   ├── health.py
│   │   └── webhook.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logger.py
│   │
│   ├── formatters/
│   │
│   ├── graphs/
│   │   └── review_graph.py
│   │
│   ├── monitoring/
│   │   └── metrics.py
│   │
│   ├── prompts/
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │   ├── gemini_service.py
│   │   ├── github_service.py
│   │   ├── langfuse_service.py
│   │   └── pr_review_service.py
│   │
│   ├── utils/
│   │
│   └── workers/
│       ├── celery_app.py
│       └── review_tasks.py
│
├── main.py
├── README.md
├── pyproject.toml
├── .env
└── PR-Reviewer Architecture.png
```

---

# 🛠️ Technology Stack

| Category         | Technology     |
| ---------------- | -------------- |
| Backend          | FastAPI        |
| Language         | Python         |
| Task Queue       | Celery         |
| Message Broker   | Redis          |
| Agent Framework  | LangGraph      |
| LLM Provider     | Gemini         |
| Observability    | LangFuse       |
| Version Control  | GitHub         |
| Containerization | Docker         |
| Monitoring       | Custom Metrics |

---

# 📋 Example Review Output

```markdown
## AI Pull Request Review

### 🔴 Critical Issues

- Hardcoded API key detected in authentication service.

### 🟠 High Severity

- Database query executed inside nested loop.

### 🟡 Medium Severity

- Missing exception handling in payment workflow.

### 🔵 Low Severity

- Function naming convention does not follow project standards.

### Recommendations

- Move secrets to environment variables.
- Optimize database access patterns.
- Add proper exception handling.
```

---

# 📈 Scalability Considerations

The system is designed using an event-driven architecture.

### Horizontal Scaling

Additional Celery workers can be added to process more Pull Requests concurrently.

### Decoupled Components

FastAPI and Celery operate independently through Redis.

### Extensible Agent Architecture

New agents can be introduced without changing the overall workflow.

Examples:

* Documentation Agent
* Test Coverage Agent
* Dependency Review Agent
* Compliance Agent

---

# 🔭 Future Enhancements

* Prometheus Metrics
* Grafana Dashboards
* Slack Notifications
* Kafka Event Streaming
* Multi-Repository Dashboard
* Historical Review Analytics
* Team-Level Review Policies
* Custom Agent Marketplace

---

# 💡 Key Engineering Highlights

* Designed a distributed asynchronous review system.
* Implemented multi-agent AI orchestration using LangGraph.
* Automated Pull Request reviews using LLMs.
* Built scalable task processing with Celery and Redis.
* Integrated GitHub Webhooks and GitHub API automation.
* Added observability using LangFuse.
* Structured AI feedback using aggregation and formatting pipelines.

---

# 👨‍💻 Author

**Sai Satya Vardhan**

Backend Engineer • AI Engineer • Distributed Systems Enthusiast

If you found this project interesting, consider giving it a ⭐ on GitHub.

```
```
