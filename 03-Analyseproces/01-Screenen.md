# Stap 1. Screenen

Screenen brengt duizenden beursbedrijven terug tot vijf tot tien namen die een snelle analyse waard zijn. Ik doe het per kwartaal als doel en minimaal één keer per jaar. Liggen er nog kansrijke kandidaten van een vorige ronde, dan werk ik die eerst af.

## Doel

Een lijst van vijf tot tien kandidaten, elk met ticker, DeGiro-code, land, de screener waar de naam uit komt, sector, industrie, het businessmodel in een paar woorden, de reden om verder te kijken, wat er mis kan gaan en het omzetmodel. Een ronde zonder geschikte kandidaten is ook een uitkomst.

## Wat ik klaarzet

De [voorbereiding](00-Voorbereiden.md), een map `Work-in-Progress/Screening JJJJ-MM/`, een kopie van het screeningtemplate, TradingView met de opgeslagen screeners, Seeking Alpha en de investor-relationspagina's van de bedrijven die ik wil bekijken, een AI-model waarin ik jaarverslagen kan plakken, en DeGiro om handelbaarheid te controleren.

## Template en tabblad

`02-Screening.xlsx`. Ik werk alleen op het tabblad Kandidaten: één rij per aandeel met ticker, DeGiro-code, land, de screener waar de naam uit komt, sector, industrie, het businessmodel in een paar woorden, de reden om verder te kijken, wat er mis kan gaan en het omzetmodel. Valuta, marktkapitalisatie in de eigen valuta en in euro, Range en P/E rekent het werkboek uit via het gegevenstype Aandelen van Excel; het tabblad Fiat levert de wisselkoersen. Het tabblad Ronde vraagt geen invoer: het telt de kandidaten per screener, land en sector en laat zien welke kernvelden nog ontbreken. Het tabblad Universums is naslag: de acht universums en drie landenlijsten met hun instellingen, zoals in [de screeners](../05-Resources/Screeners/screeners.md).

## Hoe ik de ronde doe

