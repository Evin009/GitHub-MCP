import os
from dotenv import load_dotenv
from github import Github

# load from .env
load_dotenv()
token = os.getenv("GITHUB_TOKEN")


# testing connection and printing username and name to verify
try:
    g = Github(token)
    user = g.get_user()
    print(f"GitHub connencted successfully")
    print(f"Username: {user.login}")
    print(f"Name: {user.name}")
except Exception as e:
    print(f"Error: {e}")

