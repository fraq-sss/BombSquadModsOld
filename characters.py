"""Characters/Skins

Working only in servers with the Abyss server script.
"""

from bastd.actor.spazappearance import Appearance

names = (
    "Twins", "Mosquito", "Pyramid Head", "Turtle", "Dino", "Lollipop",
    "Hunter", "Impact", "Elemental", "Frostyk", "Frost"
)

for name in names:
    Appearance(name)
