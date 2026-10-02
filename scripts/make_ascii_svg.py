from pathlib import Path

OUTPUT = Path("ved-ascii.svg")

WIDTH = 500
HEIGHT = 500


def make_svg():

    return f'''<svg
xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<defs>

    <!-- Glow -->
    <filter id="glow">
        <feGaussianBlur stdDeviation="3" result="blur"/>
        <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>
    </filter>

    <!-- Strong glow -->
    <filter id="strongGlow">
        <feGaussianBlur stdDeviation="6" result="blur"/>
        <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
        </feMerge>
    </filter>

</defs>


<!-- Background -->

<rect
    width="{WIDTH}"
    height="{HEIGHT}"
    fill="#05070a"
/>


<!-- ========================= -->
<!-- NEURAL NETWORK CONNECTIONS -->
<!-- ========================= -->

<g
    stroke="#1f6f4a"
    stroke-width="2"
    opacity="0.65"
    fill="none">

    <!-- Input → Hidden -->

    <line x1="70" y1="110" x2="190" y2="80"/>
    <line x1="70" y1="110" x2="190" y2="160"/>
    <line x1="70" y1="110" x2="190" y2="250"/>
    <line x1="70" y1="210" x2="190" y2="80"/>
    <line x1="70" y1="210" x2="190" y2="160"/>
    <line x1="70" y1="210" x2="190" y2="250"/>
    <line x1="70" y1="310" x2="190" y2="160"/>
    <line x1="70" y1="310" x2="190" y2="250"/>
    <line x1="70" y1="310" x2="190" y2="340"/>
    <line x1="70" y1="410" x2="190" y2="250"/>
    <line x1="70" y1="410" x2="190" y2="340"/>
    <line x1="70" y1="410" x2="190" y2="420"/>


    <!-- Hidden → Output -->

    <line x1="190" y1="80" x2="330" y2="120"/>
    <line x1="190" y1="80" x2="330" y2="250"/>
    <line x1="190" y1="80" x2="330" y2="380"/>

    <line x1="190" y1="160" x2="330" y2="120"/>
    <line x1="190" y1="160" x2="330" y2="250"/>
    <line x1="190" y1="160" x2="330" y2="380"/>

    <line x1="190" y1="250" x2="330" y2="120"/>
    <line x1="190" y1="250" x2="330" y2="250"/>
    <line x1="190" y1="250" x2="330" y2="380"/>

    <line x1="190" y1="340" x2="330" y2="120"/>
    <line x1="190" y1="340" x2="330" y2="250"/>
    <line x1="190" y1="340" x2="330" y2="380"/>

    <line x1="190" y1="420" x2="330" y2="120"/>
    <line x1="190" y1="420" x2="330" y2="250"/>
    <line x1="190" y1="420" x2="330" y2="380"/>


    <!-- Output → AI -->

    <line x1="330" y1="120" x2="430" y2="250"/>
    <line x1="330" y1="250" x2="430" y2="250"/>
    <line x1="330" y1="380" x2="430" y2="250"/>

</g>


<!-- ================= -->
<!-- DATA SIGNALS -->
<!-- ================= -->

<g fill="#39ff88" filter="url(#glow)">

    <!-- Signal 1 -->

    <circle r="4">
        <animateMotion
            dur="2.5s"
            repeatCount="indefinite"
            path="M70,110 L190,80 L330,120 L430,250"/>
    </circle>

    <!-- Signal 2 -->

    <circle r="4">
        <animateMotion
            dur="3s"
            begin="0.8s"
            repeatCount="indefinite"
            path="M70,210 L190,160 L330,250 L430,250"/>
    </circle>

    <!-- Signal 3 -->

    <circle r="4">
        <animateMotion
            dur="2.8s"
            begin="1.5s"
            repeatCount="indefinite"
            path="M70,310 L190,340 L330,380 L430,250"/>
    </circle>

    <!-- Signal 4 -->

    <circle r="4">
        <animateMotion
            dur="3.2s"
            begin="0.4s"
            repeatCount="indefinite"
            path="M70,410 L190,420 L330,380 L430,250"/>
    </circle>

</g>


<!-- ================= -->
<!-- INPUT NODES -->
<!-- ================= -->

<g fill="#00c853" filter="url(#glow)">

    <circle cx="70" cy="110" r="9">
        <animate
            attributeName="r"
            values="8;11;8"
            dur="1.8s"
            repeatCount="indefinite"/>
    </circle>

    <circle cx="70" cy="210" r="9">
        <animate
            attributeName="r"
            values="8;11;8"
            dur="2s"
            begin="0.3s"
            repeatCount="indefinite"/>
    </circle>

    <circle cx="70" cy="310" r="9">
        <animate
            attributeName="r"
            values="8;11;8"
            dur="1.7s"
            begin="0.6s"
            repeatCount="indefinite"/>
    </circle>

    <circle cx="70" cy="410" r="9">
        <animate
            attributeName="r"
            values="8;11;8"
            dur="2.1s"
            begin="0.2s"
            repeatCount="indefinite"/>
    </circle>

</g>


<!-- ================= -->
<!-- HIDDEN LAYER -->
<!-- ================= -->

<g fill="#26a641" filter="url(#glow)">

    <circle cx="190" cy="80" r="10">
        <animate
            attributeName="r"
            values="9;13;9"
            dur="1.5s"
            repeatCount="indefinite"/>
    </circle>

    <circle cx="190" cy="160" r="10">
        <animate
            attributeName="r"
            values="9;13;9"
            dur="1.8s"
            begin="0.3s"
            repeatCount="indefinite"/>
    </circle>

    <circle cx="190" cy="250" r="10">
        <animate
            attributeName="r"
            values="9;14;9"
            dur="1.6s"
            begin="0.5s"
            repeatCount="indefinite"/>
    </circle>

    <circle cx="190" cy="340" r="10">
        <animate
            attributeName="r"
            values="9;13;9"
            dur="1.9s"
            begin="0.2s"
            repeatCount="indefinite"/>
    </circle>

    <circle cx="190" cy="420" r="10">
        <animate
            attributeName="r"
            values="9;13;9"
            dur="1.7s"
            begin="0.7s"
            repeatCount="indefinite"/>
    </circle>

</g>


<!-- ================= -->
<!-- OUTPUT LAYER -->
<!-- ================= -->

<g fill="#39d353" filter="url(#glow)">

    <circle cx="330" cy="120" r="11">
        <animate
            attributeName="r"
            values="10;14;10"
            dur="1.7s"
            repeatCount="indefinite"/>
    </circle>

    <circle cx="330" cy="250" r="12">
        <animate
            attributeName="r"
            values="10;15;10"
            dur="1.5s"
            begin="0.4s"
            repeatCount="indefinite"/>
    </circle>

    <circle cx="330" cy="380" r="11">
        <animate
            attributeName="r"
            values="10;14;10"
            dur="1.8s"
            begin="0.8s"
            repeatCount="indefinite"/>
    </circle>

</g>


<!-- ================= -->
<!-- CENTRAL AI NODE -->
<!-- ================= -->

<circle
    cx="430"
    cy="250"
    r="32"
    fill="#07150c"
    stroke="#39d353"
    stroke-width="3"
    filter="url(#strongGlow)">

    <animate
        attributeName="r"
        values="30;35;30"
        dur="2s"
        repeatCount="indefinite"/>

</circle>


<circle
    cx="430"
    cy="250"
    r="20"
    fill="none"
    stroke="#00ff88"
    stroke-width="2"
    opacity="0.8">

    <animate
        attributeName="r"
        values="18;25;18"
        dur="2s"
        repeatCount="indefinite"/>

</circle>


<!-- AI TEXT -->

<text
    x="430"
    y="245"
    text-anchor="middle"
    font-family="Courier New, monospace"
    font-size="16"
    font-weight="bold"
    fill="#39ff88">

    AI

</text>

<text
    x="430"
    y="263"
    text-anchor="middle"
    font-family="Courier New, monospace"
    font-size="10"
    fill="#8bffb0">

    ML

</text>


<!-- ================= -->
<!-- LABELS -->
<!-- ================= -->

<g
    font-family="Courier New, monospace"
    font-size="12"
    fill="#7ee787">

    <text x="38" y="85">DATA</text>

    <text x="165" y="55">FEATURES</text>

    <text x="305" y="95">MODEL</text>

    <text x="398" y="305">PREDICT</text>

</g>


<!-- Small technical text -->

<g
    font-family="Courier New, monospace"
    font-size="10"
    fill="#3fb950"
    opacity="0.65">

    <text x="35" y="470">INPUT</text>

    <text x="185" y="470">HIDDEN</text>

    <text x="320" y="470">OUTPUT</text>

</g>


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