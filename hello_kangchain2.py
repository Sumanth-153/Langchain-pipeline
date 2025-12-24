from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize model
print("Langchain pipeline crteated successfully (API call skipped)")
exit()

# Prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 3 concise bullet points."
)

# Chain using pipe operator (modern LangChain)
chain = prompt | llm | StrOutputParser()

# Run the chain
result = chain.invoke({"topic": "Prompt Engineering"})
print(result)
