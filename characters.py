# ba_meta require api 7

"""Characters/Skins

Working only in servers with the Abyss server script.
"""

from ba import Plugin
from bastd.actor.spazappearance import Appearance

NAMES = (
    "Twins", "Mosquito", "Pyramid Head", "Turtle", "Dino", "Lollipop",
    "Hunter", "Impact", "Elemental", "Frostyk", "Frost"
)


# ba_meta export plugin
class ServerCharacters(Plugin):
    def on_app_running(self) -> None:
        for name in NAMES:
            Appearance(name)
