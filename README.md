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
optimizer.load_players_from_csv("path_to_csv")
for lineup in optimizer.optimize(10):
    print(lineup)
```

optimizer features before model is ran
add_player_to_lineup players to include in all lineups
remove_player_from_lineup players to remove in all lineups
remove_player remove player from the optimization process
restore_player restore player to the optimization process
max_exposure set at player level or can set in optimize call for all players, Player max exposure has higher priority than max_exposure
min_exposure set at player level or can set in optimize call for all players
randomness can be set at the pool or player level through 
	set_deviation 
	min_deviation 
	max_deviation
	

```python
optimizer.add_stack(TeamStack(3))  # stack 3 players
optimizer.add_stack(TeamStack(3, for_teams=['NE', 'BAL', 'KC']))  # stack 3 players from any of specified teams
optimizer.add_stack(TeamStack(3, for_positions=['QB', 'WR', 'TE']))  # stack 3 players with any of specified positions
optimizer.add_stack(TeamStack(3, spacing=2))  # stack 3 players close to each other in range of 2 spots.
optimizer.add_stack(TeamStack(3, max_exposure=0.5))  # stack 3 players from same team with 0.5 exposure for all team stacks
optimizer.add_stack(TeamStack(3, max_exposure=0.5, max_exposure_per_team={'MIA': 0.6}))  # stack 3 players from same team with 0.5 exposure for all team stacks and 0.6 exposure for MIA
```

```python
optimizer.add_stack(PositionsStack(['QB', 'WR']))  # stack QB and WR from same team
optimizer.add_stack(PositionsStack(['QB', ('WR', 'TE')]))  # stack QB and WR or TE from same team
optimizer.add_stack(PositionsStack(['QB', 'WR'], for_teams=['NO', 'MIA', 'KC']))  # stack QB and WR for one of provided teams
optimizer.add_stack(PositionsStack(['QB', 'WR'], max_exposure=0.5))  # stack QB and WR with 0.5 exposure for all team stacks
optimizer.add_stack(PositionsStack(['QB', 'WR'], max_exposure=0.5, max_exposure_per_team={'MIA': 0.6}))  # stack QB and WR  with 0.5 exposure for all team stacks and 0.6 exposure for MIA
```

```python
rodgers_adams_group = PlayersGroup([optimizer.get_player_by_name(name) for name in ('Aaron Rodgers', 'Davante Adams')], max_exposure=0.5)
brees_thomas_group = PlayersGroup([optimizer.get_player_by_name(name) for name in ('Drew Brees', 'Michael Thomas')], max_exposure=0.5)
optimizer.add_stack(Stack([rodgers_adams_group, brees_thomas_group]))
```	
	
features during model optimization
n total number of lineups


add_stack
	
max_from_team maximum number of players allowed from each team
bans row_ids of players to exclude from all lineups
stack_sizes size of each team stack
stack_teams team three word acronym to select specific team to stack with size above
stack_sizes2 size of each game stack if applicable
game_stack_sizes game three word away @ three word home string to select specific game to stack with size above
min_salary minimum salary to use
max_exposure max exposure for all players or a vector of exposures for each player
randomness a function that takes a vector of data and randomly perturbs it