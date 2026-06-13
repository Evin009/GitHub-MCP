from github_mcp_server import GitHubMCPServer

print("-- STEP 1: server init --")

try:
    server = GitHubMCPServer()
    print("Server created successfully!")
    print(f"Server name: {server.name}")
    print(f"GitHub API initialized: {server.github_api is not None}")

    # --------------------------------------------------------------------- #
    print()
    # --------------------------------------------------------------------- #

    
    # checks if get_tools() actually returns a list
    tools = server.get_tools()
    assert isinstance(tools, list), "get_tools() should return a list"
    print(f"get tools() returns a list")
    
    # --------------------------------------------------------------------- #
    print()
    # --------------------------------------------------------------------- #
    
    # check number of tools
    assert len(tools) == 3, f"Expected 3 tools, got {len(tools)}"
    print("returns 3 tools")
    
    # --------------------------------------------------------------------- #
    print()
    # --------------------------------------------------------------------- #
    
    # check each tool has required field like - name, descrp, inputSchema
    tool_names = []
    for tool in tools:
        assert "name" in tool, "Tool missing name"
        assert "description" in tool, "Tool missing descprition"
        assert "inputSchema" in tool, "Tool missing inputSchema"
        
        tool_names.append(tool['name'])
        print(f"{tool['name']} has all needed fields")
    
    
except Exception as e:
    print("Error", e)