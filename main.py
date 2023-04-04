channel_id = "UCez3RAXfVyUCOShv9_iydYA"
client_id = "1034149047244-jvpggaqjcc03re9cf2d7mka8ga242hig.apps.googleusercontent.com"
client_secret = "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"

from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

def is_subscribed_to_channel(channel_id, client_id, client_secrets):
    try:
        credentials = Credentials.from_authorized_user_info(info={
            'client_id': client_id,
            'client_secret': client_secret,
        }, scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
        youtube = build('youtube', 'v3', credentials=credentials)
        subscriptions = youtube.subscriptions().list(part='snippet', mine=True).execute()
        subscribed_channel_ids = [s['snippet']['resourceId']['channelId'] for s in subscriptions['items']]
        return channel_id in subscribed_channel_ids
    except HttpError as error:
        print(f'An error occurred: {error}')
        return False
    except Exception as error:
        print(f'An error occurred: {error}')
        return False

if is_subscribed_to_channel(channel_id, client_id, client_secret):
    print('You are subscribed to the channel!')
else:
    print('You are not subscribed to the channel.')