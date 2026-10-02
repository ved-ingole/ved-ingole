from pathlib import Path
import random

OUTPUT = Path("ved-ascii.svg")

WIDTH = 500
HEIGHT = 500

COLS = 28
ROWS = 30

CELL_W = WIDTH / COLS
CELL_H = HEIGHT / ROWS

random.seed(42)


def make_svg():

    elements = []

    # Background
    elements.append(
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#000000"/>'
    )

    # Subtle glow
    elements.append("""
<defs>
    <filter id="glow">
        <feGaussianBlur stdDeviation="1.2" result="blur"/>
        <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>
    </filter>
</defs>
""")

    # Create independent falling streams
    for col in range(COLS):

        x = col * CELL_W + CELL_W / 2

        duration = random.uniform(3.5, 7.0)
        delay = random.uniform(-7.0, 0.0)

        stream_length = random.randint(18, 30)

        # Each column gets its own group
        elements.append(
            f'''
<g>

    <animateTransform
        attributeName="transform"
        type="translate"
        from="0 -520"
        to="0 520"
        dur="{duration:.2f}s"
        begin="{delay:.2f}s"
        repeatCount="indefinite"
    />
'''
        )

        for row in range(stream_length):

            y = row * CELL_H

            digit = random.choice("0123456789")

            # Bright leading digits
            if row >= stream_length - 2:
                fill = "#00ff41"
                opacity = 1.0
            elif row >= stream_length - 6:
                fill = "#00c832"
                opacity = 0.85
            else:
                fill = "#006b1b"
                opacity = random.uniform(0.35, 0.7)

            elements.append(
                f'''
<text
    x="{x:.1f}"
    y="{y:.1f}"
    text-anchor="middle"
    font-family="Courier New, monospace"
    font-size="17"
    font-weight="bold"
    fill="{fill}"
    opacity="{opacity:.2f}"
    filter="url(#glow)">
    {digit}
</text>
'''
            )

        elements.append("</g>")

    return f'''<svg
xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

{''.join(elements)}

</svg>
'''


def main():

    OUTPUT.write_text(
        make_svg(),
        encoding="utf-8"
    )

    print("SUCCESS!")
    print(f"Created: {OUTPUT}")
    print(f"Size: {WIDTH} x {HEIGHT}")


if __name__ == "__main__":
    main()