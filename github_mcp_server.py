'''
PART - 2 creating MCP server that connects github api to claude using JSON-RPC

What is github_mcp_server.py?
It's the translator between Claude and GitHub API:
 - Claude sends: "Get my repos"
 - Server translates to: Call get_repos() function
 - Server returns: JSON-RPC formatted response
 - Claude reads: "You have 5 repos"


-- MCP Structure --
The server needs to do 3 things:
 - Define Tools : Tell Claude what it can do
 - Handle Requests : Read incoming JSON-RPC requests
 - Send Responses : Send back JSON-RPC responses


'''

import sys
import json
from github_api import GitHubAPI

class GitHubMCPServer:
    ''' MCP server for GitHub'''

    def __init__(self):
        self.name = "github mcp"
        self.github_api = GitHubAPI()
        print("Github MCP Server intilized", file=sys.stderr)