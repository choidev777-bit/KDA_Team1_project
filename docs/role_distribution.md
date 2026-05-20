# 역할 분배표

## 팀원

| 이름 | 담당 역할 | 담당 파일 | 브랜치 |
| --- | --- | --- | --- |
| 최연준 | 팀장, 전체 구조, 메인 메뉴, 저장 기능, 통합, 문서 | `main.py`, `game_app/app.py`, `game_app/game_state.py`, `game_app/storage.py`, `game_app/ranking.py`, 문서 | `feature/project-structure` |
| 최지현 | 무기 강화 기능 | `game_app/enhancement.py` | `feature/enhancement` |
| 김민기 | 일반 전투 기능 | `game_app/battle.py` | `feature/battle` |
| 이동수 | 보스 레이드 기능 | `game_app/raid.py` | `feature/raid` |

## 최연준 상세 역할

최연준은 팀장으로서 프로젝트의 기본 구조를 만든다.

담당 업무:

- GitHub 저장소 생성
- 팀원 초대
- Slack 소통 관리
- `AGENTS.md` 작성
- 프로젝트 기획서 작성
- 메인 메뉴 작성
- JSON 저장/불러오기 구조 작성
- 팀원 코드 통합
- Pull Request 확인
- 최종 발표/제출 자료 정리

주의할 점:

- 팀원들이 작업할 파일을 미리 만들어주면 충돌이 줄어든다.
- 각 팀원의 기능이 같은 데이터 구조를 사용하도록 안내해야 한다.
- 팀원들이 AI에게 줄 프롬프트를 최대한 구체적으로 제공해야 한다.

## 최지현 상세 역할

최지현은 무기 강화 기능을 담당한다.

담당 업무:

- 현재 무기 강화 단계 출력
- 현재 골드 출력
- 강화 비용 계산
- 강화 성공 확률 계산
- 강화 성공/실패 처리
- 최고 강화 단계 갱신
- 강화 메뉴에서 메인 메뉴로 돌아가기

수정 권장 파일:

```text
game_app/enhancement.py
```

가능하면 다른 파일은 수정하지 않는다.

## 김민기 상세 역할

김민기는 일반 전투 기능을 담당한다.

담당 업무:

- 랜덤 NPC 목록 만들기
- 플레이어 전투력 계산
- NPC 전투력 계산
- 승패 판정
- 승리 시 골드 지급
- 패배 시 골드 차감
- 전투 로그 저장
- 일반 전투 메뉴에서 메인 메뉴로 돌아가기

수정 권장 파일:

```text
game_app/battle.py
```

가능하면 다른 파일은 수정하지 않는다.

## 이동수 상세 역할

이동수는 보스 레이드 기능을 담당한다.

담당 업무:

- 보스 스테이지 목록 만들기
- 보스별 필요 강화 단계 설정
- 플레이어가 도전 가능한지 확인
- 보스 클리어 처리
- 클리어 보상 지급
- 레이드 로그 저장
- 레이드 메뉴에서 메인 메뉴로 돌아가기

수정 권장 파일:

```text
game_app/raid.py
```

가능하면 다른 파일은 수정하지 않는다.

## 협업 규칙

1. `main` 브랜치에 직접 작업하지 않는다.
2. 각자 담당 브랜치를 만든다.
3. 작업 전 항상 `git pull origin main`을 실행한다.
4. 작업이 끝나면 commit 후 push한다.
5. GitHub에서 Pull Request를 만든다.
6. 충돌이 발생하면 팀장에게 공유한다.
7. merge 후에는 팀원 모두 최신 `main`을 다시 pull한다.

## 추천 커밋 메시지

```text
feat: add enhancement feature
feat: add normal battle feature
feat: add raid feature
feat: add json save and load
docs: add project plan
fix: handle invalid menu input
```

## 최종 보고에 넣을 내용

- 프로젝트 이름
- 팀원별 역할
- 기능 설명
- 실행 방법
- 파일 구조
- GitHub 협업 방식
- 브랜치 사용 내역
- Pull Request 또는 merge 내역
- 충돌 또는 오류 해결 경험
- 팀원별 회고
