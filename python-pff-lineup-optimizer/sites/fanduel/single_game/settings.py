from typing import Type
from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.rules import FanduelSingleGameMaxQBRule
from pydfs_lineup_optimizer.sites.fanduel.classic.importer import FanDuelCSVImporter, FanDuelMVPCSVImporter
from pydfs_lineup_optimizer.sites.fanduel.single_game.importer import build_fanduel_single_game_importer


class FanDuelSingleGameSettings(BaseSettings):
    site = Site.FANDUEL_SINGLE_GAME
    budget = 60000
    max_from_one_team = 4
    csv_importer = FanDuelMVPCSVImporter  # type: Type[FanDuelCSVImporter]


@SitesRegistry.register_settings
class FanDuelSingleGameFootballSettings(FanDuelSingleGameSettings):
    sport = Sport.FOOTBALL
    extra_rules = [FanduelSingleGameMaxQBRule]
    positions = [
        LineupPosition('MVP', ('MVP', )),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K')),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K')),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K')),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K')),
    ]

@SitesRegistry.register_settings
class FanDuelSingleGameFootballNCAASettings(FanDuelSingleGameSettings):
    sport = Sport.FOOTBALLNCAA
    extra_rules = [FanduelSingleGameMaxQBRule]
    positions = [
        LineupPosition('MVP', ('MVP', )),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K')),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K')),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K')),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K')),
    ]

