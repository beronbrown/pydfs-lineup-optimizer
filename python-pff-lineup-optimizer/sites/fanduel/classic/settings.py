from typing import List, Type, Optional
from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.lineup_printer import IndividualSportLineupPrinter
from pydfs_lineup_optimizer.rules import OptimizerRule, FanduelBaseballRosterRule
from pydfs_lineup_optimizer.sites.fanduel.classic.importer import FanDuelCSVImporter, FanDuelLOLCSVImporter, \
    FanDuelMVPCSVImporter


class FanDuelSettings(BaseSettings):
    site = Site.FANDUEL
    budget = 60000
    max_from_one_team = 4  # type: Optional[int]
    min_teams = 3  # type: Optional[int]
    csv_importer = FanDuelCSVImporter





@SitesRegistry.register_settings
class FanDuelFootballSettings(FanDuelSettings):
    sport = Sport.FOOTBALL
    positions = [
        LineupPosition('QB', ('QB', )),
        LineupPosition('RB', ('RB', )),
        LineupPosition('RB', ('RB', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('TE', ('TE', )),
        LineupPosition('FLEX', ('RB', 'WR', 'TE')),
        LineupPosition('DEF', ('D', )),
    ]

@SitesRegistry.register_settings
class FanDuelFootballNCAASettings(FanDuelSettings):
    sport = Sport.FOOTBALLNCAA
    positions = [
        LineupPosition('QB', ('QB', )),
        LineupPosition('RB', ('RB', )),
        LineupPosition('RB', ('RB', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('SUPERFLEX', ('QB','RB', 'WR', 'TE')),
    ]

