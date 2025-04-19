from pathlib import Path
from ultralytics import YOLO
import cv2
from PIL import Image
from IPython.display import display


def run_inference(model_path, image_path, conf_threshold=0.60):
    """
    Run inference on an image using a trained YOLOv8 model

    Args:
        model_path (str): Path to the trained model
        image_path (str): Path to the image for inference
        conf_threshold (float): Confidence threshold for detections

    Returns:
        list: Results from the model inference
    """
    model = YOLO(model_path)
    results = model(image_path, conf=conf_threshold, iou=0.50)

    for result in results:
        bgr_image = result.plot()
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        result_image = Image.fromarray(rgb_image)

        print(f"Detected Animals in {Path(image_path).name}:")
        display(result_image)
        print(f"Found {len(result.boxes)} animals:")
        for box in result.boxes:
            cls_id = int(box.cls.item())
            cls_name = model.names[cls_id]
            conf = box.conf.item()
            print(f"{cls_name}: {conf:.2f} confidence")

    return results
