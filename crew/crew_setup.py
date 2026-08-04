from crewai import Crew
from crew.agents import create_agents
from crew.tasks import create_tasks

def run_crew(product, websites):
    researcher, analyst = create_agents()
    t1, t2 = create_tasks(product, websites, researcher, analyst)

    crew = Crew(
        agents=[researcher, analyst],
        tasks=[t1, t2],
        verbose=True
    )

    result = crew.kickoff()
    return result