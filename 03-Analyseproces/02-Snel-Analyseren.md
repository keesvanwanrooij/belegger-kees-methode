# Stap 2. Snel analyseren

De snelle analyse beantwoordt één vraag: wil ik ongeveer twintig uur verder onderzoek aan dit bedrijf besteden, of staat er een betere kandidaat op mijn lijst? Ik kijk eerst naar wat fout kan gaan en pas daarna naar wat goed kan gaan. De uitkomst is een keuze per kandidaat en een voorkeursvolgorde over alle kandidaten heen.

## Doel

Per kandidaat: verder onderzoeken, later terugkomen of stoppen, met een reden in maximaal tien regels. Over alle kandidaten: een volgorde waarin ik mijn tijd besteed, en een pre-mortem voor de kandidaat die naar stap 3 gaat.

## Wat ik klaarzet

De [voorbereiding](00-Voorbereiden.md) voor dit bedrijf, met de werkmap, de kopie `Bedrijfsnaam-Snelle-Analyse.xlsx`, het laatste jaarverslag, het laatste kwartaal- of halfjaarbericht en het laatste transcript van de earnings call.

## Template en tabblad

`03-Snelle-Analyse.xlsx`, met per fase een tabblad. Op het tabblad Overzicht staat bovenaan de incheck, in het midden per fase de keuze, en onderaan de afsluiting. Het tabblad Bedrijfsinfo neemt de koers, het aantal aandelen, de cash, de schuld en de leaseverplichtingen op en berekent de ondernemingswaarde met en zonder leases.

| Fase | Tabblad | Wat ik onderzoek | Checks |
| --- | --- | --- | --- |
| 0. Datasnapshot | Bedrijfsinfo | Identiteit, boekhoudstandaard, valuta, koersdatum, verslagperiode, handelbaarheid, kerncijfers | 1 |
| 1. Business snap | Bedrijf | Verdienmodel in gewone taal, balans, winstgevendheid, kwaliteit van de cijfers | 3, 6, 7, 8 |
| 2. Markt en groeiruimte | Markt | Groeidragers als parameters, omzetplafond, operationele hefboom, concurrentie | 2, 4 |
| 3. Waardering | Waardering | Koers-winstverhouding en PEG, verkorte omgekeerde DCF, eerste eigen verwachting | 5, 10 |
| 4. Prijs en kwaliteit | Prijs en kwaliteit | De bear case van de markt, scores voor prijs en kwaliteit, vergelijking met andere kansen | 9, en vragen 11 tot en met 14 |
| 5. Management | Management | Beloftes tegenover resultaten, kapitaalallocatie, eigen belang, taal in de laatste call | Vragen 15 en 16 |

Op het tabblad Checks staan de tien directe checks en de zes aanvullende vragen onder elkaar, elk met de uitkomst als keuze (geen belemmering, belemmering, onbekend, niet van toepassing), een toelichting, een bron en het gevolg voor mijn afweging. Er staat geen totaalscore onder, want een belemmering bij check 6 weegt niet hetzelfde als een vraagteken bij vraag 13.

## Hoe ik de fasen doe

