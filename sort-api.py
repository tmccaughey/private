import json
import requests

# Load remote OpenAPI spec
url = 'https://api-trial.cognigy.ai/openapi/openapi-viewer.json'
response = requests.get(url)
spec = response.json()

# Sort the paths
sorted_paths = dict(sorted(spec['paths'].items()))

# Replace the paths with sorted version
spec['paths'] = sorted_paths

# Save to a new file
with open('sorted-openapi.json', 'w') as f:
    json.dump(spec, f, indent=2)