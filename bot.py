from __future__ import annotations

import random
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
GUIDES_DIR = BASE_DIR / "guides"
SITE_DIR = BASE_DIR / "site"
DATA_DIR = BASE_DIR / "data"

GUIDES_DIR.mkdir(exist_ok=True)
SITE_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

TOPICS = [
    {
        "id": "robot-tondeuse-ch",
        "title": "Les meilleurs robots tondeuses en Suisse 2026",
        "category": "Jardin",
        "intro": (
            "En 2026, le marché suisse des robots tondeuses est dominé par des marques fiables comme "
            "Husqvarna Automower, Worx Landroid, Yardmaster et Bosch Indego. Ce guide compare les modèles "
            "adaptés aux pelouses suisses, du petit jardin de ville à la grande parcelle en zone résidentielle."
        ),
        "products": [
            {
                "name": "Husqvarna Automower 305",
                "price": "~2 490 CHF",
                "pros": ["Fiable", "Gestion des pentes jusqu'à 45°", "Connecté et programmable"],
                "cons": ["Prix élevé", "Installation du fil périphérique nécessaire"],
                "affiliate_url": "https://www.amazon.ch/s?k=husqvarna+automower+305",
                "best_for": "Pelouses jusqu'à 1000 m² avec pentes",
            },
            {
                "name": "Worx Landroid M500",
                "price": "~1 299 CHF",
                "pros": ["Bon rapport qualité/prix", "Multi-zones", "Facile à configurer"],
                "cons": ["Moins adapté aux grandes pentes", "Bruit modéré"],
                "affiliate_url": "https://www.amazon.ch/s?k=worx+landroid+m500",
                "best_for": "Jardins moyens (500-1000 m²) en plat ou peu pentu",
            },
            {
                "name": "Yardmaster YRM40 G6",
                "price": "~899 CHF",
                "pros": ["Très abordable", "Bonne couverture", "Robuste"],
                "cons": ["Moins de fonctions connectées", "Bruit plus marqué"],
                "affiliate_url": "https://www.amazon.ch/s?k=yardmaster+robot+tondeuse",
                "best_for": "Petits jardins (< 500 m²) sans pentes importantes",
            },
        ],
        "faqs": [
            ("Quelle surface maximum pour un robot tondeuse ?", "La plupart des modèles couvrent 500 à 2000 m². Pour des surfaces plus grandes, prévoyez 2 zones ou un modèle haut de gamme."),
            ("Faut-il une garantie prolongée en Suisse ?", "Oui, nombreux détaillants suisses proposent des extensions de garantie. Vérifiez le SAV local avant achat."),
            ("Les robots tondeuses sont-ils bruyants ?", "Ils sont plus silencieux qu'une tondeuse classique, surtout le weekend. La réglementation communale peut imposer des plages horaires."),
        ],
    },
    {
        "id": "caisse-maladie-comparatif-ch",
        "title": "Comparatif caisses maladie LAMal Suisse 2026",
        "category": "Finance / Santé",
        "intro": (
            "Chaque Suisse doit souscrire une assurance maladie de base (LAMal). Les primes varient fortement "
            "selon la caisse, la franchise choisie et le modèle de soins. Ce guide compare les critères à vérifier "
            "avant de changer de caisse et les pièges à éviter."
        ),
        "products": [
            {
                "name": "Helsana",
                "price": "Prime variable selon canton",
                "pros": ["Large réseau", "Services en ligne complets", "Bon SAV"],
                "cons": ["Primes parfois au-dessus de la moyenne"],
                "affiliate_url": "https://www.helsana.ch/fr",
                "best_for": "Familles et personnes cherchant un équilibre prix/services",
            },
            {
                "name": "CSS",
                "price": "Prime variable selon canton",
                "pros": ["Souvent parmi les moins chères", "Appli mobile pratique"],
                "cons": ["Réseau plus restreint dans certaines régions"],
                "affiliate_url": "https://www.css.ch/fr",
                "best_for": "Personnes en bonne santé souhaitant réduire les coûts",
            },
            {
                "name": "Groupe Mutuel",
                "price": "Prime variable selon canton",
                "pros": ["Offres modulaires", "Présence en Romandie"],
                "cons": ["Variations régionales importantes"],
                "affiliate_url": "https://www.groupemutuel.ch/fr",
                "best_for": "Romands cherchant une caisse avec ancrage local",
            },
        ],
        "faqs": [
            ("Puis-je changer de caisse chaque année ?", "Oui, avec un délai de résiliation de 3 mois avant la fin de l'année d'assurance."),
            ("Faut-il prendre une complémentaire ?", "La base LAMal est obligatoire. La complémentaire est utile pour soins dentaires, hospitalisation à choix, etc."),
            ("Comment économiser sur ses primes ?", "Augmenter la franchise, choisir un modèle de médecin référent, ou comparer chaque année."),
        ],
    },
    {
        "id": "creer-sa-startup-ch",
        "title": "Créer sa startup en Suisse Romande en 2026",
        "category": "Business",
        "intro": (
            "La Suisse, et particulièrement Genève, Vaud et Neuchâtel, attire de plus en plus de fondateurs. "
            "Ce guide résume les étapes clés pour lancer sa startup : statut juridique, financement, incubateurs et aides disponibles."
        ),
        "products": [
            {
                "name": "Fondation Innosuisse",
                "price": "Jusqu'à 350k CHF de soutien",
                "pros": ["Aide publique majeure", "Accompagnement technique"],
                "cons": ["Dossier exigeant", "Sélection compétitive"],
                "affiliate_url": "https://www.innosuisse.ch",
                "best_for": "Startups deep tech et innovantes en phase R&D",
            },
            {
                "name": "EPFL Innovation Park",
                "price": "Bureaux + programmes",
                "pros": ["Écosystème dense", "Réseau investisseurs", "Accès talent EPFL"],
                "cons": ["Sélection sur dossier"],
                "affiliate_url": "https://www.epfl.ch/innovation/innovation-park/",
                "best_for": "Startups deep tech, IA, biotech, robotics",
            },
            {
                "name": "Fondation 30 Ventures (Genève)",
                "price": "Investissement 100k-500k CHF",
                "pros": ["Focus Genève", "Accélération 6-12 mois"],
                "cons": ["Equity prise en contrepartie"],
                "affiliate_url": "https://30ventures.ch/",
                "best_for": "Startups genevoises en phase early growth",
            },
        ],
        "faqs": [
            ("Quel statut choisir pour une startup ?", "SA pour lever des fonds, SARL pour la simplicité, ou Foundation pour l'impact social."),
            ("Où trouver les meilleurs incubateurs ?", "Innosuisse, EPFL Innovation Park, Trusted Insight (Genève), Startup Campus (Lausanne)."),
            ("Quel budget minimum pour lancer ?", "De 20k à 50k CHF pour se lancer sans financement externe."),
        ],
    },
]


