import json
from pathlib import Path
from datetime import date, timedelta

INPUT = Path("data/contributions.json")
OUTPUT = Path("contrib-heatmap.svg")

# GitHub-style colors
PALETTE = [
    "#161b22",  # 0
    "#0e4429",  # 1
    "#006d32",  # 2
    "#26a641",  # 3
    "#39d353",  # 4
    "#69f0a0",  # 5
]

# --------------------------------------------------
# Layout
# --------------------------------------------------

CELL = 12
GAP = 4
STEP = CELL + GAP

LEFT = 58
TOP = 45

ROWS = 7
WEEKS = 53

GRID_WIDTH = WEEKS * STEP
GRID_HEIGHT = ROWS * STEP

WIDTH = 1000
HEIGHT = 245

# --------------------------------------------------
# Load contribution data
# --------------------------------------------------

with open(INPUT, "r", encoding="utf-8") as f:
    data = json.load(f)

days = {
    item["date"]: item
    for item in data["days"]
}

# --------------------------------------------------
# Find calendar start
# --------------------------------------------------

today = date.today()

# GitHub calendar is Sunday -> Saturday.
# Start 364 days before today and move back to Sunday.
start = today - timedelta(days=364)

start -= timedelta(days=(start.weekday() + 1) % 7)

# --------------------------------------------------
# Build 53 weeks
# --------------------------------------------------

weeks = []

for week_index in range(WEEKS):

    week = []

    for row in range(ROWS):

        current_date = start + timedelta(
            days=week_index * 7 + row
        )

        if current_date > today:

            item = None

        else:

            item = days.get(
                current_date.isoformat()
            )

        week.append(
            {
                "date": current_date,
                "item": item
            }
        )

    weeks.append(week)

# --------------------------------------------------
# SVG
# --------------------------------------------------

svg = []

svg.append(
    f'''<svg xmlns="http://www.w3.org/2000/svg"
    width="{WIDTH}"
    height="{HEIGHT}"
    viewBox="0 0 {WIDTH} {HEIGHT}">'''
)

# --------------------------------------------------
# CSS
# --------------------------------------------------

svg.append("""
<style>

    .background {
        fill: #0d1117;
    }

    .title {
        fill: #f0f6fc;
        font-family: monospace;
        font-size: 16px;
        font-weight: bold;
    }

    .month {
        fill: #8b949e;
        font-family: monospace;
        font-size: 11px;
    }

    .weekday {
        fill: #8b949e;
        font-family: monospace;
        font-size: 10px;
    }

    .stats {
        fill: #8b949e;
        font-family: monospace;
        font-size: 12px;
    }

    .legend {
        fill: #8b949e;
        font-family: monospace;
        font-size: 10px;
    }

    .cell {
        opacity: 0;
        transform-box: fill-box;
        transform-origin: center;
        animation:
            cellAppear
            0.35s
            ease
            forwards;
    }

    @keyframes cellAppear {

        0% {
            opacity: 0;
            transform: translateY(-12px);
        }

        70% {
            opacity: 1;
            transform: translateY(2px);
        }

        100% {
            opacity: 1;
            transform: translateY(0);
        }

    }

</style>
""")

# --------------------------------------------------
# Background
# --------------------------------------------------

svg.append(
    f'''
    <rect
        class="background"
        x="0"
        y="0"
        width="{WIDTH}"
        height="{HEIGHT}"
        rx="12"
    />
    '''
)

# --------------------------------------------------
# Title
# --------------------------------------------------

svg.append(
    '''
    <text
        class="title"
        x="35"
        y="22"
    >
        GitHub Contributions
    </text>
    '''
)

# --------------------------------------------------
# Weekday labels
# GitHub shows Mon, Wed, Fri
# --------------------------------------------------

weekday_labels = {
    1: "Mon",
    3: "Wed",
    5: "Fri",
}

for row, label in weekday_labels.items():

    y = TOP + row * STEP + 10

    svg.append(
        f'''
        <text
            class="weekday"
            x="8"
            y="{y}"
        >
            {label}
        </text>
        '''
    )

# --------------------------------------------------
# Month labels
# --------------------------------------------------

last_month = None

for week_index, week in enumerate(weeks):

    # Look at the first day of each week
    current_date = week[0]["date"]

    month = current_date.strftime("%b")

    if month != last_month:

        x = LEFT + week_index * STEP

        svg.append(
            f'''
            <text
                class="month"
                x="{x}"
                y="38"
            >
                {month}
            </text>
            '''
        )

        last_month = month

