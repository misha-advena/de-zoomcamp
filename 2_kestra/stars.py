import requests

r = requests.get("https://api.github.com/repos/kestra-io/kestra")
gh = r.json()['stargazers_count']
print(f"Kestra has {gh} stars on GitHub.")
# The above code fetches the number of stars for the Kestra GitHub repository using the GitHub API.
# It uses the requests library to make a GET request to the API endpoint for the repository.
# The response is then parsed as JSON, and the number of stargazers (stars) is extracted and printed.
# The code is a simple example of how to interact with the GitHub API to retrieve information about a repository.

