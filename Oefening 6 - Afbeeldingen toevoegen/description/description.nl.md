
# Afbeeldingen in HTML: Breng je Gerecht tot Leven

Een aantrekkelijke webpagina bevat niet alleen tekst, maar ook afbeeldingen. In HTML worden afbeeldingen ingevoegd met de `img` tag. Deze tag maakt je pagina visueel aantrekkelijker en kan helpen om je verhaal te versterken.

**Belangrijk:**
* De `img` tag wordt gebruikt om afbeeldingen in een HTML-pagina in te voegen.
* Belangrijke attributen van de `img` tag zijn `src` (de bron van de afbeelding) en `alt` (alternatieve tekst voor als de afbeelding niet geladen kan worden).
* De `alt` tekst is ook belangrijk voor toegankelijkheid, omdat het schermlezers helpt om de inhoud van de afbeelding te beschrijven.

## Gegeven
We breiden onze HTML-structuur uit met een afbeelding van het gerecht. De basisstructuur met de toevoeging van de `img` tag ziet er als volgt uit:

* `!DOCTYPE html`
* `html-tag`
* `head`
  * `title`
* `body`
  * `h1`
  * `h2`
  * `p` (alinea's)
  * `img` (afbeelding)
* Afsluitende `html-tag`

## Gevraagd
* Maak een HTML-pagina over het gerecht "Kapsalon".
* Gebruik de elementen uit de basisstructuur.
* Geef de pagina de `title`: "Het Verhaal van Kapsalon".
* In de `body`, voeg een `h1` kop toe met "Kapsalon", een `h2` kop met "De Geschiedenis", en een alinea over de oorsprong van het gerecht.
* Voeg een afbeelding toe van het gerecht Kapsalon. Zorg ervoor dat je de `img` tag gebruikt met de juiste `src` en `alt` attributen.

Bijvoorbeeld:
```
...
        <h1>Kapsalon</h1>
        <h2>De Geschiedenis</h2>
        <p>Het gerecht Kapsalon is ontstaan in Rotterdam en heeft een interessante oorsprong...</p>
        <img src="url_van_je_afbeelding.jpg" alt="Afbeelding van een schotel Kapsalon">
... 
```

{: .callout.callout-info}
>## Tip
>* Gebruik de `img` tag om afbeeldingen toe te voegen. Vergeet niet de `src` te specificeren, waar je de URL van de afbeelding plaatst, en de `alt` voor alternatieve tekst.
