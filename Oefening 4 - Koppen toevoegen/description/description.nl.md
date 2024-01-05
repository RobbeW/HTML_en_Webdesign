
# Koppen in HTML: Leren van Boeken en Kranten

Net als de hoofdstuktitels in een boek of de koppen in een krant, gebruikt een webpagina koppen om de inhoud te organiseren en de leesbaarheid te verbeteren. In HTML worden deze koppen gecreëerd met `h1`, `h2`, `h3`, enzovoort.

**Belangrijk:**
* Een `title` in de `head` van een HTML-pagina is anders dan een kop. De `title` verschijnt in de titelbalk van de browser of op het tabblad en wordt gebruikt door zoekmachines, maar is niet direct zichtbaar op de webpagina.
* Koppen (`h1`, `h2`, `h3`, ...) zijn zichtbaar op de webpagina en functioneren zoals de koppen in een krant of de titels van hoofdstukken in een boek. Ze helpen de inhoud te structureren.
* `h1` is de hoofdkop en is meestal het grootst, vergelijkbaar met een hoofdstuktitel in een boek of de hoofdkop van een krantenartikel. `h2`, `h3`, enzovoort, zijn subkoppen, vergelijkbaar met subtitels, en worden gebruikt voor subsecties. De grootte en het belang nemen af naarmate het nummer toeneemt.

## Gegeven
Met deze kennis van koppen kunnen we een gestructureerde webpagina maken. Onze basisstructuur breiden we nu uit met koppen in de `body`:

* `!DOCTYPE html`
* `html-tag`
* `head`
  * `title`
* `body`
  * `h1`
  * `h2`
* Afsluitende `html-tag`

## Gevraagd
* Maak een HTML-pagina over jouw favoriete gerecht.
* Gebruik de elementen uit de basisstructuur.
* Geef de pagina de `title`: Mijn Favoriete Gerecht. Zet dit in de `head` sectie, bijvoorbeeld `<title>Mijn Favoriete Gerecht</title>`.
* Gebruik de juiste openingstags (`<tag>`) en sluitingstags (`</tag>`).
* In de `body`, voeg een `h1` kop toe met de naam van het gerecht en een `h2` kop met een subtitel, bijvoorbeeld "Waarom dit mijn favoriet is".

Bijvoorbeeld:
```
...
    <body>
        <h1>Vegetarisch Kapsalon</h1>
        <h2>Waarom dit mijn favoriet is</h2>
    </body>
... 
```

{: .callout.callout-info}
>## Tip
>* Gebruik `h1` voor de hoofdtitel en `h2` voor subtitels op je pagina, net zoals in een boek of krant. Dit helpt de structuur en leesbaarheid van je pagina te verbeteren.
