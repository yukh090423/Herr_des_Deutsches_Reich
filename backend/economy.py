def cal_tax(state):
    tax = state["economy"]["tax_rate"] * state["national_stats"]["economy"] * 1000
    return tax

def cal_ongoing_expenditure(ongoing_policy):
    expenditure = 0
    for key in ongoing_policy.items():
        expenditure += ongoing_policy[key]["ongoing_cost"]
    return expenditure