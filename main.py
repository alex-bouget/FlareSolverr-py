from flaresolverr import FlareSolverr

# Create a new instance of FlareSolverr
solver = FlareSolverr("http://localhost:8191", log_level="INFO")

session = solver.sessions.create()
result = solver.request.get("TEST HERE", session=session)

# Print the result
print(result.json())
