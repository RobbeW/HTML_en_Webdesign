
# Ongeordende Lijsten in HTML: Boodschappenlijstje voor je Gerecht

Een ongeordende lijst (`ul`) in HTML is ideaal voor het weergeven van items waarvan de volgorde niet van belang is, zoals een boodschappenlijstje. Deze lijsten worden vaak gebruikt om items op te sommen zonder een specifieke volgorde, en elk item wordt gemarkeerd met een bullet point.

**Belangrijk:**
* Een ongeordende lijst (`ul`) wordt gebruikt om een lijst van items weer te geven zonder een specifieke volgorde.
* Net als bij geordende lijsten, wordt elk item in een ongeordende lijst aangeduid met een `li` (list item) tag.
* Ongeordende lijsten zijn perfect voor boodschappenlijstjes, to-do lijsten, of elke andere content waarbij de volgorde van de items niet uitmaakt.

## Gegeven
Naast de geordende lijst voor het recept, voegen we nu een ongeordende lijst toe voor het boodschappenlijstje van het gerecht "Vegetarisch Kapsalon". De uitgebreide basisstructuur ziet er nu als volgt uit:

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
  * `ul` (ongeordende lijst)
* Afsluitende `html-tag`

## Gevraagd
* Maak een HTML-pagina over het gerecht "Vegetarisch Kapsalon".
* Gebruik de elementen uit de basisstructuur.
* Geef de pagina de `title`: "Het Verhaal van Kapsalon".
* In de `body`, voeg een `h1` kop toe met "Kapsalon" en een `h2` kop met "Het Recept".
* Voeg een afbeelding toe van het gerecht Kapsalon.
* Voeg een **geordende lijst** toe met de stappen om het gerecht te maken.
* Voeg een **ongeordende lijst** toe met de ingrediënten voor het gerecht. Dit is het boodschappenlijstje.

Bijvoorbeeld:
```
...
        <ul>
            <li>Aardappelen</li>
            <li>Veggie shoarma</li>

...
```

De volledige **ongeordende lijst** ziet er als volgt uit: 

```
- Aardappelen
- Veggie shoarma
- Kaas
- Salade
- Olijfolie
- Kruiden naar keuze
```

{: .callout.callout-info}
>## Tip
>* Gebruik de `ul` tag voor een ongeordende lijst en `li` voor elk item in de lijst. Dit is ideaal voor lijsten waar de volgorde van de items niet belangrijk is.
