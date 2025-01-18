from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

result = llm.invoke("What is the square root of `49`?")
print(result.content)
print(result.usage_metadata)