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
        # print("Github MCP Server intilized", file=sys.stderr)
        
    def get_tools(self):
        '''list all the tools avalaiable for Claude'''  
        
        # listing out all the tools, its descp, input params and its defination 
        return [
            {
                "name": "get_user",
                "description": "Get your GitHub profile information",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }

            },
            {
                "name": "get_repos",
                "description": "Get your GitHub repositories",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "sort": {
                            "type": "string",
                            "description": "Sort by: updated, created, or pushed"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Number of repos to return",
                            "default": 10
                        }
                    }
                }   
            },
            {
                "name": "get_issues",
                "description": "Search for issues in your repositories",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query (e.g.,'bug', 'feature')"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "number of issues to return",
                            "default": 10
                        }
                    },
                    "required": ["query"]
                }
            }
        ]
        
    def handle_tool_call(self, tool_name: str, arguments: dict):
        ''' Execute a tool based on its name'''
        
        if tool_name == "get_user":
            return self.github_api.get_user()
        
        elif tool_name == "get_repos":
            return self.github_api.get_repos(
                sort= arguments.get("sort", "updated"),
                limit= arguments.get("limit", 10)
            )   
            
        elif tool_name == "get_issues":
            return self.github_api.get_issues(
                query= arguments.get("query"),
                limit= arguments.get("limit", 10)
            )   
        
        else:
            return {"error": f"Unknown tool: {tool_name}"}
        
    
    def handle_requests(self, request: dict):
        ''' Process a JSON-RPC request coming from Claude'''
    
        method = request.get("method")
        request_id = request.get("id")
        
        # Request: list all the tools
        if method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "tools": self.get_tools() # getting the result from get_tool from github api
                }
            }
         
         # Request: Call a tools
        elif method == "tools/call":
            
            tool_name = request["params"]["name"]
            arguments = request["params"]["arguments"]
            
            result = self.handle_tool_call(tool_name, arguments)
            
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": result
            }   

        #Request: Unknown tool
        else:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32601,
                    "message": "Method not found!"
                }
                
            }
        
def main():
    ''' Main loop - read from stdin, write to stdout'''
    
    server = GitHubMCPServer()
    
    # read JSON-RPC request from stdin
    for line in sys.stdin:
        try:  
            # parse incoming data into json
            request = json.loads(line)
            
            # handle the request
            response = server.handle_requests(request)
            
            # send response to stdout
            print(json.dumps(response))
            sys.stdout.flush()
        
        
        # common error handling
        except json.JSONDecodeError as e:
            # Invalid JSON
            error_response = {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32700,
                    "message": "Parse error"
                }
            }
            print(json.dumps(error_response))
            sys.stdout.flush()
            
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": f"Internal error: {str(e)}"
                }
            }
            print(json.dumps(error_response))
            sys.stdout.flush()
   
if __name__ == "__main__":
    main()
    
        
            