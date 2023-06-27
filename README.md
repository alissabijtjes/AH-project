# RailNL
Welke trein waar en wanneer rijdt wordt bepaald door de lijnvoering. Maar wat is de optimale samenstelling van deze trajecten? In deze case wordt een oplossing gezocht om een optimale lijnvoering te maken voor Nederland. Hier zijn bepaalde voorwaarden aan verbonden, zo mag een traject niet langer zijn dan 180 minuten en mogen er maximaal 20 trajecten worden gebruikt. Daarbij is de data over de stations en de connecties tussen stations beschikbaar. Voor de bepaling van de kwaliteit van de lijnvoering is een doelfunctie opgesteld: 
```
 K = p*10000 - (T*100 + Min)
```

## Aanpak algoritmen
### Random

### Greedy

### Hillclimber
Voor het hillclimber algoritme wordt een random beginoplossing gegenereerd. Daarna wordt er een nieuwe oplossing gemaakt waarbij 1 random traject wordt uitgekozen uit de gehele lijnvoering en deze wordt verandert in een nieuw traject. Dit nieuwe traject kan bestaan uit een random gegenereerd traject of een traject met heuristieken die kiest voor connecties die nog niet bereden zijn. Als de nieuwe oplossing een hogere K-waarde heeft dan de huidige oplossing wordt deze de nieuwe huidige oplossing.

## Aan de slag
### Vereisten
Deze codebase is geschreven in Python 3.9. Er hoeven geen packages te worden geinstalleerd om de code te runnen.

### Gebruik
Bestand runnen:

```
python main.py
```
In main.py staan voorbeelden voor het gebruik van de de verschillende functies om de algoritmes te draaien.

Runnen experimenten:
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