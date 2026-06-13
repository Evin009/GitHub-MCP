import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from github import Github

print("✓ requests installed!")
print("✓ PyGithub installed!")