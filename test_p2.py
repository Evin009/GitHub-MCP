from github_mcp_server import GitHubMCPServer

print("-- STEP 1: server init --")

try:
    server = GitHubMCPServer()
    print("Server created successfully!")
    print(f"Server name: {server.name}")
    print(f"GitHub API initialized: {server.github_api is not None}")

    
    
    
    
    
except Exception as e:
    print("Error", e)