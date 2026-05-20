# 팀원별 AI 명령 프롬프트

이 문서는 팀원이 AI에게 그대로 복사해서 붙여넣을 수 있도록 작성한 프롬프트 모음이다.

각 팀원은 먼저 자기 브랜치로 이동한 뒤 AI에게 프롬프트를 입력한다.

공통으로 AI에게 반드시 말해야 할 내용:

```text
먼저 AGENTS.md를 읽고 프로젝트 규칙을 이해하세요.
이 프로젝트는 Python 터미널 게임입니다.
GUI, 웹, pygame은 사용하지 마세요.
내 담당 파일 중심으로만 수정하세요.
다른 팀원의 파일은 필요 없으면 수정하지 마세요.
```

---

## 최연준 팀장용 프롬프트

```text
너는 Python 미니 프로젝트의 팀장 역할을 돕는 AI야.

먼저 AGENTS.md를 읽고 프로젝트 규칙을 이해해줘.

프로젝트는 터미널에서만 실행되는 "무기 강화 RPG"야.

게임 흐름은 다음과 같아.
1. 플레이어가 무기를 강화한다.
2. 강화한 무기로 일반 NPC 전투를 해서 골드를 얻는다.
3. 강화한 무기로 단계별 보스 레이드를 클리어한다.
4. 골드, 무기 강화 단계, 전투 기록, 레이드 기록은 JSON 파일로 저장한다.

내 담당은 프로젝트 전체 구조, 메인 메뉴, 저장 기능, 공통 데이터 관리, 기능 연결이야.

다음 파일을 만들어줘.

- main.py
- game_app/__init__.py
- game_app/app.py
- game_app/game_state.py
- game_app/storage.py
- game_app/ranking.py
- game_app/enhancement.py
- game_app/battle.py
- game_app/raid.py
- data/save_data.json
- README.md

단, enhancement.py, battle.py, raid.py는 팀원들이 구현할 예정이므로 최소한의 임시 함수 또는 클래스만 만들어줘.
팀원들이 나중에 해당 파일만 수정해도 전체 앱과 연결될 수 있게 인터페이스를 명확하게 만들어줘.

필수 조건:
- python main.py로 실행되어야 한다.
- 메인 메뉴는 다음 항목을 가진다.
  1. 프로필 보기
  2. 무기 강화
  3. 일반 전투
  4. 보스 레이드
  5. 랭킹/기록 보기
  6. 저장하고 종료
- 숫자가 아닌 입력이나 잘못된 번호를 입력해도 프로그램이 종료되지 않아야 한다.
- JSON 저장 파일이 없으면 기본 데이터를 생성해야 한다.
- 저장 파일 위치는 data/save_data.json 이다.
- Python 표준 라이브러리만 사용한다.
- 코드에는 너무 어려운 문법을 쓰지 말고, 비개발자 팀원이 이해할 수 있게 작성한다.

공통 데이터 구조는 다음 형태를 사용해줘.

{
  "player": {
    "nickname": "player",
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

각 기능 파일은 다음처럼 호출될 수 있게 만들어줘.

- enhancement.run_enhancement_menu(state)
- battle.run_battle_menu(state)
- raid.run_raid_menu(state)
- ranking.show_records(state)

각 함수는 state 딕셔너리를 받아서 필요한 값을 수정하고, 수정된 state를 반환하도록 만들어줘.

작업 후에는 어떤 파일을 만들었고, 각 파일이 무슨 역할인지 설명해줘.
```

---

## 최지현 무기 강화 담당 프롬프트

