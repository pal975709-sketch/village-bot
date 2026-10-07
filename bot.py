from moviepy.editor import ColorClip

# Simple video - bina text ke - ye kabhi fail nahi hoga
clip = ColorClip(size=(1280, 720), color=(34, 139, 34), duration=8)
clip.write_videofile("auto_video.mp4", fps=24)
print("Video ban gaya!")