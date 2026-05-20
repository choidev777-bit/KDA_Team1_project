from game_app import battle, enhancement, raid
from game_app.storage import DEFAULT_SAVE_PATH, load_state, save_state
from game_app.weapon_data import sync_player_weapon


class GameApp:
    def __init__(self, save_path=DEFAULT_SAVE_PATH):
        self.save_path = save_path
        self.state = load_state(self.save_path)

    def run(self):
        self.show_intro_if_needed()
        running = True

        while running:
            self.show_main_menu()
            choice = input("메뉴 번호를 선택하세요: ").strip()
            running = self.handle_menu_choice(choice)

    def show_intro_if_needed(self):
        settings = self.state["settings"]

        if settings["intro_seen"]:
            return

        print()
        print("===== 무기 강화 RPG =====")
        print("상점에서 무기를 사고, 강화해서 더 강해지는 터미널 RPG입니다.")
        print("일반 전투로 골드를 벌고, 강해진 무기로 보스 레이드에 도전하세요.")
        print("창고에서는 내가 가진 무기를 확인하고 장착할 수 있습니다.")
        print()

        nickname = input("닉네임을 입력하세요: ").strip()
        if nickname:
            self.state["player"]["nickname"] = nickname

        settings["intro_seen"] = True
        save_state(self.state, self.save_path)

    def show_main_menu(self):
        print()
        print("===== 무기 강화 RPG =====")
        print("1. 프로필 보기")
        print("2. 무기 강화")
        print("3. 일반 전투")
        print("4. 보스 레이드")
        print("5. 게임 종료")

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
            save_state(self.state, self.save_path)
            print("게임 데이터를 저장했습니다. 프로그램을 종료합니다.")
            return False

        print("잘못된 입력입니다. 1부터 5까지의 숫자를 입력해주세요.")
        return True

    def show_profile(self):
        sync_player_weapon(self.state)

        player = self.state["player"]
        battle_state = self.state["battle"]
        raid_state = self.state["raid"]
        weapon_count = len(self.state["inventory"]["weapons"])

        print()
        print("===== 프로필 =====")
        print(f"닉네임: {player['nickname']}")
        print(f"골드: {player['gold']}")
        print(f"장착 무기: {player['weapon_name']} +{player['weapon_level']}")
        print(f"보유 무기 수: {weapon_count}")
        print(f"최고 강화 단계: +{player['best_weapon_level']}")
        print(f"일반 전투: {battle_state['win']}승 {battle_state['lose']}패")
        print(f"보스 레이드 클리어 단계: {raid_state['cleared_stage']}단계")