1. **Fase 0.** Ik vul Bedrijfsinfo in vanuit het jaarverslag en de koersdata. Boekhoudstandaard en verslagperiode staan erbij, want die bepalen hoe ik de rest lees; zie [hoofdstuk 6](../02-Manifesto/06-DCF-Model.md).
2. **Fase 1.** Ik beschrijf in drie tot vijf zinnen wie betaalt, waarvoor en waarom hij terugkomt. Lukt dat niet na een half uur, dan is dat een uitkomst. Daarna de balans: schuld, rente, looptijden, cash, en of het bedrijf twee slechte jaren kan financieren.
3. **Fase 2.** Ik schrijf de omzet uit in een paar parameters, zoals vestigingen maal klanten per vestiging maal besteding per klant, en zoek per parameter de historie en de grens. Drie tot vijf keer de omzet in tien jaar is de vraag die ik stel.
4. **Fase 3.** Ik leg P/E en verwachte winstgroei naast elkaar, reken met de verkorte omgekeerde DCF op het tabblad Waardering terug welke groei de koers inprijst, en zet mijn eerste eigen verwachting ernaast.
5. **Fase 4.** Ik zoek de bear case die de markt al heeft voordat ik er zelf een bedenk. Dan geef ik een score van 1 tot 10 voor kwaliteit (hoe goed is het bedrijf) en van 1 tot 10 voor prijs (hoe laag is de waardering tegenover de eigen historie en vergelijkbare bedrijven; een hoge score is een lage prijs). Een goed bedrijf kan duur zijn en een slecht bedrijf goedkoop; ik zoek de combinatie van twee hoge scores.
6. **Fase 5.** Ik vergelijk wat het bestuur drie tot vijf jaar geleden beloofde met wat er kwam, kijk naar inkoop, overnames en beloning, en lees de laatste call op wat er ontbreekt of verschuift.
7. **Afsluiting.** Ik kies per kandidaat en schrijf de voorkeursvolgorde, de belangrijkste open vraag en de eerstvolgende stap op het tabblad Overzicht. Voor de kandidaat die doorgaat schrijf ik de pre-mortem op het tabblad Pre-mortem: het is drie jaar later, de belegging is tegengevallen, wat is er gebeurd en wat had ik eerder kunnen zien.

## Prompts

Per fase één prompt uit [de promptbibliotheek](../05-Resources/AI-Prompts/prompts-library.md): 1 business snapshot bij fase 0, 2 businessmodel en parameters bij fase 1 en 2, 3 markt en concurrenten bij fase 2, 4 waardering en omgekeerde DCF bij fase 3, 5 prijs en kwaliteit bij fase 4 als ik meerdere kandidaten vergelijk, 6 management bij fase 5, en 7 pre-mortem bij de afsluiting. Elk cijfer dat mijn keuze draagt controleer ik zelf bij de bron.

## Checks

Alle zestien, verdeeld over de fasen zoals in de tabel. Een belemmering bij een directe check kan genoeg zijn om te stoppen; ik hoef de rest dan niet af te maken. Een onbekend antwoord is een open vraag, geen bewijs.

## Wat ik vastleg

Het ingevulde werkboek in de werkmap. In het [universumbestand](05-Universum-Bijhouden.md): de fase (uitgebreide analyse, later terugkomen met datum, of gestopt), de these in één zin, de belangrijkste open vraag en de volgende actie. Een kandidaat die stopt krijgt de reden erbij, want een No Go zonder reden leer ik niets van.

## Wanneer de stap af is

De [Definition of Done](Bijlagen/03-Definition-of-Done.md) voor de snelle analyse: ik begrijp de eerste kans en de belangrijkste belemmeringen genoeg om te kiezen waar mijn volgende twintig uur heen gaan, ik heb de kandidaat vergeleken met de andere kansen, en de afsluiting op het tabblad Overzicht is ingevuld. Voor dieper onderzoek ligt er een pre-mortem.

## Hoe lang het duurt

Enkele uren per kandidaat. Een naam die snel afvalt kost een uur. Zit ik na een dag nog in fase 2, dan pak ik het [vastloopprotocol](Bijlagen/04-Vastloop-Protocol.md) erbij: meestal ben ik dan aan het verzamelen in plaats van aan het filteren.

De content op Belegger Kees is uitsluitend bedoeld voor educatieve doeleinden en vormt geen persoonlijk beleggingsadvies. Beleggen brengt risico's met zich mee. De waarde van beleggingen kan fluctueren en je kunt je inleg verliezen. Resultaten uit het verleden bieden geen garantie voor de toekomst. Raadpleeg een erkende financieel adviseur voor advies op maat. Belegger Kees is geen geregistreerde beleggingsonderneming bij de AFM.

## Verder lezen

[Analyseproces](README.md) · [Stap 3: Uitgebreid analyseren](03-Uitgebreid-Analyseren.md) · [Hoofdstuk 4: Snelle aandelenanalyse](../02-Manifesto/04-Snelle-Analyse.md) · [No Go checks](Bijlagen/02-NoGo-Checks.md)

---

Bijgewerkt: 21 september 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
