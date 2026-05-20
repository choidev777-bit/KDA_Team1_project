WEAPON_ROUTES = [
    {"id": "iron_sword", "type": "검", "price": 300, "names": ["철검", "푸른 철검", "청린검", "창천검 청린"]},
    {"id": "long_sword", "type": "검", "price": 320, "names": ["낡은 장검", "다시 벼린 장검", "맹세의 장검", "왕의 맹세검"]},
    {"id": "nameless_sword", "type": "검", "price": 350, "names": ["이름 없는 검", "침묵의 검", "무명기사의 검", "무명왕검"]},
    {"id": "black_dagger", "type": "검", "price": 280, "names": ["검은 단검", "그림자 단검", "월식 단검", "흑월도 야명"]},
    {"id": "rusty_greatsword", "type": "검", "price": 420, "names": ["녹슨 대검", "무거운 대검", "산을 가르는 대검", "천붕대검 태산"]},
    {"id": "thin_rapier", "type": "검", "price": 330, "names": ["얇은 세검", "바람 세검", "번개 세검", "뇌섬검 세이라"]},
    {"id": "glass_sword", "type": "검", "price": 450, "names": ["유리 조각검", "수정검", "별빛 수정검", "성정검 루미나"]},
    {"id": "wood_spear", "type": "창", "price": 300, "names": ["나무창", "철촉창", "청룡창", "청룡언월창"]},
    {"id": "soldier_spear", "type": "창", "price": 330, "names": ["병사의 장창", "붉은깃 장창", "전장의 혈창", "적룡창 파군"]},
    {"id": "hunter_spear", "type": "창", "price": 320, "names": ["사냥창", "늑대창", "은빛 늑대창", "월랑창 하울린"]},
    {"id": "ash_spear", "type": "창", "price": 360, "names": ["물푸레창", "파도창", "해룡의 창", "해왕창 네레우스"]},
    {"id": "short_javelin", "type": "창", "price": 340, "names": ["짧은 투창", "회전 투창", "별뚫는 투창", "성멸창 아스트라"]},
    {"id": "wood_bow", "type": "활", "price": 300, "names": ["나무활", "사냥꾼의 활", "매의 장궁", "천응궁 하늘매"]},
    {"id": "bent_bow", "type": "활", "price": 330, "names": ["휘어진 활", "바람깃 활", "폭풍궁", "풍신궁 갈라진하늘"]},
    {"id": "old_horn_bow", "type": "활", "price": 360, "names": ["오래된 각궁", "달빛 각궁", "은월궁", "월영궁 루나리스"]},
    {"id": "bone_bow", "type": "활", "price": 380, "names": ["뼈 활", "망자의 활", "혼령궁", "사혼궁 네크라"]},
    {"id": "ember_bow", "type": "활", "price": 400, "names": ["불씨 활", "화염 장궁", "태양궁", "일식궁 솔라크"]},
    {"id": "hand_axe", "type": "도끼", "price": 360, "names": ["손도끼", "벌목 도끼", "거인의 도끼", "거신부 골리앗"]},
    {"id": "stone_hammer", "type": "망치", "price": 380, "names": ["돌망치", "철벽 망치", "대지의 망치", "지진추 가이아"]},
    {"id": "farmer_scythe", "type": "낫", "price": 420, "names": ["농부의 낫", "검은 낫", "사신의 낫", "명계낫 아비소스"]},
]


def get_route(route_id):
    for route in WEAPON_ROUTES:
        if route["id"] == route_id:
            return route
    return WEAPON_ROUTES[0]


def get_weapon_name(weapon):
    route = get_route(weapon["route_id"])
    level = weapon["level"]

    if level >= 9:
        name_index = 3
    elif level >= 6:
        name_index = 2
    elif level >= 3:
        name_index = 1
    else:
        name_index = 0

    return route["names"][name_index]


def create_weapon(route_id, weapon_id):
    route = get_route(route_id)
    return {
        "id": weapon_id,
        "route_id": route["id"],
        "type": route["type"],
        "level": 0,
    }


def make_weapon_id(state):
    weapons = state["inventory"]["weapons"]
    return f"weapon_{len(weapons) + 1}"


def get_equipped_weapon(state):
    inventory = state["inventory"]
    equipped_id = inventory["equipped_weapon_id"]

    for weapon in inventory["weapons"]:
        if weapon["id"] == equipped_id:
            return weapon

    if len(inventory["weapons"]) == 0:
        return None

    inventory["equipped_weapon_id"] = inventory["weapons"][0]["id"]
    return inventory["weapons"][0]


def sync_player_weapon(state):
    weapon = get_equipped_weapon(state)

    if weapon is None:
        return state

    state["player"]["weapon_name"] = get_weapon_name(weapon)
    state["player"]["weapon_level"] = weapon["level"]

    if weapon["level"] > state["player"]["best_weapon_level"]:
        state["player"]["best_weapon_level"] = weapon["level"]

    return state


def get_weapon_art(weapon_type):
    if weapon_type == "창":
        return [
            "        /\\",
            "       /  \\",
            "       ||||",
            "       ||||",
            "       ||||",
            "       ||||",
            "       ||||",
        ]

    if weapon_type == "활":
        return [
            "      )\\",
            "     )  \\",
            "    )---->",
            "     )  /",
            "      )/",
        ]

    if weapon_type == "도끼":
        return [
            "       ___",
            "      / __|",
            "     | |__",
            "      \\___|",
            "        ||",
            "        ||",
        ]

    if weapon_type == "망치":
        return [
            "     ______",
            "    |______|",
            "       ||",
            "       ||",
            "       ||",
        ]

    if weapon_type == "낫":
        return [
            "       _____",
            "     /",
            "    /",
            "   /",
            "  /______",
            "       ||",
        ]

    return [
        "          /\\",
        "         /  \\",
        "         ||||",
        "         ||||",
        "      ___||||___",
        "          ||",
        "          ||",
    ]
