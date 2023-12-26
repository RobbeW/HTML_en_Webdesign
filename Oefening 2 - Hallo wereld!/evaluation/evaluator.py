from validators.checks import HtmlSuite, TestSuite, ChecklistItem

def create_suites(content: str) -> list[TestSuite]:
    html = HtmlSuite(content)

    # Basisstructuur van de HTML-pagina
    el_doctype = html.has_doctype()
    el_html = html.element("html")
    el_body = el_html.get_child("body")

    # Controles toevoegen
    html.make_item("De webpagina heeft een doctype", el_doctype)

    html.make_item("De webpagina heeft een <html> tag", el_html.exists())

    html.make_item("Binnen de <html> tag bevindt zich de <body> tag.",
                   el_body.exists())

    # Controle voor "Hallo Wereld" in de body
    body_content = el_body.get_content() if el_body else ""
    contains_hello_world = "Hallo Wereld" in body_content
    html.make_item("De <body> tag bevat de tekst 'Hallo Wereld'", contains_hello_world)

    return [html]
