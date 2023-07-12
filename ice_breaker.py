from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os
from third_parties.linkedin import scrape_linkedin_profile
from dotenv import load_dotenv
from agents.linkedin_lookup_agent import linkedin_lookup_agent

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    print("Hello Langchain")

    linkedin_profile_url = linkedin_lookup_agent(name_of_person="Maria da Gloria Ponte Burlamaqui")

    # Changed to Python f-string syntax
    summary_template = """
        given the Linkedin information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    # Ensure that the `run` method of `LLMChain` can accept keyword arguments
    print(chain.run(information=linkedin_data))

