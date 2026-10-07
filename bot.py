import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from moviepy.editor import TextClip, ColorClip, CompositeVideoClip

print("Video bana raha hu...")
bg = ColorClip(size=(1280,720), color=(34,139,34)).set_duration(8)
text = TextClip("Gaon Ki Subah 3D", fontsize=80, color='white', size=(1280,720), method='caption', align='center').set_duration(8)
video = CompositeVideoClip([bg, text]).set_duration(8)
video.write_videofile("auto_video.mp4", fps=24)
print("Ban gaya!")

with open('token.pickle', 'rb') as f:
    creds = pickle.load(f)
youtube = build('youtube', 'v3', credentials=creds)
youtube.videos().insert(
    part="snippet,status",
    body={"snippet":{"title":"Village 3D Auto","categoryId":"22"},"status":{"privacyStatus":"public"}},
    media_body=MediaFileUpload('auto_video.mp4')
).execute()
print("YouTube pe chala gaya!")
