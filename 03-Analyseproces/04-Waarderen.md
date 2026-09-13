# Stap 4. Waarderen

Waarderen is fase 5 van de uitgebreide analyse, en het is de fase waarin mijn verwachtingen een getal worden. Ik reken drie scenario's door, lees het verwachte rendement per jaar af, en bepaal een koopzone: het prijsbereik waarin ik het aandeel aantrekkelijk vind voor mijn eigen afweging. De theorie staat in [hoofdstuk 6](../02-Manifesto/06-DCF-Model.md); dit is de volgorde waarin ik het doe.

## Doel

Per scenario een verwacht intern rendement, een gekozen exit multiple en discount rate met onderbouwing, een koopzone, en het cijfer dat ik het meest moet volgen.

## Wat ik klaarzet

Het ingevulde tabblad Historie en het tabblad Parameters met de historische waarden uit [stap 3](03-Uitgebreid-Analyseren.md). De koersdata gekoppeld op het tabblad Invoer. De historische koers-winstverhouding van het bedrijf over vijf tot tien jaar en de multiples van vergelijkbare bedrijven op dezelfde boekhoudbasis.

## Template en tabblad

`04-Uitgebreide-Analyse.xlsx`, tabbladen Invoer, Parameters, Model, Gevoeligheid en Controles. Het tabblad Model volgt de indeling uit hoofdstuk 6: rij 3 de jaarnummers 0 tot en met 11, rij 4 de kalenderjaren, rij 5 de kasstroom voor de aandeelhouder per jaar, B8 de discount rate, en daaronder de opbouw, de eindwaarde, de contante waarden, het interne rendement en de netto contante waarde.

## Hoe ik het doe

1. **De parameters per scenario.** Op het tabblad Parameters vul ik per jaar 1 tot en met 11 de omzetgroei of de bedrijfsparameters in, de nettowinstmarge, de kasstroomconversie en de verandering van het aantal aandelen, voor een tegenvallend, een midden- en een gunstig scenario. Elk scenario moet intern kloppen: hoge groei hoort bij hoge investeringen en dus een lagere conversie in de eerste jaren.
2. **De discount rate.** Ik kies binnen 8 tot 12 procent op basis van het vertrouwen dat ik in de kasstromen heb, en schrijf op welke risico's die keuze dragen. Meer decimalen maken het niet beter.
3. **De exit P/E.** Ik kijk naar de eigen historische range van het bedrijf, naar sectorgenoten die in jaar 11 op het bedrijf lijken, en naar de groei die ik in jaar 11 nog verwacht. Voor een uitgegroeid bedrijf begin ik bij 12 tot 15, voor een bedrijf dat nog groeit bij 15 tot 20. Daarboven moet ik het kunnen uitleggen.
4. **De Gordon-controle.** Het tabblad Model toont welke P/E de Gordon-formule bij mijn conversie, groei en discount rate impliceert. Ligt mijn exit P/E daar ver boven, dan schrijf ik op welke groei na jaar 11 het verschil rechtvaardigt. Kan ik dat niet, dan is mijn multiple te hoog.
5. **De uitkomst lezen.** Per scenario het interne rendement, het aandeel van de eindwaarde in de waardering, de koersruimte en de korting op de berekende waarde. Het tegenvallende scenario zegt mij het meest: levert dat nog een rendement op dat ik acceptabel vind, dan heb ik een sterke zaak.
6. **De gevoeligheid.** Op het tabblad Gevoeligheid zie ik de waarde per aandeel bij andere multiples, discount rates en groei. Slaat de uitkomst om bij twee punten in de multiple, dan is dat de aanname waar mijn onderzoek naartoe moet.
7. **Omgekeerd rekenen.** Met Doelzoeken op de omzetgroei reken ik terug welke groei bij de huidige koers past, met de andere aannames vast. Zo zie ik of de markt meer of minder inprijst dan het bedrijf historisch heeft laten zien.
8. **De koopzone.** Ik zoek de koers waarbij het middenscenario mijn rendementseis haalt en de koers waarbij het tegenvallende scenario dat doet. Daartussen ligt mijn koopzone; de onderkant is de prijs waarbij ik ook bij tegenvallen tevreden ben. Een vaste korting van 30 procent is geen regel; de zone volgt uit de scenario's.
9. **De controles.** Het tabblad Controles moet overal In orde tonen: eenheid gekozen, aandelen groter dan nul, koers ingevuld, discount rate groter dan de groei, elf perioden, geen lege parameters, nettoschuld niet dubbel afgetrokken.

## Prompts

[Prompt 4, waardering en omgekeerde DCF](../05-Resources/AI-Prompts/prompts-library.md), voor de historische P/E-range, de multiples van vergelijkbare bedrijven en een tweede blik op de ingeprijsde groei. [Prompt 8, DCF-model controleren](../05-Resources/AI-Prompts/prompts-library.md), met mijn parameters als invoer, voor een factcheck van de aannames en een tweede mening over discount rate en exit multiple. Het model bouw ik zelf; AI controleert.

## Checks

Check 5 en check 10, nu volledig. En de vraag achter alle checks: welke ene aanname draagt het meeste gewicht, en valt de hele these om als die fout is?

## Wat ik vastleg

De drie scenario's, de gekozen discount rate en exit P/E met de reden, de koopzone en de rekendatum in het werkboek. In het [universumbestand](05-Universum-Bijhouden.md): koopzone, verwacht rendement bij de huidige koers, het kerncijfer dat ik volg en de datum van de waardering.

## Wanneer de stap af is

Drie scenario's rekenen door zonder foutcellen, de exit P/E en de discount rate zijn onderbouwd, de koopzone staat met datum in het universum, en ik kan in twee zinnen zeggen welke aanname het model draagt.

## Hoe lang het duurt

Een dagdeel als de historie er staat. Het meeste werk zit in de parameters, niet in het rekenen. Blijf ik aan de discount rate schaven, dan is dat een teken dat ik de uitkomst probeer te sturen; dan noteer ik dat en stop ik.

## Verder lezen

[Analyseproces](README.md) · [Stap 5: Universum bijhouden](05-Universum-Bijhouden.md) · [Hoofdstuk 6: DCF, exit multiple en intern rendement](../02-Manifesto/06-DCF-Model.md) · [Templates](../05-Resources/Templates/README.md)

---

Bijgewerkt: 13 september 2026. Auteur: Kees van Wanrooij, Belegger Kees. Status: Openbare werkversie; ik verbeter deze methode door haar te gebruiken en helder uit te leggen.
