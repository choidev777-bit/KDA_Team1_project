import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from game_app.app import GameApp
from game_app.game_state import create_default_state
from game_app.storage import load_state, save_state


class GameStateTests(unittest.TestCase):
    def test_create_default_state_has_expected_player_values(self):
        state = create_default_state()

        self.assertEqual(state["player"]["nickname"], "player")
        self.assertEqual(state["player"]["gold"], 1000)
        self.assertEqual(state["player"]["weapon_name"], "철검")
        self.assertEqual(state["player"]["weapon_level"], 0)
        self.assertEqual(state["player"]["best_weapon_level"], 0)
        self.assertEqual(state["inventory"]["equipped_weapon_id"], "weapon_1")
        self.assertEqual(len(state["inventory"]["weapons"]), 1)

    def test_create_default_state_returns_independent_data(self):
        first_state = create_default_state()
        second_state = create_default_state()

        first_state["battle"]["logs"].append("첫 번째 기록")
        first_state["inventory"]["weapons"][0]["level"] = 3

        self.assertEqual(second_state["battle"]["logs"], [])
        self.assertEqual(second_state["inventory"]["weapons"][0]["level"], 0)


class StorageTests(unittest.TestCase):
    def test_load_state_creates_default_file_when_missing(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            save_path = Path(temp_dir) / "save_data.json"

            state = load_state(save_path)

            self.assertTrue(save_path.exists())
            self.assertEqual(state["player"]["gold"], 1000)
            self.assertEqual(state["raid"]["cleared_stage"], 0)
            self.assertEqual(len(state["inventory"]["weapons"]), 1)

    def test_load_state_adds_inventory_to_old_save_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            save_path = Path(temp_dir) / "save_data.json"
            old_state = {
                "player": {
                    "nickname": "player",
                    "gold": 1000,
                    "weapon_name": "기본 검",
                    "weapon_level": 2,
                    "best_weapon_level": 2,
                },
                "battle": {"win": 0, "lose": 0, "logs": []},
                "raid": {"cleared_stage": 0, "logs": []},
            }

            save_path.parent.mkdir(parents=True, exist_ok=True)
            with save_path.open("w", encoding="utf-8") as file:
                json.dump(old_state, file, ensure_ascii=False)

            state = load_state(save_path)

            self.assertEqual(state["inventory"]["weapons"][0]["level"], 2)
            self.assertEqual(state["player"]["weapon_name"], "철검")
            self.assertEqual(state["player"]["weapon_level"], 2)

    def test_save_state_round_trips_json_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            save_path = Path(temp_dir) / "save_data.json"
            state = create_default_state()
            state["player"]["gold"] = 1500
            state["battle"]["logs"].append("전투 승리")

            save_state(state, save_path)

            with save_path.open("r", encoding="utf-8") as file:
                saved_data = json.load(file)

            self.assertEqual(saved_data["player"]["gold"], 1500)
            self.assertEqual(saved_data["battle"]["logs"], ["전투 승리"])


class GameAppTests(unittest.TestCase):
    def test_exit_menu_choice_saves_state_and_stops_app(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            save_path = Path(temp_dir) / "save_data.json"
            app = GameApp(save_path=save_path)

            with patch("builtins.print"):
                should_continue = app.handle_menu_choice("8")

            self.assertFalse(should_continue)
            self.assertTrue(save_path.exists())

    def test_invalid_menu_choice_keeps_app_running(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            save_path = Path(temp_dir) / "save_data.json"
            app = GameApp(save_path=save_path)

            with patch("builtins.print"):
                should_continue = app.handle_menu_choice("잘못된 입력")

            self.assertTrue(should_continue)


if __name__ == "__main__":
    unittest.main()
