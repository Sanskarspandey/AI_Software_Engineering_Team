from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

TEMPERATURE = 0

PROJECT_NAME = "AI Software Engineering Team"