# --------------------------------------------------
# Contribution cells
# --------------------------------------------------

animation_index = 0

for week_index, week in enumerate(weeks):

    for row, entry in enumerate(week):

        x = LEFT + week_index * STEP
        y = TOP + row * STEP

        count = 0

        if entry["item"]:

            count = entry["item"]["count"]

        # GitHub-like contribution levels
        if count == 0:

            level = 0

        elif count <= 2:

            level = 1

        elif count <= 5:

            level = 2

        elif count <= 9:

            level = 3

        elif count <= 14:

            level = 4

        else:

            level = 5

        color = PALETTE[level]

        # Diagonal / left-to-right animation
        delay = (
            week_index * 0.025
            + row * 0.012
        )

        svg.append(
            f'''
            <rect
                class="cell"
                x="{x}"
                y="{y}"
                width="{CELL}"
                height="{CELL}"
                rx="3"
                fill="{color}"
                style="animation-delay:{delay:.3f}s"
            />
            '''
        )

        animation_index += 1

# --------------------------------------------------
# Statistics / Streak Cards
# --------------------------------------------------

card_y = 160
card_height = 48

# Divider positions
divider1 = 300
divider2 = 600

# Left: total contributions
svg.append(
    f'''
    <text
        x="80"
        y="{card_y + 18}"
        fill="#f0f6fc"
        font-family="monospace"
        font-size="20"
        font-weight="bold"
        text-anchor="middle"
    >
        {data["total_contributions"]}
    </text>

    <text
        x="80"
        y="{card_y + 38}"
        fill="#8b949e"
        font-family="monospace"
        font-size="10"
        text-anchor="middle"
    >
        Contributions
    </text>
    '''
)

# Divider
svg.append(
    f'''
    <line
        x1="{divider1}"
        y1="{card_y - 4}"
        x2="{divider1}"
        y2="{card_y + card_height}"
        stroke="#30363d"
        stroke-width="1"
    />
    '''
)

# Middle: current streak
svg.append(
    f'''
    <text
        x="450"
        y="{card_y + 18}"
        fill="#39d353"
        font-family="monospace"
        font-size="20"
        font-weight="bold"
        text-anchor="middle"
    >
        {data["current_streak"]}
    </text>

    <text
        x="450"
        y="{card_y + 38}"
        fill="#8b949e"
        font-family="monospace"
        font-size="10"
        text-anchor="middle"
    >
        Current Streak
    </text>
    '''
)

# Divider
svg.append(
    f'''
    <line
        x1="{divider2}"
        y1="{card_y - 4}"
        x2="{divider2}"
        y2="{card_y + card_height}"
        stroke="#30363d"
        stroke-width="1"
    />
    '''
)

# Right: longest streak
svg.append(
    f'''
    <text
        x="750"
        y="{card_y + 18}"
        fill="#f0f6fc"
        font-family="monospace"
        font-size="20"
        font-weight="bold"
        text-anchor="middle"
    >
        {data["longest_streak"]}
    </text>

    <text
        x="750"
        y="{card_y + 38}"
        fill="#8b949e"
        font-family="monospace"
        font-size="10"
        text-anchor="middle"
    >
        Longest Streak
    </text>
    '''
)

# --------------------------------------------------
# Legend
# --------------------------------------------------

legend_y = 225

svg.append(
    f'''
    <text
        class="legend"
        x="35"
        y="{legend_y}"
    >
        Less
    </text>
    '''
)

for index, color in enumerate(PALETTE):

    x = 70 + index * 19

    svg.append(
        f'''
        <rect
            x="{x}"
            y="{legend_y - 10}"
            width="13"
            height="13"
            rx="3"
            fill="{color}"
        />
        '''
    )

svg.append(
    f'''
    <text
        class="legend"
        x="190"
        y="{legend_y}"
    >
        More
    </text>
    '''
)
# --------------------------------------------------
# Close SVG
# --------------------------------------------------

svg.append("</svg>")

OUTPUT.write_text(
    "".join(svg),
    encoding="utf-8"
)

print("SUCCESS!")
print(f"Created: {OUTPUT}")
print(f"Weeks rendered: {WEEKS}")
print(f"Cells rendered: {WEEKS * ROWS}")