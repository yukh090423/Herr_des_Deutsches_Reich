import json
from pathlib import Path



# 프로젝트의 최상위 폴더 경로
BASE_DIR = Path(__file__).resolve().parent.parent

# 초기 국가 데이터 불러오기
def load_initial_state():
    file_path = BASE_DIR / "data" / "initial_stats.json"

    with open(file_path, "r", encoding="utf-8") as filename:
        state = json.load(filename)

    return state

state = load_initial_state()

def next_turn(state):
    state["game_date"]["quarter"] += 1
    if state["game_date"]["quarter"] > 4:
        state["game_date"]["quarter"] = 1
        state["game_date"]["year"] += 1

def save_game_state(state):
    file_path = BASE_DIR / "data" / "save_game.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(state, file, ensure_ascii=False, indent=4)

print(f'before: {state["game_date"]["year"]}, {state["game_date"]["quarter"]}')
next_turn(state)
print(f'after: {state["game_date"]["year"]}, {state["game_date"]["quarter"]}')