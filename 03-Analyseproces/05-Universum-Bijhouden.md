# Stap 5. Universum bijhouden

Mijn aandelenuniversum is de lijst van bedrijven die ik werkelijk volg: twintig tot veertig namen waarvan ik elke naam kan uitleggen. Het bestand houdt twee dingen apart die vaak door elkaar lopen: in welke fase het onderzoek zit, en waarom ik een naam volg. Een afgerond dossier kan op de watchlist staan omdat de prijs nog niet past; een positie die ik bezit kan opnieuw onderzoek nodig hebben.

## Doel

Eén rij per bedrijf, altijd actueel, met de fase, de reden om te volgen, de laatste update, de belangrijkste vraag en de volgende actie. En per afgerond dossier de waardering, de koopzone en het cijfer dat ik volg, zodat ik in één blik zie welke naam bij de huidige koers het meest oplevert.

## Wat ik klaarzet

`Work-in-Progress/Universum.xlsx`, mijn kopie van het universumtemplate, met de koersdata gekoppeld aan het gegevenstype Aandelen. Prijsalerts bij mijn broker of in TradingView op de bovenkant van elke koopzone.

## Template en tabblad

`01-Universum.xlsx`. Het tabblad Universum heeft per bedrijf de identificatie, de fase als keuzelijst, de datums, de gekoppelde koersdata, mijn parameters en de mini-waardering die daaruit volgt: winst per aandeel in jaar 10, waarde per aandeel bij mijn target P/E, verwacht rendement per jaar bij de huidige koers, en de koopzone bij mijn rendementseis. Het tabblad Overzicht telt per fase. Het tabblad Onderhoud is de checklist van wat ik wanneer bijwerk.

| Fase | Wat ik ermee bedoel |
| --- | --- |
| Kandidaat | Uit een screening; nog een eerste beoordeling nodig |
| Snelle analyse | Ik onderzoek of ik hier meer tijd aan wil besteden |
| Uitgebreide analyse | Ik werk de belangrijkste vragen en de waardering uit |
| Afgerond, met onderhoud | Er ligt genoeg onderzoek voor mijn huidige afweging; nieuwe informatie kan die veranderen |
| Gestopt | Ik besteed er voorlopig geen onderzoekstijd meer aan en heb vastgelegd waarom |

De reden om te volgen staat in een aparte kolom: een open onderzoeksvraag, watchlist (afgerond dossier, prijs past nog niet), eigen positie, of een combinatie.

## Hoe ik het bijhoud

1. **Na elke stap.** Bij stap 1 komt een kandidaat erbij. Bij stap 2 verandert de fase en komen de these en de open vraag erbij. Bij stap 4 komen koopzone, verwacht rendement en het kerncijfer erbij. Bij stap 6 verandert de reden om te volgen.
2. **Bij nieuwe cijfers.** Bij een kwartaal- of halfjaarbericht vergelijk ik het kerncijfer met mijn verwachting, werk ik de parameters bij als het beeld verandert, en zet ik de datum van de update. Tien tot vijftien minuten per naam. Bij een overname, een financieringsprobleem of een onverwachte ontwikkeling wordt het meer, en dan is dat een bewuste keuze.
3. **Bij een prijsalert.** Een alert is een herinnering om opnieuw te kijken, geen koopopdracht. Ik controleer of de analyse nog actueel is en waarom de koers is veranderd, en ga dan naar [stap 6](06-Kopen-Aanhouden-Verkopen.md).
4. **Wekelijks nieuws.** Eén keer per week laat ik [prompt 11](../05-Resources/AI-Prompts/prompts-library.md) het nieuws samenvatten voor de sectoren, industrieën en bedrijven op mijn lijst. Belangrijke gebeurtenissen verdienen eerder aandacht; een samenvatting pikt niet alles op.
5. **Per kwartaal.** Ik loop de hele lijst langs met drie vragen: weet ik nog waarom deze naam erop staat, is het onderzoek actueel genoeg, en staat er een zinvolle volgende stap? Een naam die ik niet meer kan uitleggen gaat naar Gestopt, met de reden.
6. **Het volgende uur kiezen.** Ik kies op basis van de verwachte waarde van het onderzoek: hoe interessant lijkt de kans, hoeveel weet ik al, welke vraag kan ik nu beantwoorden, en wat laat ik liggen als ik dit bedrijf kies. De mini-waardering helpt daarbij, want ze laat zien welke naam bij de huidige koers het meest belooft. Ze beslist niet; de waardering in [stap 4](04-Waarderen.md) doet dat.

## Prompts

Prompt 11 voor het wekelijkse nieuws. Bij een kwartaalbericht dat het beeld verandert: prompt 1, business snapshot, voor de nieuwe cijfers met bron en datum.

## Checks

Geen nieuwe. Wel de vraag bij elke update: raakt dit een van mijn eerder vastgelegde signalen uit stap 6?

## Wat ik vastleg

De hele rij per bedrijf. Bij een verandering van fase of reden de datum erbij. Een verkoop is een gebeurtenis in de geschiedenis; daarna bepaal ik opnieuw of ik het bedrijf blijf volgen.

## Wanneer de stap af is

Deze stap is nooit af; hij is op orde als elke rij een fase, een reden, een datum van de laatste update en een volgende actie heeft, en als geen naam ouder is dan een kwartaal zonder dat ik weet waarom.

## Hoe lang het duurt

Een uur per week voor de lijst als geheel, plus tien tot vijftien minuten per naam bij nieuwe cijfers. Kost het structureel meer, dan is de lijst te lang.

De content op Belegger Kees is uitsluitend bedoeld voor educatieve doeleinden en vormt geen persoonlijk beleggingsadvies. Beleggen brengt risico's met zich mee. De waarde van beleggingen kan fluctueren en je kunt je inleg verliezen. Resultaten uit het verleden bieden geen garantie voor de toekomst. Raadpleeg een erkende financieel adviseur voor advies op maat. Belegger Kees is geen geregistreerde beleggingsonderneming bij de AFM.

## Verder lezen

[Analyseproces](README.md) · [Stap 6: Kopen, aanhouden en verkopen](06-Kopen-Aanhouden-Verkopen.md) · [Hoofdstuk 7: Het aandelenuniversum beheren](../02-Manifesto/07-Universum-Beheren.md) · [Templates](../05-Resources/Templates/README.md)

---

Bijgewerkt: 21 september 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
