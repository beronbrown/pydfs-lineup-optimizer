# PYDFS-LINEUP-OPTIMIZER 
pydfs-lineup-optimizer is a tool for creating optimal lineups for daily fantasy sport. 

## Installation
To install pydfs-lineup-optimizer, simply run:
```
$ pip install pydfs-lineup-optimizer
```


## Example
Here is an example for evaluating optimal lineup for Yahoo fantasy NBA. It loads players list from "yahoo-NBA.csv" and select 10 best lineups.
```python
from pydfs_lineup_optimizer import Site, Sport, get_optimizer


optimizer = get_optimizer(Site.DRAFTKINGS, Sport.FOOTBALL)
optimizer.load_players_from_csv("contests\DKSalaries_NFL_SHOWDOWN_WEEK_1_2020_THU.csv")
for lineup in optimizer.optimize(10):
    print(lineup)
```
