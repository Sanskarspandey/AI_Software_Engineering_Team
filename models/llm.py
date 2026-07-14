from langchain_ollama import ChatOllama
from config import *

llm = ChatOllama(
    model=MODEL_NAME,
    base_url=BASE_URL,
    temperature=0,
)