1. Ik begin met universum A, snelle groeiers. Dat is mijn hoofdroute. D, E en F gebruiken dezelfde industrieën als A en zoeken wat A op winst, land of omvang buiten laat: D omzetgroei zonder winst, E Amerikaanse smallcaps en F midcaps. B, C, G en H zijn de vangnetten voor de industrieën die niet in A horen: B voor cyclische bedrijven die vooral een grondstofprijs of de economische cyclus volgen, C voor gereguleerde bedrijven die afhangen van overheid of toezichthouder, G voor life sciences en H voor financials en vastgoed. Alleen E kijkt naar de Verenigde Staten. Die universums pak ik erbij als ik daar een reden voor heb. Twee of drie universums per kwartaal is genoeg; ik hoef niet alle acht elke keer te draaien. Een van de drie landenlijsten, Nederland, Hongkong of de Verenigde Staten, open ik alleen als ik uit interesse een markt wil doorlopen; dat is geen vaste stap.
2. Ik open de opgeslagen screener in TradingView. De filters en kolommen staan daarin en op [de screenerpagina](../05-Resources/Screeners/screeners.md); die schrijf ik niet per ronde opnieuw over. Verander ik een filter, dan pas ik de screenerpagina aan en zet ik de reden erbij.
3. Ik sorteer de uitkomst op de kolom Industry. Dan staan vergelijkbare bedrijven onder elkaar en zie ik per industrie wie harder groeit, wie een hogere marge haalt en wie lager gewaardeerd is. Een kengetal zegt mij pas iets naast bedrijven met hetzelfde verdienmodel: een nettomarge van 8 procent is hoog voor een groothandel en laag voor een softwarebedrijf. Wat een industrie kenmerkt, staat in [Sectoren en industrieën](../05-Resources/Sectoren/README.md). Een bedrijf dat ik niet in twee zinnen kan omschrijven, krijgt een vraagteken en geen plek.
4. Per industrie vergelijk ik de parameters uit de kolommen: omzetgroei over de laatste twaalf maanden en over het laatste boekjaar, winstgroei per aandeel, brutomarge, operationele marge en nettomarge, vrije-kasstroommarge, rendement op eigen vermogen, schuld, en de waardering met P/E, PEG, koers-omzet en EV/EBITDA. De bedrijven die eruit springen, of die ik niet kan verklaren, neem ik mee naar de volgende stap.
5. Van die bedrijven bekijk ik er een of meer op Seeking Alpha en op hun eigen investor-relationspagina: wat is de historische P/E ratio in de grafiek, wat het bedrijf zegt dat het doet, de laatste presentatie en wat anderen erover schrijven. Seeking Alpha lees ik als de mening van anderen en de investor-relationspagina als wat het bedrijf over zichzelf zegt. Geen van beide is al een controle van de cijfers.
6. Wil ik meer weten, dan geef ik een AI-model de jaarverslagen, halfjaarberichten of presentaties van die bedrijven als pdf of link, met [prompt 13](../05-Resources/AI-Prompts/prompts-library.md#13-bedrijven-in-één-industrie-vergelijken). Dat levert per bedrijf een snelle eerste analyse met de bear case eerst, een vergelijking, en een keuze welk bedrijf de beperkte plek op mijn lijst voor de snelle analyse krijgt. De cijfers die die keuze dragen, zoek ik daarna zelf op in het jaarverslag.
7. Per naam die overblijft doe ik direct check 1 uit de [No Go checks](Bijlagen/02-NoGo-Checks.md): is het aandeel bij DeGiro te koop, wat is de lotgrootte, hoe groot is de spread, wat zijn de kosten. Ik noteer de DeGiro-code in de kolom DeGiro. Een naam die ik niet praktisch kan kopen, gaat eraf voordat ik er tijd in steek.
8. Ik zet de kandidaat op het tabblad Kandidaten. In de kolom Data typ ik de ticker en zet ik de cel om naar het gegevenstype Aandelen, zodat valuta, marktkapitalisatie, de plek van de koers in de range van 52 weken en de P/E vanzelf meekomen. Zelf schrijf ik het businessmodel, de reden om verder te kijken, wat er mis kan gaan en het omzetmodel, telkens in een paar woorden of één zin. Lukt de reden niet in één zin, dan hoort de naam er niet op.
9. Bij meer dan tien namen kies ik de vijf waar ik het minst van begrijp en het meest nieuwsgierig naar ben. Die gaan naar de snelle analyse; de rest haal ik van de lijst.

## Prompts

[Prompt 13, bedrijven in één industrie vergelijken](../05-Resources/AI-Prompts/prompts-library.md#13-bedrijven-in-één-industrie-vergelijken), als ik de jaarverslagen van bedrijven uit dezelfde industrie wil laten vergelijken. Bij een bedrijf dat ik niet kan plaatsen, gebruik ik [prompt 1, business snapshot](../05-Resources/AI-Prompts/prompts-library.md#1-business-snapshot) om in tien minuten te weten wat het doet en of het in het universum thuishoort.

## Checks

Check 1, praktische uitvoerbaarheid, volledig. Check 2, hoe groot het bedrijf kan worden, en check 3, of ik het verdienmodel begrijp, alleen als eerste indruk. De rest hoort bij stap 2.

## Wat ik vastleg

Op het tabblad Kandidaten: per naam de kolommen hierboven. Meer administratie houd ik tijdens het screenen niet bij, want die helpt mij niet kiezen. In het [universumbestand](05-Universum-Bijhouden.md): elke kandidaat die naar de snelle analyse gaat als nieuwe rij met fase Kandidaat en de datum.

## Wanneer de stap af is

De [Definition of Done](Bijlagen/03-Definition-of-Done.md) voor screening: vijf tot tien kandidaten, en op het tabblad Ronde staan geen kandidaten meer zonder reden, risico, omzetmodel of DeGiro-code. Ik pas geen filter aan alleen om de lijst alsnog te vullen.

## Hoe lang het duurt

Een middag voor de filters, het sorteren en de vergelijking per industrie. Een vergelijking van jaarverslagen met AI doe ik alleen voor de industrie waar ik het meest nieuwsgierig naar ben. Duurt het langer, dan ben ik namen aan het onderzoeken in plaats van aan het screenen. Dan stop ik, noteer ik welke naam mij meetrok, en zet ik die bovenaan voor stap 2.

## Verder lezen

[Analyseproces](README.md) · [Stap 2: Snel analyseren](02-Snel-Analyseren.md) · [Screeners](../05-Resources/Screeners/screeners.md) · [Hoofdstuk 3: Aandelen screenen](../02-Manifesto/03-Screening-Systeem.md)

---

Bijgewerkt: 15 september 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
