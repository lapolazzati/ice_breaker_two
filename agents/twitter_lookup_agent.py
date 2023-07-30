from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from tools import get_profile_url


def lookup(name_of_person: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Define the template as a normal string with a placeholder for the variable
    template = "given the full name {name_of_person} I want you to get it me a link to their Twitter profile page. Your answer should contain only the person username"

    tools_for_agents = [
        Tool(
            name="Crawl Google for a Twitter profile page, return username",
            func=get_profile_url,
            description="useful for when you need to find a twitter profile",
        )
    ]
    agent = initialize_agent(
        tools=tools_for_agents,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    # Initialize the PromptTemplate with the template and the list of input variables
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    # Format the prompt with the actual input and run the agent
    twitter_username = agent.run(prompt_template.format(name_of_person=name_of_person))
    return "twitter_username"
