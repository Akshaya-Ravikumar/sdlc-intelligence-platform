# SDLC Intelligence Platform

## Overview

SDLC Intelligence Platform is an AI-powered Change Impact Analysis system that helps engineering teams assess the impact of software changes across the Software Development Lifecycle (SDLC).

The platform uses:

* LangGraph for agent orchestration
* OpenAI GPT-4.1 Mini for reasoning
* ChromaDB for vector storage
* RAG (Retrieval Augmented Generation)
* Sentence Transformers for embeddings

The system analyzes architecture documents, API specifications, and historical incident reports to provide:

* Dependency Analysis
* Incident Analysis
* Test Recommendations
* Risk Assessment
* Change Impact Reports

---

## Project Structure

```text
sdlc-intelligence/

├── app.py

├── agents/
│   ├── llm.py
│   ├── planner_agent.py
│   ├── dependency_agent.py
│   ├── incident_agent.py
│   ├── test_agent.py
│   ├── risk_agent.py
│   └── report_agent.py

├── orchestration/
│   ├── workflow.py
│   ├── router.py
│   └── state.py

├── knowledge/
│   ├── chroma_store.py
│   ├── document_loader.py
│   ├── retrieval.py
│   └── ingest.py

├── data/
│   ├── architecture_docs/
│   └── incident_docs/

├── chroma_db/

├── requirements.txt

└── .env
```

---

## Prerequisites

### Python

Python 3.11 or above

Verify installation:

```bash
python --version
```

### OpenAI API Key

Generate an API key from:

https://platform.openai.com/api-keys

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>

cd sdlc-intelligence
```

### 2. Create Virtual Environment

Mac/Linux:

```bash
python -m venv venv

source venv/bin/activate
```

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your-openai-api-key
```

---

## Supported Knowledge Sources

The ingestion pipeline supports the following file types:

```text
.pdf
.txt
.md
.yaml
.yml
.json
.csv
```

---

## Adding Knowledge Documents

### Architecture Documents

Place files under:

```text
data/architecture_docs/
```

Example:

```text
transaction_service.txt
fraud_service.txt
statement_service.txt
transaction_api.yml
notification_service.yml
```

### Incident Reports

Place files under:

```text
data/incident_docs/
```

Example:

```text
inc_1045.txt
inc_1178.txt
inc_1290.txt
```

---

## Building the Knowledge Base

Documents must be ingested before running the application.

Run:

```bash
python -m knowledge.ingest
```

Expected Output:

```text
========== INGESTION STARTED ==========

Scanning Folder: ./data/architecture_docs

Files Found: 8

Processing: transaction_service.txt
Added 2 chunks

Processing: fraud_service.txt
Added 1 chunks

Processing: transaction_api.yml
Added 1 chunks

Total Chunks Added: 8

Scanning Folder: ./data/incident_docs

Files Found: 3

Processing: inc_1045.txt
Added 1 chunks

Processing: inc_1178.txt
Added 1 chunks

Processing: inc_1290.txt
Added 1 chunks

Total Chunks Added: 3

========== COLLECTION STATS ==========

Architecture Count: 8
Incident Count: 3

========== INGESTION COMPLETE ==========
```

---

## Running the Application

Execute:

```bash
python app.py
```

Example Query:

```python
result = run_query(
    "What is the impact of changing Transaction Service API?"
)

print(result["final_report"])
```

---

## Agent Workflow

```text
User Query
     │
     ▼

Planner Agent
     │
     ▼

Dependency Agent
     │
     ▼

Incident Agent
     │
     ▼

Test Agent
     │
     ▼

Risk Agent
     │
     ▼

Report Agent
     │
     ▼

Change Impact Analysis Report
```

---

## Agent Responsibilities

### Planner Agent

* Understand user query
* Extract service name
* Identify change type
* Generate execution plan

### Dependency Agent

* Retrieve architecture documents
* Identify affected systems
* Identify dependent services
* Identify impacted APIs

### Incident Agent

* Retrieve historical incidents
* Analyze root causes
* Extract lessons learned

### Test Agent

* Recommend test scenarios
* Suggest regression testing strategy
* Recommend integration testing

### Risk Agent

* Assess deployment risk
* Generate risk score
* Recommend deployment strategy

### Report Agent

* Consolidate all findings
* Generate final impact analysis report

---

## Supported Change Types

The Planner Agent automatically classifies:

```text
API Change
Database Change
Bug Fix
Configuration Change
New Feature
Service Migration
Deployment Change
General Change
```

---

## Example Queries

```text
What is the impact of changing Transaction Service API?

What is the risk of modifying Fraud Monitoring Service?

Which systems are affected if Notification Service changes?

What tests should be executed for Payment Service?

Show previous incidents related to Transaction Service.
```

---

## Rebuilding ChromaDB

If documents change or the vector database becomes corrupted:

Delete the existing database:

Mac/Linux:

```bash
rm -rf chroma_db
```

Windows:

```cmd
rmdir /s chroma_db
```

Rebuild:

```bash
python -m knowledge.ingest
```

---

## Troubleshooting

### ModuleNotFoundError: No module named 'knowledge'

Run ingestion from the project root:

```bash
python -m knowledge.ingest
```

Do not run:

```bash
python knowledge/ingest.py
```

---

### Architecture Count = 0

Verify documents exist under:

```text
data/architecture_docs/
```

Then rerun:

```bash
python -m knowledge.ingest
```

---

### Incident Count = 0

Verify documents exist under:

```text
data/incident_docs/
```

---

### OpenAI Authentication Error

Verify:

```env
OPENAI_API_KEY=<valid-key>
```

exists in `.env`.

---

## Technology Stack

| Component           | Technology                             |
| ------------------- | -------------------------------------- |
| Agent Orchestration | LangGraph                              |
| LLM                 | OpenAI GPT-4.1 Mini                    |
| Embeddings          | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database     | ChromaDB                               |
| Chunking            | LangChain Text Splitter                |
| Language            | Python                                 |
| Retrieval           | Custom RAG Pipeline                    |

---

## Future Enhancements

* FastAPI Backend
* React UI
* Jira Integration
* Confluence Integration
* ServiceNow Integration
* Graph-based Dependency Visualization
* Deterministic Risk Scoring
* Source Citations and Traceability
* Live Risk Monitoring
* Deployment Approval Workflow
* Source citations in responses
* Deterministic risk scoring
* Team notification recommendations

---

## Author

Akshaya Ravikkumar