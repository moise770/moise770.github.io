"""Pages « Conseils » : une page par article et par langue, avec leur propre référencement."""
import json, html as H
from articles import ARTICLES

SRC = "/home/claude/sites_demo"
BASE = "https://moiseberrebi.com"
DATE = "2026-11-04"
LOCALE = {"fr": "fr_FR", "he": "he_IL"}

TXT = {
    "fr": {"accueil": "Accueil", "conseils": "Conseils", "autre": "עברית", "cta_t": "Vous voulez un site pour votre commerce ?",
           "cta_p": "Je crée des sites en français et en hébreu pour les commerces de Jérusalem et d'ailleurs. Écrivez-moi : je vous réponds par email ou sur WhatsApp, et je vous prépare une maquette gratuite.",
           "cta_b": "Demander ma maquette gratuite", "lire": "À lire aussi", "metier": "Sites sur mesure à Jérusalem",
           "pied": "Moïse Berrebi · Création de sites pour commerces · Jérusalem", "auteur": "Moïse Berrebi",
           "maj": "Mis à jour le 4 novembre 2026", "marque": "Moïse Berrebi"},
    "he": {"accueil": "דף הבית", "conseils": "טיפים", "autre": "Français", "cta_t": "רוצים אתר לעסק שלכם?",
           "cta_p": "אני בונה אתרים בעברית ובצרפתית לעסקים בירושלים ובכל הארץ. כתבו לי ואענה במייל או בוואטסאפ, עם סקיצה בחינם.",
           "cta_b": "לקבלת סקיצה בחינם", "lire": "עוד מאמרים", "metier": "אתרים בהתאמה אישית בירושלים",
           "pied": "משה מאיז ברבי · בניית אתרים לעסקים · ירושלים", "auteur": "משה מאיז ברבי",
           "maj": "עודכן ב־4 בנובמבר 2026", "marque": "משה מאיז ברבי"},
}

CSS = """* { box-sizing: border-box; }
body { margin: 0; background: var(--ivoire); color: var(--encre); font: 18px/1.7 var(--texte); -webkit-font-smoothing: antialiased; }
h1, h2, h3 { font-family: var(--titre); font-weight: 600; line-height: 1.15; margin: 0; letter-spacing: -0.015em; text-wrap: balance; }
[dir="rtl"] h1, [dir="rtl"] h2, [dir="rtl"] h3 { letter-spacing: 0; }
a { color: var(--bleu); }
:focus-visible { outline: 3px solid var(--bleu); outline-offset: 3px; border-radius: 4px; }
.env { max-width: 760px; margin-inline: auto; padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px)); }
header { background: var(--encre-nuit); color: var(--sur-nuit); }
header .env { max-width: 1180px; display: flex; align-items: center; justify-content: space-between; gap: 16px; min-height: 68px; }
.logo { display: flex; align-items: center; gap: 12px; color: inherit; text-decoration: none; line-height: 1.2; }
.logo svg { width: 36px; height: 36px; flex: none; }
.logo b { font-family: var(--titre); font-weight: 600; }
.logo small { display: block; color: var(--sur-nuit-doux); font-size: 13px; }
.langue { font-weight: 700; text-decoration: none; color: var(--sur-nuit); border: 1px solid rgba(255,255,255,0.2); border-radius: 999px; padding: 6px 14px; white-space: nowrap; }
.fil { font-size: 14.5px; color: var(--doux); margin: 32px 0 14px; }
.fil a { color: var(--doux); }
article h1 { font-size: clamp(32px, 5vw, 46px); }
.date { color: var(--doux); font-size: 14.5px; margin: 12px 0 28px; }
.chapo { font-size: 20px; }
article h2 { font-size: 28px; margin: 44px 0 10px; color: var(--marine); }
article h3 { font-size: 21px; margin: 24px 0 6px; }
article li { margin-bottom: 8px; }
.appel { margin: 56px 0; background: var(--encre-nuit); color: var(--sur-nuit); border-radius: 22px; padding: 30px; display: grid; gap: 12px; }
.appel h2 { font-size: 26px; color: #fff; }
.appel p { margin: 0; color: var(--sur-nuit-doux); }
.bouton { justify-self: start; background: var(--bleu); color: #fff; text-decoration: none; font-weight: 700; border-radius: 999px; padding: 13px 24px; margin-top: 6px; }
.lire { font-size: 24px; margin-bottom: 8px; }
.autres { display: grid; padding: 0; margin: 0; list-style: none; }
.autres a { display: block; border-top: 1px solid var(--trait); padding: 16px 0; text-decoration: none; color: var(--encre); font-weight: 700; }
.autres a:hover { color: var(--bleu); }
footer { background: var(--encre-nuit); margin-top: 64px; }
footer .env { max-width: 1180px; padding-block: 32px; font-size: 14.5px; color: var(--sur-nuit-doux); }
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Rubik:wght@500;600;700&family=Heebo:wght@400;500;700&display=swap">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{style()}
</head>
<body>
<header><div class="env">
  <a class="logo" href="{accueil}"><svg viewBox="200 270 624 560" aria-hidden="true"><path d="M390 340 L 230 512 L 390 684 M634 340 L 794 512 L 634 684" fill="none" stroke="#8fb8f2" stroke-width="64" stroke-linecap="round" stroke-linejoin="round"/><path d="M598 566 C 540 610, 420 590, 330 596 C 230 604, 220 720, 300 760" fill="none" stroke="#8fb8f2" stroke-width="18" stroke-linecap="round" stroke-dasharray="30 26"/><g transform="rotate(32 512 512)"><path d="M512 250 C 532 250, 540 300, 540 330 L 524 780 L 512 812 L 500 780 L 484 330 C 484 300, 492 250, 512 250 Z" fill="#ffffff"/><ellipse cx="512" cy="318" rx="10" ry="34" fill="#0e1f40"/></g><path d="M621 346 C 690 380, 680 500, 598 566" fill="none" stroke="#8fb8f2" stroke-width="18" stroke-linecap="round"/></svg><span><b>{t["marque"]}</b><small>{t["metier"]}</small></span></a>
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
