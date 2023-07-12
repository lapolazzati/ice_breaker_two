import requests

api_endpoint = "https://nubela.co/proxycurl/api/linkedin/profile/resolve"
api_key = "Y8MkVA4sLxEMJrndG2P9yw"
header_dic = {"Authorization": "Bearer " + api_key}
params = {
    "company_domain": "cloudwalk.io",
    "first_name": "Lapo",
    "similarity_checks": "include",
    "enrich_profile": "enrich",
    "location": "Sao Paulo",
    "title": "Head of Product",
    "last_name": "Lazzati",
}
response = requests.get(api_endpoint, params=params, headers=header_dic)

fullprofile = response.json()

print(fullprofile)
