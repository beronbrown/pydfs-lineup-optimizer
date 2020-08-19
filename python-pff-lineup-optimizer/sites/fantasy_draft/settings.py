from typing import Optional
from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.lineup_printer import IndividualSportLineupPrinter
from pydfs_lineup_optimizer.sites.fantasy_draft.importer import FantasyDraftCSVImporter
from pydfs_lineup_optimizer.lineup_exporter import FantasyDraftCSVLineupExporter


class FantasyDraftSettings(BaseSettings):
    site = Site.FANTASY_DRAFT
    budget = 100000
    max_from_one_team = 6  # type: Optional[int]
    csv_importer = FantasyDraftCSVImporter
    csv_exporter = FantasyDraftCSVLineupExporter




@SitesRegistry.register_settings
class FantasyDraftFootballSettings(FantasyDraftSettings):
    sport = Sport.FOOTBALL
    positions = [
        LineupPosition('QB', ('QB', )),
        LineupPosition('RB', ('RB', )),
        LineupPosition('RB', ('RB', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('TE', ('TE', )),
        LineupPosition('FLEX', ('RB', 'WR', 'TE')),
        LineupPosition('FLEX', ('RB', 'WR', 'TE')),
        LineupPosition('DST', ('DST', ))
    ]
