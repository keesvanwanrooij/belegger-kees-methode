# Startpagina voor AI-agents

Deze pagina bevat de werkafspraken voor AI-agents in de repository van de Belegger Kees Methode. De bestandsnaam is een toegangspunt, geen beperking tot een bepaalde aanbieder. Neem niet aan dat een omgeving dit bestand automatisch heeft geladen; lees het expliciet.

De [README](README.md) is de startpagina voor menselijke lezers. Hier staat hoe we aan die inhoud werken. Er is geen afzonderlijk lokaal instructiebestand naast deze pagina nodig.

## Drie regels die altijd gelden

Deze regels gelden ook in een openbare clone zonder `00-Merkgids`.

1. **Educatie, geen advies.** Nooit een aandeel, fonds of product aanbevelen om te kopen of te verkopen, nooit een koersdoel of een rendement in het vooruitzicht, nooit een reactie op iemands persoonlijke situatie met een handelsadvies, nooit de suggestie dat beleggen zonder risico is. Twee vragen: staat er wat iemand moet doen, en is het gericht op deze ene persoon? Allebei ja is advies en mag niet.
2. **Geen verboden woorden, ook niet in een ontkennende zin:** ruis, hype, in de wereld van vandaag, transformeren, state-of-the-art, naadloos, innovatief, snel rijk, gegarandeerd rendement, logica boven emotie, emoties uitsluiten.
3. **Geen lang streepje, en niets verzinnen.** Gebruik een komma, een punt, een dubbele punt of een gewoon streepje. Verzin nooit een cijfer, bron, datum of citaat: kun je het niet controleren, zet er `[te controleren]` bij.

## Het doel begrijpen

Kees van Wanrooij legt zijn persoonlijke analyseproces vast: fundamentele aandelenanalyse, waardering, beleggingspsychologie en NLP. Hij modelleert ook zijn eigen denken en taal. De openbare inhoud moet bruikbaar en controleerbaar zijn en de herkenbaarheid van Belegger Kees versterken.

Vindbaarheid in zoekmachines en AI-zoekresultaten is een doel, geen beloofde uitkomst. Verzin geen bewezen beleggingsvoorsprong, kwalificaties, gebruikersaantallen of beschikbare producten.

## Leesroute bij een opdracht

1. Lees de actuele gebruikersopdracht en [README](README.md).
2. Controleer de werkboom en lees de documenten die de opdracht raakt.
3. Als `00-Merkgids/README.md` lokaal bestaat, lees die wegwijzer en de relevante interne documenten.
4. Lees vervolgens de passende hoofdstukken, procedures, bronafspraken en hulpmiddelen.
5. Meld een inhoudelijk conflict of ontbrekende beslissing voordat je daar zelf een nieuwe visie voor invult.

`00-Merkgids/` bevat alle merkafspraken: merk en stem, schrijfregels en verboden woorden, de juridische grens met de disclaimervormen, huisstijl, vindbaarheid, vertrouwen en de publicatiebesluiten. De README van die map zegt wat je bij welke opdracht leest.

In een openbare clone ontbreekt `00-Merkgids` bewust. De publieke [schrijfwijze](01-Docs/02-Schrijfwijze.md), [redactionele werkwijze](01-Docs/01-Redactionele-Werkwijze.md) en het Manifesto geven dan de basis. Een gewone correctie hoeft daarop niet vast te lopen. Vraag Kees om context wanneer een merk- of visiekeuze die ontbrekende informatie werkelijk nodig heeft.

## Waar informatie hoort

