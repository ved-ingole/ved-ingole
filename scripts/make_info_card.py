from pathlib import Path


OUTPUT = Path("info-card.svg")

WIDTH = 820
HEIGHT = 650


def make_svg():

    return f'''<svg
xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<style>

.terminal {{
    fill: #0d1117;
    stroke: #30363d;
    stroke-width: 2;
}}

.titlebar {{
    fill: #161b22;
}}

.title {{
    font-family: "Courier New", monospace;
    font-size: 18px;
    fill: #8b949e;
}}

.dot-red {{
    fill: #ff5f56;
}}

.dot-yellow {{
    fill: #ffbd2e;
}}

.dot-green {{
    fill: #27c93f;
}}


/* Python prompt */

.prompt {{
    font-family: "Courier New", monospace;
    font-size: 17px;
    fill: #58a6ff;
}}


/* Normal code */

.code {{
    font-family: "Courier New", monospace;
    font-size: 18px;
    fill: #c9d1d9;
}}


/* Comments */

.comment {{
    font-family: "Courier New", monospace;
    font-size: 17px;
    fill: #8b949e;
}}


/* Python keywords */

.keyword {{
    fill: #ff7b72;
    font-weight: bold;
}}


/* Strings */

.string {{
    fill: #a5d6ff;
}}


/* Function */

.function {{
    fill: #d2a8ff;
    font-weight: bold;
}}


/* Section headings */

.section {{
    font-family: "Courier New", monospace;
    font-size: 18px;
    font-weight: bold;
    fill: #7ee787;
}}


/* List items */

.item {{
    font-family: "Courier New", monospace;
    font-size: 17px;
    fill: #c9d1d9;
}}


/* Separators */

.separator {{
    font-family: "Courier New", monospace;
    font-size: 17px;
    fill: #484f58;
}}


/* Animations */

.type {{
    opacity: 0;
    clip-path: inset(0 100% 0 0);
    animation: typeLine 0.75s steps(38, end) forwards;
}}

.fade {{
    opacity: 0;
    animation: fadeIn 0.45s ease-out forwards;
}}

.cursor {{
    fill: #58a6ff;
    animation: blink 1s step-end infinite;
}}


@keyframes typeLine {{

    0% {{
        opacity: 1;
        clip-path: inset(0 100% 0 0);
    }}

    100% {{
        opacity: 1;
        clip-path: inset(0 0 0 0);
    }}

}}


@keyframes fadeIn {{

    from {{
        opacity: 0;
        transform: translateY(5px);
    }}

    to {{
        opacity: 1;
        transform: translateY(0);
    }}

}}


@keyframes blink {{

    0%, 45% {{
        opacity: 1;
    }}

    46%, 100% {{
        opacity: 0;
    }}

}}

</style>


<!-- Terminal -->

<rect
    class="terminal"
    x="1"
    y="1"
    width="{WIDTH - 2}"
    height="{HEIGHT - 2}"
    rx="12"
    ry="12"
/>


<!-- Title bar -->

<rect
    class="titlebar"
    x="2"
    y="2"
    width="{WIDTH - 4}"
    height="38"
    rx="11"
    ry="11"
/>


<!-- Mac-style terminal buttons -->

<circle class="dot-red" cx="22" cy="21" r="6"/>
<circle class="dot-yellow" cx="42" cy="21" r="6"/>
<circle class="dot-green" cx="62" cy="21" r="6"/>


<text class="title" x="85" y="26">
Python Terminal — ved@github
</text>


<!-- Python startup -->

<g class="type" style="animation-delay:0.2s">

<text class="prompt" x="35" y="72">
Python 3.x.x
</text>

</g>


<!-- Comment -->

<g class="type" style="animation-delay:0.85s">

<text class="comment" x="35" y="94">
&gt;&gt;&gt; # developer_profile.py
</text>

</g>


<!-- Developer -->

<g class="type" style="animation-delay:1.5s">

<text class="prompt" x="35" y="120">
&gt;&gt;&gt;
</text>

<text class="code" x="75" y="120">
developer = <tspan class="string">"Ved Ingole"</tspan>
</text>

</g>


<!-- Focus -->

<g class="type" style="animation-delay:2.15s">

<text class="prompt" x="35" y="146">
&gt;&gt;&gt;
</text>

<text class="code" x="75" y="146">
focus = <tspan class="string">"AI / ML + Development"</tspan>
</text>

</g>


<!-- Separator -->

<text
    class="separator"
    x="35"
    y="171">
# ------------------------------------------------------------
</text>


<!-- Currently working -->

<g class="fade" style="animation-delay:2.4s">

<text class="section" x="35" y="202">
CURRENTLY WORKING ON
</text>

</g>


<g class="fade" style="animation-delay:2.55s">

<text class="item" x="42" y="227">
├─ <tspan class="string">DSA with Python</tspan>
</text>

</g>


<g class="fade" style="animation-delay:2.7s">

<text class="item" x="42" y="249">
└─ <tspan class="string">JavaScript</tspan>
</text>

</g>


<!-- Projects -->

<g class="fade" style="animation-delay:2.9s">

<text class="section" x="35" y="285">
PROJECTS
</text>

</g>


<g class="fade" style="animation-delay:3.05s">

<text class="item" x="42" y="310">
├─ <tspan class="string">Diabetes Prediction Model</tspan>
</text>

</g>


<g class="fade" style="animation-delay:3.2s">

<text class="item" x="42" y="332">
├─ <tspan class="string">Deccan EnM Solutions Website</tspan>
</text>

</g>


<g class="fade" style="animation-delay:3.35s">

<text class="item" x="42" y="354">
└─ <tspan class="string">Multiple ML Models</tspan>
</text>

</g>


<!-- Languages -->

<g class="fade" style="animation-delay:3.55s">

<text class="section" x="35" y="390">
LANGUAGE
</text>

</g>


<g class="fade" style="animation-delay:3.7s">

<text class="item" x="42" y="415">
Python · C++ · JavaScript · HTML5
</text>

</g>


<g class="fade" style="animation-delay:3.85s">

<text class="item" x="42" y="437">
CSS · Java · SQL
</text>

</g>


<!-- Tools -->

<g class="fade" style="animation-delay:4.05s">

<text class="section" x="35" y="473">
TOOLS
</text>

</g>


<g class="fade" style="animation-delay:4.2s">

<text class="item" x="42" y="498">
PyCharm · Git · GitHub
</text>

</g>


<g class="fade" style="animation-delay:4.35s">

<text class="item" x="42" y="520">
NumPy · Pandas · scikit-learn
</text>

</g>


<g class="fade" style="animation-delay:4.5s">

<text class="item" x="42" y="542">
Matplotlib
</text>

</g>


<!-- Final Python command -->

<g class="fade" style="animation-delay:4.75s">

<text class="prompt" x="35" y="585">
&gt;&gt;&gt;
</text>

<text class="code" x="75" y="585">
<tspan class="function">build</tspan>()
</text>

<rect
    class="cursor"
    x="128"
    y="571"
    width="8"
    height="18"
/>

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
