# Acht universums en drie landenlijsten in TradingView: zo stel ik mijn screeners in

Een screener brengt duizenden beursbedrijven terug tot een lijst die ik in een middag kan doorlopen. Ik gebruik daarvoor de aandelenscreener van TradingView, met per universum een opgeslagen instelling. Hieronder staat per universum welke filters ik in de kop zet, welke kolommen ik op het scherm zet om een bedrijf te begrijpen, en welke sectoren en industrieën aan of uit staan.

> In English: The Belegger Kees screening set in TradingView has eight universes. A (fast growers) is the main route; D (revenue growth without profit), E (US small caps) and F (mid caps) use the same industries as A with different profitability, country or size filters. B (cyclicals), C (regulated companies), G (life sciences) and H (financials and real estate) catch the industries A leaves out, so every industry belongs to exactly one of A, B, C, G or H. Only E covers the United States. Three country lists (Netherlands, Hong Kong, United States) sit outside the main route. Filters are working hypotheses, not optimised settings.

De instellingen zijn werkhypothesen, geen gemeten optimale filters. Ik pas ze aan als de situatie of de onderzoeksvraag verandert en schrijf op waarom. De filters mogen niet achteraf zo worden gekozen dat één vroegere winnaar er precies doorheen komt. Een ronde zonder geschikte kandidaten is een geldige uitkomst.

## Hoe ik de screener gebruik

TradingView werkt met twee lagen. Boven de tabel staan de filters die bepalen welke bedrijven in de lijst komen. Een deel staat er standaard, zoals Mkt cap, P/E, Revenue growth, Sector en Div yield %; de rest voeg je toe met de plusknop, waarna je de filter op naam zoekt. In de tabel staan de kolommen die per bedrijf zichtbaar zijn; die filteren niet, maar laten mij in één blik zien wat voor bedrijf het is. De landen kies je met de marktknop linksboven, met de vlag erop.

