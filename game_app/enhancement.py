"""
enhancement.py - 무기 강화 기능 모듈
담당: 최지현

메인 메뉴에서 run_enhancement_menu(state) 를 호출하여 사용합니다.
state 딕셔너리를 직접 수정한 뒤 반환합니다.
"""

import random


# ──────────────────────────────────────────────
#  계산 함수들
# ──────────────────────────────────────────────

def calculate_cost(level):
    """현재 강화 단계(level)에 따른 강화 비용을 계산합니다.

    비용 = 100 + 현재강화단계 × 80
    예) +0→+1 : 100G,  +3→+4 : 340G
    """
    return 100 + level * 80


def calculate_success_rate(level):
    """현재 강화 단계(level)에 따른 성공 확률을 반환합니다 (0~100 정수).

    +0→+1 : 90%
    +1→+2 : 80%
    +2→+3 : 70%
    +3→+4 : 60%
    +4→+5 : 50%
    +5 이상 : 10%씩 감소하되 최소 20%
    """
    rate = 90 - level * 10
    return max(rate, 20)


# ──────────────────────────────────────────────
#  화면 출력 함수들
# ──────────────────────────────────────────────

def show_weapon_info(state):
    """현재 무기 상태를 한눈에 보여줍니다."""
    player = state["player"]
    level = player["weapon_level"]
    cost = calculate_cost(level)
    rate = calculate_success_rate(level)

    print()
    print(f"  현재 무기  : {player['weapon_name']} +{level}")
    print(f"  현재 골드  : {player['gold']}G")
    print(f"  최고 기록  : +{player['best_weapon_level']}")
    print(f"  강화 비용  : {cost}G")
    print(f"  성공 확률  : {rate}%")


def show_enhancement_table():
    """강화 단계별 비용·확률 표를 출력합니다."""
    print()
    print("  ┌──────────────┬─────────┬───────────┐")
    print("  │   강화 단계   │  비용   │ 성공 확률  │")
    print("  ├──────────────┼─────────┼───────────┤")
    for lv in range(11):
        cost = calculate_cost(lv)
        rate = calculate_success_rate(lv)
        label = f"+{lv} → +{lv + 1}"
        print(f"  │  {label:<11} │ {cost:>5}G  │   {rate:>3}%     │")
    print("  └──────────────┴─────────┴───────────┘")
    print()


# ──────────────────────────────────────────────
#  핵심 강화 로직
# ──────────────────────────────────────────────

def try_enhance(state):
    """강화를 한 번 시도합니다.

    1) 골드 부족 → 강화 불가 안내
    2) 골드 차감
    3) 성공/실패 판정
       - 성공 : weapon_level +1, best_weapon_level 갱신
       - 실패 : weapon_level → 0
    """
    player = state["player"]
    level = player["weapon_level"]
    cost = calculate_cost(level)
    rate = calculate_success_rate(level)

    # 골드 부족 확인
    if player["gold"] < cost:
        print()
        print(f"  [!] 골드가 부족합니다! (필요: {cost}G / 보유: {player['gold']}G)")
        return

    # 골드 차감 (먼저 지불)
    player["gold"] -= cost

    # 성공·실패 판정 (1~100 사이 난수)
    roll = random.randint(1, 100)
    success = roll <= rate

    print()
    if success:
        player["weapon_level"] += 1
        # 최고 기록 갱신
        if player["weapon_level"] > player["best_weapon_level"]:
            player["best_weapon_level"] = player["weapon_level"]
        print(f"  [성공] 강화 성공! "
              f"{player['weapon_name']} +{level} -> +{player['weapon_level']}")
    else:
        player["weapon_level"] = 0
        print(f"  [실패] 강화 실패...  "
              f"{player['weapon_name']} +{level} -> +0  (초기화)")

    print(f"      비용: -{cost}G  |  남은 골드: {player['gold']}G")


# ──────────────────────────────────────────────
#  메인 메뉴에서 호출되는 진입 함수
# ──────────────────────────────────────────────

def run_enhancement_menu(state):
    """무기 강화 메뉴를 반복 실행합니다.

    사용자가 '3. 메인 메뉴로 돌아가기'를 선택하면
    변경된 state를 반환합니다.
    """
    while True:
        print()
        print("========== [ 무기 강화 ] ==========")
        show_weapon_info(state)
        print()
        print("  1. 강화 시도")
        print("  2. 강화 정보 보기")
        print("  3. 메인 메뉴로 돌아가기")
        print()

        choice = input("  선택> ").strip()

        if choice == "1":
            try_enhance(state)
        elif choice == "2":
            show_enhancement_table()
        elif choice == "3":
            print()
            print("  메인 메뉴로 돌아갑니다.")
            break
        else:
            print()
            print("  [!] 잘못된 입력입니다. 1, 2, 3 중에서 선택해주세요.")

    return state


# ──────────────────────────────────────────────
#  단독 테스트 (이 파일만 직접 실행할 때)
# ──────────────────────────────────────────────

if __name__ == "__main__":
    test_state = {
        "player": {
            "nickname": "테스트유저",
            "gold": 1000,
            "weapon_name": "기본 검",
            "weapon_level": 0,
            "best_weapon_level": 0
        },
        "battle": {
            "win": 0,
            "lose": 0,
            "logs": []
        },
        "raid": {
            "cleared_stage": 0,
            "logs": []
        }
    }

    print("=" * 40)
    print("  enhancement.py 단독 테스트 모드")
    print("=" * 40)

    result = run_enhancement_menu(test_state)

    print()
    print("── 테스트 종료 후 플레이어 상태 ──")
    for key, value in result["player"].items():
        print(f"  {key}: {value}")
