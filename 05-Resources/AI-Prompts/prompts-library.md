# Promptbibliotheek van de Belegger Kees Methode

Dit zijn de prompts waarmee ik AI inzet in mijn aandelenonderzoek, in de volgorde van mijn [analyseproces](../../03-Analyseproces/README.md). Mijn onderzoek dient één vraag: koop ik dit aandeel, en tegen welke prijs?

## Zo schrijf ik een prompt

Twee regels zijn belangrijker dan de rest.

1. **Korter is beter, zonder informatie te verliezen.** AI schrijft graag lange prompts die alles vastleggen, maar daarin raakt de hoofdzaak zoek. Ik schrap tot alleen de taak, de invoer en de gewenste uitkomst overblijven.
2. **Ik zeg wat er wel moet gebeuren.** Een verbod werkt slecht, want iets niet doen is geen handeling. "Verzin geen cijfers" doet minder dan "Schrijf Niet gevonden met de beste vindplaats erbij".

Verder krijgt elke prompt één taak en vaste koppen in de uitkomst, zodat de volgende stap weet waar alles staat. Elk antwoord eindigt met een lege kop voor mijn correcties, want wat ik zelf in de bron zag gaat voor op wat een model schreef.

## Zo gebruik ik ze

1. Ik zet de vaste regels hieronder als projectinstructie in het gesprek, of plak ze bovenaan.
2. Ik kopieer de prompt, vul de vierkante haken in en geef de genoemde bestanden mee.
3. Ik bewaar het antwoord in de map van het bedrijf in mijn werkmap en corrigeer het onder "Correcties van Kees".
4. Corrigeer ik drie keer hetzelfde, dan verander ik de prompt.

Ik gebruik één model per taak en controleer daarna zelf. Drie modellen naast elkaar leverden mij vooral meer tekst en meer fouten om te corrigeren op. De zes cijfers die mijn waardering dragen controleer ik altijd bij de bron: omzet, winst, vrije kasstroom, koers, aantal aandelen en nettoschuld. Wat AI voor mij doet staat in [hoofdstuk 10](../../02-Manifesto/10-AI-Werkwijze.md). Het oordeel is van mij.

## De vaste regels, als projectinstructie

```text
Je bent de onderzoeksassistent van Kees van Wanrooij (Belegger Kees). Mijn onderzoek dient één vraag: koop ik dit aandeel, en tegen welke prijs? De methode is groei tegen een redelijke prijs in de stijl van Peter Lynch, DCF-waardering en NLP als bron van onderzoeksvragen. Deel het bedrijf in (snelle groeier, stalwart, turnaround, cyclisch, langzame groeier), schrijf de omzet als een paar parameters, zoek operationele hefboom en beoordeel wat de prijs vraagt. Ik zoek de beste combinatie van kwaliteit en prijs: bedrijven met minder risico dan de markt denkt.

Snelle analyse: aangepaste FCF = operationele kasstroom - investeringen - aandelenbeloning - rente-inkomsten na belasting + rente-uitgaven na belasting, bij een normale belastingdruk. Onder IFRS 16 gaan ook de leasebetalingen eraf. Omgekeerde DCF: tien jaar FCF-groei plus 2 tot 3 procent eeuwige groei, bij een discount rate van 10 procent (8 tot 12 als het risico dat onderbouwt), geeft de ondernemingswaarde = koers x verwaterde aandelen van het laatste kwartaal - netto cash. Aandelenbeloning eraf betekent een vlak aantal aandelen. Daarna bear, base en bull met een gewogen gemiddelde waarde (25/50/25).

Uitgebreide analyse: het winstmodel. Omzet x nettowinstmarge x kasstroomconversie, verandering van het aantal aandelen, exit P/E op de winst van jaar 11, intern rendement, drie scenario's en Gordon Growth als controle.

Werkwijze:
1. Onderzoek eerst wat fout kan gaan en zoek bewijs tegen mijn idee met dezelfde zorg als bewijs ervoor.
2. Geef elk cijfer met bron, periode, valuta en IFRS, GAAP of aangepast. Zet [berekend] met de invoer bij een eigen berekening.
3. Houd feiten, berekeningen, aannames en interpretaties herkenbaar uit elkaar.
4. Schrijf Niet gevonden met de beste vindplaats bij wat ontbreekt, [te controleren] bij wat je niet kon bevestigen en [Kees vult in] bij wat alleen ik weet.
5. Zoek op het web waar dat helpt en noem elke bron met datum.
6. Lever één Markdown-bestand in begrijpelijk Nederlands, kort en precies, met de koppen uit de prompt, en eindig met de lege kop "## Correcties van Kees".
7. Lever onderzoek: feiten, berekeningen, open vragen en de waarde bij deze aannames met rekendatum. De beslissing is van mij.
```

## Overzicht

