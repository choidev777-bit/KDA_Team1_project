# AGENTS.md

## Project Overview

This project is a terminal-only Python mini game project for a 4-person team.

The game concept is a simple weapon-growth RPG:

1. The player enhances a weapon.
2. The player uses the enhanced weapon in random NPC battles to earn gold.
3. The player challenges staged raid bosses using the enhanced weapon.
4. Player data is saved in JSON so progress remains after restarting the program.

The program must run from `main.py` and show a terminal menu.

Do not build a GUI, web app, pygame app, or notebook. Use only terminal input/output with `print()` and `input()`.

## Team Members

- Choi Yeonjun: team leader, project structure, main menu, shared state, storage, integration, documentation
- Choi Jihyun: weapon enhancement feature
- Kim Mingi: normal battle feature
- Lee Dongsu: boss raid feature

## Planned File Structure

```text
team1_game/
  main.py
  AGENTS.md
  README.md
  docs/
    project_plan.md
    role_distribution.md
    ai_prompts.md
  game_app/
    __init__.py
    app.py
    game_state.py
    storage.py
    enhancement.py
    battle.py
    raid.py
    ranking.py
  data/
    save_data.json
```

## Core Rules For AI Agents

1. Read this file before editing code.
2. Keep the project terminal-only.
3. Use Python standard library only unless the team leader explicitly approves another library.
4. Keep each feature in its assigned file.
5. Do not modify another teammate's feature file unless the team leader asks.
6. Do not directly edit `main` or `master` branch work. Work on a feature branch.
7. Do not remove existing code written by another teammate.
8. Keep function names and return values compatible with the shared design.
9. Use clear Korean terminal messages.
10. Handle invalid user input without crashing.

## Shared Game Data

The project should use one shared dictionary-like state.

Recommended JSON shape:

```json
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
```

## Feature Boundaries

### Team Leader Files

The team leader owns:

- `main.py`
- `game_app/app.py`
- `game_app/game_state.py`
- `game_app/storage.py`
- `game_app/ranking.py`
- documentation files

### Enhancement Feature

Owner: Choi Jihyun

Main file:

- `game_app/enhancement.py`

Expected behavior:

- Show enhancement menu.
- Show current gold and weapon level.
- Calculate enhancement cost based on current weapon level.
- Calculate success rate based on current weapon level.
- On success, increase weapon level by 1.
- On failure, reset weapon level to 0.
- Save best weapon level.
- Spend gold when enhancement is attempted.
- Return to the main menu when the user chooses to quit.

### Normal Battle Feature

Owner: Kim Mingi

Main file:

- `game_app/battle.py`

Expected behavior:

- Show normal battle menu.
- Randomly select an NPC enemy.
- Compare player weapon power and NPC power.
- Decide win or loss.
- On win, give gold.
- On loss, subtract some gold if possible.
- Add battle log.
- Return to the main menu when the user chooses to quit.

### Raid Feature

Owner: Lee Dongsu

Main file:

- `game_app/raid.py`

Expected behavior:

- Show boss raid menu.
- Bosses are staged, not random.
- Each boss has a required weapon level.
- Player cannot challenge a boss if weapon level is too low.
- If player clears the current boss, increase cleared stage.
- Give gold reward for clear.
- Add raid log.
- Return to the main menu when the user chooses to quit.

## Recommended Main Menu

```text
===== 무기 강화 RPG =====
1. 프로필 보기
2. 무기 강화
3. 일반 전투
4. 보스 레이드
5. 랭킹/기록 보기
6. 저장하고 종료
```

## Git Collaboration Rules

Recommended branches:

- `main`: stable integrated branch
- `feature/project-structure`: team leader
- `feature/enhancement`: Choi Jihyun
- `feature/battle`: Kim Mingi
- `feature/raid`: Lee Dongsu

Recommended workflow:

```bash
git checkout main
git pull origin main
git checkout -b feature/my-feature
git add .
git commit -m "feat: add my feature"
git push origin feature/my-feature
```

Then create a Pull Request on GitHub.

## Definition Of Done

A feature is complete when:

1. The menu opens without crashing.
2. Invalid input is handled.
3. The feature updates the shared game state correctly.
4. JSON save data remains valid.
5. The feature can return to the main menu.
6. The teammate can explain what the code does.
