import os
import langchain_experimental.agents 
import langchain_experimental.agents.agent_toolkits.csv.base
from langchain_openai import ChatOpenAI

# ⚠️ Replace with your OpenAI API key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

def get_agent():
    llm = ChatOpenAI(temperature=0)

    agent = langchain_experimental.agents.create_csv_agent(
        llm,
        "titanic.csv",
        verbose=True,
        allow_dangerous_code=True
    )

    return agent