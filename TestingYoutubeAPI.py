
from googleapiclient.discovery import build

api_key = ENV_GOOGLE_KEY

youtube = build("youtube", "v3", developerKey = api_key)

request = youtube.channels().list(
        part = "statistics",
        forUsername = "sentdex"
    )

response = request.execute()

print(response)
