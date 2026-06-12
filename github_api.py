'''
Github_api - translator for performing tasks
- Takes simple requests (like "get my repos")
- Calls GitHub's API
- Cleans up the messy response
- Returns nice, simple data 
'''

import os
import requests
from dotenv import load_dotenv

class GitHubAPI:
    ''' handle add Github API interactions'''
    
    def __init__(self):
        # load token from .env
        load_dotenv()
        self.token = os.getenv("GITHUB_TOKEN")
        
        # base url for all GitHub Api calls
        self.base_url = "https://api.github.com"

        # header for authentication
        self.headers = {
                "Authorization": f"token {self.token}",
                "Accept": "application/vnd.github.v3+json"
        }
        
        print(f"GitHub Initilized")
        
    def get_user(self):
        ''' retreive github profile info'''
        
        try:
            # make GET request to /user endpoint
            url = f"{self.base_url}/user"
            response = requests.get(url, headers=self.headers)
            
            # check if request was successful
            if response.status_code != 200:
                return {"error" : f"Failed to get user info: {response.status_code}"}
            
            # parse the data to json
            data = response.json()
            
            # returning imp info from the json just parsed
            return {
                "username": data.get("login"),
                "name": data.get("name"),
                "bio": data.get("bio"),
                "public_repose": data.get("public_repose"),
                "followers": data.get("followers"),
                "following": data.get("following")
            }
            
        except Exception as e:
            return {"error": str(e)}
