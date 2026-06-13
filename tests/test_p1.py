from github_api import GitHubAPI

api = GitHubAPI()

try:
    print(f"Token loaded: {api.token}")
    print(f"Base URL: {api.base_url}")
    print("Headers set: ", "Authorization" in api.headers)
    ''' get users test '''
    user = api.get_user()
    print(" --- get users ---\n",user)
    
    ''' get repo info '''
    repos = api.get_repos(limit=5)
    print(" --- get repo ---")
    print(f"Found {len(repos['repos'])} repos: ")
    
    for r in repos['repos']:
        print(f" - {r['repo_name']} : stars = {r['stars']}, language: {r['language']}")
    
    ''' get issues info '''
    issues = api.get_issues('bug',limit=5)
    print(" --- get issues --- ")
    print(f"Found {issues['total']} issues with 'bug':")
    
    if issues.get('issues'): 
        for issue in issues['issues'][:3]:
            print(f" - {issue['title']}: state = {issue['state']}, repo = {issue['repo']}")
    else:
        print("No issues found!")
    
except Exception as e:
    print("Error:", e)

