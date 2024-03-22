# FlareSolverr-py
Python module for (flaresolverr)[https://github.com/FlareSolverr/FlareSolverr]

```python
import flaresolverr

# Create a new instance of the client
client = flaresolverr.FlareSolverr("http://localhost:8191")

session = client.session.create() # Create a new session

# Solve a challenge
solution = client.request.get("https://www.example.com", session=session)

# Print the body of the response
print(solution.response)

# Get the json of the response if it is json
print(solution.json) # False if the response is not json
```

for more information on the API, see the (commands)[https://github.com/FlareSolverr/FlareSolverr?tab=readme-ov-file#commands] section.

All commands of the API are available with the same name. For example, `sessions.destroy` is available as `client.sessions.destroy()`.

## Installation
```bash
pip install flaresolverr
```