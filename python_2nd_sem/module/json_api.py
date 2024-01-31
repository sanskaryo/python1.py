import json
import requests  # Don't forget to import the requests module

# Specify the URL of the API endpoint for retrieving information about fish species.
url = "https://www.fishwatch.gov/api/species"
# Make an HTTP GET request to the specified URL and store the response in the data variable.
data = requests.get(url)
# Parse the JSON data received from the API response using json.loads() and store it in the results variable.
results = json.loads(data.text)
