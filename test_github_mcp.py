import subprocess
import json
import time

#start server
server = subprocess.Popen(
    ['python', 'github_mcp_server.py'], # run cmd python github_mcp_server.py
    stdin=subprocess.PIPE, # input pipe
    stdout=subprocess.PIPE, # output pipe
    stderr=subprocess.PIPE, # error pipe
    text=True # text mode
)

print("Server Started...")
time.sleep(1)

# Check if server crashed immediately
if server.poll() is not None:
    print("❌ Server crashed!")
    stderr = server.stderr.read()
    stdout = server.stdout.read()
    print("\nServer stdout:")
    print(stdout)
    print("\nServer stderr:")
    print(stderr)
    exit(1)
    
    

# Send request
request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list"   
}

print("Sending: ", json.dumps(request)) #printing info in json text format
print()

server.stdin.write(json.dumps(request) + "\n") # convert dict to json text format and write to stdin
server.stdin.flush() # make sure it goes immediately

# Get response send to stdout
response_line = server.stdout.readline()
print("Response:", response_line)
print("Response length: ", len(response_line))

if response_line:
    response = json.loads(response_line) # convert json text to dict
    print("Success!!\n")
    print(f"Got {len(response['result']['tools'])} tools")
else:
    print("No response")
    print("Server stderr:", server.stderr.read())
    


server.terminate()



