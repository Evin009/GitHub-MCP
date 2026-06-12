from github_api import GitHubAPI

api = GitHubAPI()

try:
    print(f"Token loaded: {api.token}")
    print(f"Base URL: {api.base_url}")
    print("Headers set: ", "Authorization" in api.headers)
except Exception as e:
    print("Error", e)

