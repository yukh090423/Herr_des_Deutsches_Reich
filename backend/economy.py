def cal_tax(state):
    tax = state["economy"]["tax_rate"] * state["national_stats"]["economy"] * 1000
    return tax

def cal_ongoing_expenditure(state):
    expenditure = 0
    for policy in state["active_policies"].values():
        expenditure += policy["ongoing_cost"]
    return expenditure

def cal_event_expenditure(ongoing_events, quarterly_events):
    expenditure = 0
    for value in quarterly_events.values():
        expenditure += value["budget_effect"]
    for value in ongoing_events.values():
        expenditure += value["budget_effect"]
    return expenditure