from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.sites.yahoo.importer import YahooCSVImporter
from pydfs_lineup_optimizer.lineup_exporter import YahooCSVLineupExporter


class YahooSettings(BaseSettings):
    site = Site.YAHOO
    budget = 200
    max_from_one_team = 6
    csv_importer = YahooCSVImporter
    csv_exporter = YahooCSVLineupExporter



@SitesRegistry.register_settings
class YahooFootballSettings(YahooSettings):
    sport = Sport.FOOTBALL
    positions = [
        LineupPosition('QB', ('QB', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('RB', ('RB', )),
        LineupPosition('RB', ('RB', )),
        LineupPosition('TE', ('TE', )),
        LineupPosition('FLEX', ('WR', 'RB', 'TE')),
        LineupPosition('DEF', ('DEF', ))
    ]

