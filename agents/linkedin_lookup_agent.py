from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.serpapi import SerpAPIWrapper

def get_profile_url(text: str) -> str:
    """Searches for Linkedin Profile Page."""
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res

def linkedin_lookup_agent(name_of_person: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Define the template as a normal string with a placeholder for the variable
    template = "given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page. Your answer should contain only a URL"

    tools_for_agents = [
        Tool(
            name="Crawl Google for a Linkedin profile page",
            func=get_profile_url,
            description="useful for when you need to find a linkedin profile",
        )
    ]
    agent = initialize_agent(
        tools=tools_for_agents,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    # Initialize the PromptTemplate with the template and the list of input variables
    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])

    # Format the prompt with the actual input and run the agent
    linkedin_profile_url = agent.run(prompt_template.format(name_of_person=name_of_person))
    return linkedin_profile_url
