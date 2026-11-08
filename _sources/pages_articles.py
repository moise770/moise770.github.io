"""Pages « Conseils » : une page par article et par langue, avec leur propre référencement."""
import json, html as H
from articles import ARTICLES

SRC = "/home/claude/sites_demo"
BASE = "https://moiseberrebi.com"
DATE = "2026-11-04"
LOCALE = {"fr": "fr_FR", "he": "he_IL"}

TXT = {
    "fr": {"accueil": "Accueil", "conseils": "Conseils", "autre": "עברית", "cta_t": "Vous voulez un site pour votre commerce ?",
           "cta_p": "Je crée des sites en français et en hébreu pour les commerces de Jérusalem et d'ailleurs. Laissez votre numéro, je vous rappelle gratuitement.",
           "cta_b": "Être rappelé gratuitement", "lire": "À lire aussi", "metier": "Sites pour commerces · Jérusalem",
           "pied": "Moïse Berrebi · Création de sites pour commerces · Jérusalem", "auteur": "Moïse Berrebi",
           "maj": "Mis à jour le 4 novembre 2026", "marque": "Moïse Berrebi"},
    "he": {"accueil": "דף הבית", "conseils": "טיפים", "autre": "Français", "cta_t": "רוצים אתר לעסק שלכם?",
           "cta_p": "אני בונה אתרים בעברית ובצרפתית לעסקים בירושלים ובכל הארץ. השאירו מספר טלפון ואחזור אליכם בחינם.",
           "cta_b": "שיחה חוזרת בחינם", "lire": "עוד מאמרים", "metier": "אתרים לעסקים · ירושלים",
           "pied": "משה מאיז ברבי · בניית אתרים לעסקים · ירושלים", "auteur": "משה מאיז ברבי",
           "maj": "עודכן ב־4 בנובמבר 2026", "marque": "משה מאיז ברבי"},
}

CSS = """* { box-sizing: border-box; }
body { margin: 0; background: var(--fond); color: var(--encre); font: 18px/1.7 var(--texte); }
h1, h2, h3 { font-family: var(--titre); font-weight: 400; line-height: 1.15; margin: 0; text-wrap: balance; }
a { color: var(--turquoise); }
:focus-visible { outline: 3px solid var(--ocre); outline-offset: 2px; }
.env { max-width: 760px; margin-inline: auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
header { border-bottom: 1px solid var(--trait); background: var(--surface); }
header .env { max-width: 1120px; display: flex; align-items: center; justify-content: space-between; gap: 16px; padding-block: 14px; }
.logo { display: flex; align-items: center; gap: 10px; color: var(--encre); text-decoration: none; line-height: 1.2; }
.logo small { display: block; color: var(--doux); font-size: 13px; }
.carreau { width: 30px; height: 30px; border-radius: 8px; flex: none; background: var(--turquoise) radial-gradient(circle, var(--ocre) 0 4px, transparent 5px); }
.langue { font-weight: 700; text-decoration: none; border: 1px solid var(--trait); border-radius: 999px; padding: 6px 14px; white-space: nowrap; }
.fil { font-size: 14.5px; color: var(--doux); margin: 28px 0 14px; }
.fil a { color: var(--doux); }
article h1 { font-size: clamp(32px, 5vw, 46px); }
.date { color: var(--doux); font-size: 14.5px; margin: 12px 0 28px; }
.chapo { font-size: 20px; }
article h2 { font-size: 28px; margin: 40px 0 10px; color: var(--turquoise); }
article h3 { font-size: 21px; margin: 24px 0 6px; }
article li { margin-bottom: 8px; }
.appel { margin: 48px 0; background: var(--turquoise-fond); border-radius: var(--rayon); padding: 26px; display: grid; gap: 12px; }
.appel h2 { font-size: 26px; }
.appel p { margin: 0; }
.bouton { justify-self: start; background: var(--turquoise); color: #fff; text-decoration: none; font-weight: 700; border-radius: 999px; padding: 12px 22px; }
.lire { font-size: 24px; margin-bottom: 12px; }
.autres { display: grid; gap: 10px; padding: 0; margin: 0; list-style: none; }
.autres a { display: block; background: var(--surface); border: 1px solid var(--trait); border-radius: 12px; padding: 14px 18px; text-decoration: none; color: var(--encre); font-weight: 700; }
.autres a:hover { border-color: var(--turquoise); }
footer { border-top: 1px solid var(--trait); margin-top: 56px; }
footer .env { max-width: 1120px; padding-block: 28px; font-size: 14.5px; color: var(--doux); }
"""