```text
너는 Python 미니 프로젝트에서 무기 강화 기능을 구현하는 AI야.

먼저 AGENTS.md를 읽고 프로젝트 규칙을 이해해줘.

이 프로젝트는 터미널에서만 실행되는 "무기 강화 RPG"야.
GUI, 웹, pygame은 사용하지 마.

내 담당 파일은 game_app/enhancement.py 야.
가능하면 이 파일만 수정해줘.
다른 파일 수정이 꼭 필요하면 수정하기 전에 이유를 먼저 설명해줘.

프로젝트의 공통 state 데이터 구조는 다음과 같아.

{
  "player": {
    "nickname": "player",
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

game_app/enhancement.py에 무기 강화 기능을 구현해줘.

반드시 다음 함수가 있어야 해.

def run_enhancement_menu(state):
    ...
    return state

이 함수는 메인 메뉴에서 호출된다.

기능 요구사항:
1. 현재 골드, 무기 이름, 현재 강화 단계, 최고 강화 단계를 보여준다.
2. 강화 메뉴를 보여준다.
   - 1. 강화 시도
   - 2. 강화 정보 보기
   - 3. 메인 메뉴로 돌아가기
3. 강화 시도 시 현재 강화 단계에 따라 비용을 계산한다.
4. 골드가 부족하면 강화하지 못하게 한다.
5. 강화 시도 시 골드를 먼저 차감한다.
6. random 모듈을 사용해서 성공/실패를 결정한다.
7. 성공하면 weapon_level을 1 올린다.
8. 실패하면 weapon_level을 0으로 초기화한다.
9. best_weapon_level은 최고 기록이므로 현재 강화 단계가 더 높으면 갱신한다.
10. 잘못된 입력을 해도 프로그램이 종료되지 않게 한다.

추천 강화 비용:
- 비용 = 100 + 현재강화단계 * 80

추천 성공 확률:
- +0 -> +1: 90%
- +1 -> +2: 80%
- +2 -> +3: 70%
- +3 -> +4: 60%
- +4 -> +5: 50%
- +5 이상: 최소 20%까지 단계가 높아질수록 감소

출력 문구는 한국어로 작성해줘.

예시 출력:
현재 무기: 기본 검 +3
현재 골드: 760
강화 비용: 340
성공 확률: 60%

코드는 비개발자도 이해할 수 있게 간단한 함수로 나눠줘.
예를 들어 calculate_cost(level), calculate_success_rate(level), try_enhance(state) 같은 함수를 만들어도 좋아.

작업 후에는 내가 확인할 수 있도록 변경한 파일과 실행 방법을 설명해줘.
```

---

## 김민기 일반 전투 담당 프롬프트

```text
너는 Python 미니 프로젝트에서 일반 전투 기능을 구현하는 AI야.

먼저 AGENTS.md를 읽고 프로젝트 규칙을 이해해줘.

이 프로젝트는 터미널에서만 실행되는 "무기 강화 RPG"야.
GUI, 웹, pygame은 사용하지 마.

내 담당 파일은 game_app/battle.py 야.
가능하면 이 파일만 수정해줘.
다른 파일 수정이 꼭 필요하면 수정하기 전에 이유를 먼저 설명해줘.

프로젝트의 공통 state 데이터 구조는 다음과 같아.

{
  "player": {
    "nickname": "player",
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

game_app/battle.py에 일반 전투 기능을 구현해줘.

반드시 다음 함수가 있어야 해.

def run_battle_menu(state):
    ...
    return state

이 함수는 메인 메뉴에서 호출된다.

일반 전투의 목적:
- 플레이어가 강화한 무기로 랜덤 NPC와 싸운다.
- 승리하면 골드를 얻는다.
- 패배하면 골드를 조금 잃는다.
- 전투 결과는 battle.logs에 저장한다.

기능 요구사항:
1. 일반 전투 메뉴를 보여준다.
   - 1. 전투 시작
   - 2. 전투 기록 보기
   - 3. 메인 메뉴로 돌아가기
2. 전투 시작 시 NPC를 랜덤으로 하나 선택한다.
3. NPC는 이름, 전투력, 승리 보상, 패배 손실금을 가진다.
4. 플레이어 전투력은 무기 강화 단계에 따라 계산한다.
5. 플레이어 전투력과 NPC 전투력을 비교해서 승패를 정한다.
6. 약간의 랜덤 요소를 넣어도 된다.
7. 승리하면 gold를 증가시키고 battle.win을 1 증가시킨다.
8. 패배하면 gold를 감소시키고 battle.lose를 1 증가시킨다.
9. 패배 시 골드는 0 미만이 되지 않게 한다.
10. 전투 결과는 battle.logs에 문자열로 저장한다.
11. 로그가 너무 길어지면 최근 10개 정도만 유지해도 된다.
12. 잘못된 입력을 해도 프로그램이 종료되지 않게 한다.

추천 NPC:
- 훈련병: 전투력 5, 승리 보상 120, 패배 손실 50
- 산적: 전투력 15, 승리 보상 250, 패배 손실 100
- 암흑 기사: 전투력 30, 승리 보상 500, 패배 손실 200

추천 플레이어 전투력:
- 기본 전투력 = 10
- 무기 강화 단계 1당 전투력 +5
- 랜덤 보너스 0~10 추가 가능

출력 문구는 한국어로 작성해줘.

예시 출력:
상대 NPC: 산적
내 전투력: 27
상대 전투력: 19
전투 결과: 승리
획득 골드: 250

코드는 비개발자도 이해할 수 있게 간단한 함수로 나눠줘.
예를 들어 get_random_enemy(), calculate_player_power(state), play_battle(state), show_battle_logs(state) 같은 함수를 만들어도 좋아.

작업 후에는 내가 확인할 수 있도록 변경한 파일과 실행 방법을 설명해줘.
```