| Locatie | Functie |
| --- | --- |
| `00-Merkgids/` | Belangrijke informatie over het merk Belegger Kees die de combinatie van minset en beleggen vormt. Belegger Kees is het Nederlandse merk voor NLP voor financiën |
| `04-Onderzoek/Work-in-Progress/` | De werkmap: screeningronden, ingevulde templates, het universum en lopende analyses. Negeert zichzelf via een eigen `.gitignore`; alleen die en de README zijn zichtbaar |
| [01-Docs](01-Docs/README.md) | Openbare afspraken over bronnen, schrijven, publiceren en vertrouwen |
| [02-Manifesto](02-Manifesto/README.md) | De persoonlijke beleggingsfilosofie en uitleg van de methode |
| [03-Analyseproces](03-Analyseproces/README.md) | Praktische onderzoeksprocedures |
| [04-Onderzoek](04-Onderzoek/README.md) | Bewust gedeelde analyses, besluiten en terugblikken |
| [05-Resources](05-Resources/README.md) | Herbruikbare templatespecificaties, screeners, prompts en achtergrond |
| [06-Community](06-Community/README.md) | De rol van samen leren en eventuele verdere begeleiding |
| [07-NLP-coaching-voor-beleggers](07-NLP-coaching-voor-beleggers/README.md) | NLP-coaching voor beleggers: hulpvragen, technieken, koppeltabel en de coachingssessie |
| [08-Over-Belegger-Kees](08-Over-Belegger-Kees/README.md) | Maker, achtergrond en contact |

De openbare methode mag voor begrip niet afhankelijk zijn van een privébestand. Link vanuit openbare lezerspagina's naar openbare uitleg. Interne navigatie op deze agentpagina mag privélocaties noemen, zonder hun inhoud openbaar te maken.

## Waarom de merkgids buiten Git blijft

Interne strategie, persoonlijke antwoorden en levende analyses zijn niet voor publieke verspreiding bedoeld. `00-Merkgids/`, de inhoud van `04-Onderzoek/Work-in-Progress/` en feedbackbestanden worden genegeerd. Zet nieuwe interne inhoud daar neer en controleer de ignore-regel voordat je aan publicatie of staging denkt.

Git-ignore verwijdert geen eerder gevolgde bestanden of geschiedenis. Forceer geen toevoeging van genegeerde bestanden. Bekijk vóór een eventuele toekomstige openbare release ook de bestaande geschiedenis: oudere versies kunnen informatie bevatten die nu intern staat.

Een eigen website-export moet een expliciete selectie openbare bestanden gebruiken. De aanwezigheid van een ignore-regel is geen garantie dat ieder exportscript die respecteert.

## Inhoudelijke afspraken

- Alle beleggingsdrempels, aantallen en tijdsindicaties zijn richtlijnen met ruimte voor gemotiveerde afwijking. Dit is geen toestemming om feiten te verzinnen of privacycontroles over te slaan.
- Screening: per kwartaal als doel, jaarlijks als minimum; bestaande kansrijke kandidaten mogen voorgaan. Werkbare selectie vijf tot tien namen. Acht universums: A snelle groeiers (hoofdroute), B cyclische bedrijven, C gereguleerde bedrijven, D omzetgroei zonder winst, E Amerikaanse smallcaps, F midcaps, G life sciences, H financials en vastgoed. A, D, E en F delen dezelfde industrieën; B, C, G en H zijn de vangnetten voor de rest, en elke industrie hoort bij precies één van A, B, C, G en H. Alleen E bevat de Verenigde Staten. Daarnaast drie landenlijsten (Nederland, Hongkong, Verenigde Staten) buiten de hoofdroute.
- De Excel-werkboeken `03-Snelle-Analyse.xlsx` en `04-Uitgebreide-Analyse.xlsx` zijn door Kees met de hand aangepast. Bouw ze nooit opnieuw vanuit een script; wijzig ze in Excel zelf en houd de documentatie gelijk aan hun indeling.
- Tien directe No Go checks en zes aanvullende vragen, zonder verplichte totaalscore.
- Een snelle analyse helpt kiezen waar de volgende ongeveer twintig onderzoeksuren het meest zinvol zijn.
- Watchlist betekent een afgerond dossier met koopzone waarvan de prijs nog niet past. Onderzoeksfase en reden om te volgen blijven apart.
- DCF: jaar 0 en prognosejaren 1–11, eindmultiple als hoofdmethode, Gordon Growth als controle; doorgaans 8–12 procent als onderbouwde subjectieve disconteringsvoet.
- De werkset is vijf Excel-werkboeken en twee Word-sjablonen in `05-Resources/Templates/`, gebouwd met scripts en in Excel doorgerekend. Status: werkversie, nog niet in een echte doorloop getoetst. Noem ze niet gevalideerd.
- NLP is hier neurolinguïstisch programmeren. Persoonlijke modellering is niet hetzelfde als een getraind AI-model of bewijs van voorspellend rendement.
- NLP-coaching: Kees is opgeleid als NLP Practitioner; noem geen instituut, Master-titel of andere certificering zonder bevestiging. Coaching is geen therapie en geen beleggingsadvies; beschrijf NLP niet als wetenschappelijk bewezen. Betaalde coachingssessies mogen genoemd worden zonder prijs, met verwijzing naar beleggerkees.nl; registreren voor de Community via https://community.beleggerkees.nl/registreren. Geen verzonnen klantverhalen, citaten of resultaten, en niets van klanten of leden in een publicatie zonder schriftelijke toestemming. De ambitie om de herkenbare naam voor NLP-coaching voor beleggers te worden, blijft een ambitie en geen claim.
- Gebruik publiek aandelenanalyse en onderzoeksrapport. Voeg geen betaalde rapportstatus, koopadvies, prijs of beschikbaarheid toe.