def chemin(slug, lang):
    return ("/he" if lang == "he" else "") + f"/conseils/{slug}/"


def style():
    src = open(f"{SRC}/mon-site/site.html").read()
    racine = src[src.index(":root {"):src.index("* { box-sizing")]
    return "<style>\n" + racine + CSS + "</style>"


def page(a, lang):
    t, x = TXT[lang], a[lang]
    autre = "he" if lang == "fr" else "fr"
    d = "rtl" if lang == "he" else "ltr"
    url = BASE + chemin(a["slug"], lang)
    accueil = "/he/" if lang == "he" else "/"
    ld = [{"@context": "https://schema.org", "@type": "Article", "headline": x["titre"], "description": x["desc"],
           "inLanguage": lang, "datePublished": DATE, "dateModified": DATE, "mainEntityOfPage": url,
           "image": BASE + "/og.png",
           "author": {"@type": "Person", "name": "Moïse Berrebi", "url": BASE + "/"},
           "publisher": {"@type": "Organization", "name": "Moïse Berrebi",
                         "logo": {"@type": "ImageObject", "url": BASE + "/apple-touch-icon.png"}}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": t["accueil"], "item": BASE + accueil},
              {"@type": "ListItem", "position": 2, "name": x["titre"], "item": url}]}]
    autres = "\n".join(f'    <li><a href="{chemin(b["slug"], lang)}">{H.escape(b[lang]["titre"])}</a></li>'
                       for b in ARTICLES if b is not a)
    titre = H.escape(x["titre"])
    desc = H.escape(x["desc"], quote=True)
    fr_url, he_url = BASE + chemin(a["slug"], "fr"), BASE + chemin(a["slug"], "he")
    return f"""<!doctype html>
<html lang="{lang}" dir="{d}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titre} | Moïse Berrebi</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="fr" href="{fr_url}">
<link rel="alternate" hreflang="he" href="{he_url}">
<link rel="alternate" hreflang="x-default" href="{fr_url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Moïse Berrebi">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{titre}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{BASE}/og.png">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Secular+One&family=Heebo:wght@400;500;700&display=swap">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{style()}
</head>
<body>
<header><div class="env">
  <a class="logo" href="{accueil}"><span class="carreau" aria-hidden="true"></span><span><b>{t["marque"]}</b><small>{t["metier"]}</small></span></a>
  <a class="langue" href="{chemin(a["slug"], autre)}" hreflang="{autre}" lang="{autre}">{t["autre"]}</a>
</div></header>
<main class="env">
  <nav class="fil" aria-label="{t["accueil"]}"><a href="{accueil}">{t["accueil"]}</a> › <a href="{accueil}#conseils">{t["conseils"]}</a></nav>
  <article>
    <h1>{titre}</h1>
    <p class="date">{t["auteur"]} · {t["maj"]}</p>
{x["corps"].strip()}
  </article>
  <section class="appel">
    <h2>{t["cta_t"]}</h2>
    <p>{t["cta_p"]}</p>
    <a class="bouton" href="{accueil}#contact">{t["cta_b"]}</a>
  </section>
  <h2 class="lire">{t["lire"]}</h2>
  <ul class="autres">
{autres}
  </ul>
</main>
<footer><div class="env">{t["pied"]}</div></footer>
</body>
</html>
"""
