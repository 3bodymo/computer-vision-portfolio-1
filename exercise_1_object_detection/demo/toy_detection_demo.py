import cv2
import argparse
import time
from pathlib import Path
from datetime import datetime
import sys
import os

# Add parent directory to path to import YOLOv8 trainer
sys.path.append(str(Path(__file__).parents[1]))

try:
    from ultralytics import YOLO
except ImportError:
    print(
        "Error: ultralytics not installed. Please install with 'pip install ultralytics'"
    )
    sys.exit(1)


class WebcamDetectionDemo:
    def __init__(self, model_path, conf_threshold=0.60, iou_threshold=0.50):
        """
        Initialize the webcam detection demo

        Args:
            model_path: Path to the trained YOLOv8 model
            conf_threshold: Confidence threshold for detection
            iou_threshold: IoU threshold for NMS
        """
        self.model_path = model_path
        self.conf_threshold = conf_threshold
        self.iou_threshold = iou_threshold
        self.model = None
        self.class_names = []
        self.save_dir = Path("captured_frames")
        self.save_dir.mkdir(exist_ok=True)

        # Initialize the model
        self._load_model()

    def _load_model(self):
        """
        Load the YOLOv8 model
        """
        try:
            self.model = YOLO(self.model_path)
            self.class_names = self.model.names
            print(f"Model loaded successfully. Classes: {self.class_names}")
        except Exception as e:
            print(f"Error loading model: {e}")
            sys.exit(1)

    def start_webcam(self, camera_id=0):
        """
        Start webcam detection

        Args:
            camera_id: Webcam ID (default 0 for primary camera)
        """
        cap = cv2.VideoCapture(camera_id)
        if not cap.isOpened():
            print(f"Error: Cannot open camera with ID {camera_id}")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Can't receive frame. Exiting...")
                break

            # Flip horizontally
            frame = cv2.flip(frame, 1)

            results = self.model(
                frame, conf=self.conf_threshold, iou=self.iou_threshold
            )

            annotated_frame = results[0].plot()
            cv2.imshow("YOLOv8 Webcam Demo", annotated_frame)

            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == 27:  # q or ESC
                print("Exiting...")
                break

        cap.release()
        cv2.destroyAllWindows()


def main():
    current_dir = Path(__file__).parent.absolute()
    parent_dir = current_dir.parent.absolute()
    default_model_path = os.path.join(parent_dir, "model", "best.pt")

    parser = argparse.ArgumentParser(description="YOLOv8 Webcam Detection Demo")
    parser.add_argument(
        "--model",
        type=str,
        default=default_model_path,
        help="Path to the YOLOv8 model",
    )
    parser.add_argument(
        "--conf", type=float, default=0.60, help="Confidence threshold for detection"
    )
    parser.add_argument("--iou", type=float, default=0.50, help="IoU threshold for NMS")
    parser.add_argument("--camera", type=int, default=0, help="Camera device ID")

    args = parser.parse_args()

    # Check if model exists
    if not os.path.exists(args.model):
        print(f"Error: Model not found at {args.model}")
        print(
            "Please provide the correct path to the trained model using --model argument"
        )
        sys.exit(1)

    demo = WebcamDetectionDemo(args.model, args.conf, args.iou)
    demo.start_webcam(args.camera)


if __name__ == "__main__":
    main()
