from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
def is_subscribed(request):
    channel_id = "UCez3RAXfVyUCOShv9_iydYA"
    client_id = "1034149047244-jvpggaqjcc03re9cf2d7mka8ga242hig.apps.googleusercontent.com"
    client_secret = "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"

    user_email = request.user.email
    is_subscribed = False

    if request.user.is_authenticated:
        try:
            credentials = Credentials.from_authorized_user_info(request.user.social_auth.get(provider='google-oauth2').extra_data)
            youtube = build('youtube', 'v3', credentials=credentials)
            subscriptions = youtube.subscriptions().list(
                part='snippet',
                channelId=channel_id,
                mine=True,
                maxResults=50
            ).execute()

            for subscription in subscriptions['items']:
                if subscription['snippet']['subscriberSnippet']['email'] == user_email:
                    is_subscribed = True
                    break
        except HttpError as error:
            print(f"An error occurred: {error}")
            is_subscribed = False

    return render(request, 'is_subscribed.html', {'is_subscribed': is_subscribed})