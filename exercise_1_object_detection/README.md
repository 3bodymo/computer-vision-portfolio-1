# Exercise 1: Object Detection for Giraffe and Rhinoceros Recognition

This project implements a custom object detection system to identify giraffes and rhinoceroses on a conveyor belt. The solution uses YOLOv8 to create a robust detection system capable of recognizing these specific animal figures from various angles.

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Dataset

The dataset consists of custom-collected images of giraffe and rhinoceros figures annotated with bounding boxes. The data collection strategy involved:

1. Capturing images of giraffe and rhinoceros figures from multiple angles and orientations
2. Ensuring varied backgrounds, lighting conditions, and object placements
3. Annotating objects with bounding boxes using a labeling tool
4. Splitting data into training and validation sets

### Data Collection Strategy

Our comprehensive data collection strategy was designed to ensure robust model performance across various real-world scenarios:

1. **Environment Diversity**

   - Varied lighting conditions (bright, dim, natural, artificial)
   - Different backgrounds and surfaces
   - Various times of day to capture different shadow patterns

2. **Capture Perspectives (Excluding Bottom Views)**

   - Ensured coverage of:
     - Front
     - Back
     - Top
     - Left
     - Right
     - Angled (45°) from above and side

3. **Control Object Arrangement**
   - Varied object position:
     - Centered in frame
     - Partially out of frame
     - Overlapping with other objects
   - Included both single-object and multi-object scenes
   - Different distances from camera to object

### HEIC Image Conversion

During our data collection process, we encountered an issue with images taken using iPhone cameras, which were saved in HEIC format. Label Studio, which we used for annotation, does not support HEIC format.

To address this issue, we created a custom utility script (`utils/heic_converter.py`) to convert HEIC images to JPG or PNG format. This script uses `pillow_heif` library to handle HEIC files and can be used as follows:

```bash
# Convert a single HEIC file
python utils/heic_converter.py path/to/image.heic

# Convert all HEIC files in a directory
python utils/heic_converter.py path/to/directory

# Specify output format (jpg or png)
python utils/heic_converter.py path/to/directory -f png

# Specify output quality for JPG
python utils/heic_converter.py path/to/directory -q 95
```

## Model Training

You can train the model from scratch using the `main.ipynb` notebook.

### Quick Start with Pre-trained Model

If you don't want to run the entire training process, you can use the pre-trained model:

1. Open `main.ipynb`
2. Look for cells with green headers:
   - **Import Required Libraries**
   - **Download Pre-trained Model**
   - **Test Inference with YOLOv8**
3. Run these specific cells to download and test the pre-trained model

## Test Results

We tested our trained model on 4 images to demonstrate its capabilities in real-world scenarios.

<table>
  <tr>
    <td><img src="model/results/test1.jpg" alt="Test Result 1" width="100%"></td>
    <td><img src="model/results/test2.jpg" alt="Test Result 2" width="100%"></td>
  </tr>
  <tr>
    <td><img src="model/results/test3.jpg" alt="Test Result 3" width="100%"></td>
    <td><img src="model/results/test4.jpg" alt="Test Result 4" width="100%"></td>
  </tr>
</table>

The bounding boxes show the detected giraffes and rhinoceroses with their class labels and confidence scores.

## Evaluation Results

Our trained YOLOv8 model achieved excellent performance on the validation dataset:

```
     Class     Images  Instances      Box(P          R      mAP50  mAP50-95)
       all         36         41      0.963      0.972      0.975      0.795
   giraffe         18         18      0.932      0.944      0.956      0.746
rhinoceros         23         23      0.995          1      0.995      0.845
```

Key metrics:

- **Precision (P)**: 96.3% overall (93.2% for giraffe, 99.5% for rhinoceros)
- **Recall (R)**: 97.2% overall (94.4% for giraffe, 100% for rhinoceros)
- **mAP50**: 97.5% overall (95.6% for giraffe, 99.5% for rhinoceros)
- **mAP50-95**: 79.5% overall (74.6% for giraffe, 84.5% for rhinoceros)

## Demo: Real-time Object Detection

The project includes a demo application that can detect giraffe and rhinoceros figures in real-time using a webcam.

### Running the Demo

1. Make sure the trained model (`best.pt`) is in the `model` directory
2. Navigate to the exercise directory:
   ```bash
   cd exercise_1_object_detection
   ```
3. Run the demo script:
   ```bash
   python demo/toy_detection_demo.py
   ```

### Demo Options

You can customize the demo with the following arguments:

- `--model`: Path to the YOLOv8 model (default: `model/best.pt`)
- `--conf`: Confidence threshold (default: 0.60)
- `--iou`: IoU threshold for NMS (default: 0.50)
- `--camera`: Camera device ID (default: 0)

Example:

```bash
python demo/toy_detection_demo.py --conf 0.5 --camera 1
```

### Using a Custom Model Path

If you want to use a model saved in a different location:

```bash
python demo/toy_detection_demo.py --model /path/to/your/model.pt
```
