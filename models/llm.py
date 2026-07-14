from langchain_ollama import ChatOllama
from config import MODEL_NAME, BASE_URL, TEMPERATURE

llm = ChatOllama(
    model=MODEL_NAME,
    base_url=BASE_URL,
    temperature=TEMPERATURE,
)