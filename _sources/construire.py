"""Construit les pages publiées de moise770.github.io à partir des sources des artifacts."""
import json, os, re
from playwright.sync_api import sync_playwright

SRC = "/home/claude/sites_demo"
DEST = "/home/claude/moise770.github.io"
BASE = "https://moise770.github.io"

META = {
    "fr": ("Création de sites pour commerces à Jérusalem, en français et en hébreu | Moïse Berrebi",
           "Le site de votre commerce en français et en hébreu, visible sur Google Maps, avec WhatsApp et prise de rendez-vous. Vitrine, Vitrine + ou boutique en ligne, en ligne en une semaine. Jérusalem, Israël et France.",
           "fr_FR", "/"),
    "he": ("בניית אתרים לעסקים בירושלים, בעברית ובצרפתית | משה מאיז ברבי",
           "האתר של העסק שלכם בעברית ובצרפתית, מופיע בגוגל מפות, עם וואטסאפ וקביעת תורים. אתר תדמית או חנות אונליין, באוויר תוך שבוע. ירושלים, ישראל וצרפת.",
           "he_IL", "/he/"),
}

def jsonld(lang):
    d = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": "Moïse Berrebi — Création de sites pour commerces" if lang == "fr" else "משה מאיז ברבי — בניית אתרים לעסקים",
        "url": BASE + META[lang][3], "image": BASE + "/og.png",
        "description": META[lang][1],
        "address": {"@type": "PostalAddress", "addressLocality": "Jérusalem" if lang == "fr" else "ירושלים", "addressCountry": "IL"},
        "areaServed": [{"@type": "City", "name": "Jerusalem"}, {"@type": "Country", "name": "Israel"}, {"@type": "Country", "name": "France"}],
        "availableLanguage": ["fr", "he"],
        "serviceType": ["Création de sites internet", "Boutique en ligne", "Référencement local Google Maps"],
    }
    return json.dumps(d, ensure_ascii=False)

def tete(lang):
    titre, desc, locale, chemin = META[lang]
    autre = "he" if lang == "fr" else "fr"
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titre}</title>
<meta name="description" content="{desc}">
<meta name="google-site-verification" content="ocGXDJN6NkBjCIQqLeDsyyLvTQ0OhC97x3OOsmQPNXs">
<link rel="canonical" href="{BASE}{chemin}">
<link rel="alternate" hreflang="fr" href="{BASE}/">
<link rel="alternate" hreflang="he" href="{BASE}/he/">
<link rel="alternate" hreflang="x-default" href="{BASE}/">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}{chemin}">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{locale}">
<meta property="og:locale:alternate" content="{META[autre][2]}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.png">
<script type="application/ld+json">{jsonld(lang)}</script>'''

def corps_et_style(src):
    body = open(src).read()
    i = body.index("<style>"); j = body.index("</style>") + 8
    avant = body[:i]
    liens = "\n".join(l for l in avant.splitlines() if l.startswith("<link"))
    return liens, body[i:j], body[j:].strip()

def page_site(lang):
    liens, style, corps = corps_et_style(f"{SRC}/mon-site/site.html")
    d = "rtl" if lang == "he" else "ltr"
    return f'<!doctype html>\n<html lang="{lang}" dir="{d}">\n<head>\n{tete(lang)}\n{liens}\n{style}\n</head>\n<body>\n{corps}\n</body>\n</html>\n'

def page_demo(src, desc):
    liens, style, corps = corps_et_style(src)
    titre = re.search(r"<title>(.*?)</title>", open(src).read()).group(1)
    return f'<!doctype html>\n<html lang="fr" dir="ltr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<title>{titre}</title>\n<meta name="description" content="{desc}">\n<meta property="og:image" content="{BASE}/og.png">\n<link rel="icon" href="/favicon.png">\n{liens}\n{style}\n</head>\n<body>\n{corps}\n</body>\n</html>\n'

def main():
    os.makedirs(f"{DEST}/he", exist_ok=True)
    open(f"{DEST}/index.html", "w").write(page_site("fr"))
    # Version hébraïque pré-rendue : le texte hébreu est déjà dans le HTML, lisible par Google.
    brut = f"{DEST}/he/index.html"
    open(brut, "w").write(page_site("he"))
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto("file://" + brut); pg.wait_for_timeout(300)
        html = pg.evaluate("document.documentElement.outerHTML")
        b.close()
    open(brut, "w").write("<!doctype html>\n" + html + "\n")
    open(f"{DEST}/coiffure/index.html", "w").write(page_demo(f"{SRC}/coiffure/coiffure.html", "Atelier Shira, salon de coiffure à Netanya : exemple de site Vitrine + avec prise de rendez-vous, réalisé par Moïse Berrebi."))
    open(f"{DEST}/boutique/index.html", "w").write(page_demo(f"{SRC}/boutique/boutique.html", "Atelier Or, judaïca à Jérusalem : exemple de boutique en ligne bilingue avec panier, réalisé par Moïse Berrebi."))
    urls = ["/", "/he/", "/demo-comptoir/", "/coiffure/", "/boutique/"]
    open(f"{DEST}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"  <url><loc>{BASE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    open(f"{DEST}/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")

if __name__ == "__main__":
    main()
