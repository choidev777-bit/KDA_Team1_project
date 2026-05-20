def get_bosses():
    return [
        {
            "stage": 1,
            "name": "슬라임 왕",
            "required_level": 0,
            "reward": 300,
        },
        {
            "stage": 2,
            "name": "늑대 대장",
            "required_level": 3,
            "reward": 600,
        },
        {
            "stage": 3,
            "name": "돌 골렘",
            "required_level": 5,
            "reward": 1000,
        },
        {
            "stage": 4,
            "name": "저주받은 마법사",
            "required_level": 8,
            "reward": 2000,
        },
        {
            "stage": 5,
            "name": "불꽃 거인",
            "required_level": 11,
            "reward": 3000,
        },
        {
            "stage": 6,
            "name": "얼음 여왕",
            "required_level": 13,
            "reward": 4200,
        },
        {
            "stage": 7,
            "name": "심연의 기사",
            "required_level": 16,
            "reward": 5800,
        },
        {
            "stage": 8,
            "name": "고대 드래곤",
            "required_level": 18,
            "reward": 7500,
        },
        {
            "stage": 9,
            "name": "마왕",
            "required_level": 20,
            "reward": 10000,
        },
    ]


def show_boss_list(state):
    bosses = get_bosses()
    cleared_stage = state["raid"]["cleared_stage"]

    print()
    print("===== 보스 목록 =====")

    for boss in bosses:
        if boss["stage"] <= cleared_stage:
            status = "클리어"
        else:
            status = "미클리어"

        print(
            f"스테이지 {boss['stage']}: {boss['name']} "
            f"| 필요 강화 +{boss['required_level']} "
            f"| 보상 {boss['reward']} 골드 "
            f"| {status}"
        )


def show_raid_logs(state):
    logs = state["raid"]["logs"]

    print()
    print("===== 레이드 기록 =====")

    if not logs:
        print("아직 레이드 기록이 없습니다.")
        return

    for log in logs:
        print(log)


def challenge_next_boss(state):
    bosses = get_bosses()
    cleared_stage = state["raid"]["cleared_stage"]

    if cleared_stage >= len(bosses):
        print()
        print("모든 보스를 클리어했습니다.")
        print("더 이상 도전할 보스가 없습니다.")
        return state

    boss = bosses[cleared_stage]
    player = state["player"]
    weapon_level = player["weapon_level"]

    print()
    print(f"다음 보스: {boss['name']}")
    print(f"필요 강화 단계: +{boss['required_level']}")
    print(f"현재 무기 단계: +{weapon_level}")

    if weapon_level < boss["required_level"]:
        print("강화 단계가 부족하여 도전할 수 없습니다.")
        return state

    player["gold"] += boss["reward"]
    state["raid"]["cleared_stage"] += 1

    log = (
        f"스테이지 {boss['stage']} {boss['name']} 클리어! "
        f"보상 {boss['reward']} 골드 획득"
    )
    state["raid"]["logs"].append(log)

    print()
    print("보스 레이드 성공!")
    print(f"{boss['name']}을(를) 클리어했습니다.")
    print(f"획득 골드: {boss['reward']}")
    print(f"현재 골드: {player['gold']}")

    return state


def run_raid_menu(state):
    while True:
        print()
        print("===== 보스 레이드 =====")
        print("1. 다음 보스 도전")
        print("2. 보스 목록 보기")
        print("3. 레이드 기록 보기")
        print("4. 메인 메뉴로 돌아가기")

        choice = input("메뉴 번호를 선택하세요: ").strip()

        if choice == "1":
            state = challenge_next_boss(state)
        elif choice == "2":
            show_boss_list(state)
        elif choice == "3":
            show_raid_logs(state)
        elif choice == "4":
            return state
        else:
            print("잘못된 입력입니다. 1부터 4까지의 숫자를 입력해주세요.")