Na het filteren klik ik op de kolomkop Industry, zodat de lijst op industrie gesorteerd staat. Vergelijkbare bedrijven staan dan onder elkaar, en de kolommen hieronder heb ik gekozen om ze naast elkaar te kunnen leggen. Hoe ik daarna vergelijk, staat onder [Van lijst naar vergelijking](#van-lijst-naar-vergelijking).

Ik sla per universum één screener op met een herkenbare naam, zoals BK A Snelle groeiers of BK Land Nederland. Heeft een universum meer varianten, dan sla ik ze allemaal op: BK C1 en BK C2, BK G1 en BK G2, en BK H1, BK H2 en BK H3.

Drie dingen controleer ik voordat ik een lijst vertrouw.

- **De valuta.** In een screener over meerdere landen toont TradingView bedragen in één valuta, standaard de dollar. Alle bedragen hieronder zijn daarom in dollars `[te controleren of de valuta in jouw weergave op USD staat]`.
- **De periode.** Veel filters, zoals Revenue growth % en Net margin %, hebben een keuze voor de periode. Ik kies de laatste twaalf maanden (TTM), en bij groei de vergelijking met dezelfde periode een jaar eerder (YoY), tenzij er iets anders staat.
- **De peildatum.** De cijfers lopen achter op het laatste kwartaalbericht. Een bedrijf dat net goede cijfers heeft gepubliceerd, kan nog buiten een filter vallen.

Filters met een slotje, zoals Price to earnings ratio forward en Enterprise value to EBITDA ratio forward, vragen een betaald abonnement. De instellingen hieronder gebruiken ze niet.

De filters en kolommen staan in de opgeslagen screeners en op deze pagina; die schrijf ik niet per ronde opnieuw over. Verander ik een filter, dan pas ik deze pagina aan en zet ik de reden erbij. De kandidaten die overblijven, zet ik in het [screeningwerkboek](../Templates/README.md), met in de kolom Screener het universum of de landenlijst waar de naam uit komt.

## De indeling in één oogopslag

| Universum | Rol | Landen | Market capitalization | Sectoren |
| --- | --- | --- | --- | --- |
| A. Snelle groeiers | Hoofdroute | Alle DeGiro-landen behalve de Verenigde Staten | 200 miljoen tot 5 miljard dollar | De groeisectoren |
| B. Cyclische bedrijven | Vangnet: grondstofprijzen en de economische cyclus | Alle DeGiro-landen behalve de Verenigde Staten | 200 miljoen tot 10 miljard dollar | Energie, mijnbouw, metalen, basischemie, landbouwgrondstoffen, papier, scheepvaart, auto's, woningbouw, metaalbewerking, zware machines |
| C. Gereguleerde bedrijven | Vangnet: overheid en toezichthouder | Alle DeGiro-landen behalve de Verenigde Staten | 500 miljoen tot 30 miljard dollar | Nuts, telecom, vervoer, pijpleidingen, afval, defensie, zorgdiensten, kansspelen, tabak, overheid |
| D. Omzetgroei zonder winst | Vangnet: nog geen winst | DeGiro-landen in Europa, en Canada | 200 miljoen tot 5 miljard dollar | De groeisectoren |
| E. Amerikaanse smallcaps | Vangnet: kleiner en Amerikaans | Verenigde Staten | 100 miljoen tot 2 miljard dollar | De groeisectoren |
| F. Midcaps | Vangnet: groter | Alle DeGiro-landen behalve de Verenigde Staten | 5 tot 30 miljard dollar | De groeisectoren |
| G. Life Sciences | Vangnet: farmacie, biotechnologie en medische technologie | Alle DeGiro-landen behalve de Verenigde Staten | 200 miljoen tot 20 miljard dollar | Farmacie, biotechnologie, medische technologie |
| H. Financials en vastgoed | Vangnet: banken, verzekeraars, vastgoed en financiële dienstverleners | Alle DeGiro-landen behalve de Verenigde Staten | 300 miljoen tot 30 miljard dollar | Finance en Miscellaneous |
| Landenlijst Nederland | Buiten de hoofdroute | Nederland | Geen ondergrens | Alle sectoren |
| Landenlijst Hongkong | Buiten de hoofdroute | Hongkong | Meer dan 1 miljard dollar | Alle sectoren |
| Landenlijst Verenigde Staten | Buiten de hoofdroute | Verenigde Staten | Meer dan 2 miljard dollar | Alle sectoren |

A, D, E en F delen dezelfde industrieën: de groeisectoren. B, C, G en H zijn de vangnetten voor de industrieën die daar niet in zitten, en elke industrie hoort bij precies één van A, B, C, G en H. Alleen E kijkt naar de Verenigde Staten. Welke industrie waar hoort, staat in de [sectortabel](#welke-sector-en-industrie-bij-welk-universum) onderaan.

## Landen en beurzen

Ik screen alleen op beurzen waar ik bij mijn broker gewone aandelen kan kopen. Dit is de lijst van beurzen die DeGiro voor aandelenorders aanbiedt, volgens de openbare beurzenlijst van DeGiro op 12 september 2026. Voorwaarden en beschikbaarheid veranderen; ik controleer ze bij de broker voordat ik een order plaats.

| Groep | Land en beurs | Bij welk universum of welke lijst |
| --- | --- | --- |
| Kern van Europa | Nederland (Euronext Amsterdam), België (Euronext Brussel), Frankrijk (Euronext Paris), Duitsland (Xetra, Börse Frankfurt), Verenigd Koninkrijk (London Stock Exchange, inclusief AIM), Zwitserland (SIX), Oostenrijk (Wiener Börse), Ierland (Euronext Dublin) | A, B, C, D, F, G, H; Nederland ook in de landenlijst Nederland |
| Noord- en Zuid-Europa | Denemarken (Nasdaq Copenhagen), Zweden (Nasdaq Stockholm), Noorwegen (Oslo Børs), Finland (Nasdaq Helsinki), Spanje (Bolsa de Madrid), Italië (Euronext Milan), Portugal (Euronext Lisbon) | A, B, C, D, F, G, H |
| Oost- en Zuidoost-Europa | Polen (Warsaw Stock Exchange), Tsjechië (Prague Stock Exchange), Griekenland (Athens Stock Exchange) | A, B, C, F, G, H; kleiner en minder liquide, dus extra aandacht voor handelbaarheid |
| Verenigde Staten | NASDAQ, NYSE, NYSE American; NYSE Arca laat ik uit, daar noteren vooral fondsen | Alleen E en de landenlijst Verenigde Staten |
| Canada | Toronto Stock Exchange, TSX Venture | A, B, C, D, F, G, H |
| Hongkong | Hong Kong Stock Exchange | A, B, C, F, G, H en de landenlijst Hongkong; let op de lotgrootte |
| Japan, Singapore, Australië | Tokyo Stock Exchange, Singapore Exchange, ASX | A, B, C, F, G, H; bij Japan let ik op verslaggeving in het Engels |

Wat ik bewust weglaat: Tradegate is een handelsplatform en geen thuisbeurs, dus daar screen ik niet op. Chinese A-aandelen op Shanghai of Shenzhen kan ik niet kopen. OTC-noteringen, handel buiten een gereguleerde beurs, laat ik buiten de screener; een bedrijf dat alleen daar noteert bekijk ik hoogstens via zijn thuisbeurs.

Met de marktknop kies je een of meer landen; dan zitten alle beurzen van dat land erin. Een beurs binnen een land uitzetten, zoals TSX Venture bij Canada of NYSE Arca bij de Verenigde Staten, kan met een filter op de beurs `[te controleren: de naam van dat filter in jouw weergave]`. Lukt dat niet, dan zet ik de kolom met de beurs op het scherm en sla ik die namen bij het doorlopen over.

## Kolommen op het scherm

Deze kolommen zet ik in elke screener, zodat ik een bedrijf kan plaatsen zonder het aan te klikken. De namen zijn de namen in TradingView.

| Kolom in TradingView | Wat hij mij vertelt |
| --- | --- |
| Symbol | Ticker en naam |
| Price | Koers op de peildatum |
| Market capitalization | Omvang; ik lees hem samen met de valuta |
| Price to earnings ratio | Koers-winstverhouding over de laatste twaalf maanden; leeg bij verlies |
| Price to earning to growth | De PEG: koers-winstverhouding gedeeld door de verwachte winstgroei |
| Price to sales ratio | Koers-omzetverhouding; de waardering die bij een verliesgevend bedrijf nog iets zegt |
| Enterprise value to EBITDA ratio | Ondernemingswaarde tegenover bedrijfsresultaat vóór afschrijvingen; bruikbaar waar de P/E misleidt |
| Revenue growth % | Omzetgroei; ik zet hem twee keer neer, over de laatste twaalf maanden en over het laatste boekjaar, zodat ik zie of de groei versnelt of vertraagt |
| Earnings per share diluted growth % | Winstgroei per aandeel, na verwatering |
| Gross margin % | Brutomarge; laat zien of het bedrijf prijszettingsmacht heeft |
| Operating margin % | Bedrijfsresultaat als percentage van de omzet |
| Net margin % | Nettomarge; het getal dat mijn parametermodel gebruikt |
| Free cash flow margin % | Vrije kasstroom als percentage van de omzet |
| Return on equity % | Rendement op eigen vermogen; hoog bij een goed bedrijf, maar ook bij een bedrijf met veel schuld |
| Debt to equity ratio | Schuld tegenover eigen vermogen; ik lees hem samen met de sector |
| Current ratio | Vlottende activa gedeeld door kortlopende schulden; belangrijk bij verliesgevende bedrijven |
| Dividend yield % | Dividendrendement |
| Perf % | Koersverandering, dit jaar en over een jaar; een aandeel dat hard is gedaald verdient de vraag waarom |
| Price × average volume | Gemiddelde dagomzet in geld; onder ongeveer 1 miljoen dollar per dag wordt handelbaarheid een vraag |
| Sector en Industry | De FactSet-indeling die TradingView gebruikt; ik sorteer op Industry om vergelijkbare bedrijven onder elkaar te zetten, en de sectortabel staat onderaan |
| Upcoming earnings date | Wanneer het volgende cijferbericht komt |
| Analyst rating | Consensus van analisten, als die er is; een signaal dat het bedrijf dekking heeft, geen oordeel |

Het land van vestiging en het land waar de meeste omzet vandaan komt, zet ik er ook bij als TradingView die kolommen in mijn weergave toont `[te controleren: kolomnamen]`. Het land van notering zegt vaak weinig over de markt van het bedrijf.

## A. Snelle groeiers, de hoofdroute

Hier zoek ik winstgevende bedrijven met hoge groei van omzet en winst, in de landen en industrieën die ik niet bewust apart houd. Dit universum levert de meeste kandidaten voor de snelle analyse.

| Filter in TradingView | Instelling |
| --- | --- |
| Marktknop | Alle DeGiro-landen uit de tabel hierboven, behalve de Verenigde Staten |
| Market capitalization | 200 miljoen tot 5 miljard dollar |
| Price × average volume, 10 dagen | Meer dan 50.000 dollar |
| Revenue growth, 5 year CAGR | Meer dan 10 procent |
| Net income growth % (TTM, YoY) | Meer dan 10 procent |
| Net margin % (FY) | Meer dan 10 procent |
| Return on equity % (TTM) | Meer dan 10 procent |
| Price to earnings ratio | Minder dan 35 |
| Sector en Industry | De groeisectoren uit de sectortabel |

Op 16 september 2026 heb ik deze filters bijgewerkt: de omzetgroei kijk ik nu over vijf jaar in plaats van over de laatste twaalf maanden, zodat een eenmalige piek minder telt. Winstgroei filter ik nu op de nettowinst in plaats van op de winst per aandeel, want die laatste kan door inkoop van aandelen worden vertekend. Nettomarge kijk ik nu over het boekjaar in plaats van de laatste twaalf maanden. Het rendement op eigen vermogen is niet langer optioneel. Er is een liquiditeitsfilter bijgekomen op koers maal gemiddeld volume over tien dagen, zodat de allerkleinste, moeilijk verhandelbare namen er al bij het screenen uitvallen. Historische groei bewijst geen toekomstige groei. Sneller stijgende winst kan door marges, belastingvoordelen, financiering of een tijdelijk lage basis komen. De screener geeft mij namen; de [snelle analyse](../../02-Manifesto/04-Snelle-Analyse.md) beoordeelt ze.

Een bedrijf dat net winstgevend wordt, valt hier vaak af op nettomarge of koers-winstverhouding, terwijl de operationele hefboom juist dan begint. Zo'n bedrijf vind ik eerder via D of via een landenlijst.

## B. Cyclische bedrijven

Dit is het vangnet voor bedrijven waarvan omzet en winst vooral de prijs van een grondstof volgen: olie, gas en kolen, metalen en mijnbouw, landbouwgrondstoffen zoals palmolie, basischemie, papier en de vrachttarieven in de scheepvaart. Daarnaast staan hier de industrieën die vooral de rente en de economische cyclus volgen: auto's, toeleveranciers van autofabrikanten, woningbouw, metaalbewerking en zware machines voor bouw, mijnbouw en landbouw. Hun omzet volgt de prijs van hun product of de fase van de cyclus meer dan hun eigen plannen, en daarom horen ze niet tussen de groeiers.

| Filter in TradingView | Instelling |
| --- | --- |
| Marktknop | Alle DeGiro-landen, behalve de Verenigde Staten |
| Market capitalization | 200 miljoen tot 10 miljard dollar |
| Enterprise value to EBITDA ratio | Tussen 0 en 7 |
| Debt to equity ratio | Minder dan 1 |
| Free cash flow margin % (TTM) | Meer dan 0 procent |
| Current ratio | Meer dan 1 |
| Price to earnings ratio | Geen filter |
| Sector en Industry | Precies deze industrieën: Energy Minerals (Oil & Gas Production, Integrated Oil, Oil Refining/Marketing, Coal); Non-Energy Minerals (Steel, Aluminum, Precious Metals, Other Metals/Minerals, Forest Products, Construction Materials); Industrial Services (Contract Drilling, Oilfield Services/Equipment); Process Industries (Chemicals: Major Diversified, Chemicals: Agricultural, Agricultural Commodities/Milling, Pulp & Paper, Textiles); Transportation (Marine Shipping); Producer Manufacturing (Metal Fabrication, Auto Parts: OEM, Trucks/Construction/Farm Machinery); Consumer Durables (Motor Vehicles, Homebuilding) |

Bij een cyclisch bedrijf misleidt de koers-winstverhouding. Aan de top van de cyclus is de winst hoog en de P/E laag; dat is het moment waarop het aandeel duur is. Ik filter daarom op ondernemingswaarde tegenover EBITDA, op de balans en op een positieve vrije kasstroom, en niet op P/E. Mijn parametermodel wordt hier prijs maal volume, met de prijs als variabele die ik niet kan voorspellen. Peter Lynch noemt dit de categorie waar de meeste fouten worden gemaakt: een cyclisch bedrijf behandelen als een groeier. Ik schrijf bij elke kandidaat op in welke fase van de cyclus de sector volgens mij zit en waarom.

Palmolieplantages vallen onder Agricultural Commodities/Milling. Scheepvaart staat hier en niet bij C, omdat de vrachttarieven de uitkomst bepalen en geen toezichthouder.

## C. Gereguleerde bedrijven

Dit is het vangnet voor bedrijven die afhangen van overheidsuitgaven, vergunningen of tarieven die een toezichthouder vaststelt. De belangrijkste variabele ligt buiten het bedrijf, en daarom houd ik ze apart. Omdat een netbeheerder iets anders is dan een defensiebedrijf, heeft dit universum twee opgeslagen varianten.

| Filter in TradingView | C1 infrastructuur | C2 overheid en vergunning |
| --- | --- | --- |
| Marktknop | Alle DeGiro-landen, behalve de Verenigde Staten | Alle DeGiro-landen, behalve de Verenigde Staten |
| Market capitalization | 500 miljoen tot 30 miljard dollar | 500 miljoen tot 30 miljard dollar |
| Revenue growth % (TTM, YoY) | Meer dan 3 procent | Meer dan 3 procent |
| Net margin % (TTM) | Meer dan 3 procent | Meer dan 3 procent |
| Return on equity % (TTM) | Meer dan 8 procent | Meer dan 8 procent |
| Debt to equity ratio | Minder dan 2; deze bedrijven dragen structureel meer schuld | Minder dan 1 |
| Enterprise value to EBITDA ratio | Tussen 0 en 12 | Tussen 0 en 12 |
| Dividend yield % | Meer dan 2,5 procent | Geen filter; niet elk bedrijf keert uit |
| Sector en Industry | Utilities (Electric Utilities, Gas Distributors, Water Utilities, Alternative Power Generation); Communications (Major Telecommunications, Specialty Telecommunications, Wireless Telecommunications); Transportation (Railroads, Airlines, Other Transportation); Industrial Services (Oil & Gas Pipelines, Environmental Services) | Electronic Technology (Aerospace & Defense); Health Services (Hospital/Nursing Management, Managed Health Care, Medical/Nursing Services); Consumer Services (Casinos/Gaming); Consumer Non-Durables (Tobacco); Government (Sovereign) |

Waarom deze industrieën hier staan: nuts en pijpleidingen hebben tarieven die een toezichthouder vaststelt; telecom werkt met frequenties en vergunningen; spoor, luchtvaart en luchthavens of tolwegen (Other Transportation) hangen af van concessies, landingsrechten en overheidsbeleid; afvalverwerking werkt met vergunningen en gemeentelijke contracten; defensie hangt af van begrotingen; ziekenhuizen en zorgverzekeraars van vergoedingen die de overheid regelt; kansspelen van vergunningen en kansspelbelasting; tabak van accijnzen en regelgeving. Government is de sector voor overheden zelf; als aandeel komt hij bijna niet voor, maar van alle universums past hij hier het best.

Mijn parametermodel is hier vaak capaciteit maal tarief maal bezetting, of bij defensie het orderboek maal de marge. Ik schrijf bij elke kandidaat op wie het tarief of het budget vaststelt en wanneer dat opnieuw wordt bekeken.

## D. Omzetgroei zonder winst

Dit is het vangnet voor bedrijven met klanten en snel groeiende omzet, maar nog zonder bestendige winst. Het pad naar winst onderzoek ik apart; de screener kan dat niet zien.

| Filter in TradingView | Instelling |
| --- | --- |
| Marktknop | De DeGiro-landen in Europa, en Canada; niet de Verenigde Staten |
| Market capitalization | 200 miljoen tot 5 miljard dollar |
| Omzet over de laatste twaalf maanden | Meer dan 50 miljoen dollar `[te controleren: filternaam voor de totale omzet]` |
| Revenue growth % (TTM, YoY) | Meer dan 20 procent |
| Gross margin % (TTM) | Meer dan 30 procent |
| Net margin % (TTM) | Minder dan 5 procent; zo overlapt D niet met A |
| Price to sales ratio | Minder dan 6 |
| Current ratio | Meer dan 1,5 |
| Sector en Industry | De groeisectoren |

Een positieve brutomarge betekent niet dat winstgevendheid alleen een kwestie van tijd is. Acquisitiekosten, vaste kosten, behoud van klanten en concurrentie kunnen dat pad veranderen. Bij deze bedrijven horen de financieringsvragen uit check 6 en 7 van de [No Go checks](../../03-Analyseproces/Bijlagen/02-NoGo-Checks.md) voorop. Azië en Oost-Europa laat ik hier uit, omdat de informatie over verliesgevende kleine bedrijven daar voor mij moeilijker te controleren is. De Verenigde Staten zitten alleen in E.

## E. Amerikaanse smallcaps

Dit is het vangnet voor kleinere winstgevende groeibedrijven in de Verenigde Staten. Alle andere universums laten de Verenigde Staten uit; hier pak ik ze, met een lagere marktkapitalisatie. Een Amerikaanse notering garandeert geen volledige informatie of voldoende liquiditeit.

| Filter in TradingView | Instelling |
| --- | --- |
| Marktknop | Verenigde Staten; beurzen NASDAQ, NYSE en NYSE American |
| Market capitalization | 100 miljoen tot 2 miljard dollar |
| Price | Meer dan 3 dollar |
| Price × average volume | Meer dan 1 miljoen dollar per dag |
| Revenue growth % (TTM, YoY) | Meer dan 12 procent |
| Earnings per share diluted growth % (TTM, YoY) | Meer dan 18 procent |
| Net margin % (TTM) | Meer dan 5 procent |
| Price to earnings ratio | Tussen 0 en 35 |
| Sector en Industry | De groeisectoren, dezelfde industrieën als A, D en F |

E is het enige universum met de Verenigde Staten, en het gebruikt dezelfde industrieën als A, D en F. Amerikaanse cyclische, gereguleerde en financiële bedrijven en Amerikaanse life sciences zitten dus in geen enkel universum; die zie ik alleen in de landenlijst Verenigde Staten. Wil ik in een ronde toch een van die industrieën in E meenemen, dan zet ik hem bewust aan en noteer ik dat op deze pagina als afwijking.

De ondergrens van 3 dollar en de dagomzet van 1 miljoen dollar houden de allerkleinste en minst verhandelbare aandelen buiten de lijst. Bij Amerikaanse bedrijven let ik op de boekhoudstandaard: US GAAP behandelt leases en ontwikkelkosten anders dan IFRS. Wat dat voor mijn cijfers betekent staat in [hoofdstuk 6](../../02-Manifesto/06-DCF-Model.md). Een bedrijf dat in de Verenigde Staten noteert maar elders is gevestigd en daar zijn omzet haalt, bekijk ik extra kritisch op informatie en toezicht.

## F. Midcaps

Dit is het vangnet voor grotere bedrijven buiten de Verenigde Staten die door hun marktkapitalisatie buiten A vallen. Ik neem niet aan dat een bekende naam al perfect geprijsd is.

| Filter in TradingView | Instelling |
| --- | --- |
| Marktknop | Alle DeGiro-landen, behalve de Verenigde Staten |
| Market capitalization | 5 tot 30 miljard dollar |
| Revenue growth % (TTM, YoY) | Meer dan 8 procent |
| Earnings per share diluted growth % (TTM, YoY) | Meer dan 10 procent |
| Net margin % (TTM) | Meer dan 5 procent |
| Price to earnings ratio | Tussen 0 en 30 |
| Sector en Industry | De groeisectoren |

Bij een bedrijf van deze omvang is drie tot vijf keer de omzet in tien jaar zeldzaam. Ik zoek hier eerder een bedrijf dat twee keer zo groot kan worden met een stijgende marge, en ik schrijf op waarom dat bij mijn methode past.

## G. Life Sciences

Life Sciences staat voor farmacie, biotechnologie en medische technologie. Het is een vangnet en geen onderdeel van de hoofdroute. Bij deze bedrijven kan één goedkeuring door een toezichthouder of één studie-uitkomst de koers in een dag omgooien. Ik kan de wetenschappelijke artikelen lezen, maar zelfs de onderzoekers weten niet zeker wat er uit een studie komt; daarom doen ze die studie. Wat ik heb is een vermoeden en een kansberekening, en of het een goede belegging is, volgt uit de combinatie van koers en kansberekening. Dat past niet in het winstmodel van A tot en met F, maar ik wil deze bedrijven wel kunnen zien.

| Filter in TradingView | G1 met productomzet | G2 in ontwikkeling |
| --- | --- | --- |
| Marktknop | Alle DeGiro-landen, behalve de Verenigde Staten | Alle DeGiro-landen, behalve de Verenigde Staten |
| Market capitalization | 200 miljoen tot 20 miljard dollar | 200 miljoen tot 10 miljard dollar |
| Revenue growth % (TTM, YoY) | Meer dan 10 procent | Geen filter |
| Gross margin % (TTM) | Meer dan 50 procent | Geen filter |
| Debt to equity ratio | Minder dan 1 | Minder dan 0,5 |
| Current ratio | Geen filter | Meer dan 3; het geld moet de studies kunnen dragen |
| Price to cash ratio | Geen filter | Minder dan 3 |
| Sector en Industry | Health Technology: Pharmaceuticals: Major, Pharmaceuticals: Other, Pharmaceuticals: Generic, Biotechnology, Medical Specialties | Dezelfde industrieën |

Bij een kandidaat uit G schrijf ik op welke goedkeuring of studie-uitkomst de koers bepaalt, wanneer die wordt verwacht, welke kans ik daaraan toeken en waar die inschatting op rust, en wat de koers bij succes en bij mislukking zou betekenen. De kans komt met een bron of staat er als mijn eigen inschatting.

## H. Financials en vastgoed

Dit is het vangnet voor banken, verzekeraars, vastgoedbedrijven, vermogensbeheerders en andere financiële bedrijven, en voor de beursgenoteerde fondsen. Bij deze bedrijven is geld zelf de grondstof of zit de waarde in vastgoed, en daardoor zeggen de kengetallen van A weinig: schuld is voor een bank het bedrijf zelf, en een vastgoedfonds keert het grootste deel van zijn winst uit. Omdat een bank, een vastgoedfonds en een betaalnetwerk elk een ander model vragen, heeft dit universum drie opgeslagen varianten. De filters zijn een eerste werkhypothese, die ik na de eerste ronde bijstel.

| Filter in TradingView | H1 banken en verzekeraars | H2 vastgoed | H3 dienstverleners en fondsen |
| --- | --- | --- | --- |
| Marktknop | Alle DeGiro-landen, behalve de Verenigde Staten | Alle DeGiro-landen, behalve de Verenigde Staten | Alle DeGiro-landen, behalve de Verenigde Staten |
| Market capitalization | 500 miljoen tot 30 miljard dollar | 300 miljoen tot 10 miljard dollar | 300 miljoen tot 10 miljard dollar |
| Price to book ratio | Tussen 0 en 1,5 | Tussen 0 en 1,2 | Geen filter |
| Return on equity % (TTM) | Meer dan 10 procent | Geen filter | Meer dan 12 procent |
| Price to earnings ratio | Tussen 0 en 12 | Geen filter; afschrijvingen op vastgoed maken de winst weinig zeggend | Tussen 0 en 25 |
| Dividend yield % | Geen filter | Meer dan 4 procent | Geen filter |
| Debt to equity ratio | Geen filter; voor een bank zegt dit weinig | Minder dan 1,5 | Minder dan 1 |
| Revenue growth % (TTM, YoY) | Geen filter | Geen filter | Meer dan 8 procent |
| Net margin % (TTM) | Geen filter | Geen filter | Meer dan 10 procent |
| Sector en Industry | Finance (Major Banks, Regional Banks, Savings Banks, Property/Casualty Insurance, Multi-Line Insurance, Life/Health Insurance, Specialty Insurance) | Finance (Real Estate Investment Trusts, Real Estate Development) | Finance (Investment Managers, Investment Banks/Brokers, Insurance Brokers/Services, Financial Conglomerates, Finance/Rental/Leasing); Miscellaneous (Investment Trusts/Mutual Funds, Miscellaneous) |

Mijn waardering werkt hier anders dan in [hoofdstuk 6](../../02-Manifesto/06-DCF-Model.md). Bij een bank of verzekeraar leg ik de koers-boekwaardeverhouding naast het rendement op eigen vermogen, en kijk ik naar kapitaalbuffers, kredietverliezen of de combined ratio. Bij vastgoed kijk ik naar de kasstroom uit verhuur, de bezetting en de waarde van het vastgoed min de schuld. Bij een financiële dienstverlener zonder grote eigen balans, zoals een vermogensbeheerder of een betaalnetwerk, werkt het winstmodel van A nog het best. Fondsen vallen door de groei- en margefilters van H3 meestal af; wil ik een beleggingsmaatschappij bekijken, dan zet ik die filters bewust uit en noteer ik dat als afwijking. Wat elke industrie kenmerkt, staat bij [Finance](../Sectoren/19-Finance.md) en [Miscellaneous](../Sectoren/20-Miscellaneous.md).

## Drie landenlijsten

De landenlijsten zijn geen universums en horen niet bij de hoofdroute. Ik volg Nederland, Hongkong en de Verenigde Staten uit persoonlijke interesse en heb er eigen informatiebronnen voor. Met deze lijsten neem ik een kijkje zonder groeifilters.

| Filter in TradingView | Nederland | Hongkong | Verenigde Staten |
| --- | --- | --- | --- |
| Marktknop | Nederland (Euronext Amsterdam) | Hongkong (Hong Kong Stock Exchange) | Verenigde Staten (NASDAQ, NYSE, NYSE American) |
| Market capitalization | Geen ondergrens | Meer dan 1 miljard dollar | Meer dan 2 miljard dollar; kleinere bedrijven komen via D en E |
| Price × average volume | Geen filter | Meer dan 1 miljoen dollar per dag | Geen filter |
| Groei-, marge- en waarderingsfilters | Geen | Geen | Geen |
| Sector en Industry | Alle industrieën, behalve de twee van Miscellaneous | Alle industrieën, behalve de twee van Miscellaneous | Alle industrieën, behalve de twee van Miscellaneous |

In de landenlijsten blijven banken, verzekeraars en vastgoedbedrijven zichtbaar, omdat ze bij het beeld van een markt horen. De landenlijst Verenigde Staten is de enige plek waar ik Amerikaanse bedrijven buiten de groeisectoren van E zie. Een naam uit een landenlijst die ik verder wil onderzoeken, zet ik in het screeningwerkboek met de landenlijst in de kolom Screener; daarna doorloopt hij dezelfde snelle analyse als elke andere kandidaat.

## Welke sector en industrie bij welk universum

TradingView deelt bedrijven in met de sector- en industrie-indeling van FactSet, op basis van waar het grootste deel van de omzet vandaan komt. Dit is mijn keuze per industrie. De groeisectoren zijn de rijen met A, D, E, F: die vier universums gebruiken dezelfde industrieën en verschillen in land, omvang en winstgevendheid. Elke industrie hoort bij precies één van A, B, C, G en H.

| Sector | Industrieën | Universum |
| --- | --- | --- |
| Technology Services | Data Processing Services, Information Technology Services, Packaged Software, Internet Software/Services | A, D, E, F |
| Electronic Technology | Semiconductors, Electronic Components, Electronic Equipment/Instruments, Telecommunications Equipment, Computer Processing Hardware, Computer Peripherals, Computer Communications, Electronic Production Equipment | A, D, E, F |
| Electronic Technology | Aerospace & Defense | C |
| Health Technology | Pharmaceuticals: Major, Pharmaceuticals: Other, Pharmaceuticals: Generic, Biotechnology, Medical Specialties | G |
| Health Services | Hospital/Nursing Management, Managed Health Care, Medical/Nursing Services | C |
| Health Services | Services to the Health Industry | A, D, E, F |
| Consumer Services | Restaurants, Hotels/Resorts/Cruise lines, Movies/Entertainment, Other Consumer Services, Publishing: Books/Magazines, Publishing: Newspapers, Broadcasting, Cable/Satellite TV, Media Conglomerates | A, D, E, F |
| Consumer Services | Casinos/Gaming | C |
| Retail Trade | Food Retail, Drugstore Chains, Department Stores, Discount Stores, Apparel/Footwear Retail, Home Improvement Chains, Electronics/Appliance Stores, Specialty Stores, Catalog/Specialty Distribution, Internet Retail | A, D, E, F |
| Consumer Durables | Automotive Aftermarket, Home Furnishings, Electronics/Appliances, Tools & Hardware, Recreational Products, Other Consumer Specialties | A, D, E, F |
| Consumer Durables | Motor Vehicles, Homebuilding | B; ze volgen de rente en de economische cyclus |
| Consumer Non-Durables | Food: Major Diversified, Food: Specialty/Candy, Food: Meat/Fish/Dairy, Beverages: Alcoholic, Beverages: Non-Alcoholic, Household/Personal Care, Apparel/Footwear, Consumer Sundries | A, D, E, F |
| Consumer Non-Durables | Tobacco | C |
| Commercial Services | Miscellaneous Commercial Services, Advertising/Marketing Services, Commercial Printing/Forms, Financial Publishing/Services, Personnel Services | A, D, E, F |
| Distribution Services | Wholesale Distributors, Food Distributors, Electronics Distributors, Medical Distributors | A, D, E, F |
| Producer Manufacturing | Industrial Machinery, Building Products, Electrical Products, Office Equipment/Supplies, Miscellaneous Manufacturing, Industrial Conglomerates | A, D, E, F; bij Industrial Machinery en Building Products kies ik de Lynch-categorie in de snelle analyse met extra zorg |
| Producer Manufacturing | Metal Fabrication, Auto Parts: OEM, Trucks/Construction/Farm Machinery | B |
| Process Industries | Chemicals: Specialty, Industrial Specialties, Containers/Packaging | A, D, E, F; hier helpt mijn achtergrond in chemische technologie |
| Process Industries | Chemicals: Major Diversified, Chemicals: Agricultural, Agricultural Commodities/Milling, Pulp & Paper, Textiles | B |
| Industrial Services | Engineering & Construction | A, D, E, F |
| Industrial Services | Contract Drilling, Oilfield Services/Equipment | B |
| Industrial Services | Oil & Gas Pipelines, Environmental Services | C |
| Energy Minerals | Oil & Gas Production, Integrated Oil, Oil Refining/Marketing, Coal | B |
| Non-Energy Minerals | Steel, Aluminum, Precious Metals, Other Metals/Minerals, Forest Products, Construction Materials | B |
| Utilities | Electric Utilities, Gas Distributors, Water Utilities, Alternative Power Generation | C |
| Communications | Major Telecommunications, Specialty Telecommunications, Wireless Telecommunications | C |
| Transportation | Railroads, Airlines, Other Transportation | C |
| Transportation | Marine Shipping | B |
| Transportation | Air Freight/Couriers, Trucking | A, D, E, F |
| Finance | Major Banks, Regional Banks, Savings Banks, Property/Casualty Insurance, Multi-Line Insurance, Life/Health Insurance, Specialty Insurance | H1 |
| Finance | Real Estate Investment Trusts, Real Estate Development | H2 |
| Finance | Investment Managers, Investment Banks/Brokers, Insurance Brokers/Services, Financial Conglomerates, Finance/Rental/Leasing | H3 |
| Miscellaneous | Miscellaneous, Investment Trusts/Mutual Funds | H3; uit in de landenlijsten |
| Government | Sovereign | C2; alleen gezien in India |

Wat elke sector en industrie kenmerkt en waar ik als belegger op let, staat in [Sectoren en industrieën](../Sectoren/README.md).

Deze indeling is mijn vertrekpunt. Kom ik een bedrijf tegen dat volgens de indeling in een universum hoort maar er naar mijn inschatting niet past, of andersom, dan noteer ik dat bij de kandidaat en pas ik de indeling in een volgende ronde bewust aan.

## Wat ik aan- of uitvink per universum

Ik werk hiervoor alleen met het filter **Industry** en laat het standaardfilter Sector leeg. Industry voeg ik toe met de plusknop: zoeken op "Industry", onder Security info. Een leeg filter laat alles door, precies alsof alles is aangevinkt. Zodra ik één vakje aanvink, laat het filter alleen nog de aangevinkte industrieën door. Zet ik ook iets in het Sector-filter, dan moet een bedrijf aan allebei voldoen, en dan zijn fouten lastig terug te vinden.

Daaruit volgt de snelste route:

- **Bij een universum dat de meeste industrieën wil** (A, D, E, F en de landenlijsten): onderaan op **Select all** klikken, en daarna de industrieën uit de lijst uitvinken.
- **Bij een universum dat een handvol industrieën wil** (B, C1, C2, G1, G2, H1, H2, H3): direct die industrieën aanvinken, zonder Select all.

Het Sector-filter toont ook een sector Government. Van de vijf landen die ik op 13 september 2026 heb bekeken, kwam die alleen in India voor, met de industrie Sovereign en één notering. Die industrie hoort bij C2; wat erachter zit, staat bij [Government](../Sectoren/21-Government.md) `[te controleren: of het Industry-filter deze industrie als Sovereign toont]`.

De namen staan zoals het filter ze toont, met kleine letters na het eerste woord. Per sector staan ze op alfabet, zodat je ze in de lijst makkelijk terugvindt.

### A. Snelle groeiers, en D, E, F met dezelfde groeisectoren

Select all, en dan deze 63 industrieën uitvinken. Er blijven 67 van de 130 industrieën aan.

**Hele sector uit:**

- Communications: Major telecommunications, Specialty telecommunications, Wireless telecommunications.
- Energy minerals: Coal, Integrated oil, Oil & gas production, Oil refining/marketing.
- Finance: Finance/Rental/Leasing, Financial conglomerates, Insurance brokers/services, Investment banks/brokers, Investment managers, Life/health insurance, Major banks, Multi-line insurance, Property/casualty insurance, Real estate development, Real estate investment trusts, Regional banks, Savings banks, Specialty insurance.
- Government: Sovereign.
- Health technology: Biotechnology, Medical specialties, Pharmaceuticals: generic, Pharmaceuticals: major, Pharmaceuticals: other.
- Miscellaneous: Investment trusts/mutual funds, Miscellaneous.
- Non-energy minerals: Aluminum, Construction materials, Forest products, Other metals/minerals, Precious metals, Steel.
- Utilities: Alternative power generation, Electric utilities, Gas distributors, Water utilities.

**Deels uit, binnen een sector die verder aan blijft:**

- Consumer durables: Homebuilding, Motor vehicles.
- Consumer non-durables: Tobacco.
- Consumer services: Casinos/gaming.
- Electronic technology: Aerospace & defense.
- Health services: Hospital/nursing management, Managed health care, Medical/nursing services.
- Industrial services: Contract drilling, Environmental services, Oil & gas pipelines, Oilfield services/equipment.
- Process industries: Agricultural commodities/milling, Chemicals: agricultural, Chemicals: major diversified, Pulp & paper, Textiles.
- Producer manufacturing: Auto parts: OEM, Metal fabrication, Trucks/construction/farm machinery.
- Transportation: Airlines, Marine shipping, Other transportation, Railroads.

Ook Investment managers en Finance/Rental/Leasing gaan uit, al klinken ze minder als een bank. Op 13 september 2026 stonden in TradingView onder Investment managers ook Morgan Stanley, UBS en Northern Trust, en onder Finance/Rental/Leasing staat Visa naast kredietverstrekkers en verhuurbedrijven. Voor geen van die verdienmodellen werken mijn kengetallen betrouwbaar; ik zie ze in H3.

A en F gebruiken de marktknop op alle DeGiro-landen behalve de Verenigde Staten, D op Europa en Canada, en E op alleen de Verenigde Staten. De Industry-instelling is voor alle vier gelijk.

### B. Cyclische bedrijven

Geen Select all: direct deze 23 industrieën aanvinken.

- Consumer durables: Homebuilding, Motor vehicles.
- Energy minerals: Coal, Integrated oil, Oil & gas production, Oil refining/marketing.
- Industrial services: Contract drilling, Oilfield services/equipment.
- Non-energy minerals: Aluminum, Construction materials, Forest products, Other metals/minerals, Precious metals, Steel.
- Process industries: Agricultural commodities/milling, Chemicals: agricultural, Chemicals: major diversified, Pulp & paper, Textiles.
- Producer manufacturing: Auto parts: OEM, Metal fabrication, Trucks/construction/farm machinery.
- Transportation: Marine shipping.

### C1. Gereguleerd, infrastructuur

Geen Select all: direct deze 12 industrieën aanvinken.

- Communications: Major telecommunications, Specialty telecommunications, Wireless telecommunications.
- Industrial services: Environmental services, Oil & gas pipelines.
- Transportation: Airlines, Other transportation, Railroads.
- Utilities: Alternative power generation, Electric utilities, Gas distributors, Water utilities.

### C2. Gereguleerd, overheid en vergunning

Geen Select all: direct deze 7 industrieën aanvinken.

- Consumer non-durables: Tobacco.
- Consumer services: Casinos/gaming.
- Electronic technology: Aerospace & defense.
- Government: Sovereign.
- Health services: Hospital/nursing management, Managed health care, Medical/nursing services.

### G1 en G2. Life Sciences

Geen Select all: direct deze 5 industrieën aanvinken.

- Health technology: Biotechnology, Medical specialties, Pharmaceuticals: generic, Pharmaceuticals: major, Pharmaceuticals: other.

### H1. Financials, banken en verzekeraars

Geen Select all: direct deze 7 industrieën aanvinken.

- Finance: Life/health insurance, Major banks, Multi-line insurance, Property/casualty insurance, Regional banks, Savings banks, Specialty insurance.

### H2. Financials, vastgoed

Geen Select all: direct deze 2 industrieën aanvinken.

- Finance: Real estate development, Real estate investment trusts.

### H3. Financials, dienstverleners en fondsen

Geen Select all: direct deze 7 industrieën aanvinken.

- Finance: Finance/Rental/Leasing, Financial conglomerates, Insurance brokers/services, Investment banks/brokers, Investment managers.
- Miscellaneous: Investment trusts/mutual funds, Miscellaneous.

### Drie landenlijsten

Select all, en dan alleen de 2 industrieën van Miscellaneous uitvinken: Investment trusts/mutual funds en Miscellaneous. Finance blijft hier aan, zodat ik ook banken, verzekeraars en vastgoed in Nederland, Hongkong en de Verenigde Staten zie.

Wat de industrieën kenmerken en waarom ze bij een universum horen, staat per sector in [Sectoren en industrieën](../Sectoren/README.md).

## Bedrijven die een ander model vragen

Banken, verzekeraars en vastgoedbedrijven hebben met H een eigen universum, omdat hun winst en balans anders werken en de kengetallen van A er weinig over zeggen. Een kandidaat uit H analyseer ik met een ander waarderingsmodel dan het winstmodel uit hoofdstuk 6.

Een kleine marktkapitalisatie vraagt extra onderzoek naar informatie en handelbaarheid, geen automatische conclusie dat het bedrijf ondeugdelijk is. Een overheidsbelang maakt een onderneming evenmin tot een lege vennootschap. Een bedrijf met een tweede notering, bijvoorbeeld op Tradegate naast Hongkong, controleer ik op beide plekken op lotgrootte en spread.

## Van lijst naar vergelijking

Een screener geeft mij een lijst, geen vergelijking. Een nettomarge van 8 procent is hoog voor een groothandel en laag voor een softwarebedrijf, dus een kengetal zegt mij pas iets naast bedrijven met hetzelfde verdienmodel. Daarom sorteer ik de uitkomst op Industry en kijk ik per industrie wie harder groeit, wie een hogere marge haalt, wie meer vrije kasstroom overhoudt en wie lager gewaardeerd is. Wat een industrie kenmerkt en waar ik op let, staat in [Sectoren en industrieën](../Sectoren/README.md).

De vergelijking zelf doe ik in TradingView, op het gesorteerde scherm; ik neem de kengetallen niet over in een werkboek. Van de bedrijven die eruit springen, in positieve of negatieve zin, of die ik niet kan verklaren, bekijk ik er een of meer op Seeking Alpha en op de investor-relationspagina van het bedrijf zelf. Seeking Alpha lees ik als de mening van anderen en de investor-relationspagina als wat het bedrijf over zichzelf zegt. Geen van beide is al een controle van de cijfers.

Wil ik meer weten, dan geef ik een AI-model de jaarverslagen, halfjaarberichten of presentaties van die bedrijven als pdf of link, met [prompt 13](../AI-Prompts/prompts-library.md#13-bedrijven-in-één-industrie-vergelijken). Die prompt geeft per bedrijf een snelle eerste analyse met de bear case eerst, legt de bedrijven naast elkaar en kiest welk bedrijf de beperkte plek op mijn lijst voor de snelle analyse krijgt. De cijfers die die keuze dragen, zoek ik daarna zelf op in het jaarverslag.

## De ronde afronden

Het tabblad Ronde van het screeningwerkboek telt de kandidaten per screener, land en sector en laat zien welke kernvelden nog ontbreken. Ongeveer honderd ruwe namen zijn doorgaans genoeg om vijf tot tien kandidaten te selecteren. Kom ik ver boven de honderd uit, dan scherp ik één filter aan; kom ik onder de twintig, dan verruim ik er één, en ik schrijf op welke.

Bij elke kandidaat controleer ik bereikbaarheid, lotgrootte, spread en kosten voor mijn beoogde positie. Voor actuele handelsvoorwaarden raadpleeg ik de broker en de betreffende beurs. Historische voorbeelden zijn geen actuele orderinformatie.

Mijn doel is een bruikbare selectie in een middag, met screening doorgaans per kwartaal en minimaal jaarlijks. Wat ik daarna met de kandidaten doe staat in [de werkwijze voor het screenen](../../03-Analyseproces/01-Screenen.md).

## Verder lezen

[Screeners](README.md) · [Resources](../README.md) · [Hoofdstuk 3: Aandelen screenen](../../02-Manifesto/03-Screening-Systeem.md) · [Snelle analyse](../../02-Manifesto/04-Snelle-Analyse.md)

---

Bijgewerkt: 16 september 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
