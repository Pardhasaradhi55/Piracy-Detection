import os
import random
import shutil
from pathlib import Path

# ---------------- CONFIG ---------------- #
frames_root = Path("/home/pardhasaradhi/projects/NueralNetworks/piracy_detection/data/frames")
sampled_root = Path("/home/pardhasaradhi/projects/NueralNetworks/piracy_detection/data/seed_frames")
subfolders = ["pirated", "genuine"]
total_samples = 150  # total frames to sample across both folders
# --------------------------------------- #

sampled_root.mkdir(parents=True, exist_ok=True)

# Calculate how many per subfolder
samples_per_sub = total_samples // len(subfolders)

for sub in subfolders:
    frame_folder = frames_root / sub
    all_frames = []

    # Collect all jpg files in all clip subfolders
    for clip_subfolder in frame_folder.iterdir():
        if clip_subfolder.is_dir():
            all_frames.extend(list(clip_subfolder.glob("*.jpg")))

    print(f"{sub}: {len(all_frames)} frames available.")

    # Randomly sample frames
    sampled_frames = random.sample(all_frames, min(samples_per_sub, len(all_frames)))

    # Create output folder
    out_subfolder = sampled_root / sub
    out_subfolder.mkdir(exist_ok=True)

    # Copy and rename frames uniquely
    for i, f in enumerate(sampled_frames, start=1):
        new_name = f"{sub}_{i:04d}.jpg"  # e.g., pirated_0001.jpg
        shutil.copy(f, out_subfolder / new_name)

    print(f"{sub}: {len(sampled_frames)} frames copied to {out_subfolder}")

print(f"✅ All seed frames uniquely named and saved in {sampled_root}")
