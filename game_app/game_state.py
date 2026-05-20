from copy import deepcopy


DEFAULT_STATE = {
    "player": {
        "nickname": "player",
        "gold": 1000,
        "weapon_name": "기본 검",
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
}


def create_default_state():
    return deepcopy(DEFAULT_STATE)


def ensure_state_shape(state):
    default_state = create_default_state()

    if not isinstance(state, dict):
        return default_state

    for section_name, section_value in default_state.items():
        if section_name not in state or not isinstance(state[section_name], dict):
            state[section_name] = section_value
            continue

        for key, default_value in section_value.items():
            if key not in state[section_name]:
                state[section_name][key] = default_value

    return state