## Taal en broncontrole

Schrijf in begrijpelijk Nederlands, met volledige zinnen en concrete uitleg. Gebruik de ik-vorm voor Kees' vastgelegde afwegingen. Vermijd geforceerde tegenstellingen, losse slogans en een afstandelijke bedrijfsstem. Herkenbare taal betekent niet dat je nieuwe persoonlijke ervaringen mag verzinnen.

Ieder cijfer kan informatie zijn. Beoordeel herkomst, relevantie en betrouwbaarheid. Markeer onbevestigde gegevens en controleer feiten die een conclusie dragen. Scheid feiten, berekeningen, aannames, scenario's en interpretaties.

Verifieer veranderlijke externe claims aan actuele primaire bronnen. Een modelberekening mag verwachtingen tonen, maar wordt niet als objectief koersdoel of persoonlijk advies gepresenteerd. Taalobservaties bewijzen geen intentie of misleiding.

## Aanpassingen uitvoeren

Blijf binnen deze repository. Wijzig geen andere projecten, betaalinstellingen of publicatiekanalen zonder aparte opdracht.

Bewaar bestaande gebruikerswijzigingen. Lees een document voordat je het herschrijft. Als je een map verplaatst, werk links en metadata mee bij. Iedere README verwijst naar de root en waar relevant naar de bovenliggende map en inhoudelijke vervolgstappen.

Corrigeer historische gegevens transparant. Schrijf geen beleggingsbeslissing of positie op die Kees niet heeft genomen. Interne uitvoeringsnotities mogen in `00-Merkgids`.

Bij ontbrekende informatie: stel een concrete vraag op de manier die Kees vraagt. Als hij een leesbaar vragenbestand wil, maak dat bestand. Blokkeer gewone uitvoering niet met onnodige vragen.

## Controleren en overdragen

Controleer relatieve links, oude mapverwijzingen, tellingen, bronvermeldingen en de scheiding tussen privé en publiek. Reken aangepaste financiële voorbeelden na. Zeg wat wel is gecontroleerd en wat niet.

Ik commit en push niet uit mezelf. Is werk klaar om vast te leggen, dan geef ik in de chat een kant-en-klaar codeblok dat Kees zelf kan kopiëren of direct kan uitvoeren:

```bash
git add .
git commit -m "<Engelse omschrijving, door mij voorgesteld>"
git push
```

Dat hij dit zelf uitvoert, geldt als zijn goedkeuring voor precies die wijziging. Vraagt hij mij expliciet om zelf te committen of te pushen, dan doe ik dat direct. Publicatie, een wijziging van de zichtbaarheid van een repository en elke ingreep in de Git-geschiedenis (force-push, reset, rewrite) blijven altijd een aparte, met naam genoemde opdracht vereisen; het uitvoeren van een gewone add-commit-push-reeks is daarvoor niet genoeg.

Geef na afloop de belangrijkste wijzigingen, leesroute en open controles terug in de chat.

## Verder lezen

[De Belegger Kees Methode](README.md) · [Openbare documentatie](01-Docs/README.md) · [Analyseproces](03-Analyseproces/README.md)

---

Bijgewerkt: 14 september 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
