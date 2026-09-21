# Stap 3. Uitgebreid analyseren

In de uitgebreide analyse wil ik een bedrijf zo goed begrijpen dat ik mijn verwachtingen kan uitleggen en verdedigen. Ik werk in negen fasen, van documenten verzamelen tot rapportage. De waardering zelf is fase 5; die staat als [stap 4](04-Waarderen.md) apart uitgewerkt, omdat het rekenwerk een eigen werkwijze heeft. Deze pagina gaat over de andere acht fasen.

## Doel

Een dossier waarin het parametermodel, de markt, de risico's, de financiering en het bestuur zo beschreven zijn dat ik de kans kan vergelijken met mijn andere kansen en kan uitleggen wat mijn verwachting zou veranderen.

## Wat ik klaarzet

De [voorbereiding](00-Voorbereiden.md) met de volledige bronnenset: jaarverslagen van de laatste vijf tot tien jaar, kwartaal- of halfjaarberichten van de laatste twee jaar, de calls van de laatste vier kwartalen, de presentaties, het beloningsverslag en de openbare insidertransacties. De kopie `Bedrijfsnaam-Uitgebreide-Analyse.xlsx`. De pre-mortem uit stap 2, want die bepaalt waar ik het eerst naar kijk.

## Template en tabblad

`04-Uitgebreide-Analyse.xlsx`:

| Tabblad | Fase | Wat erop staat |
| --- | --- | --- |
| Invoer | 1 en 4 | Bedrijf, boekhoudstandaard, eenheid, koersdata, aandelen, discount rate, exit P/E, actief scenario |
| EV en kapitaalstructuur | 4 | Wat wel en niet meetelt als cash en schuld, leaseverplichtingen, ondernemingswaarde met en zonder leases |
| Historie | 4 | Tien jaar en acht kwartalen gerapporteerde cijfers, met afgeleide marges, kasstroomconversie en groei |
| Parameters | 2 en 4 | Het parametermodel per scenario en per jaar |
| Model | 5 | De berekening, zie stap 4 |
| Gevoeligheid | 5 | Waarde per aandeel bij andere multiples, discount rates en groei |
| Rode vlaggen | 6 | De controlelijst boekhouding, bestuur, balans, bedrijfsvoering en waardering |
| Analisten | 3 en 7 | Wie het aandeel volgt, wat ze vragen, wat ze niet vragen |
| Technisch en instap | 8 | Weekgrafiek, Stoch RSI, 200-weeks gemiddelde, zones, koopzone |
| Controles | alle | Eenheden, schuld niet dubbel, aandelen, ontbrekende waarden, de vaste rekencontroles |

## Hoe ik de fasen doe

1. **Documenten verzamelen.** Ik maak een bronnenlijst met publicatiedatum, verslagperiode, vindplaats en het onderwerp waarvoor ik de bron gebruik. Een samenvatting behandel ik niet alsof ik het document zelf heb gelezen.
2. **Het bedrijfsmodel.** Ik werk het parametermodel uit vanuit het bedrijf en zoek per parameter de historie in de jaarverslagen. Ik let op de samenhang: meer klanten kan een lagere gemiddelde opbrengst betekenen, nieuwe vestigingen kunnen bestaande vestigingen raken. Dit vult het tabblad Parameters met de historische waarden en de eerste verwachting.
3. **Sector, concurrentie en analisten.** Concurrenten, marktaandelen, toetreders, klantgedrag. Daarna de analisten: wie volgt het aandeel, welke achtergrond hebben ze, welke vragen stellen ze in de calls en welke niet. Dit vult het tabblad Analisten.
4. **Het financiële model.** Ik voer tien jaar cijfers in op het tabblad Historie, vanuit de jaarverslagen en niet vanuit een dataleverancier. Op EV en kapitaalstructuur bepaal ik wat meetelt als cash en schuld, met de leaseverplichtingen apart. Uit de historie lees ik de kasstroomconversie af en zie ik wat die heeft bepaald. [Hoofdstuk 6](../02-Manifesto/06-DCF-Model.md) zegt welke regels ik uit de jaarrekening haal en waar IFRS en US GAAP verschillen.
5. **Waardering en vergelijking.** Zie [stap 4](04-Waarderen.md).
6. **Risico en rode vlaggen.** Ik loop de lijst op het tabblad Rode vlaggen af en noteer bij elk punt wat ik vond, ook als het niets is. De bear case uit stap 2 verbind ik hier aan de cijfers, de financiering en de concurrentiepositie. Eén ernstig financieringsprobleem weegt zwaarder dan drie kleine onzekerheden.
7. **Management en taalgebruik.** Ik vergelijk beloofd en gerealiseerd over vijf jaar in een tabel, beoordeel de kapitaalallocatie, en lees vier opeenvolgende calls van dezelfde spreker op verschuivingen: van concreet naar algemeen, een onderwerp dat verdwijnt, een maatstaf die ontbreekt. Een observatie krijgt citaat, vindplaats en de vraag die hij bij mij oproept.
8. **Voorwaarden voor mijn besluit.** Ik schrijf op bij welke combinatie van prijs, verwacht rendement en risico ik het aandeel aantrekkelijk vind, wat mijn verwachting zou veranderen, en welk kerncijfer ik ga volgen. Op het tabblad Technisch en instap plaats ik de koers in de weekgrafiek en noteer ik zones. Past de prijs niet, dan gaat het dossier naar de watchlist.
9. **Rapportage.** Zie [stap 7](07-Rapporteren-Publiceren.md).

