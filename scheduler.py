from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
HISTORY_PATH = DATA_DIR / "history.json"

DEFAULT_INTERVAL = 7 * 24 * 60 * 60  # 7 jours en secondes


def load_history() -> list[dict[str, str]]:
    if HISTORY_PATH.exists():
        try:
            return json.loads(HISTORY_PATH.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def save_history(history: list[dict[str, str]], last_run: str) -> None:
    HISTORY_PATH.write_text(
        json.dumps({"last_run": last_run, "history": history}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def push_new_guide() -> dict[str, str] | None:
    try:
        completed = subprocess.run(
            [sys.executable, str(BASE_DIR / "bot.py")],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"bot generation failed: {exc.stderr or exc.stdout or exc.returncode}")

    # On récupère le dernier fichier généré
    try:
        newest = sorted((BASE_DIR / "guides").glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)[0]
    except IndexError:
        return None

    stem = newest.stem
    return {
        "id": stem,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "md": str(newest),
        "html": str(BASE_DIR / "site" / "guides" / f"{stem}.html"),
    }


def run(interval_seconds: int = DEFAULT_INTERVAL) -> None:
    now = datetime.now(timezone.utc)
    print(f"[scheduler] start — {now.isoformat()}")

    history = load_history()
    history = [entry for entry in history if entry.get("id")]

    try:
        entry = push_new_guide()
    except RuntimeError as exc:
        print(f"[scheduler] generation failed: {exc}")
        save_history(history, now.isoformat())
        sys.exit(2)

    if not entry:
        print("[scheduler] no guide generated after run")
        save_history(history, now.isoformat())
        sys.exit(0)

    history.append(entry)
    save_history(history, now.isoformat())

    print(f"[scheduler] generated {entry['id']}")
    print(f"[scheduler] created_at={entry['created_at']}")
    print(f"[scheduler] files={entry['md']}, {entry['html']}")
    print(f"[scheduler] history={[x['id'] for x in history]}")
