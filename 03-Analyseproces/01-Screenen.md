# Stap 1. Screenen

Screenen is het vinden van de top 50 kansen die het meest beloven. Uit die lijst pak ik steeds de volgende naam voor een snelle analyse. Mijn doel is een ronde per kwartaal en mijn minimum is een ronde per jaar. Liggen er nog kansrijke kandidaten van een vorige ronde, dan werk ik die eerst af.

## Twee bronnen, en waarom

Twee bronnen voeden samen één lijst: de lijst met undercovered aandelen van Seeking Alpha en de acht universums in de screener van TradingView. Undercovered betekent dat er op dat platform recent weinig over een bedrijf is geschreven.

Eerlijk gezegd is de zware rol van die eerste lijst een keuze om kosten. Voor TradingView hoort eigenlijk een betaald abonnement, en dat kost ongeveer €500 per jaar. In deze fase levert dat te weinig op. De undercovered-lijst heb ik als auteur op Seeking Alpha al, dus dan is het veel voordeliger en efficiënter om daar te beginnen.

Een naam op die lijst is een goede aanwijzing dat een bedrijf onder de radar zit, al is het vaker een Amerikaanse smallcap dan ik uit mezelf zou kiezen. TradingView blijft op de lange termijn mijn hoofdroute. Als de tijd het toelaat, kijk ik daarmee ook weer naar kleine bedrijven buiten de Verenigde Staten.

## Doel

Een top 50 op volgorde van belofte, elk met ticker, DeGiro-code, land, de herkomst van de naam, sector, industrie, het businessmodel in een paar woorden, de reden om verder te kijken, wat er mis kan gaan en het omzetmodel. Vind ik minder overtuigende namen, dan laat ik het daarbij.

## Wat ik klaarzet

De [voorbereiding](00-Voorbereiden.md), een map `Work-in-Progress/Screening JJJJ-MM/` voor de ronde, een kopie van het screeningtemplate, de undercovered-lijst van Seeking Alpha, TradingView met de opgeslagen screeners, de investor-relationspagina's van de bedrijven die ik wil bekijken, een AI-model waarin ik jaarverslagen kan plakken, en DeGiro om handelbaarheid te controleren. De undercovered-lijst staat in het auteursdeel van Seeking Alpha en is bedoeld voor wie daar schrijft. Per aandeel zie ik hoe lang het geleden is dat er een artikel over verscheen. Ik download hem als bestand, zodat ik later kan nagaan met welke versie ik werkte.

## Template en tabblad

`02-Screening.xlsx`. Ik werk alleen op het tabblad Kandidaten: één rij per aandeel met ticker, DeGiro-code, land, de herkomst van de naam in de kolom Screener, sector, industrie, het businessmodel in een paar woorden, de reden om verder te kijken, wat er mis kan gaan en het omzetmodel. In de kolom Screener staat de naam van de lijst, het universum of de landenlijst. De kolom # geeft de volgorde van belofte. Valuta, marktkapitalisatie in de eigen valuta en in euro, Range en P/E rekent het werkboek uit via het gegevenstype Aandelen van Excel; het tabblad Fiat levert de wisselkoersen. Het tabblad Ronde vraagt geen invoer: het telt de kandidaten per screener, land en sector en laat zien welke kernvelden nog ontbreken. Het tabblad Universums is naslag: de acht universums en drie landenlijsten met hun instellingen, zoals in [de screeners](../05-Resources/Screeners/screeners.md).

## Hoe ik een ronde doe

