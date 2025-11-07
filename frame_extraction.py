import os
import subprocess
from pathlib import Path

# ---------------- CONFIG ---------------- #
# Root folder where your clips are stored
clips_root = Path("/home/pardhasaradhi/projects/NueralNetworks/piracy_detection/data/videos")
# Subfolders: 'pirated' and 'genuine'
subfolders = ["pirated", "genuine"]
# Folder to save extracted frames
frames_root = Path("/home/pardhasaradhi/projects/NueralNetworks/piracy_detection/data/frames")
# FPS to extract (1 frame per second)
fps = 1
# --------------------------------------- #

for sub in subfolders:
    clip_folder = clips_root / sub
    output_folder = frames_root / sub
    output_folder.mkdir(parents=True, exist_ok=True)

    # Loop through all mp4 clips
    for clip_file in sorted(clip_folder.glob("*.mp4")):
        clip_name = clip_file.stem  # e.g., mv1_clip_000
        # Create a subfolder per clip to keep frames organized
        clip_frame_folder = output_folder / clip_name
        clip_frame_folder.mkdir(exist_ok=True)

        # FFmpeg command to extract frames
        cmd = [
            "ffmpeg",
            "-i", str(clip_file),
            "-vf", f"fps={fps}",
            str(clip_frame_folder / f"{clip_name}_%03d.jpg")
        ]
        print(f"Extracting frames from {clip_file} → {clip_frame_folder}")
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("✅ Frame extraction complete!")
