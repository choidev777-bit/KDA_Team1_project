from game_app import battle, enhancement, raid, ranking
from game_app.storage import DEFAULT_SAVE_PATH, load_state, save_state


class GameApp:
    def __init__(self, save_path=DEFAULT_SAVE_PATH):
        self.save_path = save_path
        self.state = load_state(self.save_path)

    def run(self):
        running = True

        while running:
            self.show_main_menu()
            choice = input("메뉴 번호를 선택하세요: ").strip()
            running = self.handle_menu_choice(choice)

    def show_main_menu(self):
        print()
        print("===== 무기 강화 RPG =====")
        print("1. 프로필 보기")
        print("2. 무기 강화")
        print("3. 일반 전투")
        print("4. 보스 레이드")
        print("5. 랭킹/기록 보기")
        print("6. 저장하고 종료")

    def handle_menu_choice(self, choice):
        if choice == "1":
            self.show_profile()
            return True
        if choice == "2":
            self.state = enhancement.run_enhancement_menu(self.state)
            save_state(self.state, self.save_path)
            return True
        if choice == "3":
            self.state = battle.run_battle_menu(self.state)
            save_state(self.state, self.save_path)
            return True
        if choice == "4":
            self.state = raid.run_raid_menu(self.state)
            save_state(self.state, self.save_path)
            return True
        if choice == "5":
            self.state = ranking.show_records(self.state)
            return True
        if choice == "6":
            save_state(self.state, self.save_path)
            print("게임 데이터를 저장했습니다. 프로그램을 종료합니다.")
            return False

        print("잘못된 입력입니다. 1부터 6까지의 숫자를 입력해주세요.")
        return True

    def show_profile(self):
        player = self.state["player"]
        battle_state = self.state["battle"]
        raid_state = self.state["raid"]

        print()
        print("===== 프로필 =====")
        print(f"닉네임: {player['nickname']}")
        print(f"골드: {player['gold']}")
        print(f"무기: {player['weapon_name']} +{player['weapon_level']}")
        print(f"최고 강화 단계: +{player['best_weapon_level']}")
        print(f"일반 전투: {battle_state['win']}승 {battle_state['lose']}패")
        print(f"보스 레이드 클리어 단계: {raid_state['cleared_stage']}단계")
