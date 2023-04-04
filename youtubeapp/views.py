from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from allauth.socialaccount.models import SocialToken, SocialAccount
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

channel_id = "UCez3RAXfVyUCOShv9_iydYA"
# client_id = "1034149047244-jvpggaqjcc03re9cf2d7mka8ga242hig.apps.googleusercontent.com"
# client_secret = "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"

@login_required
def is_subscribed_to_channel(request):
    user = request.user
    if user.is_authenticated:
        channel_id = "UCez3RAXfVyUCOShv9_iydYA"
        is_subscribed = False
        social_token = SocialToken.objects.get(account__user=user.id, account__provider='google')
        credentials = Credentials.from_authorized_user_info(info=social_token.token, scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
        youtube = build('youtube', 'v3', credentials=credentials)
        subscriptions = youtube.subscriptions().list(part='snippet', mine=True).execute()
        subscribed_channel_ids = [s['snippet']['resourceId']['channelId'] for s in subscriptions['items']]
        if channel_id in subscribed_channel_ids:
            is_subscribed = True

    return render("is_subscribed.html", {"is_subcribed": is_subscribed})