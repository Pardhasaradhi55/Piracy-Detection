from ultralytics import YOLO

# Create a new model or load a pre-trained one
model = YOLO("yolov8n.pt")  # 'n' = nano, smaller and faster for learning

# Train on your dataset
model.train(
    data="/home/pardhasaradhi/projects/NueralNetworks/piracy_detection/trained_dataset/data.yaml",  # Roboflow provides this YAML
    epochs=50,                      # Number of training epochs
    imgsz=640,                      # Image size
    batch=8                         # Batch size
)

