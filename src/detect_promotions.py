from ultralytics import YOLO

# Load your trained model
model = YOLO("runs/train/your_model/best.pt")

# Run detection on a frame or video
results = model("path/to/frame_or_video.jpg")  # or mp4 file

# Show results
results.show()        # Displays bounding boxes
results.print()       # Prints detected classes and coordinates