import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()
NUBELA_KEY_LINK = os.getenv('NUBELA_KEY_LINK')
OPENAI_API_KEY= os.getenv('OPENAI_API_KEY')





def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape infomration from LinkedIn profiles,
    Manually scrape the information from the linkedin profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("NUBELA_KEY_LINK")}'}
    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    
    return data





# def dbug_scrape_linkedin_test():
#     """scrape infomration from LinkedIn profiles for debugging,
#     Manually scrape the information from the linkedin profile"""
#     requests
#     response = requests.get("https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
#     )

#     data = response.json()
#     data = {
#         k: v
#         for k, v in data.items()
#         if v not in ([], "", "", None)
#         and k not in ["people_also_viewed", "certifications"]
#     }
#     if data.get("groups"):
#         for group_dict in data.get("groups"):
#             group_dict.pop("profile_pic_url")
    
#     return data
#     print(data)

# test = dbug_scrape_linkedin_test()
# print(test)
