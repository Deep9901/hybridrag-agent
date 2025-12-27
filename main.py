from fastapi import FastAPI, HTTPException, Query, Body
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
import uvicorn

app = FastAPI(title="HybridRAG Agent API", version="1.0.0")

@app.get("/health")
async def health_check():
    return {"status": "ok"}


def main():
    print("Hello from hybridrag-agent!")


if __name__ == "__main__":
    main()
