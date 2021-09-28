
from googleapiclient.discovery import build

api_key = "AIzaSyBxk7rriyZRroJRcVbykCQa2rdArP-hC_4"

youtube = build("youtube", "v3", developerKey = api_key)

request = youtube.channels().list(
        part = "statistics",
        forUsername = "sentdex"
    )

response = request.execute()

print(response)
