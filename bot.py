from moviepy.editor import TextClip, ColorClip, CompositeVideoClip
import datetime

# Date se title banega roz naya
today = datetime.datetime.now().strftime("%d %B")
title = f"Gaon Ki Subah - {today} 3D Story"

print(f"Video bana raha hu: {title}")

# Background
bg = ColorClip(size=(1280,720), color=(34,139,34)).set_duration(8)

# Text
txt = TextClip(title, fontsize=60, color='white', size=(1280,720), method='caption', align='center').set_duration(8)

# Video
video = CompositeVideoClip([bg, txt]).set_duration(8)
video.write_videofile("auto_video.mp4", fps=24)

print("Video ban gaya! Ab GitHub me save hai!")
