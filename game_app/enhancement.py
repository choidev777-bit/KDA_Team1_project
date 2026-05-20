import random

from game_app import shop, warehouse
from game_app.weapon_data import get_equipped_weapon, get_weapon_name, sync_player_weapon
from game_app.warehouse import equip_weapon


def calculate_cost(level):
    return 100 + level * 80


def calculate_success_rate(level):
    rates = {
        0: 90,
        1: 80,
        2: 70,
        3: 60,
        4: 50,
        5: 40,
        6: 30,
    }
    return rates.get(level, 20)


def is_weapon_protected(level):
    return level <= 5


def print_player_weapon(state):
    sync_player_weapon(state)
    player = state["player"]

    print(f"현재 무기: {player['weapon_name']} +{player['weapon_level']}")
    print(f"현재 골드: {player['gold']}")
    print(f"최고 강화 단계: +{player['best_weapon_level']}")


def show_enhancement_info(state):
    weapon = get_equipped_weapon(state)

    if weapon is None:
        print("강화할 무기가 없습니다.")
        return

    cost = calculate_cost(weapon["level"])
    success_rate = calculate_success_rate(weapon["level"])

    print()
    print("===== 강화 정보 =====")
    print(f"현재 무기: {get_weapon_name(weapon)} +{weapon['level']}")
    print(f"강화 비용: {cost}")
    print(f"성공 확률: {success_rate}%")
    print("성공하면 강화 단계가 1 올라갑니다.")

    if is_weapon_protected(weapon["level"]):
        print("+5 이하 무기는 실패해도 강화 단계가 유지됩니다.")
    else:
        print("+6 이상 무기는 실패하면 강화 단계가 +0으로 초기화됩니다.")


def try_enhance(state):
    weapon = get_equipped_weapon(state)

    if weapon is None:
        print("강화할 무기가 없습니다.")
        return state

    player = state["player"]
    cost = calculate_cost(weapon["level"])
    success_rate = calculate_success_rate(weapon["level"])

    print()
    print("===== 강화 시도 =====")
    print(f"현재 무기: {get_weapon_name(weapon)} +{weapon['level']}")
    print(f"현재 골드: {player['gold']}")
    print(f"강화 비용: {cost}")
    print(f"성공 확률: {success_rate}%")

    if player["gold"] < cost:
        print("골드가 부족해서 강화할 수 없습니다.")
        return state

    player["gold"] -= cost
    result_number = random.randint(1, 100)

    if result_number <= success_rate:
        weapon["level"] += 1
        print("강화 성공!")
        print(f"{get_weapon_name(weapon)} +{weapon['level']}이(가) 되었습니다.")
    else:
        print("강화 실패!")
        if is_weapon_protected(weapon["level"]):
            print("+5 이하 보호 효과로 강화 단계가 유지됩니다.")
        else:
            weapon["level"] = 0
            print("무기 강화 단계가 +0으로 초기화되었습니다.")

    sync_player_weapon(state)
    print(f"남은 골드: {player['gold']}")

    return state


def run_enhancement_menu(state):
    sync_player_weapon(state)

    while True:
        print()
        print("===== 무기 강화 =====")
        print_player_weapon(state)
        print()
        print("1. 강화 시도")
        print("2. 강화할 무기 선택")
        print("3. 강화 정보 보기")
        print("4. 상점")
        print("5. 창고")
        print("6. 메인 메뉴로 돌아가기")

        choice = input("번호를 선택하세요: ").strip()

        if choice == "1":
            state = try_enhance(state)
        elif choice == "2":
            state = equip_weapon(state)
        elif choice == "3":
            show_enhancement_info(state)
        elif choice == "4":
            state = shop.run_shop_menu(state)
            sync_player_weapon(state)
        elif choice == "5":
            state = warehouse.run_warehouse_menu(state)
            sync_player_weapon(state)
        elif choice == "6":
            print("메인 메뉴로 돌아갑니다.")
            return state
        else:
            print("잘못된 입력입니다. 1, 2, 3, 4, 5, 6 중에서 선택해주세요.")
