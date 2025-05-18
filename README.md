# 🔍 Computer Vision Portfolio 1

This project involves solving two real-world computer vision challenges.

## 📋 Table of Contents

- [Development Guidelines](#development-guidelines)
  - [Code Documentation](#code-documentation-requirements)
  - [Automated Quality Checks](#automated-code-quality-checks)
  - [Branch Protection](#branch-protection)
- [Projects](#projects)
- [Setup and Installation](#setup-and-installation)
- [Contributors](#contributors)

## Development Guidelines

### Code Documentation Requirements

#### Function Documentation ✏️

All functions must include a docstring following this format:

```python
def function_name(parameters):
    """
    [Short Description]
    A concise summary of what the function does.

    Args:
        parameter_name (type): Description of the parameter.
            Optional notes about the parameter, if necessary.
        parameter_name (type, optional): Description of the optional parameter. Defaults to default_value.

    Returns:
        type: Description of the return value, including structure and key details.
            - Optional bullet points for complex return types.
            - Describe nested data if needed.
    """
```

**Example:**

```python
def detect_objects(image, confidence_threshold=0.5):
    """
    Detects objects in the given image using YOLOv8.

    Args:
        image: Input image in BGR format.
            Must be a valid numpy array with 3 channels.
        confidence_threshold (optional): Minimum confidence score for detections. Defaults to 0.5.

    Returns:
        list: List of detected objects.
            - Each detection object contains:
                - bbox: (x1, y1, x2, y2) coordinates
                - class_id: Integer identifying the object class
                - confidence: Float detection confidence score
    """
```

### Automated Code Quality Checks ⚙️

This repository includes automated workflows that run on every pull request to maintain code quality:

- **Code Formatting**
  - Uses `black` to automatically format Python code
  - The workflow will automatically commit formatting changes to your PR

### Branch Protection 🔒

The `main` branch is protected to ensure code quality and stability:

- Direct pushes to `main` are not allowed
- All changes must go through pull requests
- Pull requests require at least one review before merging
- Status checks (including automated tests) must pass before merging

To contribute:

1. Create a new branch from `main`
2. Make your changes
3. Submit a pull request
4. Address review comments
5. Wait for approval and merge

## Projects 📁

### Exercise 1: Object Detection for Giraffe and Rhinoceros Recognition

A computer vision system that identifies giraffe and rhinoceros figures on a conveyor belt using the YOLOv8 model. The project demonstrates accurate object detection with custom-trained models capable of recognizing these specific toy animals from various angles and under different lighting conditions.

### Exercise 2: Camera-Based Queue Analysis with Person Re-Identification

A real-time queue analysis system using a dual-camera setup to track individuals in an amusement park queue. The system leverages appearance-based person re-identification to maintain consistent tracking across multiple camera views, avoid duplicate counts, and estimate waiting times for each person in the queue.

## Setup and Installation 💻

For setup and installation instructions, please refer to the README.md file within each project folder:

- [Exercise 1: Object Detection Setup](./exercise_1_object_detection/README.md)
- [Exercise 2: Queue Analysis Setup](./exercise_2_queue_analysis/README.md)

## Contributors 👥

- Abdullah Abdelrazek ([@3bodymo](https://github.com/3bodymo))
- Omar Mohamed ([@omarmo1712](https://github.com/omarmo1712))
- Parisa Ahmadlu ([@Paris-Fa](https://github.com/Paris-Fa))
- Laçin Boz ([@lacinboz](https://github.com/lacinboz))
- Fadi Sultan ([@Fadinrsultan](https://github.com/Fadinrsultan))

---

Made with ❤️ by our team
