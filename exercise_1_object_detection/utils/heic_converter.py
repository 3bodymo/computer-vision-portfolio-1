import os
from pathlib import Path
from typing import Union, List
from PIL import Image
from pillow_heif import register_heif_opener
import argparse

register_heif_opener()


def convert_heic(
    input_path: Union[str, Path],
    output_format: str = "jpg",
    output_path: Union[str, Path, None] = None,
    quality: int = 90,
) -> str:
    """
    Converts a single HEIC image to JPG or PNG format.

    Args:
        input_path (str or Path): Path to the HEIC image file to be converted.
            Must be a valid HEIC file.
        output_format (str, optional): Format to convert to - either 'jpg' or 'png'. Defaults to 'jpg'.
        output_path (str, Path or None, optional): Output file path.
            If None, the output will be saved in the same directory with the same name. Defaults to None.
        quality (int, optional): Quality of the output image (0-100). Defaults to 90.
            Only applicable for JPG format.

    Returns:
        str: Path to the converted image file.
    """
    if output_format.lower() not in ["jpg", "jpeg", "png"]:
        raise ValueError("Output format must be 'jpg', 'jpeg', or 'png'")

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    img = Image.open(input_path)

    if output_path is None:
        input_path_obj = Path(input_path)
        output_path = input_path_obj.with_suffix(f".{output_format.lower()}")

    if output_format.lower() in ["jpg", "jpeg"]:
        img.convert("RGB").save(output_path, "JPEG", quality=quality)
    else:
        img.convert("RGB").save(output_path, "PNG")

    return str(output_path)


def batch_convert_heic(
    input_dir: Union[str, Path],
    output_format: str = "jpg",
    output_dir: Union[str, Path, None] = None,
    quality: int = 90,
) -> List[str]:
    """
    Converts all HEIC images in a directory to JPG or PNG format.

    Args:
        input_dir (str or Path): Directory containing HEIC images.
            The directory must exist.
        output_format (str, optional): Format to convert to - either 'jpg' or 'png'. Defaults to 'jpg'.
        output_dir (str, Path or None, optional): Directory to save converted images.
            If None, images will be saved in the same directory as input. Defaults to None.
        quality (int, optional): Quality of the output images (0-100). Defaults to 90.
            Only applicable for JPG format.

    Returns:
        list: List of paths to the converted image files.
    """
    if not os.path.isdir(input_dir):
        raise NotADirectoryError(f"Input directory not found: {input_dir}")

    input_dir_path = Path(input_dir)

    if output_dir is not None:
        output_dir_path = Path(output_dir)
        os.makedirs(output_dir_path, exist_ok=True)
    else:
        output_dir_path = input_dir_path

    heic_files = list(input_dir_path.glob("*.heic")) + list(
        input_dir_path.glob("*.HEIC")
    )

    converted_files = []

    for heic_file in heic_files:
        output_file = output_dir_path / f"{heic_file.stem}.{output_format.lower()}"
        try:
            converted_path = convert_heic(
                heic_file,
                output_format=output_format,
                output_path=output_file,
                quality=quality,
            )
            converted_files.append(converted_path)
        except Exception as e:
            print(f"Error converting {heic_file}: {e}")

    return converted_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HEIC images to JPG or PNG")
    parser.add_argument(
        "input", help="Input HEIC file or directory containing HEIC files"
    )
    parser.add_argument(
        "-f",
        "--format",
        default="jpg",
        choices=["jpg", "png"],
        help="Output format (jpg or png)",
    )
    parser.add_argument("-o", "--output", default=None, help="Output file or directory")
    parser.add_argument(
        "-q", "--quality", type=int, default=90, help="Output quality for JPG (0-100)"
    )

    args = parser.parse_args()

    # Check if input is a file or directory
    if os.path.isfile(args.input):
        result = convert_heic(args.input, args.format, args.output, args.quality)
        print(f"Converted: {result}")
    else:
        results = batch_convert_heic(args.input, args.format, args.output, args.quality)
        print(f"Converted {len(results)} files:")
        for res in results:
            print(f"  - {res}")
