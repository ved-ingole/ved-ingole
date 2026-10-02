from pathlib import Path
import sys

import numpy as np
from PIL import Image


# Bright -> dark
RAMP = " .:-=+*#%@"

COLS = 90
ROWS = 53

OUTPUT = Path("ved-ascii.svg")


def image_to_ascii(image_path):
    image = Image.open(image_path).convert("L")

    # Fit the image to the ASCII grid while preserving aspect ratio.
    # Characters are taller than they are wide, so compensate vertically.
    width, height = image.size

    target_ratio = COLS / (ROWS * 0.5)
    image_ratio = width / height

    if image_ratio > target_ratio:
        new_width = COLS
        new_height = max(1, int(COLS / image_ratio / 0.5))
    else:
        new_height = ROWS
        new_width = max(1, int(ROWS * image_ratio * 0.5))

    image = image.resize(
        (new_width, new_height),
        Image.Resampling.LANCZOS
    )

    # Put image into a white canvas.
    canvas = Image.new("L", (COLS, ROWS), 255)

    x = (COLS - new_width) // 2
    y = (ROWS - new_height) // 2

    canvas.paste(image, (x, y))

    pixels = np.array(canvas)

    # Convert brightness to characters.
    result = []

    for row in pixels:
        line = ""

        for value in row:
            index = int(
                (255 - int(value))
                / 255
                * (len(RAMP) - 1)
            )

            line += RAMP[index]

        result.append(line.rstrip())

    return result


def make_svg(lines):
    cell_width = 9
    cell_height = 15

    width = COLS * cell_width
    height = ROWS * cell_height

    svg = []

    svg.append(
        f'''<svg xmlns="http://www.w3.org/2000/svg"
        width="{width}"
        height="{height}"
        viewBox="0 0 {width} {height}">
'''
    )

    svg.append("""
<style>
    .ascii {
        font-family: "Courier New", monospace;
        font-size: 14px;
        font-weight: 400;
        fill: #d0d0d0;
    }

    .line {
        transform-origin: left center;
        animation: reveal 1.2s ease-out forwards;
    }

    @keyframes reveal {
        from {
            clip-path: inset(0 100% 0 0);
            opacity: 0;
        }

        to {
            clip-path: inset(0 0 0 0);
            opacity: 1;
        }
    }
</style>
""")

    svg.append(
        '<rect width="100%" height="100%" fill="#050505"/>'
    )

    for row, line in enumerate(lines):
        y = (row + 1) * cell_height

        delay = row * 0.035

        # Escape XML characters.
        line = (
            line.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
        )

        svg.append(
            f'''
<text
    class="ascii line"
    x="4"
    y="{y}"
    style="animation-delay:{delay:.3f}s"
>{line}</text>
'''
        )

    svg.append("</svg>")

    return "".join(svg)


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python scripts/make_ascii_svg.py "
            "source-prepped.png"
        )
        sys.exit(1)

    image_path = Path(sys.argv[1])

    if not image_path.exists():
        print(f"ERROR: File not found: {image_path}")
        sys.exit(1)

    print(f"Reading: {image_path}")

    lines = image_to_ascii(image_path)

    print("Generating SVG...")

    svg = make_svg(lines)

    OUTPUT.write_text(
        svg,
        encoding="utf-8"
    )

    print()
    print("SUCCESS!")
    print(f"Created: {OUTPUT}")
    print(f"Grid: {COLS} x {ROWS}")


if __name__ == "__main__":
    main()