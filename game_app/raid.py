from game_app import ranking


def run_raid_menu(state):
    while True:
        print()
        print("===== 보스 레이드 =====")
        print("1. 보스 레이드 도전")
        print("2. 랭킹/기록 보기")
        print("3. 메인 메뉴로 돌아가기")

        choice = input("번호를 선택하세요: ").strip()

        if choice == "1":
            print("보스 레이드 기능은 이동수 팀원이 구현할 예정입니다.")
            input("Enter를 누르면 보스 레이드 메뉴로 돌아갑니다.")
        elif choice == "2":
            state = ranking.show_records(state)
        elif choice == "3":
            print("메인 메뉴로 돌아갑니다.")
            return state
        else:
            print("잘못된 입력입니다. 1, 2, 3 중에서 선택해주세요.")
