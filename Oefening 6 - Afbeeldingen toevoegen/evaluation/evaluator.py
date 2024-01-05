from validators.checks import HtmlSuite, TestSuite, ChecklistItem

def create_suites(content: str) -> list[TestSuite]:
    html = HtmlSuite(content)

    el_html = html.element("html")
    el_head = el_html.get_child("head")
    el_title = el_head.get_child("title")
    el_body = el_html.get_child("body")
    el_h1 = el_body.get_child("h1")
    el_h2 = el_body.get_child("h2")
    el_p = el_body.get_child("p")
    el_img = el_body.get_child("img")

    # Basisstructuur controles
    html.make_item("De webpagina heeft een doctype", html.has_doctype())

    html.make_item("Binnen de <html> tag bevindt zich de <head> tag.",
                   el_head.exists())

    html.make_item("Binnen de <head> tag bevindt zich de <title> tag.",
                   el_title.exists())

    html.make_item("Binnen de <html> tag bevindt zich de <body> tag.",
                   el_body.exists())

    # Controles voor h1, h2, en p tags
    html.make_item("Binnen de <body> tag bevindt zich de <h1> tag.",
                   el_h1.exists())

    html.make_item("Binnen de <body> tag bevindt zich de <h2> tag.",
                   el_h2.exists())

    html.make_item("Binnen de <body> tag bevindt zich minstens één <p> tag (alinea).",
                   el_p.exists())

    # Nieuwe controle voor img tag
    html.make_item("Binnen de <body> tag bevindt zich de <img> tag.",
                   el_img.exists())

    return [html]