| Prompt | Stap | Wat ik ermee vul |
| --- | --- | --- |
| [1.1 Top 50 maken](#11-top-50-maken) | [Stap 1](../../03-Analyseproces/01-Screenen.md) | Tabblad Kandidaten van het screeningwerkboek |
| [1.2 Bedrijven in één industrie vergelijken](#12-bedrijven-in-één-industrie-vergelijken) | Stap 1 | De volgorde op Kandidaten, en de kolommen Business model, Reden om verder te kijken, Wat kan er mis gaan? en Omzet model |
| [2.0 Datasnapshot](#20-datasnapshot-check-1) | [Stap 2](../../03-Analyseproces/02-Snel-Analyseren.md), fase 0 | Bedrijfsinfo |
| [2.1 Business snap](#21-business-snap-checks-3-6-7-en-8) | Stap 2, fase 1 | Bedrijf |
| [2.2 Markt en groeiruimte](#22-markt-en-groeiruimte-checks-2-en-4) | Stap 2, fase 2 | Markt |
| [2.3 Waardering en omgekeerde DCF](#23-waardering-en-omgekeerde-dcf-checks-5-en-10) | Stap 2, fase 3 | Waardering |
| [2.4 Prijs en kwaliteit](#24-prijs-en-kwaliteit-check-9-vragen-11-tot-en-met-14) | Stap 2, fase 4 | Prijs en kwaliteit |
| [2.5 Management](#25-management-vragen-15-en-16) | Stap 2, fase 5 | Management |
| [2.6 Pre-mortem](#26-pre-mortem) | Stap 2, afsluiting | Pre-mortem |
| [2.7 Checks en keuze](#27-checks-en-keuze) | Stap 2, afsluiting | Checks en Overzicht |
| [2.8 Kandidaten vergelijken](#28-kandidaten-vergelijken) | Stap 2, meerdere kandidaten | Voorkeursvolgorde op Overzicht |
| [3.1 Dekking en analistengat](#31-dekking-en-analistengat) | [Stap 3](../../03-Analyseproces/03-Uitgebreid-Analyseren.md), hulpmiddel, ook bij stap 2 | Tabblad Analisten en mijn onderzoeksvragen |
| [3.2 Onderzoeksvragen](#32-onderzoeksvragen) | Stap 3, hulpmiddel | De volgorde van mijn onderzoek |
| [3.3 Businessmodel en parameters](#33-businessmodel-en-parameters) | Stap 3, fase 2 | Parameters |
| [3.4 Markt en concurrenten](#34-markt-en-concurrenten) | Stap 3, fase 3 | Dossier markt en concurrentie |
| [3.5 Analisten: online onderzoek](#35-analisten-online-onderzoek) | Stap 3, fase 3 | Analisten, delen B en C |
| [3.6 Analisten: NLP-analyse van één analist](#36-analisten-nlp-analyse-van-één-analist) | Stap 3, fase 3 en 7 | Analisten, deel C |
| [3.7 Bestuur en kapitaalallocatie](#37-bestuur-en-kapitaalallocatie) | Stap 3, fase 7 | Analisten, deel D, en het dossier |
| [4.1 De hefboom vinden](#41-de-hefboom-vinden) | [Stap 4](../../03-Analyseproces/04-Waarderen.md), begin | De aanname waar mijn onderzoek naartoe gaat |
| [4.2 Exit P/E en ingeprijsde groei](#42-exit-pe-en-ingeprijsde-groei) | Stap 4 | Invoer en Parameters |
| [4.3 Model controleren](#43-model-controleren) | Stap 4 | Controles en de onderbouwing van discount rate en exit P/E |
| [5.1 Nieuws](#51-nieuws) | [Stap 5](../../03-Analyseproces/05-Universum-Bijhouden.md) en [stap 6](../../03-Analyseproces/06-Kopen-Aanhouden-Verkopen.md) | Universum en de signalen per positie |
| [7.1 Rapport voorbereiden](#71-rapport-voorbereiden) | [Stap 7](../../03-Analyseproces/07-Rapporteren-Publiceren.md) | De outline van het rapport |
| [7.2 Tweede lezer](#72-tweede-lezer) | Stap 7 | Mijn correctielijst voor publicatie |

Bij nieuwe kwartaalcijfers gebruik ik 2.0 opnieuw, en bij een signaal dat afgaat ook 2.6.

## Stap 1. Screenen

### 1.1 Top 50 maken

**Meegeven:** de lijst uit mijn bron, als bestand.

```text
Maak van de bijgevoegde lijst [bron: undercovered-lijst van Seeking Alpha, of TradingView-universum] mijn top 50: de bedrijven die het meest beloven voor mijn volgende onderzoek. Ik zoek structurele groei tegen een redelijke prijs, een bedrijf dat ik in parameters kan uitschrijven, en een risico dat lager lijkt dan de markt denkt. Zoek per bedrijf de laatste cijfers en het laatste nieuws.

Uitkomst, begin met "# Top 50, [datum]":
- "## De top 50": op volgorde van belofte, één rij per bedrijf met ticker, land, sector, industrie, businessmodel in een paar woorden, reden om verder te kijken, wat er mis kan gaan, omzetmodel in parameters en de volgende cijferdatum.
- "## Net afgevallen": opvallende namen buiten de top 50, met de reden in één regel.
- "## Eerst bekijken": de drie namen die de snelle analyse als eerste verdienen, en waarom.
```

**Zelf doen:** handelbaarheid bij DeGiro controleren. Mijn eigen nieuwsgierigheid telt; wijkt die af, dan volg ik haar.

### 1.2 Bedrijven in één industrie vergelijken

**Meegeven:** jaarverslagen, halfjaarberichten of presentaties als pdf of link.

```text
Vergelijk deze [aantal] bedrijven uit de industrie [industrie], gevonden via [bron], en zet ze op volgorde voor mijn snelle analyse. Kies één bedrijf dat als eerste aan de beurt komt.

Ik zoek de beste prijs-kwaliteitverhouding: hoeveel structurele groei en winst krijg ik voor de prijs, hoe zeker is die groei en welk risico hoort erbij. Het liefst een hoge potentie met minder neerwaarts risico dan het lijkt, of een risico dat al te zwaar is ingeprijsd. Weinig analisten is een pluspunt. Mijn groeidrempel is 12 procent omzetgroei per jaar; 15 is sterk en 20 uitzonderlijk. Toets die aan het plafond van de omzetparameters (klanten x ARPU, winkels x omzet per winkel) en aan een realistisch marktaandeel. Lagere groei kan winnen op kwaliteit, voorspelbaarheid, waardering en risico. Toets ook streng de 10-bagger van Peter Lynch: 10x de marktkapitalisatie.

Lees eerst wat ik aanlever, vul aan met actuele openbare informatie, en noem wat je niet kon openen.

[bedrijf], [ticker], [beurs], [link IR], [link pdf], voor alle bedrijven.

Uitkomst, begin met "# Vergelijking [industrie]":
- "## Conclusie": het beste bedrijf voor de eerste plek en de belangrijkste kanttekening.
- "## Per bedrijf": eerst de bear case, met het deel van de recente groei dat uit prijs, cyclus of eenmalige factoren komt. Dan het verdienmodel in hoogstens vijf zinnen, de omzetparameters en hun plafond, groei in volume en prijs apart, operationele hefboom, balans en kasstroom, P/E met rekenstap, wat de koers inprijst en het aantal analisten. Sluit af met het ene kerncijfer om te volgen en de waarde waarbij je oordeel omslaat.
- "## Naast elkaar": één tabel met structurele volumegroei, huidige winstgroei, financieel risico, operationele hefboom, groeiruimte uit uitbreiding of overnames, analistendekking, waardering, kans op 12 procent structurele omzetgroei en realistisch veelvoud (2x, 3x, 5x, 8x). Daarna één alinea: welk verschil geeft de doorslag?
- "## Keuze en volgorde": waarom dit bedrijf, ook tegenover het bedrijf dat op de cijfers sterker lijkt. De 10-bagger doorgerekend: wat moeten omzet, marge, aantal aandelen en multiple doen? Komt geen bedrijf er geloofwaardig, zeg dan wie het dichtst bij komt. Alle bedrijven op volgorde met één zin per bedrijf, en elke nabije cijferdatum die de keuze kan veranderen.
- "## Eerste vragen": drie onderzoeksvragen voor de snelle analyse van het gekozen bedrijf.
```

## Stap 2. Snel analyseren

Ik zoek de snelste reden om te stoppen. De prompts 2.0 tot en met 2.7 draai ik op volgorde in één gesprek. Een fase met een duidelijke belemmering bij een directe check stuurt mij meteen naar 2.7.

### 2.0 Datasnapshot (check 1)

**Meegeven:** het laatste jaarverslag, het laatste kwartaal- of halfjaarbericht.

```text
Snelle analyse van [bedrijf] ([ticker]), fase 0: alleen gegevens, met bron en datum. Gebruik wat ik meegeef en de investor-relationspagina.

Onder "## Fase 0: datasnapshot":
- Identiteit: beurs, land, valuta, IFRS of US GAAP, boekjaar, laatste verslagperiode, Lynch-categorie met één regel waarom, en bijzondere boekhoudregels (geactiveerde ontwikkelkosten, eigen kasstroomdefinities, grote leases, aangepaste winstmaatstaven).
- Kapitaal: koers met datum, uitstaande aandelen van de voorpagina van het laatste verslag, verwaterd gewogen aantal van het laatste kwartaal, marktkapitalisatie, cash, schuld zonder leases, leases apart, netto cash, ondernemingswaarde.
- Laatste twaalf maanden naast een jaar eerder: omzet en groei, bruto-, operationele en nettomarge, winst per aandeel volgens de standaard en aangepast, aandelenbeloning als percentage van de omzet.
- Van operationele winst naar nettowinst: benoem rente-inkomsten, eenmalige belastingposten, schikkingen en reorganisaties.
- Kasstroom: operationele kasstroom min investeringen; aandelenbeloning; betaalde belasting naast de belastinglast.
- Dataleverancier naast het verslag: omzet, operationele winst, nettowinst, vrije kasstroom en verwaterde aandelen van het laatste boekjaar. Elk verschil met bron.
- Bestuur en markt: bestuursvoorzitter en financieel directeur sinds wanneer, het belangrijkste nieuws van twaalf maanden, en wat kopers en verkopers nu als argument gebruiken.
```

**Zelf doen:** de zes cijfers in het verslag controleren, met de periode erbij. Een cijfer uit een transcript controleer ik in het persbericht.

### 2.1 Business snap (checks 3, 6, 7 en 8)

```text
Fase 1: hoe verdient het bedrijf geld, en kan ik de cijfers vertrouwen? Onder "## Fase 1: business snap":
- Check 3: het verdienmodel in hoogstens vijf zinnen voor iemand zonder beleggingskennis: wie betaalt waarvoor, waarom komt die terug, waarom is dat winstgevend. Omzet per product, segment, regio en klant; de grootste klant.
- Check 6: kan het bedrijf twee slechte jaren financieren zonder verwatering of nieuwe schuld? Schuld, looptijden, rente, convenanten.
- Check 7: winst en kasconversie over drie jaar; bij verlies het pad naar winst, met economie per klant, benodigde schaal en mijlpalen.
- Check 8: sluiten winst, kasstroom en balans aan? Dagen debiteuren, crediteuren en voorraad over vijf jaar, herzieningen, opmerkingen van de accountant, aangepaste maatstaven zonder terugkerende kosten, verwatering. Markeer elk rood punt.
- De twee of drie maatstaven waarop dit bedrijf wordt beoordeeld, per kwartaal over acht kwartalen, en waarom die.
Per check: geen belemmering, belemmering, onbekend of niet van toepassing, met bron.
```

### 2.2 Markt en groeiruimte (checks 2 en 4)

```text
Fase 2: hoe groot kan het bedrijf worden, en wat levert groei de aandeelhouder op? Onder "## Fase 2: markt en groeiruimte":
- De omzet als twee of drie parameters met drie tot vijf jaar waarden, gecontroleerd tegen de gerapporteerde omzet. Per parameter: recente groei, het plafond en waarom daar.
- De marktomvang volgens het bedrijf naast een onafhankelijke schatting.
- Check 2: kan de omzet in tien jaar drie tot vijf keer zo groot worden (11,6 tot 17,5 procent per jaar) met realistische aannames? Was de groei structureel, cyclisch of gekocht? Bij een cyclisch bedrijf: de laatste neergang en de plek in de cyclus nu.
- Concurrenten, wie marktaandeel wint en hoe houdbaar het voordeel over vijf jaar is, ook als AI het product of de kosten verandert.
- Check 4: operationele marge terwijl de omzet groeide, vaste tegenover variabele kosten, groei per aandeel na verwatering.
```

### 2.3 Waardering en omgekeerde DCF (checks 5 en 10)

```text
Fase 3: waardering en een korte omgekeerde DCF. Toon elke stap, zodat ik hem in Excel kan nabouwen. Onder "## Fase 3: waardering":
- Check 5: P/E op de gerapporteerde winst, op de winst zonder eenmalige posten en rente-inkomsten, en op de aangepaste winst, over twaalf maanden en vooruit. PEG = vooruitkijkende P/E / verwachte winstgroei als getal, met de reden als die weinig zegt. EV/EBITDA en FCF-rendement. Elk naast de eigen range van vijf jaar en drie tot vijf sectorgenoten op dezelfde boekhoudbasis.
- Aangepaste FCF over het laatste boekjaar en de laatste twaalf maanden, met elke correctie apart genoemd.
- Check 10: welke jaarlijkse groei van de aangepaste FCF over tien jaar, gevolgd door 2,5 procent eeuwige groei, verdisconteert bij 10 procent naar de ondernemingswaarde van vandaag? Reken vanaf beide FCF-cijfers. Een raster van de ingeprijsde groei bij discount rates van 9, 10 en 11 procent en eeuwige groei van 2, 2,5 en 3 procent.
- Controle: de EV/FCF die uit de eindwaarde volgt, naast de sectornorm.
- De ingeprijsde groei naast de omzet- en FCF-groei van de laatste vijf jaar en de consensus.
- Bear, base en bull onder "## Scenario's: bear, base en bull": dezelfde rekensom (10 procent, 2,5 procent eeuwig), met per scenario de start-FCF, de groei en de onderbouwing. Bear = het slechtste jaar uit de geschiedenis op de huidige kostenbasis of een benoemde klap; base = mijn onderbouwde verwachting, gemarkeerd als [aanname]; bull = de doelen van het bedrijf worden gehaald. Tel de netto cash één keer op en deel door de verwaterde aandelen.
- Het gewogen gemiddelde: 25 procent bear, 50 procent base, 25 procent bull, en het verschil met de koers. Bij een negatieve of heel kleine FCF: geen waarde, wel de reden.
Sluit af met de waarden bij deze aannames en de rekendatum; het is een modelwaarde, geen koersdoel.
```

**Zelf doen:** de omgekeerde DCF nabouwen op het tabblad Waardering, en mijn eerste eigen verwachting ernaast zetten.

### 2.4 Prijs en kwaliteit (check 9, vragen 11 tot en met 14)

```text
Fase 4, onder "## Fase 4: prijs en kwaliteit":
- Check 9: de bear case die de markt al heeft (artikelen, analisten, shortrapporten). Per punt: ingeprijsd, open, of waar ik het anders kan zien.
- Vraag 11: wie volgt het bedrijf en wat suggereert dat?
- Vraag 12: waar kan mijn eigen inzicht iets toevoegen? [Kees vult in], plus wat mijn onderzoeksvragen raken.
- Vraag 13: prijszettingsmacht: prijs, volume, mix en marges.
- Vraag 14: hoe herhaalbaar is de omzet: contracten, verlenging, klantverlies, concentratie.
- Twee losse scores van 1 tot 10, elk met de twee of drie feiten erachter. Kwaliteit: concurrentievoordeel, groeiruimte, financiële gezondheid, bestuur. Prijs: waardering tegenover eigen historie en sectorgenoten, 10 is heel laag geprijsd.
```

### 2.5 Management (vragen 15 en 16)

```text
Fase 5: beoordeel het bestuur op wat het deed. Onder "## Fase 5: management":
- Bestuursvoorzitter en financieel directeur: sinds wanneer, achtergrond.
- Beloftes van drie tot vijf jaar geleden naast wat er kwam, elk met bron en datum. Een belofte die niet meer terugkomt is een bevinding.
- Vraag 15: kapitaalallocatie over vijf jaar: inkoop en tegen welke koersen, overnames en hun resultaat, verwatering, beloning en waaraan de bonus hangt. Eigen belang en insidertransacties van twaalf maanden.
- Vraag 16: taal in de laatste twee calls: verdwenen maatstaven, verschoven termijnen, onbeantwoorde vragen. Observaties met citaat en vindplaats, elk met de vraag die ze oproepen.
```

### 2.6 Pre-mortem

```text
Pre-mortem: het is drie jaar later en deze belegging is duidelijk tegengevallen. Vertel het meest waarschijnlijke verhaal, concreet en nuchter: wat gebeurde er, wanneer werd het zichtbaar, wat deed het met omzet, marge of kasstroom, en hoe reageerde de markt? Welke aanname brak als eerste? Geef daarna drie tot vijf vroege signalen, elk met een drempel en het bericht of de call waar het zichtbaar wordt. Het verhaal is verzonnen om mijn redenering te testen: zet dat erboven. Onder "## Pre-mortem".
```

**Zelf doen:** alleen de signalen en drempels gaan mijn dossier in.

### 2.7 Checks en keuze

```text
Sluit de snelle analyse af.
- "## Checks": de tien checks en zes vragen, één regel per stuk: uitkomst (geen belemmering, belemmering, onbekend, niet van toepassing), waarom, bron, gevolg.
- "## Keuze": verder onderzoeken, later terugkomen of stoppen, in hoogstens tien regels. Bij verder onderzoeken: de belangrijkste open vraag. Bij later terugkomen: de open vraag en de datum. Bij stoppen: welke check.
- "## Correcties op de data": veld, waarde, bron.
```

### 2.8 Kandidaten vergelijken

```text
Zet deze kandidaten op volgorde voor mijn volgende twintig onderzoeksuren: [namen en tickers, hoogstens tien], met per bedrijf mijn notitie [wat ik weet en welke zorg ik heb]. Gebruik per bedrijf de twee losse scores van 1 tot 10 voor kwaliteit en prijs, met P/E, koers-omzet, PEG en EV/EBITDA tegenover eigen historie en sectorgenoten. Ik zoek twee hoge scores: een goed bedrijf kan duur zijn en een zwak bedrijf goedkoop.

Uitkomst, begin met "# Volgorde kandidaten, [datum]":
- "## Per bedrijf": beide scores, elk met de twee of drie feiten en de bron.
- "## Volgorde": van meest naar minst aantrekkelijk, per bedrijf één zin waarom daar en welke vraag die plek het sterkst kan veranderen.
- "## Volgende twintig uur": de twee bedrijven die ze het meest waard lijken, en wat ik nodig heb om zelf te kiezen.
```

## Stap 3. Uitgebreid analyseren

Hier wil ik alles te weten komen. 3.1 en 3.2 zijn hulpmiddelen: ze laten zien waar de markt niet kijkt en richten mijn uren. Ik gebruik ze ook al bij stap 2 als een bedrijf veel dekking heeft.

### 3.1 Dekking en analistengat

**Meegeven:** geplakte artikelen, reacties en de vragenronde van de laatste calls; analistenconsensus; mijn notities.

```text
Breng de dekking van [bedrijf] ([ticker]) in kaart: wat gelooft de markt, welke aanname toetst niemand, en welke belangrijke vraag beantwoordt niemand? Gebruik voor wat auteurs schreven alleen de geplakte teksten; open verslagen om een cijfer te controleren.

Uitkomst, begin met "# Dekking en analistengat: [bedrijf] ([ticker])":
- "## A. Per artikel", nieuwste eerst: these in één regel, cijfers, waardering, katalysatoren, risico's, wat het zonder toets aanneemt, wat het mist.
- "## B. De consensus onder auteurs": bull en bear, de verdeling van oordelen, gedeelde ongetoetste aannames, waar auteurs het oneens zijn.
- "## C. De consensus onder analisten": oordelen en trend, spreiding in koersdoelen, herzieningen, verrassingen, en wat de schattingen impliceren voor groei en marge.
- "## D. Het gat op de call": onderwerpen en door hoeveel analisten gevraagd; vage antwoorden waar een getal nodig was (citeer hoogstens twintig woorden); wat niemand vroeg dat een model nodig heeft; wat veranderde tussen twee calls.
- "## E. Lezers": scherpe punten uit de reacties die geen artikel beantwoordt.
- "## F. Wat veranderde" sinds de oudere artikelen, en welke argumenten verouderd zijn. Beantwoord hier de vragen uit mijn notities.
- "## G. De gaten, op volgorde": vijf tot zeven open vragen, elk met het belang voor de waarde, het bewijs dat ze open is en waar het antwoord kan staan.
- "## H. Samenvatting": hoogstens 150 woorden. Het belangrijkste gat in één regel, beginnend met "Niemand heeft gecontroleerd of".
- "## I. Wat ontbreekt in de invoer".
```

**Zelf doen:** eerst G lezen, dan D. Een vage quote controleer ik in het transcript. Een ontbrekende vraag bewijst niet dat niemand keek; analisten kunnen het elders hebben gehoord.

### 3.2 Onderzoeksvragen

```text
Maak van de gaten en mijn eigen vragen hoogstens drie onderzoeksvragen voor [bedrijf] ([ticker]). Een goede vraag heeft een einde, raakt de waarde en is te beantwoorden uit openbare bronnen.

Uitkomst, begin met "# Onderzoeksvragen: [bedrijf] ([ticker])":
- "## 1. Kandidaten": hoogstens zes, gescoord van 0 tot 2 op: raakt de waarde, open in de dekking, openbare bronnen, past in de tijd, mijn voorsprong.
- "## 2. De drie vragen", op volgorde: de vraag met maatstaf en periode, het belang voor de waarde met een ruwe [berekend], waar te zoeken, wat telt als antwoord, wat mijn idee tegenspreekt, een tijdsgrens.
- "## 3. Werkhypothese en tegendeel": beide toetsbaar, en de ene waarneming die ze scheidt.
- "## 4. Eerste checks": drie, zodat een belemmering vroeg zichtbaar wordt.
- "## 5. Poort": verandert een goed antwoord mijn beslissing om te kopen of niet?
```

### 3.3 Businessmodel en parameters

```text
Ik wil de omzet van [bedrijf] ([ticker]) schrijven als een klein aantal parameters die ik zelf kan volgen. Mijn eerste idee is [bijvoorbeeld clubs x leden per club x omzet per lid]; corrigeer dat waar nodig. Gebruik het laatste jaarverslag, de segmentinformatie, de laatste twee calls en de operationele cijfers van het bedrijf. Staan die er niet, gebruik dan externe bronnen en zeg hoe betrouwbaar ze zijn. Beschrijf het bedrijf in je eigen woorden, los van de marketingtaal.

Uitkomst, begin met "# Parameters: [bedrijf] ([ticker])":
- "## Verdienmodel": hoogstens vijf zinnen. Lukt dat niet, zeg het: dat is een signaal.
- "## Omzet en klanten": producten, segmenten en regio's in procenten, klantprofiel, terugkerend deel, grootste klant.
- "## Kosten": kostenstructuur, investeringen die bij groei horen, en of de marge meestijgt, over drie jaar.
- "## Parametermodel": twee of drie parameters met vijf tot tien jaar historie en bron, het plafond en waarom daar, een groeiverwachting per jaar voor tien jaar met aannames. Controleer het product tegen de omzet van het laatste jaar en verklaar het verschil.
- "## Karakter van de groei": structureel, cyclisch, tijdelijk of gekocht.
- "## Onderschat risico": het grootste fundamentele risico in drie zinnen.
Zet bij elk deel een betrouwbaarheidslabel met de reden.
```

### 3.4 Markt en concurrenten

```text
Hoeveel ruimte heeft [bedrijf] ([ticker]) nog: zit het rond 20, 50 of 80 procent van wat het in zijn markt kan halen? Boven de helft is de gemakkelijke groei eruit. Segmenten: [segmenten, of leeg]. Begin met het grootste en houd ze apart. Gebruik onafhankelijke bronnen; zet een marktcijfer van het bedrijf als bedrijfsclaim naast een onafhankelijke schatting. Tel overlappende segmenten één keer.

Uitkomst, begin met "# Markt: [bedrijf] ([ticker])":
- "## Per segment": marktomvang met bron en jaar, groei voor vijf jaar, marktaandeel, het deel van het haalbare marktaandeel dat bereikt is, en het omzetplafond (haalbaar aandeel x marktomvang) met aannames.
- "## Concurrenten": drie tot vijf met omzet, marktaandeel en sterkste voordeel; wie won en verloor in twee tot drie jaar.
- "## Voordeel": waarom klanten kiezen en hoe houdbaar dat is over vijf jaar, ook als AI het product of de kosten verandert.
- "## Bear case": minstens twee concrete mechanismen die het marktaandeel over vijf jaar verlagen.
- "## Keuze": de positie wordt sterker, gelijk of zwakker, in hoogstens vier zinnen.
```

### 3.5 Analisten: online onderzoek

```text
De analisten die [bedrijf] ([ticker]) volgen zijn mijn tegenspelers. Ik wil weten hoe sterk elk van hen is en waar ze samen niet kijken. Begin bij de pagina voor beleggers en zoek per analist publicaties, interviews en vragen in de calls. Laatste call: [datum]. Gebruik alleen openbare, beroepsmatige informatie. Een uitspraak over gestelde vragen baseer je op een transcript dat je hebt gelezen.

Uitkomst, begin met "# Analisten: [bedrijf] ([ticker])":
- "## Per analist": naam, huis, opleiding en loopbaan voor zover openbaar, gevolgde bedrijven en sectoren, hoe lang dit bedrijf, oordeel en koersdoel met datum, kernargument, en publicaties over dit bedrijf of de sector met link.
- "## De dekking als geheel": dominante onderwerpen, operationele parameters die niemand volgt, en wat de spreiding in koersdoelen zegt.
- "## Mijn toevoeging": de vraag waarmee mijn onderzoek iets toevoegt.
```

### 3.6 Analisten: NLP-analyse van één analist

```text
Lees de vragen van analist [naam] van [huis] in de calls van [bedrijf] ([ticker]): [vragen per call met datum]. Werk alleen met deze vragen. Kijk met het metamodel: waar zijn ze precies en waar vaag, welke onderwerpen komen terug of verdwijnen, welke maatstaven en termijnen noemt de analist, en vraagt de analist door als het bestuur ontwijkt? Beschrijf patronen in gewone taal; een taalobservatie is een aanleiding om in de cijfers te zoeken.

Uitkomst, begin met "# NLP-analyse: [naam]":
- "## Basislijn": onderwerpen, maatstaven en termijnen die steeds terugkomen.
- "## Verschuivingen": wat erbij kwam, verdween, scherper of algemener werd, met citaat en datum.
- "## Aannames en twijfel": wat de vragen zeggen over het model van de analist.
- "## Als tegenspeler": kent deze analist het bedrijf operationeel of vooral op de cijfers?
- "## Mijn vragen": twee onderzoeksvragen die deze analist niet stelt.
```

### 3.7 Bestuur en kapitaalallocatie

```text
Beoordeel het bestuur van [bedrijf] ([ticker]) op gedrag en resultaten over vijf jaar: zou ik dit bestuur mijn geld toevertrouwen als het morgen een nieuw bedrijf begon? Mijn gevonden beloftes: [beloftes, of leeg]. Geef elke uitspraak een bron; een oordeel zonder bron heet een indruk.

Uitkomst, begin met "# Bestuur: [bedrijf] ([ticker])":
- "## Per bestuurder": achtergrond, duur, wat de persoon eerder opbouwde of achterliet, en of dat past bij de fase van het bedrijf.
- "## Beloofd en gerealiseerd": per belofte bron en datum, uitkomst met bron, en waargemaakt, gedeeltelijk, niet waargemaakt of niet meer genoemd.
- "## Kapitaalallocatie": inkoop en tegen welke koers, overnames, prijs en resultaat, dividend en verwatering.
- "## Eigen belang": aandelenbezit, gekocht of gekregen, bonuscriteria, insidertransacties van twaalf maanden als patroon of losse gevallen, als aanleiding voor verder onderzoek.
- "## Taal over vier calls": verschuivingen van concreet naar algemeen, verdwenen onderwerpen, ontbrekende maatstaven, met citaat en vindplaats.
- "## Antwoord": op de vraag hierboven, met de twee feiten die het dragen.
```

## Stap 4. Waarderen

Ik bouw het model zelf; AI vindt de hefboom, onderbouwt de grenzen en controleert. De regels staan in [hoofdstuk 6](../../02-Manifesto/06-DCF-Model.md).

### 4.1 De hefboom vinden

```text
Welke aanname beweegt de waarde van [bedrijf] ([ticker]) het meest? Reken op een eenvoudige DCF van de aangepaste FCF de waarde per aandeel door bij omzetgroei, brutomarge, operationele kosten en aandelenbeloning, elk een paar punten omhoog en omlaag. Toon elke stap.

Uitkomst, begin met "# Hefboom: [bedrijf] ([ticker])":
- "## Gevoeligheid": per aanname het effect op de waarde per aandeel, van groot naar klein.
- "## Grenzen": per aanname de ruimte volgens de eigen historie, de richtlijnen van het bestuur en vijf tot tien sectorgenoten, uit hun verslagen.
- "## Hefboom": de aanname die de waarde draagt, en de onderzoeksvraag die daaruit volgt.
```

**Zelf doen:** de grenzen naast mijn parameters zetten voordat ik ze invul. Een parameter wijzigt alleen met een reden die binnen die grenzen past.

### 4.2 Exit P/E en ingeprijsde groei

```text
Waardering van [bedrijf] ([ticker]) met het winstmodel, koers [koers] op [datum]. Nettowinst laatste twaalf maanden [bedrag], verwaterde aandelen [aantal], kasstroomconversie [ratio], discount rate [percentage], exit P/E [getal]. Vraag naar ontbrekende invoer, hoogstens twee vragen, en wacht op mijn antwoord. Toon elke rekenstap en noem de variabelen die je vasthoudt: één koers geeft geen unieke groei.

Uitkomst, begin met "# Exit P/E: [bedrijf] ([ticker])":
- "## P/E": over twaalf maanden en vooruit, de eigen range over vijf tot tien jaar met laagste, gemiddelde en hoogste punt en waar de koers nu staat, en vier tot zes sectorgenoten op dezelfde boekhoudbasis.
- "## Ingeprijsde groei": welke jaarlijkse groei van de nettowinst over elf jaar verklaart de koers, naast de winst- en omzetgroei van vijf jaar.
- "## Realistische exit P/E": op grond van eigen range, sectorgenoten en de groei die in jaar 11 nog past, naast de Gordon-P/E (conversie x (1 + g) / (r - g)) bij 2 tot 3 procent groei.
- "## Multiple": het effect op het rendement als de exit P/E vier punten lager of hoger uitvalt.
Blijf bij de nettowinst en de aandelenwaarde. Sluit af met de waarde bij deze aannames en de rekendatum.
```

### 4.3 Model controleren

```text
Controleer mijn winstmodel van [bedrijf] ([ticker]) als tweede lezer; ik bouw het zelf. Per scenario: omzetgroei of parameters per jaar [waarden], nettowinstmarge [waarden], kasstroomconversie [waarden], verandering aandelen [waarden], exit P/E [getal], discount rate [percentage], duurzame groei [percentage]. Uitkomst: waarde per aandeel [bedrag], intern rendement [percentage], koers [koers]. Is de invoer onvolledig, stel dan eerst hoogstens twee vragen. Laat ontbrekende cellen open en meld ze; een andere mening is een argument met bron.

Uitkomst, begin met "# Modelcontrole: [bedrijf] ([ticker])":
- "## Aannames": omzetgroei tegen historie, marktplafond en wet van de grote getallen; marge in jaar 11 tegen volwassen sectorgenoten onder dezelfde standaard; conversie tegen afschrijvingen, investeringen en werkkapitaal; aandelen tegen het beleid. Per aanname voorzichtig, redelijk of optimistisch, met cijfer en bron.
- "## Techniek": jaar 0 en elf perioden, eenheden en valuta, leases eenmaal in de schuld, eindwaarde eenmaal op de winst van jaar 11, discount rate boven de duurzame groei, en of waarde en rendement passen bij mijn invoer.
- "## Tweede mening": discount rate binnen 8 tot 12 procent, exit P/E tegenover range, sectorgenoten en Gordon, en de ene aanname die de uitkomst draagt.
- "## Gedaan": wat je hebt nagerekend en wat nog open staat.
```

## Stap 5 en 6. Universum en posities

### 5.1 Nieuws

```text
Schrijf mijn nieuwsoverzicht over [datum tot datum] voor de sectoren [lijst] en de bedrijven [lijst met tickers]. Ik wil de gebeurtenissen die ertoe doen, in elke regio en sector, in politiek, technologie, regelgeving, grondstoffen en consumentengedrag, en de macro alleen waar die iets verandert. Per gebeurtenis: wat gebeurde er, waarom doet het ertoe, wie wint en verliest, wat betekent het over drie tot vijf jaar. Noem gebeurtenisdatum en publicatiedatum apart.

Uitkomst, 800 tot 1.500 woorden, begin met "# Nieuws, [periode]":
- "## De belangrijkste gebeurtenissen": drie tot vijf met bron.
- "## Per regio en sector": wat verschoof en wat dat betekent.
- "## Mijn lijst": per geraakt bedrijf de gebeurtenis en de aanname of het signaal in mijn dossier die ik opnieuw moet bekijken. Is er niets, zeg dat.
- "## Doorzocht": welke bronnen je wel en niet kon doorzoeken.
```

## Stap 7. Rapporteren

Een rapport of blog is een bijproduct van mijn beslissing. Een outline van vragen maakt het schrijven makkelijker dan een outline van trefwoorden.

### 7.1 Rapport voorbereiden

```text
Zet mijn dossier van [bedrijf] ([ticker]) om in een outline van vragen die ik zelf beantwoord. Dossier: [tabbladen, notities en conclusies]. Mijn conclusie is [twee zinnen], mijn belangrijkste onzekerheid is [onzekerheid]. Volg hoofdstuk 9: onderzoeksvraag met conclusie en onzekerheid; wat het bedrijf doet; waarom ik ernaar kijk en wat de markt anders ziet; cijfers en calls; verwachtingen, scenario's en waardering; wat fout kan gaan en welke signalen ik volg; mijn afweging met datum en positie; bronnen. Gebruik alleen bevindingen uit mijn dossier.

Uitkomst, begin met "# Outline: [bedrijf] ([ticker])":
- "## Constanten": koers en datum, aantal aandelen, definities en boekjaren die elk hoofdstuk gebruikt.
- "## Per hoofdstuk": ruimte in woorden, twee tot vier vragen per alinea met de feiten eronder (cijfer, bron, periode), en wat ik kan weglaten.
- "## Publicatieblokkades": beweringen zonder bron, cijfers om te controleren, een ontbrekende positieverklaring of correctie.
- "## Onthouden": de drie dingen die de lezer moet onthouden, als voorstel dat ik zelf herschrijf.
```

### 7.2 Tweede lezer

```text
Lees mijn concept over [bedrijf] ([ticker]) als kritische redacteur, en vergelijk het met mijn werkboek. Verwijs naar alinea's op nummer en citeer hoogstens vijf woorden; de tekst blijft van mij, dus beschrijf wat er mis is en waarom.

Uitkomst, begin met "# Tweede lezing: [bedrijf] ([ticker])":
- "## These": de conclusie zoals jij die begrijpt, in één regel.
- "## Cijfers": elk cijfer in de tekst naast het werkboek en de bron. Eerst de verschillen tussen hoofdstukken, verkeerde perioden en verwisselde ondernemings- en aandelenwaarde.
- "## Inhoud": hoogstens acht materiële punten op volgorde van belang: feitelijke fouten, verkeerd toegeschreven citaten, een zwak tegenargument of een conclusie die uit de tekst moet blijken.
- "## Publicatiecontrole": de zeven punten, elk in orde of open.
```

## Hoe ik de prompts bijhoud

Na elk gebruik noteer ik in mijn werkmap de datum, de taak, wat bruikbaar was, wat fout ging en wat ik aan de prompt heb veranderd. Een antwoord dat goed werkte is leerinformatie; het maakt de prompt niet onfeilbaar. Verandert mijn methode, dan verandert eerst het hoofdstuk en daarna de prompt, niet andersom.

De content op Belegger Kees is uitsluitend bedoeld voor educatieve doeleinden en vormt geen persoonlijk beleggingsadvies. Beleggen brengt risico's met zich mee. De waarde van beleggingen kan fluctueren en je kunt je inleg verliezen. Resultaten uit het verleden bieden geen garantie voor de toekomst. Raadpleeg een erkende financieel adviseur voor advies op maat. Belegger Kees is geen geregistreerde beleggingsonderneming bij de AFM.

## Verder lezen

[AI-prompts](README.md) · [Hoofdstuk 10: AI-werkwijze](../../02-Manifesto/10-AI-Werkwijze.md) · [Analyseproces](../../03-Analyseproces/README.md) · [Analistenonderzoek](../Analistenonderzoek.md) · [Tien checks en zes vragen](../../03-Analyseproces/Bijlagen/02-NoGo-Checks.md)

---

Bijgewerkt: 2 november 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
