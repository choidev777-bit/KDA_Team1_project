from copy import deepcopy

from game_app.weapon_data import create_weapon, sync_player_weapon


DEFAULT_STATE = {
    "player": {
        "nickname": "player",
        "gold": 1000,
        "weapon_name": "철검",
        "weapon_level": 0,
        "best_weapon_level": 0,
    },
    "battle": {
        "win": 0,
        "lose": 0,
        "logs": [],
    },
    "raid": {
        "cleared_stage": 0,
        "logs": [],
    },
    "inventory": {
        "equipped_weapon_id": "weapon_1",
        "weapons": [
            {
                "id": "weapon_1",
                "route_id": "iron_sword",
                "type": "검",
                "level": 0,
            }
        ],
    },
}


def create_default_state():
    return deepcopy(DEFAULT_STATE)


def ensure_state_shape(state):
    default_state = create_default_state()

    if not isinstance(state, dict):
        return default_state

    had_inventory = "inventory" in state and isinstance(state["inventory"], dict)
    old_weapon_level = state.get("player", {}).get("weapon_level", 0)

    for section_name, section_value in default_state.items():
        if section_name not in state or not isinstance(state[section_name], dict):
            state[section_name] = deepcopy(section_value)
            continue

        for key, default_value in section_value.items():
            if key not in state[section_name]:
                state[section_name][key] = deepcopy(default_value)

    ensure_inventory(state, had_inventory, old_weapon_level)
    sync_player_weapon(state)

    return state


def ensure_inventory(state, had_inventory=True, old_weapon_level=0):
    inventory = state["inventory"]

    if "weapons" not in inventory or not isinstance(inventory["weapons"], list):
        inventory["weapons"] = []

    if not had_inventory:
        inventory["weapons"] = []

    if len(inventory["weapons"]) == 0:
        weapon = create_weapon("iron_sword", "weapon_1")
        weapon["level"] = old_weapon_level
        inventory["weapons"].append(weapon)

    if "equipped_weapon_id" not in inventory or not inventory["equipped_weapon_id"]:
        inventory["equipped_weapon_id"] = inventory["weapons"][0]["id"]

    weapon_ids = []
    for index, weapon in enumerate(inventory["weapons"], start=1):
        if "id" not in weapon:
            weapon["id"] = f"weapon_{index}"
        if "route_id" not in weapon:
            weapon["route_id"] = "iron_sword"
        if "type" not in weapon:
            weapon["type"] = "검"
        if "level" not in weapon:
            weapon["level"] = 0
        weapon_ids.append(weapon["id"])

    if inventory["equipped_weapon_id"] not in weapon_ids:
        inventory["equipped_weapon_id"] = inventory["weapons"][0]["id"]
