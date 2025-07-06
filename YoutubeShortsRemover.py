import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


def get_authenticated_service():
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json"  # Replace with your credentials file path

    # Authenticate using OAuth2 credentials
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
    return youtube


def get_playlist_items(youtube, playlist_id):
    next_page_token = None
    videos = []

    while True:
        request = youtube.playlistItems().list(
            part="contentDetails",
            maxResults=50,
            playlistId=playlist_id,
            pageToken=next_page_token,
        )
        response = request.execute()

        for item in response.get("items", []):
            videos.append(item["contentDetails"]["videoId"])

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return videos


def remove_shorts_from_playlist(youtube, playlist_id):
    videos = get_playlist_items(youtube, playlist_id)

    # Get video details to filter out shorts
    video_details = youtube.videos().list(
        part="snippet",
        id=",".join(videos),
        maxResults=50
    ).execute()

    # Filter out shorts from the playlist
    filtered_videos = [video_id for video_id, video in zip(videos, video_details["items"]) if
                       not "short" in video["snippet"]["title"].lower()]

    # Remove shorts from the playlist
    for video_id in filtered_videos:
        request = youtube.playlistItems().delete(id=video_id)
        request.execute()
        print(f"Removed video {video_id} from the playlist")


if __name__ == "__main__":
    playlist_id = "LL"  # Replace with the ID of the YouTube playlist
    youtube = get_authenticated_service()
    remove_shorts_from_playlist(youtube, playlist_id)
