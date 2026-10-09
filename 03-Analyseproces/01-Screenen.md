# Stap 1. Screenen

Screenen brengt de lijst met undercovered aandelen van Seeking Alpha terug tot de vier namen die als eerste een snelle analyse krijgen. Undercovered betekent dat er op dat platform recent weinig over een bedrijf is geschreven. Ik werk in een maandelijkse batch: de lijst, vier snelle analyses, een uitgebreide analyse voor wat overblijft en een artikel op Seeking Alpha. Liggen er nog kansrijke kandidaten van een vorige batch, dan werk ik die eerst af.

## Waarom deze lijst, en waarom nu

Eerlijk gezegd is dit een keuze om kosten. Voor dit werk hoort eigenlijk een betaald abonnement op TradingView, en dat kost ongeveer €500 per jaar. In deze fase levert dat te weinig op. De undercovered-lijst heb ik als auteur op Seeking Alpha al, en voor een artikel over een aandeel van die lijst betaalt het platform een vergoeding. Dan is het veel voordeliger en efficiënter om daar te beginnen.

Een naam op die lijst is een goede aanwijzing dat een bedrijf onder de radar zit, al is het vaker een Amerikaanse smallcap dan ik uit mezelf zou kiezen. TradingView blijft op de lange termijn mijn screener. Als de tijd het toelaat, kijk ik daarmee ook weer naar kleine bedrijven buiten de Verenigde Staten.

## Doel

Per batch vier kandidaten voor de snelle analyse, elk met ticker, DeGiro-code, land, de herkomst van de naam, sector, industrie, het businessmodel in een paar woorden, de reden om verder te kijken, wat er mis kan gaan en het omzetmodel. Aan het eind van de batch is mijn doel minstens vier artikelen. Dat is een richtlijn en geen dwang: een batch waarin minder namen de analyses overleven is ook een uitkomst.

## De batch in één oogopslag

| Onderdeel | Wat er gebeurt | Waar het staat |
| --- | --- | --- |
| 1. De lijst | Ik haal de undercovered-lijst van Seeking Alpha op en kies de vier meest kansrijke namen | Deze pagina |
| 2. Vier snelle analyses | Elk van de vier krijgt de snelle analyse | [Stap 2](02-Snel-Analyseren.md) |
| 3. Bijvullen | Valt een naam snel af en is er nog ruimte in de batch, dan krijgt de volgende naam van de lijst een snelle analyse | Deze pagina en stap 2 |
| 4. Uitgebreide analyse | Wat de snelle analyse overleeft, krijgt de uitgebreide analyse en de waardering | [Stap 3](03-Uitgebreid-Analyseren.md) en [stap 4](04-Waarderen.md) |
| 5. Artikel | De afgeronde analyse wordt een artikel op Seeking Alpha, na de publicatiecontrole | [Stap 7](07-Rapporteren-Publiceren.md) |

## Wat ik klaarzet

De [voorbereiding](00-Voorbereiden.md), een map `Work-in-Progress/Screening JJJJ-MM/` voor de batch, een kopie van het screeningtemplate, de undercovered-lijst van Seeking Alpha en de investor-relationspagina's van de bedrijven die ik wil bekijken, een AI-model waarin ik jaarverslagen kan plakken, en DeGiro om handelbaarheid te controleren. De lijst staat in het auteursdeel van Seeking Alpha en is bedoeld voor wie daar schrijft. Per aandeel zie ik hoe lang het geleden is dat er een artikel over verscheen. Ik download hem als bestand, zodat ik later kan nagaan met welke versie ik werkte.

## Template en tabblad

`02-Screening.xlsx`. Ik werk alleen op het tabblad Kandidaten: één rij per aandeel met ticker, DeGiro-code, land, de herkomst van de naam in de kolom Screener, sector, industrie, het businessmodel in een paar woorden, de reden om verder te kijken, wat er mis kan gaan en het omzetmodel. Komt de naam van de Seeking Alpha-lijst, dan schrijf ik in de kolom Screener de naam van die lijst; gebruik ik de TradingView-route hieronder, dan staat daar het universum of de landenlijst. Valuta, marktkapitalisatie in de eigen valuta en in euro, Range en P/E rekent het werkboek uit via het gegevenstype Aandelen van Excel; het tabblad Fiat levert de wisselkoersen. Het tabblad Ronde vraagt geen invoer: het telt de kandidaten per screener, land en sector en laat zien welke kernvelden nog ontbreken. Het tabblad Universums is naslag voor de TradingView-route: de acht universums en drie landenlijsten met hun instellingen, zoals in [de screeners](../05-Resources/Screeners/screeners.md).

## Hoe ik de batch doe

