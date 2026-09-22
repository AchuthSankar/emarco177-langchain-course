from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient

llm=ChatOllama(model="qwen3:4b", temperature=0)

tavily=TavilyClient()

@tool
def search(query:str) -> str :
    """
    Tool that search .
    Args:
        query: Word to search for in the web
    Returns:
        result from web
    """
    try:
        return tavily.search(query=query);
    except:
        return "Sorry cant get you any answer !!!"

def main():
    print("Hello from emarco177-langchain-course!")
    agent=create_agent(model=llm, tools=[search])
    response=agent.invoke({"messages": [HumanMessage("Find the temperature in Kochi city"), HumanMessage("How to reach Kochi city")]})
    print(response.get("messages")[-1].text)

if __name__ == "__main__":
    main()
