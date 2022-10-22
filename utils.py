# ba_meta require api 7


"""
TODO:
UnlockAllAchievements, UnlockStoreSpecialItems,
UnlockLakeFrigid, UnlockStoreMiniGames, UnlockEpicModeInAllGames
"""


import ba
import _ba
import os


def plugin_switch_off(name: str) -> None:
    ba.app.config['Plugins'][__name__ + '.' + name]['enabled'] = False
    ba.app.config.apply_and_commit()


# ba_meta export plugin
class UnlockProVersion(ba.Plugin):
    def on_app_running(self) -> None:
        ba.app.accounts_v1.have_pro = lambda: True


# ba_meta export plugin
class UnlockAllCampaign(ba.Plugin):
    def on_app_running(self) -> None:
        ba.Level.complete = True


# ba_meta export plugin
class ShowPartyIcon(ba.Plugin):
    def on_app_running(self) -> None:
        _ba.set_party_icon_always_visible(True)


# ba_meta export plugin
class UnlockTowerDMap(ba.Plugin):
    def on_app_running(self) -> None:
        from bastd.maps import TowerD
        TowerD.play_types = ['melee', 'keep_away', 'team_flag', 'king_of_the_hill']


# ba_meta export plugin
class CreateSysFolder(ba.Plugin):
    def on_app_running(self) -> None:
        path = ba.app.python_directory_user + '/sys/' + ba.app.version
        if not os.path.exists(path):
            from ba.modutils import create_user_system_scripts, show_user_scripts
            create_user_system_scripts()
            show_user_scripts()
        else:
            ba.screenmessage('Scripts folder already exists!', (1.0, 0.5, 0.0))
        plugin_switch_off('CreateSysFolder')


# ba_meta export plugin
class DeleteSysFolder(ba.Plugin):
    def on_app_running(self) -> None:
        path = ba.app.python_directory_user + '/sys/' + ba.app.version
        if os.path.exists(path):
            from ba.modutils import delete_user_system_scripts
            delete_user_system_scripts()
            ba.screenmessage('Scripts folder deleted! Quiting from app...', (0.0, 1.0, 0.0))
            ba.timer(2.5, _ba.quit)
        else:
            ba.screenmessage('Scripts folder not exists!', (1.0, 0.5, 0.0))
        plugin_switch_off('DeleteSysFolder')


# ba_meta export plugin
class RemovePyCache(ba.Plugin):
    def on_app_running(self) -> None:
        if _ba.app.platform in ('android',):
            return
        from shutil import rmtree
        paths = (
            'ba',
            'ba/ui',
            'bastd',
            'bastd/activity',
            'bastd/actor',
            'bastd/game',
            'bastd/keyboard',
            'bastd/mapdata',
            'bastd/ui',
            'bastd/ui/account',
            'bastd/ui/coop',
            'bastd/ui/gather',
            'bastd/ui/league',
            'bastd/ui/playlist',
            'bastd/ui/profile',
            'bastd/ui/settings',
            'bastd/ui/soundtrack',
            'bastd/ui/store'
        )
        for path in paths:
            rmtree(f'{ba.app.python_directory_app}/{path}/__pycache__')
        ba.screenmessage('PyCache removed!', (0.0, 1.0, 0.0))
        plugin_switch_off('RemovePyCache')
