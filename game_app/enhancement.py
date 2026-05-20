def run_enhancement_menu(state):
    print()
    print("===== 무기 강화 =====")
    print("무기 강화 기능은 최지현 팀원이 구현할 예정입니다.")
    print("현재는 메인 메뉴 연결 확인용 임시 화면입니다.")
    print_player_weapon(state)
    input("Enter를 누르면 메인 메뉴로 돌아갑니다.")
    return state


def print_player_weapon(state):
    player = state["player"]
    print(f"현재 무기: {player['weapon_name']} +{player['weapon_level']}")
    print(f"현재 골드: {player['gold']}")
    print(f"최고 강화 단계: +{player['best_weapon_level']}")
