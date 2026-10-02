import requests
from bs4 import BeautifulSoup
import json
from datetime import date, timedelta
from pathlib import Path
import re

USERNAME = "ved-ingole"
URL = f"https://github.com/users/{USERNAME}/contributions"
OUTPUT = Path("data/contributions.json")

print(f"Fetching GitHub contributions for @{USERNAME}...")

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers, timeout=20)

print(f"HTTP status: {response.status_code}")

if response.status_code != 200:
    raise SystemExit("Failed to fetch GitHub contributions.")

soup = BeautifulSoup(response.text, "html.parser")

# --------------------------------------------------
# Build tooltip map:
# <tool-tip for="contribution-day-component-...">
#   5 contributions on ...
# </tool-tip>
# --------------------------------------------------

tooltip_counts = {}

for tooltip in soup.find_all("tool-tip"):
    target = tooltip.get("for")

    if not target:
        continue

    text = tooltip.get_text(" ", strip=True)

    match = re.search(r"(\d[\d,]*)\s+contributions?", text)

    if match:
        count = int(match.group(1).replace(",", ""))
        tooltip_counts[target] = count

# --------------------------------------------------
# Read contribution cells
# --------------------------------------------------

days = []

cells = soup.select("td[data-date][data-level]")

for cell in cells:
    day_date = cell.get("data-date")
    level = int(cell.get("data-level", 0))
    cell_id = cell.get("id")

    count = 0

    if cell_id and cell_id in tooltip_counts:
        count = tooltip_counts[cell_id]

    days.append({
        "date": day_date,
        "count": count,
        "level": level
    })

# Remove duplicates
unique_days = {}

for day in days:
    unique_days[day["date"]] = day

days = list(unique_days.values())
days.sort(key=lambda x: x["date"])

# --------------------------------------------------
# Statistics
# --------------------------------------------------

total = sum(day["count"] for day in days)

current_streak = 0
longest_streak = 0
best_day = None

# Best day
if days:
    best_day = max(days, key=lambda x: x["count"])

# Calculate streaks
streak = 0

for day in days:
    if day["count"] > 0:
        streak += 1
        longest_streak = max(longest_streak, streak)
    else:
        streak = 0

# Current streak
today = date.today()

day_map = {
    date.fromisoformat(day["date"]): day["count"]
    for day in days
}

check_date = today

# If today has no contribution, check yesterday
if day_map.get(check_date, 0) == 0:
    check_date -= timedelta(days=1)

while day_map.get(check_date, 0) > 0:
    current_streak += 1
    check_date -= timedelta(days=1)

# --------------------------------------------------
# Save JSON
# --------------------------------------------------

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

data = {
    "username": USERNAME,
    "total_contributions": total,
    "current_streak": current_streak,
    "longest_streak": longest_streak,
    "best_day": best_day,
    "days": days
}

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print()
print("SUCCESS!")
print(f"Days found: {len(days)}")
print(f"Total contributions: {total}")
print(f"Current streak: {current_streak} days")
print(f"Longest streak: {longest_streak} days")

if best_day:
    print(
        f"Best day: {best_day['date']} "
        f"({best_day['count']} contributions)"
    )

print()
print(f"Created: {OUTPUT}")