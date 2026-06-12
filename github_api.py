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
