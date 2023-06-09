# RailNL
Welke trein waar en wanneer rijdt wordt bepaald door de lijnvoering. Maar wat is de optimale samenstelling van deze trajecten? In deze case wordt een oplossing gezocht om een optimale lijnvoering te maken voor Nederland. Hier zijn bepaalde voorwaarden aan verbonden, zo mag een traject niet langer zijn dan 180 minuten en mogen er maximaal 20 trajecten worden gebruikt. Daarbij is de data over de stations en de connecties tussen stations beschikbaar. Voor de bepaling van de kwaliteit van de lijnvoering is een doelfunctie opgesteld: 
```
 K = p*10000 - (T*100 + Min)
```
waarbij p de fractie van bereden verbindingen is, T het aantal trajecten en Min de totale tijd van alle trajecten.

## Aanpak algoritmen
### Random
Het random algoritme kiest eerst random hoeveel trajecten er gemaakt worden. Daarna begint het op een random station en kiest het volgende station random. Dit loopt tot dat elk traject de maximale tijd bereden heeft. Dit is dus niet random. Het algoritme maakt altijd alle trajecten af, ook al zijn alle verbindingen al bereden.

### Greedy
Het greedy algoritme begint elke keer bij het station met de minste verbindingen wat nog niet bezocht is. Vervolgens kijkt het of er verbindingen zijn die nog niet bereden zijn. Als alle verbindingen bereden zijn kijkt het naar alle verbonden stations en of er een station is die een niet bereden verbinding heeft. Als alle verbonden station geen niet-bereden verbindingen hebben stopt het traject. Het algoritme stopt direct wanneer alle verbindingen bereden zijn. Hier is niks random een dit algoritme geeft dus elke keer precies dezelfde oplossing.

### Hillclimber
Voor het hillclimber algoritme wordt een random of greedy beginoplossing gegenereerd. Daarna wordt er een nieuwe oplossing gemaakt waarbij 1 random traject wordt uitgekozen uit de gehele lijnvoering en deze wordt verandert in een nieuw traject. Dit nieuwe traject kan bestaan uit een random gegenereerd traject of een traject met heuristieken die kiest voor connecties die nog niet bereden zijn. Als de nieuwe oplossing een hogere K-waarde heeft dan de huidige oplossing wordt deze de nieuwe huidige oplossing.

## Aan de slag
### Vereisten
Deze codebase is geschreven in Python 3.9. De requirements zijn te downloaden via pip met de volgende instructie.
```
pip install -r requirements.txt
```

### Gebruik
Om de algoritmes en experimenten te runnen kan het onderstaande in de terminal worden gebruikt (of gebruik python ipv. python3).
```
python3 main.py {experiment} {iteraties}
```
#### Runnen algoritmes:
Voor het runnen van de algoritmes gebruik het gewenste aantal iteraties.
1. Run random algoritme
    - {experiment} = random_alg

2. Run greedy algoritme
    - {experiment} = greedy_alg

3. Run hillclimber algoritme
    - {experiment} = hillclimber_alg

#### Runnen experimenten:
Voor het runnen van experimenten 1 t/m 6 zijn 1000000 iteraties gedaan. Voor experiment 7 zijn 10000 iteraties gedaan.
1. Run random experiment
    - {experiment} = random_exp

2. Run hillclimber experiment(random-random) met begin is random en algoritme is random
    - {experiment} = hill_exp_rr

3. Run hillclimber experiment (random-hillclimber) met begin is random en algoritme is hillclimber
    - {experiment} = hill_exp_rh

4. Run hillclimber experiment (greedy-hillclimber) met begin is greedy en algoritme is hillclimber
    - {experiment} = hill_exp_g

5. Run hillclimber experiment (greedy-hillclimber) met begin is greedy11 en algoritme is hillclimber
    - {experiment} = hill_exp_g11

6. Run hillclimber experiment (greedy-hillclimber) met begin is greedy12 en algoritme is hillclimber
    - {experiment} = hill_exp_g12

7. Run hillclimber experiment (different number of routes)
    - {experiment} = hill_exp_routes

### Structuur
De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:
* /code: bevat alle code van dit project.
    * /code/algorithms: bevat de code van de algoritmes.
    * /code/classes: bevat de code van de classes.
    * /code/experiments: bevat de code van de experimenten.
    * /code/helper: bevat de code van helper functies.
    * /code/imports: bevat de code voor het importeren van de data.
    * /code/visualisation: bevat de code voor visualisatie van de case.
* /data: bevat de databestanden met de stations en connecties tussen stations voor Holland en Nationaal.
* /documents: bevat de bestanden met de berekening van de state space en de berekening van de theoretische optimale score.
* /results: bevat de bestanden met de output en de resultaten van de experimenten.
    * /results/greedy-hillclimber: bevat de bestanden met de grafieken van de greedy experimenten.
    * /results/hillclimber-r-h: bevat het bestand met de grafiek van hillclimber experiment.
    * /results/hillclimber-r-r: bevat het bestand met de grafiek van hillclimber experiment.
    * /results/hillclimber-trajects: bevat het bestand met de grafiek van hillclimber trajecten experiment.
    * /results/random: bevat het bestand met de grafiek van het random experiment.

## Auteurs
* Alissa Bijtjes
* Mats Cannon