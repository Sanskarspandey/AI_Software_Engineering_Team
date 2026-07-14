from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

response = llm.invoke("Say hello from our AI Software Engineering Team.")

print(response.content)