"""Pages de l'application Ivrit : support, conditions d'utilisation et confidentialité (exigées par l'App Store)."""
import html as H
from pages_articles import style

BASE = "https://moiseberrebi.com"
MAJ = "18 novembre 2026"
CONTACT = "moscheberrebi@gmail.com"

CSS_IVRIT = """<style>
.carte { border: 1px solid var(--trait); border-radius: 16px; padding: 18px 22px; margin: 18px 0; }
.carte p { margin: 6px 0; }
.liens { display: flex; flex-wrap: wrap; gap: 10px 22px; padding: 0; list-style: none; margin: 28px 0 0; }
dt { font-weight: 700; margin-top: 18px; }
dd { margin: 4px 0 0; }
</style>"""

PAGES = {
    "": {
        "titre": "Ivrit — aide et contact",
        "desc": "Aide et contact pour Ivrit, l'application pour apprendre l'hébreu en lisant des textes sur la vie en Israël.",
        "corps": f"""
<p class="chapo">Ivrit t'apprend l'hébreu en lisant de courts textes sur la vie en Israël, de l'alphabet jusqu'au niveau Hé (6 000 mots). Tu expliques le texte avec tes mots, Ivrit repère ceux qui t'ont échappé et te les fait réviser au bon moment.</p>

<div class="carte">
  <p><strong>Une question, un souci, une idée ?</strong></p>
  <p>Écris à <a href="mailto:{CONTACT}?subject=Ivrit">{CONTACT}</a>. Je réponds en général sous 48 heures, en français ou en hébreu.</p>
</div>

<h2>Bien utiliser Ivrit</h2>
<dl>
  <dt>Un entraînement, comment ça se passe ?</dt>
  <dd>Tu lis (et écoutes) un court texte, tu touches les mots qui te bloquent pour voir leur traduction, puis tu expliques en français ce que tu as compris, à l'écrit ou au micro. Ivrit compare avec le sens du texte et met de côté les mots qui t'ont échappé : ils reviendront en révision.</dd>
  <dt>La discussion : voix seule ou texte affiché ?</dt>
  <dd>Par défaut, l'IA te parle sans afficher son texte, pour entraîner ton oreille. Si tu n'as pas compris, touche « Afficher » sous le message, ou réécoute-le. Pour voir tout le texte en permanence, touche l'œil en haut à gauche de la discussion ; touche-le de nouveau pour revenir à la voix seule. Ivrit retient ton choix.</dd>
  <dt>Les voyelles (nikoud)</dt>
  <dd>Dans Réglages › Voyelles : partout, seulement sur les mots que tu ne connais pas encore (elles disparaissent au fil de tes progrès, comme à l'oulpan), ou nulle part.</dd>
  <dt>La taille du texte</dt>
  <dd>Les boutons A / A sous chaque texte, ou Réglages › Affichage, agrandissent ou réduisent l'hébreu partout dans l'app.</dd>
  <dt>Changer de niveau</dt>
  <dd>Réglages › Niveau. Les mots supposés connus suivent le niveau choisi ; ceux que tu as appris avec Ivrit sont toujours conservés.</dd>
</dl>

<h2>Questions fréquentes</h2>
<dl>
  <dt>Comment annuler mon abonnement ou mon essai gratuit ?</dt>
  <dd>Sur l'iPhone : Réglages › ton nom › Abonnements › Ivrit › Annuler l'abonnement. Tu gardes l'accès jusqu'à la fin de la période déjà payée. Pendant l'essai de 7 jours, annule au moins 24 heures avant la fin pour ne rien payer.</dd>
  <dt>Comment me faire rembourser ?</dt>
  <dd>Les paiements passent par Apple, qui traite les remboursements : va sur <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a> et choisis Ivrit.</dd>
  <dt>J'ai changé d'iPhone, je ne retrouve pas mon abonnement.</dt>
  <dd>Ouvre Ivrit, puis l'écran d'abonnement, et touche « Restaurer mes achats » avec le même compte Apple.</dd>
  <dt>Quelle différence entre Essentiel et Intensif ?</dt>
  <dd>Le nombre de textes écrits pour toi par l'intelligence artificielle et de discussions chaque jour : 2 textes et 1 discussion avec Essentiel, 10 textes et 4 discussions avec Intensif. Les textes prêts, les révisions, l'alphabet et les thèmes sont illimités dans les deux formules, et relire ou retraduire un texte déjà fait ne compte pas.</dd>
  <dt>J'ai atteint ma limite du jour.</dt>
  <dd>Elle se remet à zéro le lendemain. En attendant, tu peux continuer avec les textes prêts, tes révisions et tes anciens textes.</dd>
  <dt>Est-ce que je peux utiliser Ivrit sans l'intelligence artificielle ?</dt>
  <dd>Oui. Elle est désactivée tant que tu ne l'as pas acceptée, et tu peux la couper à tout moment dans Réglages. Les textes prêts, les révisions et l'alphabet fonctionnent sans elle.</dd>
  <dt>Mes progrès sont-ils sauvegardés ?</dt>
  <dd>Ils restent sur ton iPhone. Si tu supprimes l'application, ils sont effacés avec elle.</dd>
</dl>

<ul class="liens">
  <li><a href="/ivrit/conditions/">Conditions d'utilisation</a></li>
  <li><a href="/ivrit/confidentialite/">Politique de confidentialité</a></li>
</ul>
""",
    },
    "conditions/": {
        "titre": "Ivrit — conditions d'utilisation",
        "desc": "Conditions d'utilisation et d'abonnement de l'application Ivrit.",
        "corps": f"""
<p class="chapo">Ces conditions s'appliquent à l'application Ivrit pour iPhone, éditée par Moïse Berrebi, entrepreneur individuel à Jérusalem (Israël). En utilisant Ivrit, tu les acceptes, ainsi que le <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">contrat de licence standard d'Apple pour les applications (EULA)</a>, qui s'applique en complément.</p>

<h2>1. Le service</h2>
<p>Ivrit aide à apprendre l'hébreu avec des textes, des explications corrigées, des révisions espacées et des discussions. Une partie des contenus (textes écrits pour toi, corrections, discussions) est produite par une intelligence artificielle : elle peut se tromper, notamment sur la vocalisation ou une traduction. Ivrit est un outil d'apprentissage et ne remplace pas un enseignant.</p>

<h2>2. Abonnements</h2>
<ul>
  <li>Deux formules sont proposées, Essentiel et Intensif, chacune au mois ou à l'année. Le prix exact, dans ta monnaie, est affiché dans l'application avant tout achat.</li>
  <li>Le paiement est débité sur ton compte Apple à la confirmation de l'achat, ou à la fin de l'essai gratuit s'il y en a un.</li>
  <li>L'abonnement se renouvelle automatiquement pour la même durée, sauf si tu l'annules au moins 24 heures avant la fin de la période en cours. Le renouvellement est débité dans les 24 heures qui précèdent cette fin.</li>
  <li>Tu peux gérer ou annuler ton abonnement dans les réglages de ton compte Apple (Réglages › ton nom › Abonnements). L'annulation prend effet à la fin de la période déjà payée.</li>
  <li>Essai gratuit : 7 jours, une seule fois par compte Apple. Si tu t'abonnes pendant l'essai, la partie non utilisée de l'essai est perdue.</li>
  <li>Les remboursements sont gérés par Apple, selon ses règles.</li>
</ul>

<h2>3. Limites d'usage</h2>
<p>Chaque formule comprend un nombre de textes écrits par l'intelligence artificielle et de discussions par jour, indiqué dans l'application. Pour garder le service disponible pour tous, un plafond technique par appareil et par jour s'applique aussi. Les limites se remettent à zéro chaque jour.</p>

<h2>4. Bon usage</h2>
<p>Tu t'engages à ne pas détourner Ivrit de son but : pas de tentative de contourner les limites, de copier l'application ou ses contenus pour les revendre, ni de faire produire à l'intelligence artificielle des contenus illégaux ou blessants.</p>

<h2>5. Contenus</h2>
<p>L'application, ses textes prêts, sa liste de mots et son design appartiennent à l'éditeur. Les textes que tu écris dans Ivrit t'appartiennent.</p>

<h2>6. Responsabilité</h2>
<p>Ivrit est fourni tel quel. Je fais de mon mieux pour qu'il fonctionne et que ses contenus soient justes, sans pouvoir garantir l'absence d'erreur ou d'interruption. Rien dans ces conditions ne limite les droits que la loi te reconnaît en tant que consommateur.</p>

<h2>7. Changements</h2>
<p>Ces conditions peuvent évoluer. En cas de changement important, tu en seras informé dans l'application. La date de mise à jour figure en haut de cette page.</p>

<h2>8. Contact</h2>
<p>Moïse Berrebi, Jérusalem, Israël — <a href="mailto:{CONTACT}?subject=Ivrit">{CONTACT}</a></p>
""",
    },
    "confidentialite/": {
        "titre": "Ivrit — politique de confidentialité",
        "desc": "Ce que l'application Ivrit collecte, pourquoi, et ce qu'elle ne fait pas.",
        "corps": f"""
<p class="chapo">En bref : pas de compte, pas de publicité, pas de pistage. Tes progrès restent sur ton iPhone. Seuls les textes que tu demandes à l'intelligence artificielle de traiter quittent l'appareil, et seulement si tu l'as activée.</p>

<h2>Qui est responsable</h2>
<p>Moïse Berrebi, entrepreneur individuel, Jérusalem (Israël). Contact : <a href="mailto:{CONTACT}?subject=Ivrit%20confidentialit%C3%A9">{CONTACT}</a>.</p>

<h2>Ce qui reste sur ton iPhone</h2>
<p>Ton niveau, les mots que tu connais, tes révisions, tes textes et ta courbe de progression sont enregistrés uniquement sur ton appareil. Je n'y ai pas accès. Ils sont effacés si tu supprimes l'application.</p>
<p>La dictée utilise la reconnaissance vocale d'Apple, qui peut traiter ta voix sur ses serveurs pour la transcrire, selon sa propre politique de confidentialité ; je n'ai pas accès à l'enregistrement. L'accès au micro n'est demandé que lorsque tu touches le bouton de dictée.</p>

<h2>Ce qui est envoyé quand l'intelligence artificielle est activée</h2>
<p>L'intelligence artificielle est désactivée tant que tu ne l'as pas acceptée, et tu peux la couper à tout moment dans Réglages. Quand elle est active, et seulement au moment où tu l'utilises, Ivrit envoie :</p>
<ul>
  <li>le contenu nécessaire à la demande : ton niveau, le thème choisi, l'explication que tu as écrite ou dictée, les messages de la discussion, ou le texte à vocaliser ;</li>
  <li>un identifiant d'appareil aléatoire, créé par Ivrit et sans lien avec ton identité, ton compte Apple ou l'identifiant publicitaire. Il sert uniquement à compter tes demandes du jour.</li>
</ul>
<p>Ces données passent par un relais que j'exploite chez Cloudflare, puis sont traitées par l'API d'<a href="https://www.anthropic.com/legal/privacy">Anthropic</a> (modèles Claude), qui produit la réponse. Le relais n'enregistre pas le contenu de tes demandes ; il garde seulement un compteur par identifiant d'appareil et par jour, effacé automatiquement au bout de 2 jours. Anthropic n'utilise pas les données envoyées par son API pour entraîner ses modèles, et peut les conserver une durée limitée pour la sécurité du service, selon sa propre politique.</p>
<p>N'écris pas d'informations personnelles sensibles dans tes explications ou tes discussions : ce n'est jamais nécessaire pour apprendre.</p>

<h2>Achats</h2>
<p>Les abonnements sont gérés par Apple. Je ne reçois ni ton nom, ni ton adresse e-mail, ni tes coordonnées bancaires ; l'application sait seulement si un abonnement est actif.</p>

<h2>Ce qu'Ivrit ne fait pas</h2>
<ul>
  <li>Pas de compte à créer, pas de publicité, pas d'outil de mesure d'audience ni de pistage dans l'application.</li>
  <li>Aucune donnée vendue ni partagée à des fins commerciales.</li>
</ul>

<h2>Tes droits</h2>
<p>Comme je ne détiens pas de données permettant de t'identifier, il n'y a en principe rien à consulter ni à effacer de mon côté. Pour toute question ou demande, écris-moi : je réponds sous 30 jours. Tu peux aussi saisir l'autorité de protection des données de ton pays (en France, la CNIL ; en Israël, l'Autorité de protection de la vie privée).</p>

<h2>Enfants</h2>
<p>Ivrit ne s'adresse pas spécialement aux enfants de moins de 13 ans et ne collecte sciemment aucune donnée les concernant.</p>

<h2>Changements</h2>
<p>Si cette politique change de façon importante, tu en seras informé dans l'application. La date de mise à jour figure en haut de cette page.</p>
""",
    },
}

