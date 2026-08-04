from crewai import Agent
from tools.search_tool import get_search_tool
from crew.llm import getllm

def create_agents():
    llm = getllm()
    search_tool = get_search_tool()

    researcher = Agent(
        role ="Product Researcher",
        goal = "Find products online with links",
        backstory = "Expert in online product research, skilled at finding the best deals and products across various e-commerce platforms.",
        llm = llm,
        tools = [search_tool],
        verbose = True,
        allow_delegation = False
    )

    analyst = Agent(    
        role ="Product Analyst",
        goal = "Compare and analyze products based on research data",
        backstory = "Professional product analyst with expertise in evaluating and comparing products based on price, rating, and value for money.",
        llm = llm,
        verbose = True,
        allow_delegation = False
    )

    return researcher, analyst