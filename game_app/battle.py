import random


def get_random_enemy():
    enemies = [
        {
            "name": "훈련병",
            "power": 5,
            "reward": 120,
            "loss": 50,
        },
        {
            "name": "산적",
            "power": 15,
            "reward": 250,
            "loss": 100,
        },
        {
            "name": "암흑 기사",
            "power": 30,
            "reward": 500,
            "loss": 200,
        },
    ]
    return random.choice(enemies)


def calculate_player_power(state):
    player = state["player"]
    weapon_level = player["weapon_level"]

    base_power = 10
    weapon_power = weapon_level * 5
    random_bonus = random.randint(0, 10)

    return base_power + weapon_power + random_bonus


def add_battle_log(state, log_message):
    logs = state["battle"]["logs"]
    logs.append(log_message)

    if len(logs) > 10:
        state["battle"]["logs"] = logs[-10:]


def play_battle(state):
    enemy = get_random_enemy()
    player_power = calculate_player_power(state)
    enemy_power = enemy["power"] + random.randint(0, 10)

    print()
    print("===== 전투 시작 =====")
    print(f"상대 NPC: {enemy['name']}")
    print(f"내 전투력: {player_power}")
    print(f"상대 전투력: {enemy_power}")

    if player_power >= enemy_power:
        reward = enemy["reward"]
        state["player"]["gold"] += reward
        state["battle"]["win"] += 1

        print("전투 결과: 승리")
        print(f"획득 골드: {reward}")

        log_message = f"{enemy['name']} 전투 승리 - 골드 +{reward}"
    else:
        loss = enemy["loss"]
        current_gold = state["player"]["gold"]
        actual_loss = min(current_gold, loss)

        state["player"]["gold"] -= actual_loss
        state["battle"]["lose"] += 1

        print("전투 결과: 패배")
        print(f"잃은 골드: {actual_loss}")

        log_message = f"{enemy['name']} 전투 패배 - 골드 -{actual_loss}"

    print(f"현재 골드: {state['player']['gold']}")
    add_battle_log(state, log_message)

    return state


def show_battle_logs(state):
    logs = state["battle"]["logs"]

    print()
    print("===== 전투 기록 =====")
    print(f"승리: {state['battle']['win']}회")
    print(f"패배: {state['battle']['lose']}회")

    if len(logs) == 0:
        print("아직 전투 기록이 없습니다.")
        return

    for index, log in enumerate(logs, start=1):
        print(f"{index}. {log}")


def run_battle_menu(state):
    while True:
        print()
        print("===== 일반 전투 =====")
        print("1. 전투 시작")
        print("2. 전투 기록 보기")
        print("3. 메인 메뉴로 돌아가기")

        choice = input("번호를 선택하세요: ")

        if choice == "1":
            state = play_battle(state)
        elif choice == "2":
            show_battle_logs(state)
        elif choice == "3":
            print("메인 메뉴로 돌아갑니다.")
            return state
        else:
            print("잘못된 입력입니다. 1, 2, 3 중에서 선택해주세요.")
