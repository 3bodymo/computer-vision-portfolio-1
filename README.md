# 🔍 Computer Vision Portfolio 1

This project involves solving two real-world computer vision challenges.

## 📋 Table of Contents

- [Development Guidelines](#development-guidelines)
  - [Code Documentation](#code-documentation-requirements)
  - [Automated Quality Checks](#automated-code-quality-checks)
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

## Projects 📁

_[Project descriptions will be added as they are completed]_

## Setup and Installation 💻

_[Project setup will be added as they are completed]_

## Contributors 👥

- Abdullah Abdelrazek ([@3bodymo](https://github.com/3bodymo))
- Omar Mohamed ([@omarmo1712](https://github.com/omarmo1712))
- Parisa Ahmadlu ([@Paris-Fa](https://github.com/Paris-Fa))
- Laçin Boz ([@lacinboz](https://github.com/lacinboz))
- Fadi Sultan ([@Fadinrsultan](https://github.com/Fadinrsultan))

---

Made with ❤️ by our team
