from game_app.weapon_data import get_equipped_weapon, get_weapon_art, get_weapon_name, sync_player_weapon


def print_weapon_card(weapon, is_equipped):
    marker = "장착 중" if is_equipped else "보관 중"
    name = get_weapon_name(weapon)
    art = get_weapon_art(weapon["type"])

    print("+================================+")
    print(f"| 상태: {marker}")
    print(f"| 이름: {name} +{weapon['level']}")
    print(f"| 종류: {weapon['type']}")
    print("+--------------------------------+")

    for line in art:
        print(line)

    print("+================================+")


def show_warehouse(state):
    weapons = state["inventory"]["weapons"]
    equipped_id = state["inventory"]["equipped_weapon_id"]

    print()
    print("===== 무기 창고 =====")

    if len(weapons) == 0:
        print("보유한 무기가 없습니다.")
        return

    for index, weapon in enumerate(weapons, start=1):
        print()
        print(f"[{index}번 무기]")
        print_weapon_card(weapon, weapon["id"] == equipped_id)


def equip_weapon(state):
    weapons = state["inventory"]["weapons"]

    if len(weapons) == 0:
        print("장착할 무기가 없습니다.")
        return state

    show_weapon_summary(state)
    choice = input("장착할 무기 번호를 입력하세요: ").strip()

    if not choice.isdigit():
        print("숫자로 입력해주세요.")
        return state

    weapon_index = int(choice) - 1

    if weapon_index < 0 or weapon_index >= len(weapons):
        print("없는 무기 번호입니다.")
        return state

    selected_weapon = weapons[weapon_index]
    state["inventory"]["equipped_weapon_id"] = selected_weapon["id"]
    sync_player_weapon(state)

    print(f"{get_weapon_name(selected_weapon)} +{selected_weapon['level']}을(를) 장착했습니다.")

    return state


def show_weapon_summary(state):
    weapons = state["inventory"]["weapons"]
    equipped_id = state["inventory"]["equipped_weapon_id"]

    print()
    print("===== 보유 무기 =====")

    for index, weapon in enumerate(weapons, start=1):
        marker = "*" if weapon["id"] == equipped_id else " "
        print(f"{index}. {marker} {get_weapon_name(weapon)} +{weapon['level']} [{weapon['type']}]")


def run_warehouse_menu(state):
    sync_player_weapon(state)

    while True:
        print()
        print("===== 창고 =====")
        print("1. 무기 진열 보기")
        print("2. 무기 장착")
        print("3. 메인 메뉴로 돌아가기")

        choice = input("번호를 선택하세요: ").strip()

        if choice == "1":
            show_warehouse(state)
        elif choice == "2":
            state = equip_weapon(state)
        elif choice == "3":
            print("메인 메뉴로 돌아갑니다.")
            return state
        else:
            print("잘못된 입력입니다. 1, 2, 3 중에서 선택해주세요.")
