# GIT training
Welkom bij de GIT lab omgeving. Hier gaan we een oefening doen waarbij je de volgende stappen gaat uitvoeren;
1. het maken van een repository
2. de main branch beschermen voor directe commits
3. een aanpassing maken met een gescheiden branch 
4. een collega de aanpassingen laten reviewen met een pull request
5. de aanpassing mergen naar de main branch op basis van onderling consensus 
6. alle uitgevoerde handelingen nakijken in de git log

### Huishoudelijke mededelingen

#### * CMD instructie prefix
Waar je een instructie ziet welke begint met "cmd:" moet het commando wat er achter staat in de web terminal worden uitgevoerd.
bijvoorbeeld;
```
cmd: ls
```
hiermee voer je "ls" in bij de web terminal


#### * Web terminal tekstverwerking
Op de web terminal kun je gebruik maken van ```vi``` of ```nano```.
Wanneer je met beiden geen ervaring hebt is het advies om nano te gebruiken.
Met deze editor kun je middels ``` nano code.py``` een nieuw bestand met de naam code.py aanmaken.
Wanneer je inhoud hebt ge- copy/paste kun je het bestand opslaan met ctrl+s.
Dit is alles wat je nodig hebt voor deze training. 



### Vorm een duo en pak een voorbeeld bronbestand
0. Zoek een collega om mee samen te werken en vorm samen een duo
   hierbij zal een collega het voortouw nemen en de handelingen primair uitvoeren.
   De tweede persoon zal acteren als "reviewer". Als dit gelukt is en voldoende tijd beschikbaar is kun je de rollen
   omdraaien en de oefening in deze setting nogmaals uitvoeren zodat je er beiden het maximale van meekrijgt. 

1. pak een stukje voorbeeld code van bijvoorbeeld: https://www.programiz.com/python-programming/examples
   als je elders een stukje voorbeeld code hebt kan dat ook worden gebruikt.

2. Kopieer de gewenste code lokaal naar je machine en houd deze beschikbaar voor later gebruik


# - - - GIT Web Interface - - -

## Maak een repository
3. maak een repository aan met een naam naar keuze
   hiervoor klik je op het + teken naast 'Repositories' in de git webinterface

4. repository formulier:
     Repository Name: <gekozen naam>
     vink aan (checkbox): Initialize repository checkbox
5. Browse naar je repository -> settings -> Collaboration
   voeg hier de naam van je collega in om samen te kunnen werken in deze repo
   geef je collega 'write' rechten

5.1. Inschakelen van branch bescherming, hiermee kan er niet direct naar main worden gepushed;
    Browse naar repository -> settings -> Branches -> Branch protection -> "Add New Rule"
5.2. Noem de rule "main" (de naam van de rule is de naam van de betreffende branch) en zorg dat disable push aan staat
5.3. Zet de optie "Required approvals" op 1, hiermee geef je aan dat tenminste 1 collega akkoord moet zijn met een aanpassing
5.4. scroll naar de onderkant van de pagina en klik op "save rule"

6. klik weer op de code tab om terug te springen naar de hoofdpagina van de repository.

6.1. kopieer de SSH url van de repository

# - - - Terminal - - - 
7. Open de online terminal en log in

7.1 cmd: git config --global user.email "${USER}@example.nl"

7.2 cmd: git config --global user.name "${USER}"
```
Met deze commando's maak je een identiteit in het git protocol
deze data kan worden gebruikt door git bijvoorbeeld in de git log
```

## Downloaden van de repository data
8.1 cmd: git clone <SSH URL>

8.2 cmd: cd ~/<repository naam>

8.3 cmd: git branch -l
```
controleer de output, deze moet als volgt zijn;
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
```

## Maak een branch aan
9.1 cmd: git checkout -b "patch-1"

9.2 cmd: git status
```
controleer output (we zouden nu op de nieuw aangemaakt branch moeten staan):
On branch patch-1
nothing to commit, working tree clean
```
Hiermee is de branch met de naam patch-1 aangemaakt.
Git weet nu van het bestaan maar deze bestaat nu enkel nog lokaal en niet remote.

```
Ga alleen verder met de onderstaande stappen als het tot zover gelukt is en de output overeenkomt met de voorbeelden.
```

9.3 maak nu je bronbestand nu aan in de map van de repository
```
Dit kun je doen met: nano <jouw bestandsnaam>
vervolgens plak je de inhoud en sla je het op met de ctrl+s toetscombinatie
je kan nakijken of het gelukt is met cat <jouw bestandsnaam>, dit moet de inhoud weergeven
```
10. cmd: git status
```
controleer de output:
Your branch is up to date with '<branch naam>'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
  <jouw bestand>
```
Dit betekend dat je bestand wel bestaat maar nog niet bekend is voor git.
Om je bestand onder versiebeheer te krijgen moeten we deze eerst toevoegen.

11. cmd: git add <jouw bestand>
12. cmd: git status
```
controleer de output:
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
new file:   hoi.txt
```
Git weet nu van het bestaan van je bestand.

13. cmd: git push origin patch-1
```
Nu is het bestand zichtbaar op het git dashboard in de 'patch-1' branch
In een productie scenario zou je dit doen met een branchnaam die overeenkomt met de inhoud van de aanpassing
```

# - - - GIT Web Interface - - -
Nu is het toevoegen van het bestand middels de patch-1 branch centraal bekend bij git. Nu gaan we een pull request maken waarmee we een collega kunnen vragen om de aanpassing te beoordelen.

### Pull request
14. navigeer naar repository -> Pull requests

14.1 klik op new pull request

14.2 zorg nu dat de twee drop-down boxes ingesteld staan om patch-1 te mergen naar main
```
merge into: main | pull from: patch-1
```

14.3. Vul nu omschrijvende informatie in over de aanpassing en klik op "create pull request"
```
Nu kan de collega welke als collabrator is toegevoegd de review uitvoeren
Het is nu zijn/haar beurt om de volgende stappen uit te voeren
```
## Reviewer,
15. navigeer naar de repository -> pull requests -> open de pull request

16.1 controleer wat er is aangepast in de "files changed" tab

16.2 klik op review en typ een beknopt comment.

16.3 klik op Approve om de aanpassing goed te keuren

17. navigeer terug naar de "conversation" tab en klik op "create merge commit"
18. voeg eventueel omschrijvende informatie toe en klik weer op "create merge commit"
```
Het merge request is nu afgerond
Op dit moment kunnen we in de terminal de log bekijken en het verloop van de aanpassing inzien
```

# - - - Terminal - - - 
19. cmd: git checkout main (om terug te switchen naar de main branch)
20. cmd: git pull (voor het ophalen van de merge-actie)
21. cmd: git log --graph

```
Het proces is nu afgerond en de aanpassing heeft zijn weg naar productie gevonden
Je kunt de rollen met je collega nu omdraaien en haar of hem een aanpassing branch laten aanmaken met een aanpassing welke jij moet reviewen
```


