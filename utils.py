# ba_meta require api 7

import ba
import _ba


# ba_meta export plugin
class ProVersion(ba.Plugin):
    def on_app_running(self) -> None:
        ba.app.accounts_v1.have_pro = lambda: True


# ba_meta export plugin
class CompleteCampaign(ba.Plugin):
    def on_app_running(self) -> None:
        ba.Level.complete = True


# ba_meta export plugin
class ShowChatIcon(ba.Plugin):
    def on_app_running(self) -> None:
        _ba.set_party_icon_always_visible(True)


# ba_meta export plugin
class UnlockTowerDMap(ba.Plugin):
    def on_app_running(self) -> None:
        from bastd.maps import TowerD
        TowerD.play_types = ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']
