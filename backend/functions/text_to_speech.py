import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")


# Eleven labs
# Convert Text to Speech
def convert_text_to_speech(message):

    # Define Data (Body)
    body = {
        "text": message,
        "voice_setting": {
            "stability": 0,
            "similarity_boost": 0
        }
    }

    # Define voice
    voice_domi = "21m00Tcm4TlvDq8ikWAM"

    # Constructing Headers and Endpoint
    headers = {"xi-api-key": ELEVEN_LABS_API_KEY,
               "Content-Type": "application/json", "accept": "audio/mpeg"}

    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_domi}"

    # Send request
    try:
        response = requests.post(endpoint, json=body, headers=headers)
        print(endpoint)
        print(response)
    except Exception as e:
        print(e)
        return

    # Handle Response
    if response.status_code == 200:
        return response.content
    else:
        return