from validators.checks import HtmlSuite, TestSuite, ChecklistItem

def create_suites(content: str) -> list[TestSuite]:
    html = HtmlSuite(content)

    # Controleer de basisstructuur van de HTML-pagina
    el_doctype = html.has_doctype()
    el_html = html.element("html")
    el_head = el_html.get_child("head")
    #el_title = el_head.get_child("title")
    el_body = el_html.get_child("body")

    # Voeg de controles toe
    html.make_item("De webpagina heeft een doctype", el_doctype)

    html.make_item("Binnen de <html> tag bevindt zich de <head> tag.",
                   el_head.exists())

    #html.make_item("Binnen de <head> tag bevindt zich de <title> tag.",
                   #el_title.exists())

    #html.make_item("De <title> tag heeft inhoud.",
                   #el_title.has_content())

    html.make_item("Binnen de <html> tag bevindt zich de <body> tag.",
                   el_body.exists())

    # Nieuwe controle voor "Hallo Wereld" in de body
    html.make_item("De <body> tag bevat de tekst 'Hallo Wereld'",
                   el_body.contains_text("Hallo Wereld"))

    return [html]
