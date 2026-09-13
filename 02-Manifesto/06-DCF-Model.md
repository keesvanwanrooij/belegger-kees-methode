# DCF, exit multiple en intern rendement: hoe ik een bedrijf waardeer

Waardering is voor mij een manier om mijn verwachtingen zichtbaar te maken. Ik wil weten welk rendement per jaar uit mijn aannames volgt en hoeveel risico ik daarvoor neem. Die verhouding vergelijk ik met de andere kansen op mijn lijst. Een koersdoel publiceer ik niet, want de uitkomst hangt volledig af van aannames die van mij zijn. Wat ik wel laat zien is hoe ik reken, welke cijfers ik gebruik en waar ik onzeker ben.

Dit is het langste hoofdstuk van het manifesto, en dat is bewust. Hier staat welke cijfers ik uit een jaarverslag haal en waar ze staan, wat het verschil is tussen de kasstroom voor het hele bedrijf en de kasstroom voor de aandeelhouder, waar IFRS en US GAAP mijn getallen anders maken, welke parameters ik schat, hoe ik de eindwaarde kies en hoe het model in Excel staat. De afleidingen achter de formules staan in [de bijlage](#bijlage-de-formules-die-eronder-liggen), zodat je de uitleg kunt volgen zonder ze eerst door te werken.

## 6.1 Wat ik uit een waardering wil halen

Mijn model rekent verwachte toekomstige kasstromen terug naar hun waarde van vandaag. Dat is wat DCF betekent: discounted cash flow. Het loopt over jaren 1 tot en met 11, met mijn investering in jaar 0. Aan het einde van jaar 11 schat ik wat het aandeel dan waard is met een exit multiple: een koers-winstverhouding waartegen de markt het bedrijf dan naar mijn verwachting waardeert. Gordon Growth, een formule voor de waarde van kasstromen die daarna blijven groeien, gebruik ik alleen als controle.

De uitkomst die ik gebruik is het interne rendement, afgekort IRR. Dat is het percentage waarbij de contante waarde van alle kasstromen, inclusief mijn aankoop, op nul uitkomt. Het volgt dus uit wat ik invoer. Het vertelt mij welk rendement bij mijn scenario past, niet dat dat scenario uitkomt.

Stel dat een fictieve belegging A in mijn scenario 15 procent per jaar oplevert en belegging B 12 procent. Draagt B aanzienlijk minder risico en heb ik meer vertrouwen in die prognose, dan kan B voor mij de betere afweging zijn. In mijn prijs-kwaliteitmatrix zet ik het verwachte rendement daarom naast mijn inschatting van risico en voorspelbaarheid. Een groter verwacht rendement in een rekenmodel is geen compensatie voor een risico dat ik niet begrijp.

## 6.2 Welke cijfers ik uit het jaarverslag haal

Ik werk vanuit de jaarrekening zelf en niet vanuit een dataleverancier. Een leverancier kan een definitie anders kiezen dan het bedrijf, en dan reken ik met een getal dat ik niet kan uitleggen. Dit zijn de posten die mijn model nodig heeft, met de naam onder IFRS, de naam onder US GAAP en de plek waar ik ze vind.

| Wat ik nodig heb | IFRS | US GAAP | Waar het staat |
| --- | --- | --- | --- |
| Omzet | Revenue | Revenue of Net sales | Bovenaan de winst-en-verliesrekening |
| Nettowinst voor gewone aandeelhouders | Profit for the year attributable to owners of the parent | Net income attributable to common stockholders | Onderaan de winst-en-verliesrekening. Niet de winst inclusief minderheidsbelangen |
| Gewogen gemiddeld aantal aandelen, verwaterd | Diluted weighted average number of shares | Diluted weighted average shares outstanding | Bij de winst per aandeel, toelichting onder IAS 33 of ASC 260 |
| Uitstaande aandelen op balansdatum | Issued and outstanding shares | Shares outstanding | Toelichting eigen vermogen; bij een Amerikaans bedrijf ook op de voorpagina van de 10-K |
| Operationele kasstroom | Cash flows from operating activities | Net cash provided by operating activities | Kasstroomoverzicht |
| Investeringen in vaste activa | Purchase of property, plant and equipment; purchase of intangible assets | Purchases of property and equipment; capitalized software | Kasstroomoverzicht, investeringsactiviteiten |
| Betalingen voor leases | Repayment of lease liabilities, en de rente daarop | Bij operationele leases: onderdeel van de operationele kasstroom; bij financiële leases: financieringsactiviteiten | Kasstroomoverzicht en de leasetoelichting |
| Vrije kasstroom zoals het bedrijf die zelf definieert | Free cash flow, met de eigen definitie van het bedrijf | Free cash flow, als non-GAAP maatstaf met aansluiting | Bestuursverslag of MD&A; altijd de definitie erbij lezen |
| Afschrijvingen en amortisatie | Depreciation and amortisation, inclusief afschrijving van gebruiksrechten | Depreciation and amortization | Kasstroomoverzicht en toelichting |
| Aandelenbeloning | Share-based payment expense | Stock-based compensation | Kasstroomoverzicht, als niet-kasuitgave, en de toelichting |
| Cash, financiële schuld, leaseverplichtingen | Cash and cash equivalents; borrowings; lease liabilities | Cash; debt; lease liabilities | Balans en de toelichtingen op schuld en leases |
| Verwachting van het bestuur | Outlook of guidance | Guidance | Persbericht bij de cijfers en de presentatie |

Bij elk cijfer noteer ik de verslagperiode, de valuta en de eenheid. Een halfjaarcijfer is geen jaarcijfer, en een bedrag in duizenden is geen bedrag in miljoenen. Die twee fouten heb ik zelf gemaakt en ze zijn stil: het model rekent gewoon door.

## 6.3 Winst, kasstroom en de kasstroomconversie

Winst is niet hetzelfde als geld. Een bedrijf kan winst maken en tegelijk al zijn geld nodig hebben voor nieuwe vestigingen, voorraden of klanten die laat betalen. Daarom kijkt een waardering naar kasstroom. Er zijn twee soorten, en het verschil zit in de vraag voor wie het geld is.

| Onderdeel | Aandelenmodel | Ondernemingsmodel |
|---|---|---|
| Kasstroom | FCFE, de vrije kasstroom voor aandeelhouders, na rente en aflossing | FCFF, de vrije kasstroom voor alle financiers samen, vóór rente en aflossing |
| Waarde die eruit komt | Waarde van het eigen vermogen, dus van de aandelen | Waarde van de onderneming, dus aandelen plus schuld |
| Disconteringsvoet | Mijn rendementseis als aandeelhouder | De gewogen kosten van schuld en eigen vermogen samen, de WACC |
| Multiple die erbij past | P/E op de nettowinst, of P/FCFE | Bijvoorbeeld EV/EBIT of EV/EBITDA |
| Schuld | Zit al in de kasstroom verwerkt; niet nog eens aftrekken | Wordt aan het eind van de ondernemingswaarde afgetrokken |

De basisformules zijn:

```text
FCFF = EBIT × (1 - belastingpercentage)
       + afschrijvingen
       - investeringen
       - toename operationeel werkkapitaal

FCFE = nettowinst voor gewone aandeelhouders
       + afschrijvingen
       - investeringen
       - toename operationeel werkkapitaal
       + nieuwe schuld
       - aflossingen
```

Ik werk met het aandelenmodel, omdat mijn eindwaarde een koers-winstverhouding op de nettowinst is. Een P/E maal nettowinst geeft een aandelenwaarde, dus de kasstromen ervoor moeten ook aandelenkasstromen zijn. Wie een P/E combineert met FCFF, vergelijkt twee verschillende dingen. Damodaran beschrijft dit onderscheid in zijn [onderwijsmateriaal over waardering](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/val.html).

Wat ik niet doe, is FCFE regel voor regel opbouwen voor elk van de elf prognosejaren. Afschrijvingen, investeringen, werkkapitaal, nieuwe schuld en aflossingen zijn elk apart moeilijk te schatten, en vijf onzekere schattingen bij elkaar geven geen zekerder antwoord dan één. In plaats daarvan schat ik de kasstroomconversie: welk deel van de nettowinst komt als vrije kasstroom beschikbaar voor de aandeelhouder.

```text
kasstroomconversie c = vrije kasstroom / nettowinst
FCFE per jaar = nettowinst × c
```

Die verhouding lees ik af uit de historie. Ik neem de vrije kasstroom zoals het bedrijf die zelf berekent, controleer wat er in die definitie zit, en maak hem vergelijkbaar: na alle leasebetalingen, na investeringen, vóór dividend en inkoop van eigen aandelen. Daarna kijk ik wat de verhouding heeft bepaald.

- Investeringen tegenover afschrijvingen. Een bedrijf dat groeit investeert meer dan het afschrijft. Een sportschoolketen die clubs opent heeft jaren waarin de investeringen ver boven de afschrijvingen liggen, en dan is c laag of zelfs negatief terwijl de winst groeit. Zodra het openen vertraagt, stijgt c vanzelf.
- Werkkapitaal. Klanten die vooruitbetalen, zoals leden van een abonnement, geven een gunstig werkkapitaal. Klanten die laat betalen of voorraden die meegroeien vragen geld.
- Aandelenbeloning. Die zit als niet-kasuitgave in de operationele kasstroom, maar het is een echte kost: de aandeelhouder betaalt hem in verwatering. Ik haal hem niet uit de nettowinst en ik reken de verwatering apart mee.
- Leases. Onder IFRS 16 zitten de aflossingen van leaseverplichtingen niet in de operationele kasstroom. Wie dat vergeet, overschat de vrije kasstroom van een huurder van honderden panden fors. Zie 6.4.

De conversie is dus geen vaste eigenschap van een bedrijf. Ze verandert met de fase waarin het zit. In mijn model schat ik c daarom per jaar: laag zolang het bedrijf zwaar investeert, oplopend naar een niveau dat bij een volwassen bedrijf past. Bij een bedrijf dat vooral software levert kan c boven 1 liggen, omdat afschrijvingen op eerdere ontwikkelkosten hoger zijn dan de nieuwe investeringen. Bij een bedrijf met veel vaste activa ligt c bij volwassenheid vaak tussen 0,7 en 1,0. Die bandbreedtes zijn richtpunten uit mijn eigen onderzoek en geen sectornormen; de historie van het bedrijf zelf is de bron.

FCFE is bovendien geen dividend dat ik werkelijk ontvang. Voor een economische waardering mag ik aannemen dat de berekende FCFE beschikbaar is voor de aandeelhouder, en dan beschrijf ik dat als modelaanname. Voor het rendement op mijn eigen positie tel ik alleen wat ik echt ontvang: dividenden en de verkoopopbrengst. Ingehouden kasstroom tel ik niet tegelijk als ontvangen dividend en als extra cash in de eindwaarde.

## 6.4 IFRS en US GAAP: waar ik op let

De meeste bedrijven die ik onderzoek rapporteren onder IFRS, de internationale standaard. Amerikaanse bedrijven rapporteren onder US GAAP. Voor mijn model verschillen de twee op een handvol punten die er echt toe doen, en die loop ik hieronder langs. Ik ben geen accountant; dit is wat ik in de praktijk controleer.

### Leases: IFRS 16 en ASC 842

Dit is het grootste verschil voor de bedrijven die ik volg, want een keten met gehuurde vestigingen heeft honderden leases.

Onder IFRS 16 staat elke lease op de balans als een gebruiksrecht met daartegenover een leaseverplichting. De huur is daarmee uit de operationele kosten verdwenen en teruggekomen als twee andere posten: afschrijving van het gebruiksrecht en rente op de leaseverplichting. Drie gevolgen. De EBITDA stijgt, omdat huur niet meer als kost meetelt. De operationele kasstroom stijgt, omdat de aflossing van de leaseverplichting onder financieringsactiviteiten staat. En de nettoschuld stijgt, omdat de leaseverplichting erbij komt. De nettowinst verandert per saldo weinig, al ligt hij in de eerste jaren van een lease iets lager door de hogere rente.

Onder ASC 842 staat de lease ook op de balans, maar een operationele lease blijft in de winst-en-verliesrekening één huurkost, en de betaling blijft in de operationele kasstroom. Alleen een financiële lease wordt behandeld zoals onder IFRS 16.

Wat ik daarmee doe:

- Ik reken met de nettowinst, want die is tussen beide standaarden redelijk vergelijkbaar. Een EBITDA onder IFRS 16 vergelijk ik nooit met een EBITDA onder US GAAP zonder correctie, en ook niet met een EBITDA van het bedrijf zelf van vóór 2019.
- Bij de vrije kasstroom onder IFRS haal ik alle leasebetalingen eraf, dus de aflossing én de rente, ook als het bedrijf dat in zijn eigen definitie niet doet. Anders is de vrije kasstroom van een huurder te mooi. Sommige bedrijven publiceren daarom zelf een maatstaf als EBITDA less rent of free cash flow after lease payments; die neem ik dan over en controleer ik.
- Bij de nettoschuld noteer ik de leaseverplichting apart. Voor een vergelijking met een sectorgenoot gebruik ik dezelfde basis: met leases bij allebei, of zonder bij allebei.
- Bij EV/EBITDA neem ik de leaseverplichting mee in de ondernemingswaarde als de EBITDA vóór huur is, en laat ik hem weg als de EBITDA na huur is. Eén van beide, nooit half.

### Ontwikkelkosten

Onder IFRS mag een bedrijf ontwikkelkosten activeren als aan de voorwaarden van IAS 38 is voldaan; dan staan ze op de balans en worden ze afgeschreven. Onder US GAAP gaan onderzoeks- en ontwikkelkosten vrijwel altijd direct ten laste van de winst, met een uitzondering voor software. Een Europees softwarebedrijf kan daardoor een hogere nettowinst en een hoger investeringsbedrag tonen dan een Amerikaanse concurrent met dezelfde kosten. Ik lees de toelichting op immateriële activa en kijk hoeveel er per jaar wordt geactiveerd. Voor de kasstroomconversie maakt het niet uit, want de kas is hetzelfde; voor de winstmarge en de P/E wel.

### Aandelenbeloning en aangepaste winst

Beide standaarden nemen aandelenbeloning als kost in de winst. Veel bedrijven publiceren daarnaast een aangepaste winst zonder die kost, onder US GAAP als non-GAAP maatstaf met een verplichte aansluiting. Ik gebruik de gerapporteerde nettowinst als basis en niet de aangepaste. Aandelenbeloning is een echte kost, en het aantal aandelen dat erbij komt zet ik apart in het model als verwatering. Groeit de aandelenbeloning sneller dan de omzet, dan is dat voor mij een vraag aan het bestuur.

### Rente en dividend in het kasstroomoverzicht

Onder IFRS mag een bedrijf betaalde rente onder operationele of onder financieringsactiviteiten zetten, en ontvangen dividend onder operationele of investeringsactiviteiten. Onder US GAAP staat betaalde rente altijd in de operationele kasstroom. Ik controleer waar het staat, want anders vergelijk ik twee operationele kasstromen die niet hetzelfde meten. Voor FCFE maakt de keuze niet uit zolang ik de rente ergens aftrek.

### Eenmalige posten en herzieningen

Een verkoopwinst op een onderdeel, een afwaardering van goodwill, een reorganisatie of een boete zit in de nettowinst van dat jaar. Voor de trend in mijn winstmarge kijk ik daar doorheen, maar ik zet ze wel op een rij: een bedrijf dat elk jaar een eenmalige post heeft, heeft een gewone kost. Herziene cijfers van een vorig jaar neem ik over uit het nieuwste verslag, met een aantekening.

### Wat ik doe bij een Amerikaans bedrijf

Ik lees de 10-K, het jaarverslag dat bij de toezichthouder wordt gedeponeerd. Het aantal uitstaande aandelen staat op de voorpagina met een datum. De cijfers staan in Item 8, de toelichting van het bestuur in Item 7. Ik neem de GAAP-nettowinst, negeer de adjusted EPS als basis, en weet dat bij operationele leases de huur al als kost in de winst zit; daar hoef ik dan niets bij te corrigeren. Bij de vrije kasstroom controleer ik welke definitie het bedrijf gebruikt, want die is onder US GAAP niet voorgeschreven. Het boekjaar loopt regelmatig niet gelijk met het kalenderjaar; dat noteer ik bij de verslagperiode.

## 6.5 De parameters die ik schat

Mijn model heeft weinig parameters, en elke parameter heeft een herkomst. Dit is de volledige lijst.

| Parameter | Per jaar 1 tot en met 11 | Waar ik de schatting op baseer |
| --- | --- | --- |
| Omzet | Uit de bedrijfsparameters, zoals aantal clubs maal leden per club maal omzet per lid, of als groeipercentage per jaar | De historie van elke parameter, de eigen verwachting van het bestuur, de grens van de markt uit de snelle analyse |
| Nettowinstmarge | Percentage van de omzet | De historie onder dezelfde boekhoudstandaard, de operationele hefboom, de marge van een volwassen sectorgenoot als bovengrens |
| Kasstroomconversie c | Vrije kasstroom gedeeld door nettowinst | De historie, gecorrigeerd voor leases, en het investeringsplan van het bedrijf |
| Verandering aantal aandelen | Percentage per jaar, positief bij verwatering en negatief bij inkoop | De historie van het verwaterde aantal aandelen en het beleid van het bestuur |
| Exit P/E | Eén getal voor het einde van jaar 11 | De eigen historische range van het bedrijf, sectorgenoten op dezelfde boekhoudbasis, de groei die ik in jaar 11 nog verwacht |
| Discount rate r | Eén getal | Mijn inschatting van het risico, doorgaans 8 tot 12 procent |
| Duurzame groei g | Eén getal, alleen voor de Gordon-controle | Rond de groei van de economie, meestal 2 tot 3 procent |

Daarnaast zijn er hulpparameters die ik niet in de formules gebruik, maar wel opschrijf om de kasstroomconversie te onderbouwen: afschrijvingen als percentage van de omzet, investeringen als percentage van de omzet, en de verandering in werkkapitaal. Als ik zeg dat c oploopt van 0,3 naar 0,8, moet ik kunnen laten zien dat dat komt doordat de investeringen dalen naar het niveau van de afschrijvingen. Zo blijft één parameter het model sturen, terwijl de onderbouwing zichtbaar blijft.

De discount rate kies ik binnen mijn band op basis van het vertrouwen dat ik in de kasstromen heb:

| Mijn inschatting | Vertrekpunt | Wat ik erbij beoordeel |
|---|---|---|
| Relatief goed te overzien | Rond 8 procent | Voorspelbaarheid, financiering en mijn begrip van de bedrijfsontwikkeling |
| Meer onzekerheid | Rond 10 procent | Variatie in groei, marges, concurrentie en benodigde investeringen |
| Hoger risico | Rond 12 procent | Grotere afhankelijkheid van aannames of een minder voorspelbaar verloop |

Dit zijn mijn persoonlijke richtpunten en geen marktnormen. Risico in een discount rate verwerken lijkt exact, maar de keuze blijft subjectief. Ik maak daarom liever duidelijk welke risico's ik zie dan dat ik extra decimalen gebruik. De WACC, de gewogen gemiddelde vermogenskosten van schuld en eigen vermogen, past bij het ondernemingsmodel en niet bij het mijne; binnen één berekening gebruik ik dezelfde grondslag.

Het rekenwerk per jaar is dan:

```text
omzet_t        = omzet_t-1 × (1 + omzetgroei_t)      of uit de bedrijfsparameters
nettowinst_t   = omzet_t × nettowinstmarge_t
FCFE_t         = nettowinst_t × c_t
aandelen_t     = aandelen_t-1 × (1 + verandering_t)
winst per aandeel_t = nettowinst_t / aandelen_t
FCFE per aandeel_t  = FCFE_t / aandelen_t
```

Ik reken drie scenario's door: tegenvallend, midden en gunstig. Ik varieer daarin de echte groeidragers, de marge, de conversie, de verwatering en de exit multiple, en ik zorg dat een scenario intern klopt. Een tegenvallend scenario met hoge omzetgroei en lage investeringen is geen scenario maar een fout.

## 6.6 Jaar 11, de exit multiple en Gordon Growth als controle

Ik kies in het basismodel voor verkoop aan het einde van jaar 11, na de kasstroom van dat jaar. De elf prognosejaren krijgen elk een kolom en jaar 0 staat ervoor. Het is dus een reeks van twaalf meetmomenten.

| Moment | Jaar 0 | Jaar 1 tot en met 10 | Jaar 11 |
|---|---|---|---|
| Betekenis | Mijn investering | Tussentijdse kasstromen | Laatste expliciete kasstroom plus eindwaarde |
| Kasstroom | Negatief | Volgens het model | FCFE jaar 11 plus aandelenwaarde eind jaar 11 |
| Discontering | Geen | Met de eigen jaarexponent | Met exponent 11 |

De eindwaarde is een multiple op de winst van jaar 11:

```text
Aandelenwaarde eind jaar 11 = exit P/E × nettowinst jaar 11
Waarde per aandeel eind jaar 11 = exit P/E × winst per aandeel jaar 11
```

Dit is een multiple op de winst van het dan afgesloten jaar. Gebruik ik een forward P/E op de verwachte winst van jaar 12, dan moet dat expliciet zo in het model staan.

De exit P/E is de aanname met de meeste invloed op de uitkomst, en ik kies hem in drie stappen. Eerst kijk ik naar de eigen historische range van het bedrijf over vijf tot tien jaar: waar heeft de markt dit bedrijf in rustige jaren gewaardeerd? Dan kijk ik naar sectorgenoten die in jaar 11 op het bedrijf lijken, dus een volwassen bedrijf in dezelfde sector op dezelfde boekhoudbasis. Ten slotte kijk ik naar de groei die ik in jaar 11 nog verwacht. Een bedrijf dat dan nog met 10 tot 15 procent groeit, verdient een hogere multiple dan een bedrijf dat is uitgegroeid naar de groei van de economie. Als vertrekpunt neem ik voor een uitgegroeid bedrijf 12 tot 15, en voor een bedrijf dat nog groeit 15 tot 20. Boven de 20 moet ik kunnen uitleggen waarom, en meestal kan ik dat niet.

Een exit multiple bevat mijn verwachting van een toekomstige marktprijs. Het is daarmee ook een prijsaanname, en niet alleen een berekende intrinsieke waarde. Dat onderscheid wordt uitgelegd bij [exit multiples in Damodarans waarderingsmateriaal](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/AppldCF/derivn/ch12deriv.html).

Gordon Growth gebruik ik als controle op die multiple. De formule rekent de waarde van de kasstromen na jaar 11 uit bij een constante groei g die eeuwig doorgaat:

```text
TV11 = FCFE11 × (1 + g) / (r - g)
PV(TV11) = TV11 / (1 + r)^11
```

Hier is TV11 de eindwaarde aan het einde van jaar 11, PV(TV11) de contante waarde daarvan vandaag, r mijn discount rate en g de duurzame groei vanaf jaar 12. De formule veronderstelt dat r groter is dan g. Uit dezelfde formule volgt welke P/E de Gordon-eindwaarde impliceert: c × (1 + g) / (r - g), met c de kasstroomconversie in jaar 11. Bij c van 0,8, g van 3 procent en r van 10 procent is dat 11,8.

Dat getal laat meteen zien waarom ik Gordon niet als eindwaarde gebruik. De formule gaat ervan uit dat het bedrijf vanaf jaar 12 alleen nog met de economie meegroeit. Voor een bedrijf dat in jaar 11 nog markten opent, is dat te vroeg, en dan valt de waarde te laag uit. Zo zou een groeibedrijf afvallen zonder goede reden. Ik gebruik de Gordon-uitkomst daarom als ondergrens: ligt mijn exit P/E ver boven de geïmpliceerde P/E, dan moet ik kunnen uitleggen welke groei na jaar 11 dat verschil rechtvaardigt. Kan ik dat niet, dan is mijn multiple te hoog. De afleiding staat in [de bijlage](#bijlage-de-formules-die-eronder-liggen).

## 6.7 Excel: zo staat het model in mijn werkboek

Het [template voor de uitgebreide analyse](../05-Resources/Templates/README.md) heeft een tabblad Model met deze indeling. De bedragen staan op rij 5, in de schaal die ik op het tabblad Invoer heb gekozen: per aandeel of voor de hele positie. Die twee schalen mogen niet door elkaar lopen.

| Cellen | Inhoud |
|---|---|
| B3 | Jaar 0 |
| C3 tot en met L3 | Jaar 1 tot en met 10 |
| M3 | Jaar 11 |
| B4 tot en met M4 | Het kalenderjaar bij elk jaarnummer, zodat ik zie over welk jaar ik het heb |
| B5 | Negatieve begininvestering |
| C5 tot en met L5 | FCFE per jaar; 0 als er geen kasstroom is |
| M5 | FCFE jaar 11 plus eindwaarde |
| B8 | Gekozen discount rate |

In Nederlandstalig Excel:

```excel
=IR(B5:M5)
=NHW(B8;C5:M5)+B5
```

De eerste formule berekent het interne rendement. De tweede geeft de netto contante waarde na aftrek van de investering. Alleen NHW(B8;C5:M5) geeft de huidige waarde van de toekomstige ontvangsten.

In Engelstalig Excel heten deze functies IRR en NPV. Bij onregelmatige betaaldata gebruik ik IR.SCHEMA of XIRR met een rij van bijbehorende datums. Microsoft beschrijft dit onderscheid in [de uitleg over NHW en IR](https://support.microsoft.com/nl-NL/Excel/go-with-the-cash-flow-calculate-npv-and-irr-in-excel).

De begininvestering moet in de IR-reeks zitten. Als ik uitsluitend jaren 1 tot en met 11 selecteer en daarin alleen positieve kasstromen staan, bereken ik niet het rendement op mijn aankoop. Lege tussencellen kunnen door Excel worden overgeslagen; een jaar zonder betaling krijgt daarom expliciet 0.

Als fictieve controle investeer ik 100 in jaar 0, ontvang ik tien jaar niets en krijg ik 200 aan het einde van jaar 11. Het interne rendement is dan:

```text
(200 / 100)^(1/11) - 1 ≈ 6,50% per jaar
```

Bij wisselende tekens in de kasstromen kunnen meerdere interne rendementen bestaan. Een foutmelding of een onverwachte uitkomst vraagt controle van de reeks en de netto contante waarde. Ik vervang een fout niet door nul.

Onder rij 11 staan in het werkboek de opbouwrijen uit 6.5: omzet, nettowinst, FCFE, aantal aandelen en winst per aandeel per jaar, en daaronder de eindwaarde, de contante waarde per jaar, de som daarvan, de modelwaarde en de waarde per aandeel. Het tabblad Parameters bevat de drie scenario's; het tabblad Invoer kiest welk scenario doorwerkt.

## 6.8 Hoe ik de uitkomst weeg

Een uitkomst is pas bruikbaar als ik weet hoeveel ik erop kan bouwen. Daar gebruik ik vijf controles voor.

**Het aandeel van de eindwaarde.** Ik bereken hoeveel van mijn waardering uit de eindwaarde komt:

```text
Aandeel eindwaarde = PV(TV11) /
                    (som contante expliciete kasstromen + PV(TV11))
```

De noemer is de modelwaarde vóór aftrek van de aankoopprijs. Is die nul of negatief, dan is dit percentage niet zinvol. Bij negatieve expliciete kasstromen kan het boven 100 procent komen, en dat laat juist zien hoe afhankelijk het model van de toekomst is. Ik heb hiervoor geen vaste bovengrens. Ik beoordeel of dat aandeel past bij mijn vertrouwen in de exit multiple. Verandert het bedrijf in jaar 11 nog sterk, dan kan ik jaren 12 tot en met 15 toevoegen en de eindwaarde naar het einde van jaar 15 verplaatsen. Meer jaren modelleren verlaagt de onzekerheid niet vanzelf; het geeft mij vooral ruimte om de overgang naar een stabielere fase uit te leggen.

**De afstand tussen koers en berekende waarde.** Daar bestaan twee getallen voor, en ik benoem altijd de noemer:

```text
Koersruimte = (berekende waarde - koers) / koers
Korting op berekende waarde = (berekende waarde - koers) / berekende waarde
```

Bij een koers van 100 en een berekende waarde van 130 is de koersruimte 30 procent en de korting op waarde ongeveer 23,1 procent. Andersom: een korting van 30 procent op een berekende waarde van 100 betekent een prijs van 70, en de koersruimte naar 100 is dan ongeveer 42,9 procent. Beide getallen kunnen helpen, maar ze zijn geen synoniemen. Een marge in een model beschermt ook niet tegen iedere fout.

**De gevoeligheid.** Het werkboek toont de waarde per aandeel bij combinaties van exit multiple en discount rate, en van exit multiple en groei. Als de uitkomst omslaat bij een verschuiving van twee punten in de multiple, weet ik waar mijn onderzoek naartoe moet.

**De omgekeerde waardering.** Ik reken terug welke aanname bij de huidige koers past. Ik houd alle andere aannames vast en los één variabele op, meestal de omzetgroei, met de functie Doelzoeken. Uit één koers kan ik niet tegelijk een unieke groei, marge en multiple afleiden, maar ik zie wel of de markt meer of minder inprijst dan het bedrijf historisch heeft laten zien.

**De scenario's naast elkaar.** Ik vermeld bij een kansweging de gewichten, en ik weet dat een gewogen gemiddelde van losse interne rendementen niet hetzelfde is als het interne rendement van gewogen kasstromen. Wat mij het meest zegt, is het tegenvallende scenario: levert dat nog een rendement op dat ik acceptabel vind, dan heb ik een sterke zaak. Levert alleen het gunstige scenario iets op, dan heb ik een hoop.

Verandert er iets in de cijfers, dan werk ik het model bij en bewaar ik de aannames, bronnen en rekendatum. Het [universumoverzicht](07-Universum-Beheren.md) laat zien wanneer ik een waardering voor het laatst heb bekeken. Instappen, aanhouden en verkopen staan in [hoofdstuk 8](08-Timing.md).

## Bijlage: de formules die eronder liggen

Dit deel is er om na te rekenen. Je hebt het niet nodig om de methode te begrijpen.

### Gordon Growth, en rekenen vanuit jaar 10

De formule gebruikt de eerstvolgende kasstroom na de prognoseperiode, dus die van jaar 12:

```text
TV11 = FCFE12 / (r - g)
FCFE12 = FCFE11 × (1 + g)

TV11 = FCFE11 × (1 + g) / (r - g)
```

Groei, valuta en inflatie moeten op dezelfde basis staan, en de kasstroom moet de investeringen bevatten die de groei mogelijk maken. Reken ik vanuit jaar 10, dan mag dit alleen als dezelfde g ook tussen jaar 10 en jaar 11 geldt:

```text
TV11 = FCFE10 × (1 + g)^2 / (r - g)
```

Gebruik ik een eigen groeiverwachting voor jaar 11, dan reken ik eerst de werkelijke modelkasstroom van jaar 11 uit en kan ik de kwadraatformule niet gebruiken.

### Kasstroomconversie en de bijbehorende P/E

Noem c de verhouding tussen FCFE en nettowinst in jaar 11:

```text
c = FCFE11 / nettowinst11

P/E op jaar-11-winst = TV11 / nettowinst11
                     = c × (1 + g) / (r - g)
```

Zijn FCFE en nettowinst gelijk, dan is c gelijk aan 1. De factor (1 + g) komt hier één keer voor: de kwadraatfactor uit de vorige paragraaf verdwijnt omdat de P/E wordt gedeeld door de winst van jaar 11.

### Waarom een FCF-marge hier niet in de noemer hoort

Een FCF-marge is FCF gedeeld door omzet. Dat is een andere verhouding dan kasstroomconversie. Bij dezelfde periode en dezelfde aandelenkasstroom geldt:

```text
FCFE-marge = FCFE / omzet
nettowinstmarge = nettowinst / omzet
c = FCFE-marge / nettowinstmarge
```

Ik vermenigvuldig de afgeleide P/E dus met de kasstroomconversie. Ik deel niet door een los genoemde FCF-marge, en `P/E × winst / FCF-marge` is geen juiste definitie van aandelenwaarde.

Een fictief rekenvoorbeeld: nettowinst in jaar 11 is 10, FCFE is 6, r is 10 procent en g is 2 procent. Dan is c gelijk aan 0,6, is de eindwaarde 6 × 1,02 / 0,08 = 76,5 en is de bijbehorende P/E 7,65. Dit voorbeeld laat alleen zien dat de formules op elkaar aansluiten.

### Van ondernemingswaarde naar aandelenwaarde

Wie toch met FCFF en een ondernemingswaarde werkt, komt zo bij de aandelen uit:

```text
Aandelenwaarde = ondernemingswaarde
                 - financiële schuld
                 - leaseverplichtingen (als de kasstroom vóór leasebetalingen is)
                 - minderheidsbelangen
                 - preferente aandelen
                 + cash en liquide beleggingen
```

Elke post komt één keer voor. Een leaseverplichting die al in de kasstroom is verwerkt, wordt hier niet nog eens afgetrokken.

## Verder lezen

[Alle hoofdstukken](README.md) · [De Belegger Kees Methode](../README.md) · [Bronnen en redactionele werkwijze](../01-Docs/README.md) · [Template uitgebreide analyse](../05-Resources/Templates/README.md)

> In English: Kees values a company with an equity cash-flow model built from a small set of parameters: revenue from business drivers, net margin, cash conversion (free cash flow divided by net income), share count change, an exit P/E on year-11 earnings and a discount rate of 8 to 12 percent. The chapter explains which lines he takes from IFRS and US GAAP statements, how leases under IFRS 16 and ASC 842 change the numbers, and why Gordon Growth serves only as a floor check.

Correctie van 12 september 2026: dit hoofdstuk beschrijft het model nu als winstmodel met kasstroomconversie in plaats van een opbouw van de vrije kasstroom regel voor regel. De secties over de jaarrekening onder IFRS en US GAAP en over leases zijn nieuw. De rekenvoorbeelden zijn ongewijzigd.

De content op Belegger Kees is uitsluitend bedoeld voor educatieve doeleinden en vormt geen persoonlijk beleggingsadvies. Beleggen brengt risico's met zich mee. De waarde van beleggingen kan fluctueren en je kunt je inleg verliezen. Resultaten uit het verleden bieden geen garantie voor de toekomst. Raadpleeg een erkende financieel adviseur voor advies op maat. Belegger Kees is geen geregistreerde beleggingsonderneming bij de AFM.

---

Bijgewerkt: 13 september 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