1. Ik begin bij wat er al ligt. Zijn er kansrijke kandidaten van een vorige ronde, dan werk ik die eerst af. Daarna haal ik de undercovered-lijst op en open ik de screeners die ik deze ronde wil gebruiken. Beide lijsten veranderen, dus ik noteer de datum bovenaan mijn notities.
2. Per naam die ik serieus overweeg doe ik direct check 1 uit de [No Go checks](Bijlagen/02-NoGo-Checks.md): is het aandeel bij DeGiro te koop, wat is de lotgrootte, hoe groot is de spread, wat zijn de kosten. Ik noteer de DeGiro-code in de kolom DeGiro. Een naam die ik niet praktisch kan kopen, gaat eraf voordat ik er tijd in steek.
3. Ik vorm een eerste indruk per naam. Kan ik in twee zinnen zeggen wat het bedrijf doet en hoe het geld verdient? Kan de omzet in tien jaar drie tot vijf keer zo groot worden? Zegt een eerste prijsvergelijking dat onderzoek de moeite waard is? Dat zijn de zeven onderwerpen uit [hoofdstuk 3](../02-Manifesto/03-Screening-Systeem.md#33-zeven-onderwerpen-bij-de-eerste-selectie), in korte vorm. Een bedrijf dat ik niet in twee zinnen kan omschrijven, krijgt een vraagteken en geen plek.
4. Bedrijven uit dezelfde industrie leg ik naast elkaar op groei, marges en waardering: omzetgroei over de laatste twaalf maanden en over het laatste boekjaar, winstgroei per aandeel, brutomarge, operationele marge en nettomarge, vrije-kasstroommarge, rendement op eigen vermogen, schuld, en de waardering met P/E, PEG, koers-omzet en EV/EBITDA. Een kengetal zegt mij pas iets naast bedrijven met hetzelfde verdienmodel: een nettomarge van 8 procent is hoog voor een groothandel en laag voor een softwarebedrijf. Wat een industrie kenmerkt, staat in [Sectoren en industrieën](../05-Resources/Sectoren/README.md).
5. Van de bedrijven die eruit springen bekijk ik er een of meer op Seeking Alpha en op hun eigen investor-relationspagina: wat is de historische P/E ratio in de grafiek, wat het bedrijf zegt dat het doet, de laatste presentatie en wat anderen erover schrijven. Seeking Alpha lees ik als de mening van anderen en de investor-relationspagina als wat het bedrijf over zichzelf zegt. Geen van beide is al een controle van de cijfers. Weinig recente artikelen betekent weinig aandacht op één platform. Het zegt niet dat de markt het bedrijf verkeerd prijst, en ook niet hoeveel analisten het bedrijf volgen.
6. Wil ik meer weten, dan geef ik een AI-model de jaarverslagen, halfjaarberichten of presentaties van die bedrijven als pdf of link, met [prompt 1.2](../05-Resources/AI-Prompts/prompts-library.md#12-bedrijven-in-één-industrie-vergelijken). Dat levert per bedrijf een snelle eerste analyse met de bear case eerst, een vergelijking en een volgorde. De cijfers die die volgorde dragen, zoek ik daarna zelf op in het jaarverslag.
7. Ik zet de top 50 op het tabblad Kandidaten, op volgorde van belofte. In de kolom Data typ ik de ticker en zet ik de cel om naar het gegevenstype Aandelen, zodat valuta, marktkapitalisatie, de plek van de koers in de range van 52 weken en de P/E vanzelf meekomen. Zelf schrijf ik het businessmodel, de reden om verder te kijken, wat er mis kan gaan en het omzetmodel, telkens in een paar woorden of één zin. Lukt de reden niet in één zin, dan hoort de naam er niet op.
8. Daarna pak ik de bovenste naam voor de [snelle analyse](02-Snel-Analyseren.md). Valt die af, dan pak ik de volgende. Mijn eigen nieuwsgierigheid mag de volgorde veranderen. Een naam die afvalt, krijgt zijn reden in het universumbestand.

De lijst is een vertrekpunt en geen advies. Een naam die erop staat, is niet daarom een koopkans.

## De screener in TradingView

De acht universums en drie landenlijsten staan op [de screenerpagina](../05-Resources/Screeners/screeners.md), met de filters en de kolommen. Universum A, snelle groeiers, is de kern van die set. D, E en F gebruiken dezelfde industrieën als A en zoeken wat A op winst, land of omvang buiten laat: D omzetgroei zonder winst, E Amerikaanse smallcaps en F midcaps. B, C, G en H zijn de vangnetten voor de industrieën die niet in A horen: B voor cyclische bedrijven die vooral een grondstofprijs of de economische cyclus volgen, C voor gereguleerde bedrijven die afhangen van overheid of toezichthouder, G voor life sciences en H voor financials en vastgoed. Alleen E kijkt naar de Verenigde Staten. Een van de drie landenlijsten, Nederland, Hongkong of de Verenigde Staten, open ik alleen als ik uit interesse een markt wil doorlopen. Ik hoef niet alle acht universums te draaien; ik pak er een erbij als ik daar een reden voor heb.

Ik open de opgeslagen screener in TradingView, sorteer de uitkomst op de kolom Industry en vergelijk per industrie de parameters uit de kolommen, zoals in punt 4 hierboven. Verander ik een filter, dan pas ik de screenerpagina aan en zet ik de reden erbij.

## Prompts

[Prompt 1.1, top 50 maken](../05-Resources/AI-Prompts/prompts-library.md#11-top-50-maken), voor de eerste ordening van een lange lijst. [Prompt 1.2, bedrijven in één industrie vergelijken](../05-Resources/AI-Prompts/prompts-library.md#12-bedrijven-in-één-industrie-vergelijken), als ik de jaarverslagen van bedrijven uit dezelfde industrie wil laten vergelijken. Bij een bedrijf dat ik niet kan plaatsen, gebruik ik [prompt 2.0, datasnapshot](../05-Resources/AI-Prompts/prompts-library.md#20-datasnapshot-check-1) om in tien minuten te weten wat het doet en of het in mijn onderzoek past.

## Checks

Check 1, praktische uitvoerbaarheid, volledig. Check 2, hoe groot het bedrijf kan worden, en check 3, of ik het verdienmodel begrijp, alleen als eerste indruk. De rest hoort bij stap 2.

## Wat ik vastleg

Op het tabblad Kandidaten: per naam de kolommen hierboven. Bovenaan mijn notities van de ronde: de datum van de lijsten en de screeners die ik heb gebruikt. Meer administratie houd ik tijdens het screenen niet bij, want die helpt mij niet kiezen. In het [universumbestand](05-Universum-Bijhouden.md): elke naam die aan de snelle analyse begint als nieuwe rij met fase Kandidaat en de datum.

## Wanneer de stap af is

De [Definition of Done](Bijlagen/03-Definition-of-Done.md) voor screening: de top 50 staat op volgorde op Kandidaten, en op het tabblad Ronde staan geen kandidaten meer zonder reden, risico, omzetmodel of DeGiro-code.

## Hoe lang het duurt

Een ronde moet doorgaans in een middag kunnen, omdat de tijd naar de analyses hoort te gaan. Zit ik langer in de lijst dan in de eerste snelle analyse, dan ben ik namen aan het verzamelen in plaats van aan het kiezen. Dan stop ik, noteer ik welke naam mij meetrok, en zet ik die bovenaan voor stap 2.

De content op Belegger Kees is uitsluitend bedoeld voor educatieve doeleinden en vormt geen persoonlijk beleggingsadvies. Beleggen brengt risico's met zich mee. De waarde van beleggingen kan fluctueren en je kunt je inleg verliezen. Resultaten uit het verleden bieden geen garantie voor de toekomst. Raadpleeg een erkende financieel adviseur voor advies op maat. Belegger Kees is geen geregistreerde beleggingsonderneming bij de AFM.

## Verder lezen

[Analyseproces](README.md) · [Stap 2: Snel analyseren](02-Snel-Analyseren.md) · [Screeners](../05-Resources/Screeners/screeners.md) · [Hoofdstuk 3: Aandelen screenen](../02-Manifesto/03-Screening-Systeem.md)

---

Bijgewerkt: 2 november 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
