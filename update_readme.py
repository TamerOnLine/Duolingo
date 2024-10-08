import requests
from bs4 import BeautifulSoup
import datetime

url = "https://www.duolingo.com/profile/RoseLisaJenne714"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    xp = None
    streak = None

    xp_element = soup.find("h4", {"class": "Tm4d"}) 
    streak_element = soup.find("div", {"class": "3u0c"}) 

    if xp_element:
        xp = xp_element.get_text()
    if streak_element:
        streak = streak_element.get_text()

    with open("README.md", "r") as file:
        content = file.readlines()

    update_line = f"### Last Updated: {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n"
    xp_line = f"**Current XP:** {xp} XP 🔥\n" if xp else "**Current XP:** Data not found\n"
    streak_line = f"**Current Streak:** {streak} days 🔥\n" if streak else "**Current Streak:** Data not found\n"

    content = [line for line in content if not line.startswith("### Last Updated:") and not line.startswith("**Current XP:**") and not line.startswith("**Current Streak:**")]
    content.append(update_line)
    content.append(xp_line)
    content.append(streak_line)

    with open("README.md", "w") as file:
        file.writelines(content)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
