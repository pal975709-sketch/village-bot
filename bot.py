import numpy as np
import imageio.v2 as imageio

print("Video bana raha hu...")
frames = [np.full((720, 1280, 3), (34, 139, 34), dtype=np.uint8) for _ in range(90)]
imageio.mimsave("auto_video.mp4", frames, fps=30, macro_block_size=1)
print("Video ban gaya!")
