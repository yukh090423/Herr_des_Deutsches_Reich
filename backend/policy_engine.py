def check_condition(state, stat_name, minpoint):
    if state["national_stats"][stat_name] >= minpoint:
        return True
    else:
        return False

def check_policy_requirements(state, policy):
    for stat_name, minpoint in policy["requirements"].items():
        if check_condition(state, stat_name, minpoint) == False:
            return False
        else:
            pass
        return True

def cal_cost(state, policy):
    req_cost = policy["base_cost"]
    price_index = state["economy"]["price_index"]
    act_cost = req_cost * price_index / 100
    return act_cost

def check_policy(state, policy):
    if check_policy_requirements(state, policy) == True:
        if cal_cost(state, policy) <= state["finance"]["budget"]:
            return True
        else:
            return False
    else:
        return False

def run_policy(state, policy_id, policy):
    if check_policy(state, policy) == True:
        state["finance"]["budget"] -= cal_cost(state, policy)
        from state_utils import stats_change
        for stat_name, deltapoint in policy["effects"].items():
            stats_change(state, stat_name, deltapoint)
        if policy["ongoing"] == True:
            state["active_policies"][policy_id] = {
                "remaining_turns": policy["duration"]
            }
        return True
    else:
        return False

from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent

def load_policies():
    file_path = BASE_DIR / "data" / "policies.json"

    with open(file_path, "r", encoding="utf-8") as file:
        policies = json.load(file)

    return policies

