from __future__ import annotations

import random
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
GUIDES_DIR = BASE_DIR / "guides"
SITE_DIR = BASE_DIR / "site"
DATA_DIR = BASE_DIR / "data"

GUIDES_DIR.mkdir(exist_ok=True)
SITE_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

TOPICS = [
    {
        "id": "robot-tondeuse-ch",
        "title": "Les meilleures robots tondeuses en Suisse 2026",
        "keywords": ["robot tondeuse", "pelouse", "jardin", "automower", "worx", "landxcape", "yardmaster"],
    },
    {
        "id": "assurance-maladie-comparatif-ch",
        "title": "Comparatif assurance maladie LAMal en Suisse 2026",
        "keywords": ["assurance maladie", "caisse maladie", "LAMal", "franchise", "complementaire", "prix", "suisse"],
    },
    {
        "id": "creer-sa-startup-ch",
        "title": "Créer sa startup en Suisse Romande en 2026",
        "keywords": ["startup", "creation", "entreprise", "suisse", "incubateur", "fondateur", "capital", "business plan"],
    },
]


def _localized_intro(topic: dict[str, Any]) -> str:
    return (
        f"Guide actualisé en 2026 : {topic['title']}. "
        f"Conseils, critères de choix et astuces adaptés au marché suisse. "
        f"Prix indicatifs en CHF, disponibilité majoritairement sur Amazon.ch et chez les détaillants locaux."
    )


def _localized_section(topic: dict[str, Any]) -> list[dict[str, str]]:
    base = [
        "Comment bien choisir en fonction de vos besoins",
        "Critères essentiels à comparer avant achat",
        "Les erreurs courantes à éviter",
    ]
    enriched = [
        "Vérifiez la compatibilité avec la norme suisse et les retours en magasin locaux.",
        "Privilégiez les offres avec SAV en Suisse ou extension de garantie disponible.",
        "Utilisez les comparateurs de prix locaux avant finaliser votre commande.",
    ]
    sections = []
    for title, note in zip(base, enriched):
        sections.append({"h2": title, "p": note + " " + random.choice([
            "Les Suisses privilégient souvent la qualité et la durabilité.",
            "En Suisse romande, la saison de jardinage commence souvent fin mars.",
            "Les avis clients suisses sont un bon indicateur de fiabilité."
        ])})
    return sections


def _outro(topic: dict[str, Any]) -> str:
    return (
        "En résumé, ce guide vous propose une sélection réaliste adaptée au contexte suisse. "
        "Partagez-le si vous trouvez ces informations utiles. "
        "Prochaine mise à jour prévue selon les nouveautés du marché."
    )


def generate_article(topic: dict[str, Any]) -> str:
    intro = _localized_intro(topic)
    sections = _localized_section(topic)
    body_parts = [f"# {topic['title']}\n\n", f"{intro}\n\n"]
    for section in sections:
        body_parts.append(f"## {section['h2']}\n\n{section['p']}\n\n")
    body_parts.append(_outro(topic))
    return "".join(body_parts)


def save_article(topic: dict[str, Any], content: str) -> Path:
    path = GUIDES_DIR / f"{topic['id']}.md"
    path.write_text(content, encoding="utf-8")
    return path


def build_site() -> Path:
    index_parts = ["# Swiss Guides\n\nGuides suisses générés automatiquement.\n\n"]
    for topic in TOPICS:
        index_parts.append(f"- [{topic['title']}](guides/{topic['id']}.md)")
    index = "\n".join(index_parts)
    out = SITE_DIR / "README.md"
    out.write_text(index, encoding="utf-8")
    return out


def run() -> dict[str, Any]:
    results = []
    for topic in TOPICS:
        content = generate_article(topic)
        path = save_article(topic, content)
        topic["path"] = str(path)
        topic["chars"] = len(content)
        results.append(topic)
    build_site()
    return {"generated": len(results), "guides": results}


if __name__ == "__main__":
    res = run()
    for item in res["guides"]:
        print(f"[swiss-guides] generated {item['id']} -> {item['path']} ({item['chars']} chars)")
