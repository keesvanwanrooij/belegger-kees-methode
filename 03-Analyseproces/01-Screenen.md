# Stap 1. Screenen

Screenen brengt duizenden beursbedrijven terug tot vijf tot tien namen die een snelle analyse waard zijn. Ik doe het per kwartaal als doel en minimaal één keer per jaar. Liggen er nog kansrijke kandidaten van een vorige ronde, dan werk ik die eerst af.

## Doel

Een lijst van vijf tot tien kandidaten, elk met bedrijf, ticker, beurs, universum, bron en één zin waarom ik verder wil kijken. Een ronde zonder geschikte kandidaten is ook een uitkomst.

## Wat ik klaarzet

De [voorbereiding](00-Voorbereiden.md), een map `Work-in-Progress/Screening-JJJJ-MM/`, een kopie van het screeningtemplate, TradingView met de opgeslagen screeners, Seeking Alpha en de investor-relationspagina's van de bedrijven die ik wil bekijken, een AI-model waarin ik jaarverslagen kan plakken, en DeGiro om handelbaarheid te controleren.

## Template en tabblad

`02-Screening.xlsx`. Op het tabblad Ronde noteer ik de datum, de universums die ik gebruik, de filterwaarden per universum, het aantal ruwe namen en de conclusie. Op het tabblad Vergelijking zet ik bedrijven uit één industrie onder elkaar met de kengetallen uit de screener, zodat ik ze naast elkaar kan leggen. Op het tabblad Kandidaten komt één rij per naam die de eerste blik overleeft. Het tabblad Universums is naslag: de zeven universums en drie landenlijsten met hun instellingen, zoals in [de screeners](../05-Resources/Screeners/screeners.md).

## Hoe ik de ronde doe

