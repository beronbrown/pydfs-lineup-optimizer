from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.lineup_printer import IndividualSportLineupPrinter
from pydfs_lineup_optimizer.sites.draftkings.classic.importer import DraftKingsCSVImporter
from pydfs_lineup_optimizer.sites.draftkings.captain_mode.importer import DraftKingsCaptainModeCSVImporter
from pydfs_lineup_optimizer.rules import DraftKingsBaseballRosterRule


class DraftKingsSettings(BaseSettings):
    site = Site.DRAFTKINGS
    budget = 50000
    csv_importer = DraftKingsCSVImporter





@SitesRegistry.register_settings
class DraftKingsFootballSettings(DraftKingsSettings):
    sport = Sport.FOOTBALL
    min_games = 2
    positions = [
        LineupPosition('QB', ('QB',)),
        LineupPosition('RB', ('RB',)),
        LineupPosition('RB', ('RB',)),
        LineupPosition('WR', ('WR',)),
        LineupPosition('WR', ('WR',)),
        LineupPosition('WR', ('WR',)),
        LineupPosition('TE', ('TE',)),
        LineupPosition('FLEX', ('WR', 'RB', 'TE')),
        LineupPosition('DST', ('DST',))
    ]

@SitesRegistry.register_settings
class DraftKingsFootballNCAASettings(DraftKingsSettings):
    sport = Sport.FOOTBALLNCAA
    min_games = 2
    positions = [
        LineupPosition('QB', ('QB',)),
        LineupPosition('RB', ('RB',)),
        LineupPosition('RB', ('RB',)),
        LineupPosition('WR', ('WR',)),
        LineupPosition('WR', ('WR',)),
        LineupPosition('WR', ('WR',)),
        LineupPosition('FLEX', ('WR', 'RB', 'TE')),
        LineupPosition('SUPERFLEX', ('QB','WR', 'RB', 'TE')),
        
    ]