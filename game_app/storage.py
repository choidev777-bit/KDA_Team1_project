import json
from pathlib import Path

from game_app.game_state import create_default_state, ensure_state_shape


DEFAULT_SAVE_PATH = Path("data") / "save_data.json"


def load_state(save_path=DEFAULT_SAVE_PATH):
    save_path = Path(save_path)

    if not save_path.exists():
        state = create_default_state()
        save_state(state, save_path)
        return state

    try:
        with save_path.open("r", encoding="utf-8") as file:
            state = json.load(file)
    except (json.JSONDecodeError, OSError):
        state = create_default_state()
        save_state(state, save_path)
        return state

    return ensure_state_shape(state)


def save_state(state, save_path=DEFAULT_SAVE_PATH):
    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)

    with save_path.open("w", encoding="utf-8") as file:
        json.dump(state, file, ensure_ascii=False, indent=2)
