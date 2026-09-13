# Templates: vijf Excel-werkboeken en twee Word-sjablonen

Dit zijn de bestanden waarin ik mijn methode uitvoer. Elk Excel-werkboek begint met een tabblad Lees mij dat zegt waar het bestand voor is, hoe je het gebruikt en wat de kleuren betekenen. De uitleg staat daar, niet boven de tabellen, zodat alleen de kopregel vastgezet hoeft te zijn.

Ik kopieer een template naar [mijn werkmap](../../04-Onderzoek/Work-in-Progress/README.md), geef de kopie de naam van het bedrijf of de ronde, en vul die kopie in. De templates hier blijven leeg.

## De bestanden

| Bestand | Stap | Wat erin zit | Staat |
| --- | --- | --- | --- |
| [01-Universum.xlsx](01-Universum.xlsx) | [Stap 5](../../03-Analyseproces/05-Universum-Bijhouden.md) | Eén rij per bedrijf met onderzoeksfase, reden om te volgen, gekoppelde koersdata, een mini-waardering en de koopzone bij mijn rendementseis; een overzicht met tellingen en signalen; een onderhoudslijst | Werkversie, formules gecontroleerd |
| [02-Screening.xlsx](02-Screening.xlsx) | [Stap 1](../../03-Analyseproces/01-Screenen.md) | De ronde met incheck en uitkomst per universum; de kandidatenlijst; de vergelijking van bedrijven per industrie; de acht universums en drie landenlijsten uit de [screeners](../Screeners/screeners.md) | Werkversie, formules gecontroleerd |
| [03-Snelle-Analyse.xlsx](03-Snelle-Analyse.xlsx) | [Stap 2](../../03-Analyseproces/02-Snel-Analyseren.md) | De zes fasen van de snelle analyse, de zestien checks, de verkorte omgekeerde DCF en de pre-mortem | Werkversie, formules gecontroleerd |
| [04-Uitgebreide-Analyse.xlsx](04-Uitgebreide-Analyse.xlsx) | [Stap 3](../../03-Analyseproces/03-Uitgebreid-Analyseren.md) en [4](../../03-Analyseproces/04-Waarderen.md) | Historie, ondernemingswaarde, drie scenario's, het model uit hoofdstuk 6.7, gevoeligheid, rode vlaggen, analisten, technisch en instap, controles | Werkversie, formules gecontroleerd |
| [05-Portefeuille.xlsx](05-Portefeuille.xlsx) | [Stap 6](../../03-Analyseproces/06-Kopen-Aanhouden-Verkopen.md) | Posities met these, verkoopregel en signalen; transacties; cash en inleg | Werkversie, formules gecontroleerd |
| [Blogpost.docx](Blogpost.docx) | [Stap 7](../../03-Analyseproces/07-Rapporteren-Publiceren.md) | De korte aandelenanalyse: aanleiding, verdienmodel, cijfers, parametermodel, zorgen, open vraag, vraag aan de lezer, positie | Werkversie |
| [Onderzoeksrapport.docx](Onderzoeksrapport.docx) | [Stap 7](../../03-Analyseproces/07-Rapporteren-Publiceren.md) | De acht hoofdstukken uit [hoofdstuk 9](../../02-Manifesto/09-Rapportage.md), een correctietabel en de publicatiecontrole | Werkversie |

Werkversie betekent: de formules zijn in Excel doorgerekend en gecontroleerd met testcijfers, maar de bestanden zijn nog niet in een echte doorloop van de methode gebruikt. De snelle en de uitgebreide analyse tonen de echte jaartallen, zodat je bij elke kolom ziet over welk jaar het gaat. Ik verbeter ze aan de hand van die doorlopen, te beginnen met een uitgewerkt voorbeeld in mijn werkmap. Technische analyse is een tabblad in de uitgebreide analyse geworden; een apart bestand voor leren en begeleiding is er niet meer.

## Wat alle werkboeken gemeen hebben

Lichtblauw is een invoercel, geen kleur is een formule en lichtgeel is een controlecel die In orde toont of een melding geeft. Grijs is een kopregel. Alleen de kopregel staat vast; de uitleg staat op Lees mij.

Tekstcellen waarin ik drie tot vijf zinnen schrijf, zoals een antwoord, een reden of een these, zijn breed en hebben tekstterugloop. Ze groeien mee als ik meer schrijf.

Koers, marktkapitalisatie en koers-winstverhouding zijn invoercellen die ik zelf koppel aan het gegevenstype Aandelen van Excel. Lees mij legt in drie stappen uit hoe. Alle formules gebruiken die cellen, dus zodra ze gekoppeld zijn rekent het werkboek met actuele koersen. Werkt het gegevenstype niet, dan vul ik de cellen met de hand en zet ik de peildatum ernaast.

De bedragen staan in de rapportagevaluta van het bedrijf en in de eenheid die ik op het invoertabblad kies, duizenden of miljoenen. Het aantal aandelen staat in dezelfde eenheid, zodat winst per aandeel vanzelf klopt.

## Het model in de uitgebreide analyse

Het tabblad Model volgt de indeling uit [hoofdstuk 6.7](../../02-Manifesto/06-DCF-Model.md): rij 3 de jaarnummers 0 tot en met 11, rij 4 de kalenderjaren, rij 5 de kasstroom voor de aandeelhouder per jaar, B8 de discount rate, B9 het interne rendement met IR en B10 de netto contante waarde met NHW. Daaronder staan de opbouw per jaar, de eindwaarde als exit P/E op de winst van jaar 11, de contante waarden, de koersruimte en de korting, de Gordon-controle en de drie scenario's naast elkaar.

Het tabblad Controles bevat de vaste rekencontroles uit hoofdstuk 6: de reeks van min 100, tien keer 0 en 200 geeft 6,50 procent, drie keer je geld in tien jaar is 11,61 procent, en Gordon met nettowinst 10, conversie 0,6, groei 2 procent en discount rate 10 procent geeft een eindwaarde van 76,5 en een P/E van 7,65. Wijzig die rijen niet; ze laten zien dat het werkboek rekent zoals het hoofdstuk zegt.

De koopzone volgt uit de scenario's: de onderkant is de koers waarbij het tegenvallende scenario mijn rendementseis haalt, de bovenkant de koers waarbij het middenscenario dat doet. Het tabblad Technisch en instap neemt die twee getallen over en laat mij daar mijn eigen afweging naast zetten.

## Werk en controle

Ingevulde versies blijven in [de werkmap](../../04-Onderzoek/Work-in-Progress/README.md), die zichzelf buiten Git houdt. Alleen een gecontroleerde, bewust gekozen versie gaat naar een openbaar dossier in [Onderzoek](../../04-Onderzoek/README.md). Ik publiceer geen lokale bestandspaden, posities uit het portefeuillebestand of gegevens van anderen.

Een werkboek dat rekent is nog geen goede analyse. De formules controleren de rekenkunde; de aannames, de bronnen en de conclusie controleer ik zelf. Vind je een fout in een template, dan hoor ik dat graag via de [community](../../06-Community/README.md).

## Verder lezen

[Resources](../README.md) · [Analyseproces](../../03-Analyseproces/README.md) · [De Belegger Kees Methode](../../README.md) · [Wanneer een stap voldoende is](../../03-Analyseproces/Bijlagen/03-Definition-of-Done.md)

---

Bijgewerkt: 13 september 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
