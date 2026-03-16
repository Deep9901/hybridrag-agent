## HybridRAG Agent

A full-stack RAG (Retrieval-Augmented Generation) application featuring a FastAPI backend and a Streamlit frontend.

### Key Features

* **Hybrid AI and Intelligent Routing**: Combines internal RAG knowledge with real-time web search, dynamically selecting the best information source for each query.
* **User-Controlled Web Access**: Provides a UI toggle to enable or disable web search, allowing users to choose between internal-only knowledge or broader internet access.
* **Transparent AI Workflow**: Offers a detailed, step-by-step trace of the agent thought process, including routing decisions and retrieval summaries.
* **Contextual RAG Sufficiency Judgment**: Employs an LLM to assess if retrieved RAG content is sufficient to answer a query, prompting further search if needed.
* **Dynamic Knowledge Ingestion**: Users can upload PDF documents directly, which are processed, embedded, and added to the Pinecone knowledge base.
* **Modular Design**: Clean, layered architecture using FastAPI, LangGraph, and Streamlit.
* **Persistent Memory**: LangGraph checkpointing maintains conversation context across multiple turns.

---

### High-Level Architecture

#### Layers Overview:

* **User Interface**: Streamlit application.
* **API Layer**: FastAPI backend handling requests.
* **Agent Core**: LangGraph logic with routing and tools.
* **Knowledge Base**: Pinecone vector database with HuggingFace embeddings.
* **External Tools**: Groq LLM and Tavily Search API.

---

### Technology Stack

* **Language**: Python 3.10+
* **Frontend**: Streamlit
* **Backend**: FastAPI
* **Agent Orchestration**: LangGraph
* **LLMs and Tools**: LangChain, Groq (Llama 3)
* **Embeddings**: sentence-transformers/all-MiniLM-L6-v2
* **Vector Store**: Pinecone
* **Search Engine**: Tavily API

---

### Quick Start with Docker

The system is containerized for easy deployment.

1. **Clone the repository**:
```bash
git clone <your-repo-link>
cd hybridrag-agent

```


2. **Set up environment variables**:
Create a `.env` file in the root directory:
```text
GROQ_API_KEY="your_api_key"
PINECONE_API_KEY="your_api_key"
TAVILY_API_KEY="your_api_key"
FASTAPI_BASE_URL="http://backend:8000"

```


3. **Launch the application**:
```bash
docker compose up --build

```


4. **Access the services**:
* **Frontend**: http://localhost:8501
* **Backend**: http://localhost:8000/docs



---

### Project Structure

* **backend/**: Contains main.py (FastAPI), agent logic, and vector store configuration.
* **frontend/**: Contains app.py (Streamlit) and UI components.
* **docker-compose.yml**: Manages container orchestration and networking.

---

### Local Development

1. **Install dependencies**:
```bash
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt

```


2. **Start Backend**:
```bash
uvicorn backend.main:app --reload

```


3. **Start Frontend**:
```bash
streamlit run frontend/app.py

```

## API Testing 

### /upload-document/ (POST)

* **URL**: `http://localhost:8000/upload-document/`
* **Body**: `form-data`, key=`file`, type=`File`
* **Response**:

```json
{
  "message": "PDF 'doc.pdf' successfully uploaded and indexed.",
  "filename": "doc.pdf",
  "processed_chunks": 5
}

```

### /chat/ (POST)

* **URL**: `http://localhost:8000/chat/`
* **Body (JSON)**:

```json
{
  "session_id": "test-session-001",
  "query": "What are the treatment of diabetes?",
  "enable_web_search": true
}

```

* **Response**:

```json
{
  "response": "Your agent's answer here...",
  "trace_events": [
    {
      "step": 1,
      "node_name": "router",
      "description": "...",
      "event_type": "router_decision"
    }
  ]
}

```

---

## Future Improvements

* **Tool Integration**: Addition of calculator, calendar, and code interpreter tools.
* **Streaming**: Implementation of token-by-token LLM output streaming.
* **Advanced RAG**: Integration of reranking and multi-query retrieval techniques.
* **Persistent Storage**: Long-term database for chat history.
* **Security**: User authentication and profile management.
* **UI Enhancements**: Dark mode, animations, and custom themes.