---

## 이동수 보스 레이드 담당 프롬프트

```text
너는 Python 미니 프로젝트에서 보스 레이드 기능을 구현하는 AI야.

먼저 AGENTS.md를 읽고 프로젝트 규칙을 이해해줘.

이 프로젝트는 터미널에서만 실행되는 "무기 강화 RPG"야.
GUI, 웹, pygame은 사용하지 마.

내 담당 파일은 game_app/raid.py 야.
가능하면 이 파일만 수정해줘.
다른 파일 수정이 꼭 필요하면 수정하기 전에 이유를 먼저 설명해줘.

프로젝트의 공통 state 데이터 구조는 다음과 같아.

{
  "player": {
    "nickname": "player",
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

game_app/raid.py에 보스 레이드 기능을 구현해줘.

반드시 다음 함수가 있어야 해.

def run_raid_menu(state):
    ...
    return state

이 함수는 메인 메뉴에서 호출된다.

보스 레이드의 목적:
- 일반 전투와 다르게 정해진 보스를 순서대로 클리어한다.
- 각 보스는 필요한 무기 강화 단계가 있다.
- 플레이어의 무기 강화 단계가 부족하면 도전할 수 없다.
- 클리어하면 골드 보상과 클리어 기록을 얻는다.

기능 요구사항:
1. 보스 레이드 메뉴를 보여준다.
   - 1. 다음 보스 도전
   - 2. 보스 목록 보기
   - 3. 레이드 기록 보기
   - 4. 메인 메뉴로 돌아가기
2. 현재 cleared_stage를 기준으로 다음 보스를 정한다.
3. 플레이어 weapon_level이 보스의 required_level보다 낮으면 도전할 수 없다고 출력한다.
4. 조건을 만족하면 보스에 도전한다.
5. 도전 성공 시 cleared_stage를 1 증가시킨다.
6. 성공 시 gold를 보상만큼 증가시킨다.
7. 결과는 raid.logs에 문자열로 저장한다.
8. 모든 보스를 클리어하면 더 이상 도전할 보스가 없다고 출력한다.
9. 잘못된 입력을 해도 프로그램이 종료되지 않게 한다.

추천 보스 목록:
- 스테이지 1: 슬라임 왕, 필요 강화 +0, 보상 300
- 스테이지 2: 늑대 대장, 필요 강화 +3, 보상 600
- 스테이지 3: 돌 골렘, 필요 강화 +5, 보상 1000
- 스테이지 4: 드래곤, 필요 강화 +8, 보상 2000

출력 문구는 한국어로 작성해줘.

예시 출력:
다음 보스: 늑대 대장
필요 강화 단계: +3
현재 무기 단계: +2
강화 단계가 부족하여 도전할 수 없습니다.

코드는 비개발자도 이해할 수 있게 간단한 함수로 나눠줘.
예를 들어 get_bosses(), show_boss_list(state), challenge_next_boss(state), show_raid_logs(state) 같은 함수를 만들어도 좋아.

작업 후에는 내가 확인할 수 있도록 변경한 파일과 실행 방법을 설명해줘.
```

---

## 공통 Git 명령어 안내

작업 시작 전:

```bash
git checkout main
git pull origin main
git checkout -b feature/브랜치이름
```

작업 확인:

```bash
python main.py
```

작업 저장:

```bash
git add .
git commit -m "feat: add 기능이름"
git push origin feature/브랜치이름
```

그 다음 GitHub에서 Pull Request를 만든다.
