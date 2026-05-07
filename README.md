# 🚀 Agentic Workflow System

A production-style multi-agent AI orchestration system built with:

- FastAPI
- LangGraph
- ChromaDB
- HuggingFace
- Streamlit
- Retrieval-Augmented Generation (RAG)

This project demonstrates how modern AI systems are evolving from simple chatbots into orchestrated multi-agent workflows capable of routing, retrieval, reasoning, and specialized task execution.

---

# 🧠 What Makes This Project Different?

Most beginner AI projects are:

- single LLM calls
- prompt wrappers
- basic chatbots

This system is different.

It introduces:

✅ Multi-Agent Architecture  
✅ Agent Routing  
✅ Stateful Workflow Orchestration  
✅ Retrieval-Augmented Generation (RAG)  
✅ Vector Search  
✅ Specialized AI Agents  
✅ Modular AI Pipelines  

This is much closer to how real-world AI systems are being designed today.

---

# ⚡ System Architecture

```text
                ┌─────────────────────┐
                │     User Query      │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │    Router Agent     │
                └─────────┬───────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼

┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ Healthcare AI  │ │  Finance AI    │ │   Coding AI    │
└────────┬───────┘ └────────┬───────┘ └────────┬───────┘
         │                  │                  │
         ▼                  ▼                  ▼

   ┌─────────────────────────────────────────────┐
   │         Retriever + Vector Search           │
   └─────────────────────────────────────────────┘
                           │
                           ▼
               ┌─────────────────────┐
               │   LLM Generator     │
               └─────────────────────┘
                           │
                           ▼
               ┌─────────────────────┐
               │    Final Response   │
               └─────────────────────┘
```

---

# 🔥 Core Features

## 🧠 Multi-Agent Routing

The system intelligently routes user queries to specialized agents:

| Agent | Responsibility |
|---|---|
| Healthcare Agent | Medical + healthcare queries |
| Finance Agent | Financial + investment queries |
| Coding Agent | Programming + debugging queries |

---

## 📚 RAG Pipeline

The Healthcare Agent uses a Retrieval-Augmented Generation pipeline:

### Workflow:
1. Upload PDFs
2. Split documents into chunks
3. Generate embeddings
4. Store vectors in ChromaDB
5. Perform semantic retrieval
6. Generate grounded answers

---

## 🔎 Semantic Search

Instead of keyword matching, the system uses embeddings to retrieve semantically relevant information from uploaded documents.

---

## ⚙️ LangGraph Orchestration

LangGraph powers:

- conditional routing
- state management
- workflow execution
- agent transitions
- graph-based orchestration

---

## 🌐 FastAPI Backend

The backend provides:

- REST API endpoints
- async processing
- Swagger documentation
- scalable architecture

---

## 💬 Streamlit Frontend

Includes a ChatGPT-style UI with:

- interactive chat interface
- live responses
- clean modern layout

---

# 🏗️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| FastAPI | Backend API |
| LangGraph | Agent orchestration |
| LangChain | AI pipelines |
| ChromaDB | Vector database |
| HuggingFace | Embeddings + models |
| Streamlit | Frontend UI |
| Transformers | Local LLM inference |

---

# 📂 Project Structure

```text
Agentic Workflow System/
│
├── app/
│   ├── agents/
│   │   ├── specialized/
│   │   │   ├── healthcare.py
│   │   │   ├── finance.py
│   │   │   └── coding.py
│   │   │
│   │   ├── router.py
│   │   ├── planner.py
│   │   ├── retriever.py
│   │   ├── generator.py
│   │   └── evaluator.py
│   │
│   ├── graph.py
│   ├── ingest.py
│   ├── main.py
│   └── state.py
│
├── data/docs/
├── tools/
├── ui/
├── vectorstore/
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/agentic-workflow-system.git

cd agentic-workflow-system
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📄 Add Documents

Place PDF files inside:

```text
data/docs/
```

Examples:
- medical guidelines
- research papers
- technical documentation

---

# 🧠 Build Vector Database

```bash
python app/ingest.py
```

This performs:
- document loading
- chunking
- embedding generation
- vector storage

---

# ⚡ Run Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 💬 Run Frontend

```bash
streamlit run ui/app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# 🧪 Example Queries

## 🏥 Healthcare

```text
What foods should diabetics avoid?
```

```text
Symptoms of high blood pressure
```

---

## 💰 Finance

```text
Best crypto investment for beginners
```

```text
Explain stock market basics
```

---

## 💻 Coding

```text
How to fix Python API bug?
```

```text
Explain FastAPI middleware
```

---

# 🧠 Key Engineering Concepts Demonstrated

This project demonstrates:

- Multi-Agent Systems
- AI Workflow Orchestration
- Retrieval-Augmented Generation
- Semantic Search
- Vector Databases
- State Management
- Conditional Routing
- Modular AI Architectures

---

# 🔥 Future Improvements

## Planned Features

- Conversational memory
- Real finance APIs
- Web search tools
- Tool calling agents
- Authentication system
- Docker deployment
- Kubernetes deployment
- Cloud hosting
- Streaming responses
- Multi-modal support

---

# 📌 Why This Project Matters

Modern AI systems are shifting toward:

- agent orchestration
- modular reasoning systems
- tool-using AI
- retrieval-enhanced workflows

This project explores those concepts in a practical engineering-focused implementation.

---

# ⚠️ Disclaimer

This project is for educational and research purposes only.

Healthcare responses should NOT be considered medical advice.

---

# 📜 License

MIT License

---

# 👨‍💻 Author

Aaditya Mali

AI/ML Engineer | Generative AI | Agentic AI Systems
