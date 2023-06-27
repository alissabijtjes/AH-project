# RailNL


## Aan de slag
### Vereisten
Deze codebase is geschreven in Python 3.9. Er hoeven geen packages te worden geinstalleerd om de code te runnen.

### Gebruik
Bestand runnen:

python main.py

In main.py staan voorbeelden voor het gebruik van de de verschillende functies om de algoritmes te draaien.

Experimenten:
1. Random
    * Run experiment_random in main
2. Hillclimber (random-random)
    * In bestand hillclimber_experiment verander start_algorithm in random en route_heuristic in random
    * Run experiment_hillclimber in main
3. Hillclimber (random-hillclimber)
    * In bestand hillclimber_experiment verander start_algorithm in random en route_heuristic in hillclimber
    * Run experiment_hillclimber in main
4. Greedy

### Structuur
De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:
* /code: bevat alle code van dit project
    * /code/algorithms: bevat de code van de algoritmes
    * /code/classes: bevat de code van de classes
    * /code/experiments: bevat de code van de experimenten
    * /code/helper: bevat de code van helper functies
    * /code/imports: bevat de code voor het importeren van de data
    * /code/visualisation: bevat de code voor visualisatie van de case
* /data: bevat de databestanden met de stations en connecties
* /docs: bevat de bestanden met de berekening van de state space en de berekening van de theoretische optimale score
* /resultaten: bevat de het bestande met de output en de resultaten van de experimenten


## Auteurs
* Alissa Bijtjes
* Mats Cannon