## Prompts

Uit [de promptbibliotheek](../05-Resources/AI-Prompts/prompts-library.md): 2 businessmodel en parameters bij fase 2, 3 markt en concurrenten bij fase 3, 9 analisten online onderzoek en 10 NLP-analyse van één analist bij fase 3 en 7, 6 management bij fase 7, 8 DCF-model controleren bij fase 5, en 12 onderzoeksrapport voorbereiden bij fase 9. De zes cijfers die mijn waardering dragen controleer ik altijd zelf: omzet, winst, vrije kasstroom, koers, aantal aandelen en nettoschuld.

## Checks

Alle zestien opnieuw, maar nu met bewijs. Check 10 gaat van de verkorte naar de volledige versie. De rode-vlaggenlijst op het tabblad is de uitwerking van check 6, 7 en 8 en van vraag 15.

## Wat ik vastleg

Het werkboek, de bronnenlijst en mijn notities in de werkmap. In het [universumbestand](05-Universum-Bijhouden.md) na elke fase de stand: fase in onderzoek, belangrijkste open vraag, volgende actie. Na fase 8 de koopzone, het verwachte rendement en het controlesignaal.

## Wanneer de stap af is

De tabel in de [Definition of Done](Bijlagen/03-Definition-of-Done.md) voor de uitgebreide analyse: bronnen bekend, parameters beschreven, markt onderzocht, model controleerbaar, waardering uitgelegd, risico's beschreven, bestuur bekeken, afweging vergeleken, en ik kan uitleggen waarom ik tot deze afweging kom en wat haar kan veranderen. Een dossier kan klaar zijn voor mijn huidige afweging en later opnieuw onderzoek nodig hebben.

## Hoe lang het duurt

Ongeveer twintig uur, soms aanzienlijk meer. Ik verdeel het over sessies met elk een eigen incheck. Heb ik na vijftig uur nog een vraag die de afweging bepaalt, dan mag ik doorgaan; heb ik na vijftig uur alleen nog vragen die de afweging niet veranderen, dan is het dossier af.

De content op Belegger Kees is uitsluitend bedoeld voor educatieve doeleinden en vormt geen persoonlijk beleggingsadvies. Beleggen brengt risico's met zich mee. De waarde van beleggingen kan fluctueren en je kunt je inleg verliezen. Resultaten uit het verleden bieden geen garantie voor de toekomst. Raadpleeg een erkende financieel adviseur voor advies op maat. Belegger Kees is geen geregistreerde beleggingsonderneming bij de AFM.

## Verder lezen

[Analyseproces](README.md) · [Stap 4: Waarderen](04-Waarderen.md) · [Hoofdstuk 5: Uitgebreide aandelenanalyse](../02-Manifesto/05-Uitgebreide-Analyse.md) · [Analistenonderzoek](../05-Resources/Analistenonderzoek.md)

---

Bijgewerkt: 21 september 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