def _localized_intro(topic: dict[str, Any]) -> str:
    return topic.get("intro", "")


def _product_section(topic: dict[str, Any]) -> str:
    lines = []
    for product in topic.get("products", []):
        lines.append(f"### {product['name']}  ")
        lines.append(f"- **Prix indicatif** : {product['price']}  ")
        lines.append(f"- **Idéal pour** : {product['best_for']}  ")
        lines.append("- **Points forts** : " + ", ".join(product['pros']) + "  ")
        lines.append("- **Points faibles** : " + ", ".join(product['cons']) + "  ")
        lines.append(f"- **Vérifier** : [lien]({product['affiliate_url']})  ")
        lines.append("")
    return "\n".join(lines)


def _faq_section(topic: dict[str, Any]) -> str:
    lines = ["## FAQ\n"]
    for question, answer in topic.get("faqs", []):
        lines.append(f"**{question}**  ")
        lines.append(f"{answer}  ")
        lines.append("")
    return "\n".join(lines)


def generate_article(topic: dict[str, Any]) -> str:
    parts = [
        f"# {topic['title']}  ",
        f"*Catégorie : {topic.get('category', 'Guide')} — Suisse Romande 2026*  ",
        "",
        _localized_intro(topic),
        "",
        "## Sélection et comparaison  ",
        "",
        _product_section(topic),
        "",
        _faq_section(topic),
        "",
        "## En résumé  ",
        (
            "Ce guide synthétise les éléments concrets à vérifier avant votre achat ou votre décision. "
            "Les prix et disponibilités évoluent régulièrement : pensez à comparer les offres du moment."
        ),
        "",
        "---",
        "*Mise à jour : 2026 — Geneva Startup Radar / Swiss Guides*",
    ]
    return "\n".join(parts)


