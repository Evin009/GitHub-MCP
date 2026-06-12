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
        
    def get_repos(self, sort="updated", limit=10):
        ''' get repo from your github'''

        try:
            # make GET request to /user/repos endpoint
            url = f"{self.base_url}/user/repos"
            
            # paramenters for the request
            params = {
                "sort": sort,
                "per_page": limit
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            
            # check if request was successful
            if response.status_code != 200:
                return {"error" : f"Failed to get user info: {response.status_code}"}
        
            # parse the data to json
            repos = response.json()
            
            # returning data
            return {
                "repos": [ # using list comprehension [{} for repo in repos]
                {
                    "repo_name": repo.get("name"),
                    "url": repo.get("html_url"),
                    "description": repo.get("description"),
                    "language": repo.get("language"),
                    "stars": repo.get("stargazers_count")
                }
                for repo in repos
            ]
            }
        
        except Exception as e:
            print("Error:", e)
            
    def get_issues(self, query, limit=10):
        ''' search for issues across all the repos'''
        
        try:
            # make GET request to /search/issues endpoint
            url = f"{self.base_url}/search/issues"
            
            # github search syntax
            search_query = f"{query} is:issue user:{self.get_user()['username']}"
            
            params = {
                "q": query,
                "per_page": limit
            }

            response = requests.get(url, headers=self.headers, params=params)
            
            # check if request was successful
            if response.status_code != 200:
                return {"error" : f"Failed to get user info: {response.status_code}"}
            
            data = response.json()
            
            return {
                "total": data.get("total_count", 0),
                "issues": [
                    {
                        "title": issue.get("title"),
                        "repo": issue.get("repository_url").split("/")[-1],
                        "state": issue.get("state"),
                        "url": issue.get("html_url")
                    }
                    
                    for issue in data.get("items", [])
                ]
            }
        
        except Exception as e:
            print("Error: ", e)
        