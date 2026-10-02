from pathlib import Path
import sys

import cv2
import numpy as np
from PIL import Image


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/prep_photo.py source-photo.jpg")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path("source-prepped.png")

    if not input_path.exists():
        print(f"ERROR: File not found: {input_path}")
        sys.exit(1)

    print(f"Loading: {input_path}")

    # Load image
    image = cv2.imread(str(input_path))

    if image is None:
        print("ERROR: Could not read the image.")
        sys.exit(1)

    # Resize large images while keeping the aspect ratio
    max_width = 1200

    height, width = image.shape[:2]

    if width > max_width:
        scale = max_width / width
        image = cv2.resize(
            image,
            (int(width * scale), int(height * scale)),
            interpolation=cv2.INTER_AREA
        )

    print("Converting to grayscale...")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Improve local contrast
    print("Enhancing contrast...")

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(gray)

    # Light denoising
    enhanced = cv2.GaussianBlur(
        enhanced,
        (3, 3),
        0
    )

    # Make the image slightly brighter/cleaner
    enhanced = cv2.normalize(
        enhanced,
        None,
        0,
        255,
        cv2.NORM_MINMAX
    )

    # Save
    Image.fromarray(enhanced).save(output_path)

    print()
    print("SUCCESS!")
    print(f"Created: {output_path}")
    print(
        f"Size: {enhanced.shape[1]} x {enhanced.shape[0]}"
    )


if __name__ == "__main__":
    main()