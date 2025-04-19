import os
import yaml
from pathlib import Path
import random
import shutil
from tqdm import tqdm as tqdm_func
from ultralytics import YOLO
from typing import List, Tuple, Optional, Union


class YOLOv8Trainer:
    """Class for managing YOLOv8 training workflow"""

    def __init__(
        self,
        data_dir: str = "./dataset",
        source_img_dir: str = "./images",
        source_label_dir: str = "./labels",
        labels: Optional[List[str]] = None,
        val_split: float = 0.2,
    ) -> None:
        """
        Initialize YOLOv8 trainer

        Args:
            data_dir (str): Path to dataset directory
            source_img_dir (str): Path to source images directory
            source_label_dir (str): Path to source labels directory
            labels (list): List of class labels
            val_split (float): Validation split ratio
        """
        self.data_dir = Path(data_dir)
        self.source_img_dir = Path(source_img_dir)
        self.source_label_dir = Path(source_label_dir)
        self.labels = labels
        self.val_split = val_split
        self.yaml_path = self.data_dir / "dataset.yaml"

    def prepare_directory_structure(self) -> None:
        """
        Creates train and validation subdirectories for both images and labels folders
        """
        for split in ["train", "val"]:
            for folder in ["images", "labels"]:
                (self.data_dir / folder / split).mkdir(parents=True, exist_ok=True)
        print(f"Created dataset directory structure at {self.data_dir}")

    def split_dataset(self) -> Tuple[int, int]:
        """
        Split the dataset into training and validation sets

        Returns:
            tuple: (train_count, val_count) - Number of training and validation samples
        """
        full_img_dir = self.data_dir / self.source_img_dir
        full_label_dir = self.data_dir / self.source_label_dir

        image_files = list(full_img_dir.glob("*.jpg")) + list(
            full_img_dir.glob("*.png")
        )

        print(f"Looking for images in: {full_img_dir}")
        print(f"Found {len(image_files)} images")

        random.shuffle(image_files)

        val_size = int(len(image_files) * self.val_split)

        val_files = image_files[:val_size]
        train_files = image_files[val_size:]

        print(
            f"Splitting dataset: {len(train_files)} train, {len(val_files)} validation"
        )

        for file_list, split in [(train_files, "train"), (val_files, "val")]:
            for img_path in tqdm_func(file_list, desc=f"Copying {split} files"):
                shutil.copy(img_path, self.data_dir / "images" / split / img_path.name)

                label_path = full_label_dir / f"{img_path.stem}.txt"
                if label_path.exists():
                    shutil.copy(
                        label_path, self.data_dir / "labels" / split / label_path.name
                    )

                os.remove(img_path)
                if label_path.exists():
                    os.remove(label_path)

        return len(train_files), len(val_files)

    def create_dataset_yaml(self) -> Path:
        """
        Create YAML configuration file for YOLOv8 training

        Returns:
            Path: Path to the created YAML configuration file
        """
        data_dir_absolute = self.data_dir.absolute()
        data = {
            "path": str(data_dir_absolute),
            "train": str(data_dir_absolute / "images" / "train"),
            "val": str(data_dir_absolute / "images" / "val"),
            "nc": len(self.labels),
            "names": {i: name for i, name in enumerate(self.labels)},
        }

        with open(self.yaml_path, "w") as f:
            yaml.dump(data, f, default_flow_style=False)

        print(f"Created dataset YAML at {self.yaml_path}")
        return self.yaml_path

    def train_model(
        self,
        model_size: str = "m",
        epochs: int = 100,
        batch_size: int = 16,
        img_size: int = 640,
        device: Union[str, int] = "0",
        name: str = "yolov8_custom",
        pretrained: bool = True,
        project: str = "runs/detect",
    ) -> Optional[Path]:
        """
        Train YOLOv8 model

        Args:
            model_size (str): Model size (n=nano, s=small, m=medium, l=large, x=xlarge)
            epochs (int): Number of training epochs
            batch_size (int): Training batch size
            img_size (int): Image size for training
            device (str): GPU device ID(s) or 'cpu'
            name (str): Experiment name
            pretrained (bool): Use pretrained weights
            project (str): Project name for saving results

        Returns:
            Optional[Path]: Path to results directory if successful, None otherwise
        """
        model_file = f"yolov8{model_size}"
        if pretrained:
            model = YOLO(f"{model_file}.pt")
            print(f"Loaded pretrained YOLOv8 model: {model_file}.pt")
        else:
            model = YOLO(f"{model_file}.yaml")
            print(f"Created new YOLOv8 model from: {model_file}.yaml")

        if device.lower() == "cpu":
            device = "cpu"
        else:
            device = int(device) if device.isdigit() else device

        results = model.train(
            data=str(self.yaml_path),
            epochs=epochs,
            batch=batch_size,
            imgsz=img_size,
            device=device,
            name=name,
            project=project,
            verbose=True,
        )

        results_dir = Path(project) / name
        return results_dir
