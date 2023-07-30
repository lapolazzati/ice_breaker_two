from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os
from third_parties.linkedin import scrape_linkedin_profile
from dotenv import load_dotenv
from agents.linkedin_lookup_agent import linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.twitter_with_stubs import scrape_user_tweets_stubs

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

name_of_person = "Harrison Chase"

if __name__ == "__main__":
    print("Hello Langchain")

    linkedin_profile_url = linkedin_lookup_agent(name_of_person=name_of_person)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    twitter_username = twitter_lookup_agent(name_of_person=name_of_person)
    tweets = scrape_user_tweets_stubs(username=twitter_username, num_tweets=5)

    # Changed to Python f-string syntax
    summary_template = """
        given the Linkedin information {linkedin_information} and twitter {twitter_information} about a person I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information", "twitter_information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)


    # Ensure that the `run` method of `LLMChain` can accept keyword arguments
    print(chain.run(linkedin_information=linkedin_data,twitter_information=tweets))

scrape_user_tweets_stubs(username="@elonmusk")
