
# Geordende Lijsten in HTML: Stap-voor-stap Recepten

Naast tekst en afbeeldingen, zijn geordende lijsten (`ol`) een cruciaal element voor het structureren van inhoud op een webpagina, vooral wanneer volgorde belangrijk is, zoals in recepten. In HTML wordt een geordende lijst gebruikt om items in een specifieke volgorde weer te geven, bijvoorbeeld de stappen van een recept.

**Belangrijk:**
* Een geordende lijst (`ol`) toont items in een numerieke volgorde.
* Elk item in de lijst wordt aangeduid met een `li` (list item) tag.
* Geordende lijsten zijn ideaal voor recepten, instructies, of elke andere content waar de volgorde van stappen of items belangrijk is.

## Gegeven
Naast een afbeelding van het gerecht, voegen we nu een geordende lijst toe om het recept stap voor stap te beschrijven. De uitgebreide basisstructuur ziet er nu als volgt uit:

* `!DOCTYPE html`
* `html-tag`
* `head`
  * `title`
* `body`
  * `h1`
  * `h2`
  * `p` (alinea's)
  * `img` (afbeelding)
  * `ol` (geordende lijst)
* Afsluitende `html-tag`

## Gevraagd
* Maak een HTML-pagina over het gerecht "Vegetarisch Kapsalon".
* Gebruik de elementen uit de basisstructuur.
* Geef de pagina de `title`: "Het Verhaal van Kapsalon".
* In de `body`, voeg een `h1` kop toe met "Kapsalon", een `h2` kop met "Het Recept", en een alinea over de oorsprong van het gerecht.
* Voeg een afbeelding toe van het gerecht Kapsalon.
* Voeg een geordende lijst toe met de stappen om het gerecht te maken.

Bijvoorbeeld:
```
...
        <ol>
            <li>Snijd de aardappelen in frieten en bak ze.</li>
            <li>Bak de veggie shoarma in een aparte pan.</li>
...
```

Het volledige **geordende lijst** ziet er als volgt uit: 

```
1. Snijd de aardappelen in frieten en bak ze.
2. Bak de veggie shoarma in een aparte pan.
3. Leg de gebakken frieten in een schaal.
4. Voeg de gebakken veggie shoarma toe bovenop de frieten.
5. Bedek het geheel met kaas en laat het smelten in de oven.
6. Voeg als laatste de salade toe en serveer.

```

{: .callout.callout-info}
>## Tip
>* Gebruik de `ol` tag voor een geordende lijst en `li` voor elk item in de lijst. Dit helpt bij het duidelijk weergeven van stappen of geordende informatie.
