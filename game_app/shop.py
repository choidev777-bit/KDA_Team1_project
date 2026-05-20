from game_app.weapon_data import WEAPON_ROUTES, create_weapon, make_weapon_id


def show_shop_items():
    print()
    print("===== 무기 상점 =====")

    for index, route in enumerate(WEAPON_ROUTES, start=1):
        base_name = route["names"][0]
        final_name = route["names"][-1]
        print(f"{index}. [{route['type']}] {base_name} -> {final_name} / 가격: {route['price']}골드")


def buy_weapon(state):
    show_shop_items()
    print("0. 돌아가기")

    choice = input("구입할 무기 번호를 입력하세요: ").strip()

    if choice == "0":
        return state

    if not choice.isdigit():
        print("숫자로 입력해주세요.")
        return state

    item_index = int(choice) - 1

    if item_index < 0 or item_index >= len(WEAPON_ROUTES):
        print("없는 무기 번호입니다.")
        return state

    route = WEAPON_ROUTES[item_index]
    player = state["player"]

    if player["gold"] < route["price"]:
        print("골드가 부족해서 구입할 수 없습니다.")
        return state

    weapon_id = make_weapon_id(state)
    weapon = create_weapon(route["id"], weapon_id)

    player["gold"] -= route["price"]
    state["inventory"]["weapons"].append(weapon)

    print(f"{route['names'][0]}을(를) 구입했습니다.")
    print(f"남은 골드: {player['gold']}")

    return state


def run_shop_menu(state):
    while True:
        print()
        print("===== 상점 =====")
        print("1. 무기 구입")
        print("2. 무기 목록 보기")
        print("3. 메인 메뉴로 돌아가기")

        choice = input("번호를 선택하세요: ").strip()

        if choice == "1":
            state = buy_weapon(state)
        elif choice == "2":
            show_shop_items()
        elif choice == "3":
            print("메인 메뉴로 돌아갑니다.")
            return state
        else:
            print("잘못된 입력입니다. 1, 2, 3 중에서 선택해주세요.")