def save_article(topic: dict[str, Any], content: str) -> Path:
    path = GUIDES_DIR / f"{topic['id']}.md"
    path.write_text(content, encoding="utf-8")
    return path


def build_site() -> Path:
    index_parts = [
        "<!DOCTYPE html>",
        "<html lang='fr'>",
        "<head>",
        "  <meta charset='utf-8'>",
        "  <meta name='viewport' content='width=device-width, initial-scale=1'>",
        "  <title>Swiss Guides — Guides suisses 2026</title>",
        "  <meta name='description' content='Guides d'achat et comparatifs adaptés au marché suisse.'>",
        "  <style>",
        "    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 900px; margin: 0 auto; padding: 24px; background: #fafafa; color: #111; }",
        "    a { color: #1155cc; text-decoration: none; }",
        "    h1 { font-size: 22px; }",
        "    h2 { font-size: 18px; margin-top: 24px; }",
        "    .card { background: #fff; border: 1px solid #eee; border-radius: 8px; padding: 16px; margin: 12px 0; }",
        "    .tag { display: inline-block; padding: 2px 8px; border-radius: 999px; background: #eef1f6; font-size: 12px; color: #334; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <h1>Swiss Guides</h1>",
        "  <p class='tag'>Guides suisses générés automatiquement — 2026</p>",
        "  <ul>",
    ]
    for topic in TOPICS:
        index_parts.append(
            f"    <li><a href='guides/{topic['id']}.html'>{topic['title']}</a> <span class='tag'>{topic.get('category', 'Guide')}</span></li>"
        )
    index_parts.extend([
        "  </ul>",
        "  <p style='font-size:12px;color:#666;'>Monétisé en affiliation. Aucune donnée personnelle collectée.</p>",
        "</body>",
        "</html>",
    ])
    out = SITE_DIR / "index.html"
    out.write_text("\n".join(index_parts), encoding="utf-8")
    return out


def build_guide_html(topic: dict[str, Any], content: str) -> Path:
    body_html = content.replace("\n", "<br>").replace("**", "").replace("# ", "<h1>").replace("## ", "<h2>").replace("### ", "<h3>")
    lines = [
        "<!DOCTYPE html>",
        "<html lang='fr'>",
        "<head>",
        f"  <meta charset='utf-8'>",
        f"  <title>{topic['title']} — Swiss Guides</title>",
        "  <meta name='description' content='Guide suisse avec comparatifs et conseils.'>",
        "  <style>",
        "    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 860px; margin: 0 auto; padding: 24px; background: #fff; color: #111; }",
        "    a { color: #1155cc; text-decoration: none; }",
        "    h1 { font-size: 22px; }",
        "    h2 { font-size: 18px; margin-top: 22px; }",
        "    h3 { font-size: 16px; margin-top: 18px; }",
        "    .guide { line-height: 1.7; }",
        "    .cta { margin: 18px 0; padding: 14px; background: #f6f7f9; border-radius: 8px; border: 1px solid #e3e6eb; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <p><a href='index.html'>← Retour aux guides</a></p>",
        f"  <h1>{topic['title']}</h1>",
        f"  <p class='tag' style='color:#555;'>{topic.get('category', 'Guide')} — Suisse 2026</p>",
        f"  <div class='guide'>{body_html}</div>",
    ]
    for product in topic.get("products", []):
        lines.append("  <div class='cta'>")
        lines.append(f"    <strong>{product['name']}</strong> — {product['price']}<br>")
        lines.append(f"    <a href='{product['affiliate_url']}'>Vérifier le prix actuel →</a>")
        lines.append("  </div>")
    lines.extend([
        "  <hr>",
        "  <p style='font-size:12px;color:#666;'>Liens affiliés — Nous pouvons recevoir une commission sans surcoût pour vous.</p>",
        "</body>",
        "</html>",
    ])
    out = SITE_DIR / f"guides/{topic['id']}.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def run() -> dict[str, Any]:
    results = []
    for topic in TOPICS:
        content = generate_article(topic)
        md_path = save_article(topic, content)
        html_path = build_guide_html(topic, content)
        topic["md"] = str(md_path)
        topic["html"] = str(html_path)
        topic["chars"] = len(content)
        results.append(topic)
    build_site()
    return {"generated": len(results), "guides": results}


if __name__ == "__main__":
    res = run()
    for item in res["guides"]:
        print(f"[swiss-guides] {item['id']} -> {item['html']} ({item['chars']} chars)")