1. Ik begin bij wat er al ligt. Zijn er kansrijke kandidaten van een vorige batch, dan werk ik die eerst af. Daarna haal ik de undercovered-lijst van Seeking Alpha op. De lijst verandert, dus ik werk elke batch met de versie van dat moment en noteer de datum bovenaan mijn notities.
2. Per naam die ik serieus overweeg doe ik direct check 1 uit de [No Go checks](Bijlagen/02-NoGo-Checks.md): is het aandeel bij DeGiro te koop, wat is de lotgrootte, hoe groot is de spread, wat zijn de kosten. Ik noteer de DeGiro-code in de kolom DeGiro. Een naam die ik niet praktisch kan kopen, gaat eraf voordat ik er tijd in steek.
3. Ik vorm een eerste indruk per naam. Kan ik in twee zinnen zeggen wat het bedrijf doet en hoe het geld verdient? Kan de omzet in tien jaar drie tot vijf keer zo groot worden? Zegt een eerste prijsvergelijking dat onderzoek de moeite waard is? Dat zijn de zeven onderwerpen uit [hoofdstuk 3](../02-Manifesto/03-Screening-Systeem.md#33-zeven-onderwerpen-bij-de-eerste-selectie), in korte vorm. Een bedrijf dat ik niet in twee zinnen kan omschrijven, krijgt een vraagteken en geen plek.
4. Staan er onder de namen die ik overweeg bedrijven uit dezelfde industrie, dan leg ik hun groei, marges en waardering naast elkaar: omzetgroei over de laatste twaalf maanden en over het laatste boekjaar, winstgroei per aandeel, brutomarge, operationele marge en nettomarge, vrije-kasstroommarge, rendement op eigen vermogen, schuld, en de waardering met P/E, PEG, koers-omzet en EV/EBITDA. Een kengetal zegt mij pas iets naast bedrijven met hetzelfde verdienmodel: een nettomarge van 8 procent is hoog voor een groothandel en laag voor een softwarebedrijf. Wat een industrie kenmerkt, staat in [Sectoren en industrieën](../05-Resources/Sectoren/README.md).
5. Van de bedrijven die eruit springen bekijk ik er een of meer op Seeking Alpha en op hun eigen investor-relationspagina: wat is de historische P/E ratio in de grafiek, wat het bedrijf zegt dat het doet, de laatste presentatie en wat anderen erover schrijven. Seeking Alpha lees ik als de mening van anderen en de investor-relationspagina als wat het bedrijf over zichzelf zegt. Geen van beide is al een controle van de cijfers. Weinig recente artikelen betekent weinig aandacht op één platform. Het zegt niet dat de markt het bedrijf verkeerd prijst, en ook niet hoeveel analisten het bedrijf volgen.
6. Wil ik meer weten, dan geef ik een AI-model de jaarverslagen, halfjaarberichten of presentaties van die bedrijven als pdf of link, met [prompt 13](../05-Resources/AI-Prompts/prompts-library.md#13-bedrijven-in-één-industrie-vergelijken). Dat levert per bedrijf een snelle eerste analyse met de bear case eerst, een vergelijking, en een keuze welk bedrijf een van de vier plekken in de batch krijgt. De cijfers die die keuze dragen, zoek ik daarna zelf op in het jaarverslag.
7. Ik kies de vier namen die het meest kansrijk lijken. De rest van de lijst blijft staan. Lukt het mij niet om vier overtuigende namen te kiezen, dan begin ik met minder; ik vul de batch niet aan met namen waar ik geen reden voor heb.
8. Ik zet de vier op het tabblad Kandidaten. In de kolom Data typ ik de ticker en zet ik de cel om naar het gegevenstype Aandelen, zodat valuta, marktkapitalisatie, de plek van de koers in de range van 52 weken en de P/E vanzelf meekomen. Zelf schrijf ik het businessmodel, de reden om verder te kijken, wat er mis kan gaan en het omzetmodel, telkens in een paar woorden of één zin. Lukt de reden niet in één zin, dan hoort de naam er niet op.
9. Elk van de vier doorloopt de [snelle analyse](02-Snel-Analyseren.md). Valt een naam snel af en is er nog ruimte in de batch, dan kies ik de volgende meest kansrijke naam van de lijst, zet die op Kandidaten en geef hem dezelfde snelle analyse. Dat herhaal ik zolang er ruimte is en er namen zijn waar ik een reden voor heb. Een naam die afvalt, krijgt zijn reden in het universumbestand.
10. De namen die de snelle analyse overleven, krijgen de [uitgebreide analyse](03-Uitgebreid-Analyseren.md) en de [waardering](04-Waarderen.md). Daaruit komt per naam een [artikel op Seeking Alpha](07-Rapporteren-Publiceren.md). Mijn doel is minstens vier artikelen per batch. Haalt een naam de analyse niet, dan schrijf ik er geen artikel over om dat aantal te halen.

De lijst is een vertrekpunt en geen advies. Een naam die erop staat, is niet daarom een koopkans.

## De route voor de lange termijn: de screener in TradingView

Zolang ik met de Seeking Alpha-lijst werk, is TradingView een aanvulling: als de lijst te weinig geschikte namen geeft, of als ik bewust een bepaald soort bedrijf of een bepaald land wil doorlopen. Op de lange termijn wordt dit weer de hoofdroute, zie [Waarom deze lijst](#waarom-deze-lijst-en-waarom-nu). De acht universums en drie landenlijsten staan op [de screenerpagina](../05-Resources/Screeners/screeners.md), met de filters en de kolommen. Universum A, snelle groeiers, is de kern van die set. D, E en F gebruiken dezelfde industrieën als A en zoeken wat A op winst, land of omvang buiten laat: D omzetgroei zonder winst, E Amerikaanse smallcaps en F midcaps. B, C, G en H zijn de vangnetten voor de industrieën die niet in A horen: B voor cyclische bedrijven die vooral een grondstofprijs of de economische cyclus volgen, C voor gereguleerde bedrijven die afhangen van overheid of toezichthouder, G voor life sciences en H voor financials en vastgoed. Alleen E kijkt naar de Verenigde Staten. Een van de drie landenlijsten, Nederland, Hongkong of de Verenigde Staten, open ik alleen als ik uit interesse een markt wil doorlopen. Ik hoef niet alle acht universums te draaien; ik pak er een erbij als ik daar een reden voor heb.

Ik open de opgeslagen screener in TradingView, sorteer de uitkomst op de kolom Industry en vergelijk per industrie de parameters uit de kolommen, zoals in punt 4 hierboven. Verander ik een filter, dan pas ik de screenerpagina aan en zet ik de reden erbij. Een naam uit deze route gaat dezelfde weg als een naam van de Seeking Alpha-lijst: check 1, een eerste indruk, een plek op het tabblad Kandidaten met het universum of de landenlijst in de kolom Screener, en dan de snelle analyse.

## Prompts

[Prompt 13, bedrijven in één industrie vergelijken](../05-Resources/AI-Prompts/prompts-library.md#13-bedrijven-in-één-industrie-vergelijken), als ik de jaarverslagen van bedrijven uit dezelfde industrie wil laten vergelijken. Bij een bedrijf dat ik niet kan plaatsen, gebruik ik [prompt 1, business snapshot](../05-Resources/AI-Prompts/prompts-library.md#1-business-snapshot) om in tien minuten te weten wat het doet en of het in mijn onderzoek past.

## Checks

Check 1, praktische uitvoerbaarheid, volledig. Check 2, hoe groot het bedrijf kan worden, en check 3, of ik het verdienmodel begrijp, alleen als eerste indruk. De rest hoort bij stap 2.

## Wat ik vastleg

Op het tabblad Kandidaten: per naam de kolommen hierboven. Bovenaan mijn notities van de batch: de datum waarop ik de Seeking Alpha-lijst heb opgehaald. Meer administratie houd ik tijdens het screenen niet bij, want die helpt mij niet kiezen. In het [universumbestand](05-Universum-Bijhouden.md): elke kandidaat die naar de snelle analyse gaat als nieuwe rij met fase Kandidaat en de datum.

## Wanneer de stap af is

De [Definition of Done](Bijlagen/03-Definition-of-Done.md) voor screening: vier kandidaten voor de snelle analyse, en op het tabblad Ronde staan geen kandidaten meer zonder reden, risico, omzetmodel of DeGiro-code. De batch zelf is af als de uitgebreide analyses van de overlevers zijn omgezet in artikelen, of als ik heb vastgelegd waarom een naam is gestopt.

## Hoe lang het duurt

Het kiezen van de vier namen mag niet de hoofdmoot van de batch worden: de tijd hoort naar de analyses te gaan. Zit ik langer in de lijst dan in de eerste snelle analyse, dan ben ik namen aan het verzamelen in plaats van aan het kiezen. Dan stop ik, noteer ik welke naam mij meetrok, en zet ik die bovenaan voor stap 2.

De content op Belegger Kees is uitsluitend bedoeld voor educatieve doeleinden en vormt geen persoonlijk beleggingsadvies. Beleggen brengt risico's met zich mee. De waarde van beleggingen kan fluctueren en je kunt je inleg verliezen. Resultaten uit het verleden bieden geen garantie voor de toekomst. Raadpleeg een erkende financieel adviseur voor advies op maat. Belegger Kees is geen geregistreerde beleggingsonderneming bij de AFM.

## Verder lezen

[Analyseproces](README.md) · [Stap 2: Snel analyseren](02-Snel-Analyseren.md) · [Screeners](../05-Resources/Screeners/screeners.md) · [Hoofdstuk 3: Aandelen screenen](../02-Manifesto/03-Screening-Systeem.md)

---

Bijgewerkt: 9 oktober 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
