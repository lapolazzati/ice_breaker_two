from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


if __name__ == "__main__":
    print("Hello Langchain")

    summary_template = """ 
        given the infomration about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """