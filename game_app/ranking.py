def show_records(state):
    player = state["player"]
    battle = state["battle"]
    raid = state["raid"]

    print()
    print("===== 랭킹 / 기록 =====")
    print(f"최고 강화 단계: +{player['best_weapon_level']}")
    print(f"일반 전투 승리: {battle['win']}회")
    print(f"일반 전투 패배: {battle['lose']}회")
    print(f"보스 레이드 클리어 단계: {raid['cleared_stage']}단계")

    print()
    print("[최근 전투 기록]")
    show_log_list(battle["logs"])

    print()
    print("[최근 레이드 기록]")
    show_log_list(raid["logs"])

    return state


def show_log_list(logs):
    if len(logs) == 0:
        print("아직 기록이 없습니다.")
        return

    for index, log in enumerate(logs[-10:], start=1):
        print(f"{index}. {log}")