1. Ik begin met universum A, snelle groeiers. Dat is mijn hoofdroute. De andere zes zijn vangnetten voor bedrijven die A bewust buiten laat, en die pak ik erbij als ik daar een reden voor heb: B voor cyclische bedrijven die vooral een grondstofprijs of de economische cyclus volgen, C voor gereguleerde bedrijven die afhangen van overheid of toezichthouder, D voor omzetgroei zonder winst, E voor Amerikaanse smallcaps, F voor midcaps buiten de Verenigde Staten en G voor life sciences. Twee of drie universums per kwartaal is genoeg; ik hoef niet alle zeven elke keer te draaien. Een van de drie landenlijsten, Nederland, Hongkong of de Verenigde Staten, open ik alleen als ik uit interesse een markt wil doorlopen; dat is geen vaste stap.
2. Ik zet de filters uit de screenerpagina in de kop van TradingView en de kolommen in de tabel. Ik noteer de filterwaarden op het tabblad Ronde, ook als ik ze niet heb veranderd, want over een half jaar weet ik niet meer wat ik had ingesteld.
3. Ik sorteer de uitkomst op de kolom Industry. Dan staan vergelijkbare bedrijven onder elkaar en zie ik per industrie wie harder groeit, wie een hogere marge haalt en wie lager gewaardeerd is. Een kengetal zegt mij pas iets naast bedrijven met hetzelfde verdienmodel: een nettomarge van 8 procent is hoog voor een groothandel en laag voor een softwarebedrijf. Wat een industrie kenmerkt, staat in [Sectoren en industrieën](../05-Resources/Sectoren/README.md). Een bedrijf dat ik niet in twee zinnen kan omschrijven, krijgt een vraagteken en geen plek.
4. Per industrie vergelijk ik de parameters uit de kolommen: omzetgroei over de laatste twaalf maanden en over het laatste boekjaar, winstgroei per aandeel, brutomarge, operationele marge en nettomarge, vrije-kasstroommarge, rendement op eigen vermogen, schuld, en de waardering met P/E, PEG, koers-omzet en EV/EBITDA. De bedrijven die eruit springen, of die ik niet kan verklaren, zet ik op het tabblad Vergelijking.
5. Van die bedrijven bekijk ik er een of meer op Seeking Alpha en op hun eigen investor-relationspagina: wat het bedrijf zegt dat het doet, de laatste presentatie en wat anderen erover schrijven. Seeking Alpha lees ik als de mening van anderen en de investor-relationspagina als wat het bedrijf over zichzelf zegt. Geen van beide is al een controle van de cijfers.
6. Wil ik meer weten, dan plak ik de laatste jaarverslagen van twee tot vijf bedrijven uit dezelfde industrie in een AI-model en laat ik ze vergelijken met [prompt 13](../05-Resources/AI-Prompts/prompts-library.md#13-bedrijven-in-één-industrie-vergelijken). De cijfers die mijn keuze dragen, zoek ik daarna zelf op in het jaarverslag.
7. Per naam die overblijft doe ik direct check 1 uit de [No Go checks](Bijlagen/02-NoGo-Checks.md): is het aandeel bij DeGiro te koop, wat is de lotgrootte, hoe groot is de spread, wat zijn de kosten. Een naam die ik niet praktisch kan kopen, gaat eraf voordat ik er tijd in steek.
8. Ik schrijf per kandidaat de reden om verder te kijken in één zin. Lukt dat niet, dan hoort de naam er niet op.
9. Ik noteer het aantal analisten dat het aandeel volgt, met bron en peildatum. Dat is context voor later en geen filter.
10. Ik kies per kandidaat de volgende stap: snelle analyse, later terugkomen of stoppen. Bij meer dan tien namen voor de snelle analyse kies ik de vijf waar ik het minst van begrijp en het meest nieuwsgierig naar ben; de rest krijgt later terugkomen met een datum.

## Prompts

[Prompt 13, bedrijven in één industrie vergelijken](../05-Resources/AI-Prompts/prompts-library.md#13-bedrijven-in-één-industrie-vergelijken), als ik de jaarverslagen van bedrijven uit dezelfde industrie wil laten vergelijken. Bij een bedrijf dat ik niet kan plaatsen, gebruik ik [prompt 1, business snapshot](../05-Resources/AI-Prompts/prompts-library.md#1-business-snapshot) om in tien minuten te weten wat het doet en of het in het universum thuishoort.

## Checks

Check 1, praktische uitvoerbaarheid, volledig. Check 2, hoe groot het bedrijf kan worden, en check 3, of ik het verdienmodel begrijp, alleen als eerste indruk. De rest hoort bij stap 2.

## Wat ik vastleg

Op het tabblad Ronde: datum, universums, filters, aantal ruw, aantal kandidaten, conclusie, en wat ik volgende ronde bewust anders doe. Op het tabblad Vergelijking: per industrie de bedrijven die ik naast elkaar heb gelegd, de bronnen die ik heb bekeken en wat opviel. Op het tabblad Kandidaten: alle velden per naam. In het [universumbestand](05-Universum-Bijhouden.md): elke kandidaat als nieuwe rij met fase Kandidaat en de datum.

## Wanneer de stap af is

De [Definition of Done](Bijlagen/03-Definition-of-Done.md) voor screening: vijf tot tien kandidaten met bedrijf, ticker, beurs, datum, bron en reden, de filters vastgelegd, en de conclusie ingevuld. Ik pas geen filter aan alleen om de lijst alsnog te vullen.

## Hoe lang het duurt

Een middag voor de filters, het sorteren en de vergelijking per industrie. Een vergelijking van jaarverslagen met AI doe ik alleen voor de industrie waar ik het meest nieuwsgierig naar ben. Duurt het langer, dan ben ik namen aan het onderzoeken in plaats van aan het screenen. Dan stop ik, noteer ik welke naam mij meetrok, en zet ik die bovenaan voor stap 2.

## Verder lezen

[Analyseproces](README.md) · [Stap 2: Snel analyseren](02-Snel-Analyseren.md) · [Screeners](../05-Resources/Screeners/screeners.md) · [Hoofdstuk 3: Aandelen screenen](../02-Manifesto/03-Screening-Systeem.md)

---

Bijgewerkt: 13 september 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
