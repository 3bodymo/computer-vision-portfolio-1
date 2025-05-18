# Exercise 2: Camera-Based Queue Analysis with Person Re-Identification

This project implements a real-time queue analysis system using a dual-view camera setup. The system detects individuals, tracks them across camera angles using appearance-based embeddings, and optionally estimates their waiting time in the queue. It was developed as part of the Applied Computer Vision portfolio assignment.

## 🎯 Objective

To dynamically count the number of people waiting in an amusement park queue using a multi-camera system, avoiding duplicate counts and optionally showing the estimated waiting time for each person.

## 📦 Requirements

Install the necessary packages using:

```bash
pip install -r requirements.txt
```

Additionally, make sure to install [TorchReID](https://github.com/KaiyangZhou/deep-person-reid) and download the pretrained ReID model (`resnet50` or `osnet`) before running the notebook.

## 🎥 Input Data

The system takes as input a **stitched dual-view video** which combines:

- **Right camera view** (entry side of the queue)
- **Left camera view** (boarding side)

The people in queue appear first on the right side and move toward the left camera, forming an **L-shaped queue**.

## 📐 Queue Detection Logic

The queue is defined using polygonal areas:

- On the **left camera view**, a polygon is used to precisely identify people in queue.
- The **right camera view** does not use a polygon. Instead, a heuristic is used based on the bounding box area, aspect ratio, and detection confidence.

This hybrid approach ensures accurate inclusion and avoids missing people at the entrance.

## ⚙️ Implementation Overview

### 1. Frame Extraction

The video is processed at ~3 frames per second using OpenCV.

### 2. Person Detection

We use the `YOLOv3` model (`yolov3u.pt`) to detect people in each frame. Detections are filtered by confidence and used to generate bounding boxes.

### 3. Feature Extraction and Re-Identification

- Appearance-based features are extracted using a **pretrained ResNet50 model** from TorchReID.
- For each person, an embedding vector is computed.
- These vectors are matched against a gallery of historical embeddings using cosine similarity (via FAISS) to assign consistent person IDs.

### 4. Cross-Camera Matching

If a person appears in both right and left views, their embedding vectors are compared **within the same frame** to assign a unified ID.

### 5. Queue Entry and Exit Tracking

- When a person enters the queue zone (as defined), their entry time is recorded.
- When they exit the frame, the system calculates their time spent in the queue.

### 6. ETA (Estimated Time of Arrival)

- Each person’s ETA is computed based on:

  ```
  ETA = people_in_front × average_time_per_person
  ```

- The ETA is displayed inside each bounding box.

## 📊 Output

- Real-time bounding boxes for all detected individuals
- Cross-camera consistent person IDs
- ETA values rendered on screen
- Dynamic people count inside the queue zone

## ▶️ How to Run

1. Place your video (e.g., `first-video.mp4`) in a folder named `video_input/`.

2. Open the notebook:

   ```bash
   jupyter notebook person_reid-3.ipynb
   ```

   Or run it as a script (if exported):

   ```bash
   python person_reid.py --video_path video_input/first-video.mp4
   ```

3. Modify parameters like thresholds or polygon coordinates if needed.

## ⚙️ Parameters You Can Tune

| Parameter             | Description                                                              |
|-----------------------|--------------------------------------------------------------------------|
| `similarity_threshold`| Cosine similarity threshold for matching embeddings (default: 0.66)      |
| `confidence > 0.81`   | Minimum YOLO detection confidence to assign a new ID                     |
| `queue_polygon`       | Points defining the queue area in the left camera                        |
| `embedding_history`   | Controls how many previous features are stored per ID                    |

## 📁 Project Structure

```
.
├── person_reid-3.ipynb        # Main implementation notebook
├── video_input/               # Folder for input stitched video
├── outputs/                   # Folder for saving output frames or video (optional)
├── reid_model/                # Folder for storing ReID model weights
├── utils/                     # Utility functions (if modularized)
└── README.md                  # Project documentation
```

## 📉 Limitations

- Cross-camera matching may fail if people are heavily occluded or partially visible.
- ETA assumes a continuous and stable queue without large gaps or batching.
- System relies on visual appearance and may fail with visually similar individuals.

## 👥 Team Members

- Your Name
- Teammate 1
- Teammate 2
- Teammate 3
- Teammate 4

## 📜 License

MIT License


## 🎬 Demo: Queue Analysis Output

The project includes a demo video that shows the final output of our queue analysis system.

### 🔹 What’s Shown in the Demo

- Real-time detection of individuals across two camera views
- Bounding boxes with consistent person IDs
- Estimated Time of Arrival (ETA) shown above each bounding box
- Live queue count tracking

### ▶️ Watch the Output

You can view the demo output here:

📺 **Video File**: `video_outputs/first-video-counted_3.mp4`

> Note: The video showcases detections from a pre-processed, stitched dual-view camera setup.