LOGO = '<svg viewBox="0 0 64 64" aria-hidden="true"><rect width="64" height="64" rx="14" fill="#8fb8f2"/><text x="32" y="44" text-anchor="middle" font-size="34" font-weight="700" fill="#0e1f40" font-family="Heebo, sans-serif">א</text></svg>'


def chemin(cle):
    return "/ivrit/" + cle


def page(cle):
    p = PAGES[cle]
    url = BASE + chemin(cle)
    titre, desc = H.escape(p["titre"]), H.escape(p["desc"], quote=True)
    fil = "" if cle == "" else '<nav class="fil" aria-label="Fil d\'Ariane"><a href="/ivrit/">Ivrit</a> › ' + titre.split(" — ")[1].capitalize() + "</nav>"
    return f"""<!doctype html>
<html lang="fr" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titre}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Rubik:wght@500;600;700&family=Heebo:wght@400;500;700&display=swap">
{style()}
{CSS_IVRIT}
</head>
<body>
<header><div class="env">
  <a class="logo" href="/ivrit/">{LOGO}<span><b>Ivrit</b><small>Apprendre l'hébreu en lisant</small></span></a>
</div></header>
<main class="env">
  {fil or '<div class="fil"></div>'}
  <article>
    <h1>{titre.split(" — ")[0] if cle == "" else titre.split(" — ")[1].capitalize()}</h1>
    <p class="date">Mis à jour le {MAJ}</p>
{p["corps"].strip()}
  </article>
</main>
<footer><div class="env">Ivrit · Moïse Berrebi · Jérusalem · <a href="/ivrit/" style="color:inherit">Aide</a> · <a href="/ivrit/conditions/" style="color:inherit">Conditions</a> · <a href="/ivrit/confidentialite/" style="color:inherit">Confidentialité</a></div></footer>
</body>
</html>
"""
