def cal_tax(state):
    tax = state["economy"]["tax_rate"] * state["national_stats"]["economy"] * 1000
    return tax