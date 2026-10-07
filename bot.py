import numpy as np
import imageio.v2 as imageio

# Green background ke 240 frames (8 sec video)
frames = [np.full((720, 1280, 3), (34, 139, 34), dtype=np.uint8) for _ in range(240)]

imageio.mimsave("auto_video.mp4", frames, fps=30, macro_block_size=1)
print("Video ban gaya - success!")